---
position: 1
title: Organisations
description: The container for instances, members, usage, and billing, and what each section of the organisation view holds.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/organisations/index.mdx"
---

# Organisations

An organisation groups instances, members, usage, and billing.

Every instance, membership, and invoice belongs to exactly one organisation. Nobody in one organisation can see or change the resources of another.

Create one organisation for each company, department, or environment you keep apart. Separate organisations for production and development each get their own member list and their own invoice.

## Create an organisation

1. Open the overview page in [SurrealDB Studio](https://app.surrealdb.com).
2. Select **Create organisation**.
3. Enter a name for the organisation.
4. Confirm the name.

You become the [owner](members-and-roles.md), and Studio opens the organisation overview. The breadcrumb at the top of Studio switches between the organisations you belong to.

To create an organisation from a terminal, run `surrealctl org create`. `surrealctl org use` sets which organisation later commands apply to. See [surrealctl organisations](../surrealctl/organisations.md).

## The organisation view

The overview page shows everything the organisation holds. The sidebar leads into each area.

![The overview page for the Acme Corp organisation in SurrealDB Studio, listing the api-production, api-staging and analytics-eu instances with a Deploy new instance button, the support-agent and research-agent Agent Memory contexts below them, and a Resources panel linking to documentation, SurrealDB University, AI agents and community, with a sidebar holding Overview, Instances, Contexts, Connections, Team, Billing, Support, Usage and Settings.](../../assets/img/surrealdb/manage/studio-overview.webp)

| Section | What it holds |
| --- | --- |
| **Instances** | Every [instance](../instances/index.md) in the organisation. Deploy, open, and filter them here. |
| **Team** | [Members, invitations, and roles](members-and-roles.md). |
| **Billing** | [Billing details, payment method, discount codes, and invoices](billing.md). |
| **Usage** | [Compute, storage, and spend](billing.md#usage-and-spend) for the current or previous month. |
| **Support** | [Support plans and tickets](support.md). |
| **Settings** | The organisation name and its id. |

**Contexts** and **Connections** hold [SurrealDB Agent Memory](https://surrealdb.com/docs/agent-memory) resources rather than database instances. They use the same organisation for access and billing.

Your role decides what you see. A member without billing permissions does not see the **Billing** section. See [Members and roles](members-and-roles.md).

## Organisation settings

**Settings** holds two values: the display name, which you can change at any time, and the organisation id.

![The Settings page for the Acme Corp organisation in SurrealDB Studio, with an editable Name field, a read-only Organisation ID field with a copy button noting the id may be requested by the SurrealDB support team, and a Save changes button.](../../assets/img/surrealdb/manage/organisation-settings.webp)

Quote the organisation id when you raise a [support ticket](support.md). The id names one organisation exactly, where a display name might not.

Organisations cannot be deleted at present. Delete the instances inside an organisation you have finished with, and it stops accruing charges.

## Topics

- **[Accounts and sign-in](sign-in.md):** Create an account and sign in.
- **[Members and roles](members-and-roles.md):** Send invitations, and choose what each member can do.
- **[Billing](billing.md):** Payment details, invoices, usage, and spend.
- **[Support](support.md):** Community help, support plans, and tickets.
- **[AWS Marketplace](aws-marketplace.md):** Subscribe and pay through AWS.
- **[Referrals](referrals.md):** The referral link and the rewards it earns.
- **[FAQs](faqs.md):** General, security, pricing, legal, and troubleshooting questions.

## Related pages

- **[Instances](../instances/index.md):** Deploy and operate databases inside an organisation.
- **[surrealctl organisations](../surrealctl/organisations.md):** Organisations, teams, invitations, and tokens from the command line.
