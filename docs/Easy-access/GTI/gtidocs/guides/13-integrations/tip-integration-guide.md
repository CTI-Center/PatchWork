---
title: "TIP integration guide"
source: https://gtidocs.virustotal.com/docs/tip-integration-guide
slug: tip-integration-guide
section: guides
group: "Integrations"
updatedAt: 2026-08-13T10:38:46.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Integrations](README.md) › TIP integration guide

---

# tip-integration-guide

# 1.-executive-summary-&-the-challenge

> 📘
>
> Please note that all references to the 'Feed endpoint' apply strictly to [this specific endpoint](https://gtidocs.readme.io/reference/ioc-deltas), and do not include any other IoC Feeds or Categorized Threat List endpoints provided by our API.

## the-pain-point

Historically, keeping local enterprise indicator databases synchronized with Threat Intelligence Platforms (TIPs) suffered from the "Silent Update" challenge. Because threat indicators (IoCs) are constantly enriched, rescored, or re-categorized as new intelligence emerges, integrators previously had to rely on continuous, exhaustive API polling across massive lists of indicators simply to check if a record had been modified. This legacy pattern forced a multiplier effect where a single Collection entity required thousands of subsequent API calls, exhausting standard quotas, causing HTTP 429 errors, and creating unavoidable latency in downstream security operations.

## the-solution

To eliminate these friction points, Google Threat Intelligence (Google TI) introduces the Scalable Collection Consumption Architecture. Powered by a hybrid **Batch & Feed API model**, this framework provides:

* **Dramatically Reduced Quota Usage:** Fetch up to 10,000 indicators per request using the [`/download/batch`](https://gtidocs.readme.io/reference/iocs-batch-download) endpoint, bypassing the strict 40-object pagination limits of legacy endpoints. Plus, empty responses do not count against your API quota.
* **Hourly Low-Latency Updates:** Ingest pre-correlated, lightweight `bzip2` delta packages every hour to catch exactly what changed via the [`/sync/ioc-deltas/`](https://gtidocs.readme.io/reference/ioc-deltas) endpoint, without re-downloading static data.
* **High-Fidelity Graph Mapping:** Dynamically rebuild complex Campaign, Threat Actor, and Malware relationships locally for deep structural analysis.

***

# 2.-prerequisites-&-authentication

Before initiating development, integrators must ensure their environment meets the following prerequisites:

* **API Key:** A valid, provisioned Google TI (VirusTotal) Enterprise API key. As a best practice, use [Service Account API keys](../02-group-management/admins-guide.md#1.3.-service-accounts-management) rather than individual user API keys.
* **Licensing Tier:** Access to the Enterprise or Enterprise +.
* **HTTP Client:** Support for handling compressed stream encoding (`bzip2`) and paginated REST operations.

## authentication

All requests must be authenticated using your API key supplied via the standard `x-apikey` header.

```json
"x-apikey": <YOUR_GTI_API_KEY>
```

***

# 3.-integration-workflow-&-suggested-flow

To ensure complete synchronization, the integration must operate in a continuous loop that handles both bulk discovery and incremental updates.

## the-suggested-flow

1. **Day 0: Initial Backfill:** Query the API to **[search](https://gtidocs.readme.io/reference/intelligence-search) for all historical *curated* collections** of interest and use the **[Batch](https://gtidocs.readme.io/reference/iocs-batch-download) endpoint to download their IoCs**.
2. **Day 1+: Steady State Delta Polling:** Poll the **hourly [IoC Delta feed](https://gtidocs.readme.io/reference/ioc-deltas)** to capture modifications, net-new indicators, and relationship removals.
3. **Continuous Discovery**: Periodically (e.g., every 6 hours) query the [Search](https://gtidocs.readme.io/reference/intelligence-search) API to identify newly created curated collections, and run a targeted [Batch](https://gtidocs.readme.io/reference/iocs-batch-download) backfill on just those new collections. **The process is similar to Day 0, but uses a different time filter for collection identification.**

> 📘
>
> Please note that all indicators from the **IoC Delta feed** are only **associated with Curated Collections such as (Actors, Campaigns, Malware, Software & Toolkits, Reports and Vulnerabilities) created or reviewed by the Google Threat Intelligence Group**.

## `/intelligence/search`---collections-search-endpoint

This [endpoint](https://gtidocs.readme.io/reference/intelligence-search) allows you to search for threat intelligence objects or collections relevant to your integration. For the workflow described in this guide, use it specifically to retrieve the **unique IDs of curated collections** rather than fetching the full dataset of collections. You will then pass these IDs as a path parameter to the `/collections/{collection_id}/{ioc_type}/download/batch` endpoint to download the associated IoCs.

Note that:

* **Response format:** This endpoint returns a JSON object containing all threat intelligence objects or collections based on the query parameter.
* **Filtering Parameters**:  For the purpose of this integration, you will use several **base filters** to target the right data:
  * `entity:collection`: Restricts the type of retrieved objects to collections.
  * `collection_type`: Filters by specific threat categories. The supported types are: `threat-actor`, `malware-family`, `software-toolkit`, `campaign`, `report`, and `vulnerability`.
  * `owner:Mandiant` and `origin:"Google Threat Intelligence"`: To isolate **curated collections** and exclude community-crowdsourced data.

    Note that even if you choose to include community objects, the `/collections/sync/ioc-deltas/{time}` endpoint used for IoC updates only tracks those containing relationships with curated collections. To apply a filter, append the `query` parameter to your request URL. E.g.: `/intelligence/search?query=owner:Mandiant AND origin:"Google Threat Intelligence" AND (collection_type:campaign OR collection_type:report)`. URL-safe encoding is required. Additional filters for each collection type are documented [here](https://gtidocs.readme.io/reference/list-collections#allowed-filters-by-object-collection_type). For instance, when performing your initial backfill, you can use the `lm:365d+` or `last_modification_date:365d+` filter to start with a smaller subset of collections rather than processing the entire dataset of curated collections.

The following [Implementation & Code Examples](#4-implementation--code-examples) section provides an advanced Python example.

## `/collections/{collection_id}/{ioc_type}/download/batch`---batch-endpoint

The **Batch** [endpoint](https://gtidocs.readme.io/reference/iocs-batch-download) is optimized **for TIP integrators** by allowing them to **fetch up to 10,000 indicators per page** associated with threat intelligence objects or collections. This lets you pull large batches of JSON-represented IoCs while bypassing the strict 40-object pagination limits of legacy endpoints. Empty responses do not count against your API quota.

* **Impact:** The largest collections (approx. 4M items) would require \~400 calls, compared to thousands currently. 99% of collections will be retrievable in 1-5 calls.

Note that:

* **Response format:** The IoC batch download endpoint returns a JSON object containing all indicators associated with a collection or threat intelligence object based on the path and query parameters, with the list of IoCs nested inside a standard `data` field.
* **Pagination**: The accompanying `meta` object within the JSON response provides key metadata, including a `cursor` token to retrieve subsequent pages.
* **Path Parameters**: It requires two path parameters: the `collection_id`, which is the ID of the relevant curated collection identified via the `/intelligence/search` endpoint as described in the previous section, and the `ioc_type`, which restricts the download to a specific indicator type associated with that collection. Supported `ioc_type` values are: `files`, `urls`, `domains` and `ip_addresses`.
* **Filtering Parameters**: This endpoint allows you to filter your results using several parameters detailed in [Appendix 1](#appendix-1-filters). For example, you can filter indicators by their last modified date or creation date. Alternatively, if you want to focus strictly on maliciousness, you can filter by Google TI verdict or AV engine detections. To apply a filter, simply append the `filter_query` query parameter to your request URL. For instance, to filter by IoCs with 10 or more AV engine detections, construct your URL like this: `/collections/{collection_id}/{ioc_type}/download/batch?filter_query=p:10+`. URL-safe encoding is required.
* **IoCs Attributes**: This endpoint allows you to specify which fields from [Appendix 2](#appendix-2-attributes) to be returned for each IoC by appending the `attributes` query parameter to your request URL. For instance, to retrieve only the `gti_assessment` and `tags` fields for the indicators, construct your URL like this: `/collections/{collection_id}/{ioc_type}/download/batch?attributes=gti_assessment,tags`. URL-safe encoding is required.

> 📘
>
> Note that unlike the delta synchronization endpoint `/collections/sync/ioc-deltas/{time}`, the batch download response **does not explicitly include a field connecting the IoC back to the requested curated collection**. If your local database requires this relationship from Day 0, you can manually **inject a custom relationships field into the JSON payload before saving it**. To keep your parsing logic consistent, you can **model this custom field after the schema used by the&#x20;**`/collections/sync/ioc-deltas/{time}`**&#x20;endpoint**.
>
> Keep in mind that **a single IoC can belong to multiple curated collections simultaneously**. If you run batch downloads across different collections, the same IoC may appear in multiple responses, representing its association with different curated objects. If you want to keep relationships with other collections as well, check your local system first when injecting a relationships field into the JSON and ensure your local data stays in sync with the new payload.

The following [Implementation & Code Examples](#4-implementation--code-examples) section provides an advanced Python example, while the [Requests and Responses Examples](#7--requests-and-responses-examples) section contains sample API payloads.

## `/collections/sync/ioc-deltas/{time}`---ioc-delta-feed-endpoint

This **IoC Delta feed** is a rolling update built on Google TI's battle-tested feed architecture. The backend system generates **minute-based packages of updated IoCs**, which are then combined into a larger **hourly package** by a secondary service.

This [endpoint](https://gtidocs.readme.io/reference/ioc-deltas) allows you to sync your local data generated via the `/intelligence/search` and `/collections/{collection_id}/{ioc_type}/download/batch` endpoints, with recent updates or modifications made to IoC analysis reports.

Note that:

* **Time Frame**: This endpoint requires a `YYYYMMDD` (UTC) parameter for the requested feed time. Data is available for the trailing 7 days, with a rolling 2-hour delay/lag for the most recent batch.
* **Response format:** The feed is distributed as a compressed `bzip2` package. Once decompressed, the package contains a sequence of JSON objects directly (one per line and indicator).
* **Unordered Data:** The resulting JSON packages are not ordered deterministically.
* **Duplication:** Because of the minute-to-hourly rollup, if an IoC is updated multiple times within a single hour, it may appear multiple times within the same hourly package.
* **Temporal Relevance:** The feed contains IoCs that have been **updated within the specific time window** corresponding to the feed generation hour period.
* **Curated Association:** It includes indicators strictly associated with **curated Collections generated by the Google Threat Intelligence team**, ensuring high-fidelity alerting and reduced false positives for security operations teams.

### the-golden-rule:-`last_modification_date`

Because the feed is unordered and may contain multiple update states for a single IoC, **integrators must always check the&#x20;**`last_modification_date`**&#x20;against their local system**. Only overwrite your local record if the incoming date is strictly newer; this prevents newer information from being overwritten by older, "stale" data.

### handling-removals-(deletions)

The Google TI API does not emit explicit "delete" events. Instead, removals are signaled through state updates. When an IoC is updated in the feed, its `relationships` object contains distinct dictionaries, each containing a list of associated elements. For the purposes of this document, focus on the elements under the following fields:

* `malware_families`
* `threat_actors`
* `software_toolkits`
* `reports`
* `vulnerabilities`

Elements of interest should mirror the object types selected during your initial Day 0 searches via the `/intelligence/search` endpoint. Note that only curated relationships are included in these lists.

> 📘
>
> Note that the absence of a collection in this new `relationships` object, when compared to your local system, signals to the client that the IoC has been removed from that collection and the relationship between the IoC and the curated collection no longer exist.

The following [Implementation & Code Examples](#4-implementation--code-examples) section provides an advanced Python example, while the [Requests and Responses Examples](#7--requests-and-responses-examples) section contains sample API payloads.

***

# 4.-implementation-&-code-examples

> 🚧
>
> The code blocks provided below are strictly illustrative examples intended to demonstrate the logic. Partners should adapt and harden this code to their own enterprise-grade infrastructure, adding robust logging, retries, and local state management.

> ❗️
>
> **Mandatory Telemetry Header**
>
> Every single request (both [Batch](https://gtidocs.readme.io/reference/iocs-batch-download) and Delta Feed) **must include the&#x20;**`X-Tool`**&#x20;header.** This allows Google TI support teams to properly identify your TIP and troubleshoot issues.
>
> `X-tool: <Integration_Name>/<Version>`

## step-1:-new-collection-discovery-(day-0)

Use the `/v3/intelligence/search` [endpoint](https://gtidocs.readme.io/reference/intelligence-search) to automatically discover collections updated or created within a specific timeframe. Obtain the **IDs** of the collections we want to download. In this case, these will be the malware families, threat actors, campaigns and curated reports edited within the last year.

**Note the curated collections filters:&#x20;**`owner:Mandiant origin:"google threat intelligence"`

```python
from datetime import datetime, timedelta
import time
import requests

URL = 'https://www.virustotal.com/api/v3/intelligence/search'

total_api_calls = 0

# Calculate the date for one year ago
one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

# Malware families, threat actors, campaigns and reports
query = (
    f'entity:collection lm:{one_year_ago}+ owner:Mandiant '
    'origin:"google threat intelligence" AND '
    '(collection_type:threat-actor OR collection_type:malware-family OR '
    'collection_type:report OR collection_type:campaign)'
)

params = {
    'query': query,
    'limit': 300,
    'attributes': 'collection_type',
}
counters = Counter()
collection_ids = []
start_time = time.time()

next_url = URL

print(f'Searching for: {query}\n')

while True:
    response = requests.get(
        next_url,
        headers=HEADERS,
        params=params if next_url == URL else None,
    )
    response.raise_for_status()
    data = response.json()

    items = data.get('data', [])
    for obj in items:
        collection_ids.append(obj.get('id'))
        c_type = obj.get('attributes', {}).get('collection_type', 'unknown')
        counters[c_type] += 1

    total_api_calls += 1
    next_url = data.get('links', {}).get('next')
    if not next_url:
        break

elapsed_time = time.time() - start_time

print('\nCollection Type Counts:')
for c_type, count in counters.items():
    print(f'- {c_type}: {count}')

print(f'\nCollections ingested: {len(collection_ids)}')
print(f'Time elapsed: {elapsed_time:.2f} seconds')
print(f'Total API calls: {total_api_calls}')

with open(f'{DRIVE_PATH}/collection_ids.json', 'w') as f:
    json.dump(collection_ids, f, indent=4)
```

## step-2:-extract-iocs-(day-0)

To manage interruptions during long processes and prevent duplicate effort, a checkpointing system has been implemented. This system saves the results of each processed collection to a JSON file at regular intervals. If execution is interrupted, restarting the process will allow the code to load previous progress from the file and continue processing only the collections that have not yet been completed.

While this mechanism is set up for Google Drive in this example, you can implement a similar recovery mechanism for your own backfill operations, especially since they can last for several hours.

**Note that&#x20;**`/collections/{collection_id}/{ioc_type}/download/batch`**[endpoint](https://gtidocs.readme.io/reference/iocs-batch-download) calls with zero IoCs do not count against customer quota and this endpoint doesn't provide the&#x20;**`relationships`**&#x20;objects for IoCs.**

```python
import json
import requests
import time

# File to store checkpoint data
CHECKPOINT_FILE = f'{DRIVE_PATH}/collection_processing_results.json'

with open(f'{DRIVE_PATH}/collection_ids.json', 'r') as f:
    collection_ids = json.load(f)

# Try to load existing results if the checkpoint file exists
try:
    with open(CHECKPOINT_FILE, 'r') as f:
        all_collection_results = json.load(f)
    processed_collection_ids = {res['collection_id'] for res in all_collection_results}
    print(
        f'Loaded {len(all_collection_results)} previously '
        f'processed collections from {CHECKPOINT_FILE}'
    )
except FileNotFoundError:
    all_collection_results = []
    processed_collection_ids = set()
    print('No previous checkpoint file found. Starting fresh.')

# Filter collection_ids to only process those not already processed
collections_to_process = [c_id for c_id in collection_ids if c_id not in processed_collection_ids]
print(f'Total collections found: {len(collection_ids)}')
print(f'Collections to process in this run: {len(collections_to_process)}')

relationships = ['files', 'ip_addresses', 'domains', 'urls']
start_time_batch = time.time()
last_collection_time = start_time_batch
collections_processed = 0

def get_iocs(rel_url: str, cursor: str = None):
  try:
    return requests.get(
        rel_url,
        headers=HEADERS,
        params={'cursor': cursor} if cursor else None,
        timeout=10,
    )
  except Exception as e:
      print('  Retrying...')
      return requests.get(
        rel_url,
        headers=HEADERS,
        params={'cursor': cursor} if cursor else None,
        timeout=30,
    )

for i, c_id in enumerate(collections_to_process, 1):
    counts = {rel: 0 for rel in relationships}
    api_calls = 0

    for rel in relationships:
        # URL for the specific relationship
        rel_url = f'https://www.virustotal.com/api/v3/collections/{c_id}/{rel}/download/batch'
        cursor = None

        while True:
            try:
                resp = get_iocs(rel_url, cursor)
                api_calls += 1
                resp.raise_for_status()
                rel_data = resp.json()

                batch_items = rel_data.get('data', [])
                counts[rel] += len(batch_items)

                # Handle pagination
                cursor = rel_data.get('meta', {}).get('cursor')
                if not cursor:
                  break

            except Exception as e:
                print(f'Error fetching {rel} for {c_id}: {e}')
                break

    current_collection_time = time.time()
    collection_time = current_collection_time - last_collection_time

    result = {
        'collection_id': c_id,
        'files': counts["files"],
        'ip_addresses': counts["ip_addresses"],
        'domains': counts["domains"],
        'urls': counts["urls"],
        'api_calls': api_calls,
        'time_taken': collection_time,
    }
    all_collection_results.append(result)

    print(
        f'{len(processed_collection_ids) + i}. Collection: {c_id}. '
        f'Files: {counts["files"]}, '
        f'IPs: {counts["ip_addresses"]}, '
        f'Domains: {counts["domains"]}, '
        f'URLs: {counts["urls"]}, '
        f'API calls: {api_calls}, '
        f'Time: {collection_time:.2f} seconds'
    )
    last_collection_time = current_collection_time
    collections_processed += 1

    # Save checkpoint periodically (e.g., every 50 collections)
    if i % 50 == 0:
        with open(CHECKPOINT_FILE, 'w') as f:
            json.dump(all_collection_results, f, indent=4)
        print(f'Checkpoint saved after {len(processed_collection_ids) + i} collections.')

# Save final results after the loop completes
with open(CHECKPOINT_FILE, 'w') as f:
    json.dump(all_collection_results, f, indent=4)
print(f'Final results saved to {CHECKPOINT_FILE}')

elapsed_time_batch = time.time() - start_time_batch

# Calculate totals from cumulative results
total_time = sum(res.get('time_taken', 0) for res in all_collection_results)
total_api_calls = sum(res.get('api_calls', 0) for res in all_collection_results)

total_quota_calls = total_api_calls
for res in all_collection_results:
    # Subtract 1 for each zero-value relationship as per user request
    for rel in ['files', 'ip_addresses', 'domains', 'urls']:
        if res.get(rel) == 0:
            total_quota_calls -= 1

print(f'\n--- Batch Processing Summary ---')
print(f'Collections processed in this run: {collections_processed}')
print(f'Total collections processed (cumulative): {len(all_collection_results)}')
print(f'Time elapsed for this batch run: {elapsed_time_batch:.2f} seconds')

print(f'Total cumulative time: {total_time:.2f} seconds')
print(f'Total cumulative API calls: {total_api_calls}')
print(f'Total API calls consuming quota: {total_quota_calls}')
```

## step-3:-steady-state-ioc-deltas-(day-1+)

The previous steps (1 and 2) were intended to perform the initial backfill of IoCs from relevant collections. This step, however, marks a paradigm change, as it functions as a continuous feed providing the latest updates for the IoCs already included in the backfill. This ensures that your threat intelligence remains current and accurate.

**Note that this&#x20;**`/collections/sync/ioc-deltas/{time}`**&#x20;feed [endpoint](https://gtidocs.readme.io/reference/ioc-deltas) is intended to be called every hour for each IoC type. 96 fixed calls per day.**

**Note that this endpoint provides the&#x20;**`relationships`**&#x20;objects for IoCs.**

```python
import bz2
import io
import json
import requests
import tarfile

package = '2026032712'

response = requests.get(
    f'https://www.virustotal.com/api/v3/collections/sync/ioc-deltas/{package}',
    headers=HEADERS,
    params={'ioc_type': 'file'},
    timeout=10,
)

response.raise_for_status()
decompressed_data = bz2.decompress(response.content)

all_iocs = []

with io.BytesIO(decompressed_data) as f_bytes:
    with tarfile.open(fileobj=f_bytes, mode='r') as tar:
        # Iterate through every file (member) in the tar archive
        for member in tar.getmembers():
            if member.isfile():
                extracted_file = tar.extractfile(member)
                if extracted_file:
                    # Read line by line to handle NDJSON (Newline Delimited JSON)
                    for line in extracted_file:
                        line = line.decode('utf-8').strip()
                        if line:
                            try:
                                all_iocs.append(json.loads(line))
                            except json.JSONDecodeError as e:
                                print(f'Skipping invalid line in {member.name}: {e}')

print(f'Successfully processed {len(all_iocs)} IoCs from all files in the archive.')

# Save the processed data
# OUTPUT_FILE = f'{DRIVE_PATH}/extracted_iocs_{package}.json'
# with open(OUTPUT_FILE, 'w') as f:
#     json.dump(all_iocs, f, indent=4)
# print(f"Data saved to: {OUTPUT_FILE}")

# Display first element as sample
if all_iocs:
    print('\nSample IoC:')
    print(json.dumps(all_iocs[0], indent=2))
```

***

# 5.-best-practices:-rate-limiting-&-error-handling

* **Handling HTTP 429s:** Implement standard exponential backoff and jitter when encountering HTTP 429 (Too Many Requests) response codes to gracefully wait before retrying.
* **Quota Optimization:** If an API call (Batch or Feed) results in 0 IoCs, it will appear in the UI summary for audit purposes but will not count against your API quota. Additionally, each call to the `ioc-deltas` endpoint counts as 1 call against your quota, regardless of how many indicators are in the compressed package.
* **Idempotency (**`last_modification_date`**):** Always compare the `last_modification_date` of the incoming IoC to your local records. Only update your database if the incoming date is strictly newer, preventing stale data from overwriting recent updates.
* **Handling Deletions:** Google TI does not emit explicit "delete" events. If an IoC is removed from a collection, it republishes in the Delta Feed with an updated `relationships` object. Always ensure your system treats the latest relationships lists as the source of truth, removing any local relationships that are missing from the latest update.

***

# 6.-frequently-asked-questions-(faq)

**Q: How do I map indicators to their collections using the Batch download endpoint?**

**A:** To conserve payload bandwidth, the Batch download endpoint does not include the `relationships` metadata block. Integrators must correlate indicators locally to the specific Collection ID specified in the URL path when downloading.

**Q: If there are no explicit "delete" events, how do I know when an indicator is removed from a collection?**

**A:** When an indicator is removed from a collection, the indicator is published in the Delta feed with updated `relationships` object. Compare the new `relationships` against your local state, and if a previously associated collection ID is missing, you should remove it locally.

**Q: How do I prevent data regressions during the overlap between the Batch backfill and starting the Delta feed?**

**A:** You must implement a mandatory `last_modification_date` check. Replay the Delta feed from the timestamp you started the Batch process. Because the feed is built on the Google TI model, any "stale" updates caught in this overlap will be safely ignored if you strictly ensure incoming dates are newer than your local records.

**Q: Can I "replay" the feed if my integration goes offline?**

**A:** Yes. The Delta Feed supports a lookback of up to 7 days. If your integration is offline for a period, you can "replay" the feed from your last successful timestamp within this window.

***

# 7.-requests-and-responses-examples

## 7.1.-batch-endpoint

**[Endpoint](https://gtidocs.readme.io/reference/iocs-batch-download)**: `/collections/{collection_id}/{ioc_type}/download/batch`

Note that the Batch endpoint does not include the `relationships` block to save bandwidth. You must correlate these locally based on the URL parameter.

**The maximum limit is 10,000 objects per response.**

For request and response payload examples, please refer directly to the [Batch Endpoint Reference examples](https://gtidocs.readme.io/reference/iocs-batch-download#request-and-response-examples).

## 7.2.-ioc-delta-feed-endpoint

**[Endpoint](https://gtidocs.readme.io/reference/ioc-deltas)**: `/collections/sync/ioc-deltas/{time}`

> 📘
>
> Feed Delivery: The feed is distributed as a compressed bzip2 package. Once decompressed, the package contains a sequence of JSON objects directly (one per indicator)

For request and response payload examples, please refer directly to the [IoC Delta Feed Endpoint Reference examples](https://gtidocs.readme.io/reference/ioc-deltas#request-and-response-examples).

***

# appendix-1:-filters

The bulk export endpoint will support filtering capabilities, as detailed below.

| Filter Parameter                   | Description                                      | Supported Types           |
| :--------------------------------- | :----------------------------------------------- | :------------------------ |
| **creation\_date**                 | **IoC creation date**                            | **file, domain**          |
| **size (file\_size)**              | **File size**                                    | **file**                  |
| **fs (first\_submission)**         | **First submission date**                        | **file, url**             |
| **gti\_severity**                  | **Google TI calculated severity**                | **file, url, domain, ip** |
| **gti\_score**                     | **Google TI calculated score**                   | **file, url, domain, ip** |
| **gti\_verdict**                   | **Google TI calculated verdict**                 | **file, url, domain, ip** |
| **la (last\_analysis)**            | **Last analysis date**                           | **file, url**             |
| **lm (last\_modified)**            | **Last modification date**                       | **file, url, domain, ip** |
| **ls (last\_submission)**          | **Last submission date**                         | **file, url**             |
| **p (positives)**                  | **AV vendors detections**                        | **file, url, domain, ip** |
| **submissions (times\_submitted)** | **Times the file was submitted to the platform** | **file**                  |

# appendix-2:-attributes

The bulk export endpoint currently supports fetching attributes, as detailed below.

| Attribute                        | Supported Types           |
| :------------------------------- | :------------------------ |
| **as\_owner**                    | **ip**                    |
| **asn**                          | **ip**                    |
| **categories**                   | **url, domain**           |
| **continent**                    | **ip**                    |
| **country**                      | **ip**                    |
| **creation\_date**               | **file, domain**          |
| **first\_submission\_date**      | **file, url**             |
| **gti\_assessment**              | **file, url, domain, ip** |
| **jarm**                         | **domain, ip**            |
| **last\_analysis\_date**         | **file, url**             |
| **last\_final\_url**             | **url**                   |
| **last\_http\_response\_code**   | **url**                   |
| **last\_modification\_date**     | **file, url, domain, ip** |
| **last\_submission\_date**       | **file, url**             |
| **md5**                          | **file**                  |
| **names**                        | **file**                  |
| **positives**                    | **file, url, domain, ip** |
| **regional\_internet\_registry** | **ip**                    |
| **registrar**                    | **domain**                |
| **sha1**                         | **file**                  |
| **sha256**                       | **file, url**             |
| **size**                         | **file**                  |
| **tags**                         | **file, url, domain, ip** |
| **times\_submitted**             | **file, url**             |
| **title**                        | **url**                   |
| **url**                          | **url**                   |

---

← [Splunk integration guide](gti4splunk-guide.md) · [up](README.md) · [Palo Alto XSOAR integration guide](gti4xsoar-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/tip-integration-guide>.*
