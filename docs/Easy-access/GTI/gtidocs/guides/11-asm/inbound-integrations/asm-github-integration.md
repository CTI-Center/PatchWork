---
title: "ASM GitHub Integration"
source: https://gtidocs.virustotal.com/docs/asm-github-integration
slug: asm-github-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:29:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › ASM GitHub Integration

---

# asm-github-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

> ℹ️
>
> See how credentials for integrations are stored [here](asm-credential-security-details.md)

Attack Surface Management (ASM) provides two GitHub workflows which result in different types of Entities and Issues. Our token-based GitHub integration works with both GitHub organizations and accounts. Depending on which method you choose, the ASM workflow varies.

* **Integrate with a GitHub Organization:** ASM locates all of the users belonging to the integrated organization and creates a `GithubAccount` Entity for each of them. 
* **Integrate with a GitHub Account:** ASM creates a `GithubAccount` Entity of the user the token belongs to and `GithubRepository` Entities for all the repositories the token has access to (including private repositories owned by other users).

This integration eliminates the need for manual entry of the same data as Seeds.

Integration with GitHub requires two steps:

1. [Create a GitHub Access Token](#create-a-github-access-token)
2. [Use GitHub Access Token for ASM Integration](#use-github-access-token-for-asm-integration)

## create-a-github-access-token

There are two types of access tokens you can create for the GitHub integration: Fine-grained or Classic. To create either type of token, sign in to GitHub and navigate to <https://github.com/settings/tokens>. Then follow the steps for the type of token you want to generate:

* [Fine-grained token (Beta)](#create-a-fine-grained-token-beta): Recommended by GitHub

* [Classic token](#create-a-classic-token): Less secure option 

> ℹ️
>
> * See [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to determine which token best suits your needs.\* See <https://github.com/settings/tokens> for more information on how to create a token to access the [GitHub API](https://docs.github.com/en/rest).

### create-a-fine-grained-token-(beta)

1. Navigate to **Personal Access tokens > Fine-grained tokens**.
2. Click **Generate new token**.

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_fine_grained_20240607.png)

3. Fill in the fields as follows:

* **Token name**: Enter a name such as ASM that's easy to remember.
* **Expiration**: Set this based on your organizations's requirements and swap out the token when it expires.
* **Description**
* **Resource owner**
* **Repository access**: Select the choice which best fits your organization’s requirements.
  * **Public Repositories (read-only)**
  * **All repositories**: This includes all current and future repositories you own.
  * **Only select repositories**: You must select at least one repository and no more than 50.
* **Permissions**

  * **Repository Permissions**: This subsection only appears if **All repositories** or **Only select repositories** is selected in the **Repository access** section. \
    \- Navigate to the **Contents** option and update this **Access** to **Read-only**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_contents_read_only_20240607.png)

* **Account Permissions**:\
  \- Optional: Navigate to the **Email addresses** option and update this **Access** to **Read-only**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_email_addresses_read_only_20240607.png)

> ℹ️
>
> Setting the Email addresses option to Read-only is recommended as this allows ASM to display the email with which the access token is associated. This makes it easier to differentiate between many GitHub integrations.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_fine_grained_details_20240607.png)

4. Click **Generate token**.
5. Finally, copy the token for use in ASM when establishing the integration.

> 🛑
>
> This token is only available until you navigate away from this page .

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_fine_grained_token_20240607.png)

### create-a-classic-token

1. Navigate to **Personal Access tokens > Tokens (classic)**. 
2. Click **Generate new token > Generate new token (classic)**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_classic_details1_20240607.png)

3. Fill out the mandatory fields as follows:

* **Note**: Enter a name such as ASM that's easy to remember.
* **Expiration**: Set this based on your organizations's requirements and swap out the token when it expires.
* **Select scopes**: Select the following options:

  * **repo**: Full control of private repositories
  * Optional: **user > user:email**: Access user email addresses (read-only)

    > ℹ️
    >
    > If enabled, the **user:email** scope allows ASM to display the email with which the access token is associated. This makes it easier to differentiate between many GitHub integrations.

4. Finally, copy the token for use in ASM when establishing the integration.
   > 🛑
   >
   > This token is only available until you navigate away from this page.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_classic_token_20240607.png)

## use-github-access-token-for-asm-integration

1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_account_settings_20240504.png)

2. Click **Integrations**.
3. From **Inbound Integrations**, click **Add New** for **Github.**

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_add_20240606.png)

4. Paste the **Github Access Token** value into the **Github Access Token** field and click **Connect**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_connect_20240607.png)

5. Connect the integration to the appropriate Collectio&#x6E;**.**

   * Click **Collections** and click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_engine_icon_20240509.svg) **Collection Settings** for the Collection that you want to connect the integration to.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_collections_20240604.png)

* Select the **Integrations** tab.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_configurations_20240604.png)

* Select **Connect Integration** and **Link** the integration.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_add_20240607.png)

* The integration is immediately added to the Collection.

> 💡
>
> ### Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_delete_icon.svg) to remove the integration from this Collection. ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_delete_20240604.png)

* Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_close_icon_20240509.svg) to close the **Connect Integration** pane. Click **Scan** **Collection** to update your Collection with the current settings and integrations. Otherwise, your newly configured integration is incorporated at your regularly scheduled scan interval.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_scan_20240604.png)

## keyword-seeds-and-the-github-integration

After integrating with GitHub, when a Seed is added (see [Creating & Seeding Collections](../create-a-collection.md)) and used, ASM works in the following ways:

* **GitHub Organization:** ASM locates the public users and creates `GithubAccount` Entities for them.
* **GitHub Account:** For each `GithubAccount` Entity, available repositories are created as `GithubRepository` Entities.
* **GitHub Repository:** ASM uses [Gitleaks](https://github.com/zricethezav/gitleaks) with a modified configuration file to detect items such as: common API keys, tokens, private keys, suspicious file names, or file extensions.

## an-example-use-case

This example illustrates a sample ASM GitHub tracking workflow.

In this example, the user adds a Seed, a `GithubAccount`: **"intrigueio."**

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_example_seed_20240612.png)

Using that `GithubAccount`, ASM finds 21 related Entities which include related repositories:

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_examples_entities_20240612.png)

Selecting the first `GithubAccount` Entity from this list displays the following page of detailed information:

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_example_details.png)

When a keyword is used as a Seed, ASM turns on the GitHub tracking workflow for this collection. Keywords can contain phrases and are not required to be one word. This keyword finds related GitHub Repositories and if any have leaked secrets, an Issue type of **"Suspicious commit"** is created.

Two limitations associated with this type of workflow include:

1. Choosing poor keywords or phrases can create an overload of irrelevant results. 
2. The API rate limit can result in incomplete search results.

If any Issues are found relating to that keyword, they show up as a **Suspicious Commit in Code Repository** Issue:

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_github_example_commit_20240612.png)

In some instances, you could find 1000 `GithubRepository` Entities from a keyword, and they could all have no leaked secrets. In this case, no Issues would be created but you would still have the Entities created.

---

← [ASM DNS Made Easy Integration](asm-dns-made-easy-integration.md) · [up](../README.md) · [ASM GoDaddy Integration](asm-godaddy-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-github-integration>.*
