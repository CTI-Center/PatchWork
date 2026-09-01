---
title: "🔀 historical_whois"
source: https://gtidocs.virustotal.com/reference/ip-object-historical-whois
slug: ip-object-historical-whois
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [IP addresses](../ip-object.md) › 🔀 historical_whois

---

# 🔀-historical_whois

All whois records associated with the IP address at some moment in time.

The*historical\_whois* relationship returns a list of whois records that have been associated with the IP address at some moment in time.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/ip-addresses/ip-relationships.md). The response contains a list of [Whois](../whois-object.md) objects.

```json /ip_addresses/{ip_address}/historical_whois
{
  "data": [
    <WHOIS_OBJECT>,
    <WHOIS_OBJECT>,
    ...
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
  },
  "meta": {
    "count": <int>,
    "cursor": "<string>"
  }
}
```
```json Example
{
    "data": [
        {
            "attributes": {
                "first_seen_date": 1575586655,
                "last_updated": 1572480000,
                "registrant_country": "US",
                "whois_map": {
                    "Address": "1600 Candy Street",
                    "CIDR": "172.217.0.0/16",
                    "City": "Candyland",
                    "Comment": "Please note that the recommended way to file abuse complaints are located in the following links. |  | To report abuse and illegal activity: https://www.foo.com/contact/ | For legal requests: http://support.foo.com/legal | Regards, | The Foo Team",
                    "NetHandle": "NET-192-917-0-0-1",
                    "NetName": "FOO",
                    "NetRange": "192.297.0.0 - 192.297.255.255",
                    "NetType": "Direct Allocation",
                    "OrgAbuseEmail": "network-abuse@foo.com",
                    "OrgAbuseHandle": "ABUSE5250-ARIN",
                    "OrgAbuseName": "Abuse",
                    "OrgAbusePhone": "+1-655-255-0000",
                    "OrgAbuseRef": "https://rdap.arin.net/registry/entity/ABUSE5250-ARIN",
                    "OrgId": "FOO",
                    "OrgName": "Foo LLC",
                    "OrgTechEmail": "bar-contact@foo.com",
                    "OrgTechHandle": "ZG39-BAR",
                    "OrgTechName": "FOO LLC",
                    "OrgTechPhone": "+1-656-266-0000",
                    "OrgTechRef": "https://foo.bar.net/registry/entity/ZG39-BAR",
                    "Organization": "Foo LLC (GOGL)",
                    "OriginAS": "AS15169",
                    "Parent": "NET172 (NET-192-0-0-0-0)",
                    "PostalCode": "94043",
                    "Ref": "https://foo.bar.net/registry/entity/FOO",
                    "RegDate": "2000-03-30",
                    "Registrant Country": "US",
                    "StateProv": "CA",
                    "Updated Date": "2019-10-31"
                }
            },
            "id": "57bd386ad836b3163defe9f346690a30d7b79f34491ae432ee735d61f3dfd580",
            "links": {
                "self": "https://www.virustotal.com/api/v3/whois/57bd386ad836b3163defe9f346690a30d7b79f34491ae432ee735d61f3dfd580"
            },
            "type": "whois"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/ip_addresses/1.2.3.4/historical_whois?limit=10"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 historical_ssl_certificates](ip-object-historical-ssl-certificates.md) · [up](../README.md) · [🔀 communicating_files](ip-object-communicating-files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-object-historical-whois>.*
