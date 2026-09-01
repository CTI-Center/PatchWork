---
title: "How to Set Entities Out of Scope"
source: https://gtidocs.virustotal.com/docs/how-to-set-entities-out-of-scope
slug: how-to-set-entities-out-of-scope
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:27:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Entities](../entities-guide.md) › How to Set Entities Out of Scope

---

# how-to-set-entities-out-of-scope

In Attack Surface Management (ASM), setting up an Entity to be out of the scope of a Collection will suppress the Entity and other related Entities from being populated in the Collection. You can do this two ways:

* From individual [**Entities**](../entities-guide.md)
* From [**Collections**](#settings-from-the-collections-page)

The following table characterizes Out of Scope settings:

| Page | Entity Type | Out of Scope by Pattern | Out of Scope Single Entity |
| --- | --- | --- | --- |
| Entities | <p>Url</p> | <div style={{ textAlign: "center" }}>✔</div> | <p><br /></p> |
| <p>Domain</p> | <div style={{ textAlign: "center" }}>✔</div><br><br /> | <p><br /></p> |  |
| <p>Subdomain</p> | <div style={{ textAlign: "center" }}>✔</div><br><br /> | <p><br /></p> |  |
| <p>Other Entities</p> | <br /> | <div style={{ textAlign: "center" }}>✔</div><br><br /> |  |
| Collections | <p>Url</p> | <div style={{ textAlign: "center" }}>✔</div> | <div style={{ textAlign: "center" }}>✔</div> |
| <p>Domain</p> | <div style={{ textAlign: "center" }}>✔</div><br><br /> | <div style={{ textAlign: "center" }}>✔</div> |  |
| <p>Subdomain</p> | <div style={{ textAlign: "center" }}>✔</div><br><br /> | <div style={{ textAlign: "center" }}>✔</div> |  |
| <p>Other Entities</p> | <br /> | <div style={{ textAlign: "center" }}>✔</div><br><br /> |  |

* **Out of Scope by Pattern:** ASM uses a regex pattern to define the scope of Entities suppressed based on the Entity added to the list.
* **Out of Scope Single Entity:** ASM will prevent the specified Entity from populating in the Collection.

## settings-from-the-entities-page

As an example, we select the **DNS Record** tab from the [ASM Entities page](http://asm.advantage.mandiant.com/entities).

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/outofscope_step1_20240430.png)

Choosing the first Entity listed, **cms.hooverandstrong.com** displays the details of the Entity. On the details page, we select **Add Out Of Scope Entity** and click **Submit**. The [regex](https://en.wikipedia.org/wiki/Regular_expression) pattern defined by this submission is `\bcms\.hooverandstrong\.com\b`.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/outofscope_step2_20240430.png)

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/outofscope_step3_20240430.png)

To confirm, we navigate to **Collections > Settings** for the relevant Collection and select the **Out of Scope** tab. Here, we find both the regex **Pattern** (`\bcms\.hooverandstrong\.com\b`) and **DnsRecord** Types listed for [cms.hooverandstrong.com](https://cms.hooverandstrong.com/).

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/outofscope_step4_20240430.png)

## settings-from-the-collections-page

1. Navigate to **Collections > Settings** and select a Collection.
2. Click **+** **Add Out Of Scope Entity**.

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/outofscope_step5_20240430.png)
3. Select an Entity **Type** from the dropdown and type its **Value**.
4. Choose "**Only out of scope this entity"** (Single Entity), or **Anything this Entity contains will be out-of-scoped** (Pattern). This second option will add an additional Out of Scope line item to the Collection based on the regex pattern, as described above.

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/outofscope_step6_20240430.png)
5. Click **Submit**.

   These items are now listed under the **Out of Scope** tab of the Collection.

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/outofscope_step7_20240430.png)

---

← [Entities](../entities-guide.md) · [up](../README.md) · [Scan History](scan-history.md) →

*Archived from <https://gtidocs.virustotal.com/docs/how-to-set-entities-out-of-scope>.*
