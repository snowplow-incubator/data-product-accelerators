+++
title = "Introduction"
menuTitle = "Introduction"
pre = "<i class='fas fa-rocket'></i> "
chapter = false
weight = 1
+++

### Web Performance Accelerator

#### Introduction

This accelerator will show you how to track and model raw [core web vital](https://web.dev/vitals/) events so that you can monitor your website's performance via the most essential metrics. Improving the web performance can have a dramatic impact on how your users view and interact with your website with the potential to maximize your revenue.

Here you will learn to:

- Learn how you can monitor your website's performance
- Set-up Snowplow Tracking and Enrichment to prepare your data sources
- Model Snowplow data
    - using the `core web vitals` optional module of the [snowplow_web](https://hub.getdbt.com/snowplow/snowplow_web/latest/) dbt package
- See it all come together in a Tableau dashboard
***

#### Who is this guide for?

Data practitioners who would like to:
- Easily capture `core web vitals` on their website using the Javascript tracker
- Report and visualize the proportion of vitals [within target](https://web.dev/vitals/#core-web-vitals) using Tableau

***

#### What you will learn

In an estimated minimum of a day (~5.5 hours) you can achieve the following:

- **Monitor -** Learn why and how you can monitor your website's performance
- **Track -** Set-up and deploy tracking needed for your website performance data
- **Enrich -** Add an enrichment to your data
- **Model -** Configure and run the [core web vitals](https://docs.snowplow.io/docs/modeling-your-data/modeling-your-data-with-dbt/dbt-models/dbt-web-data-model//core-web-vitals-module/) module of the `snowplow-web` data model
- **Visualize -** Use the Tableau twbx template (csv based!) to gain insight into your own website's health
- **Next steps -** Gain more in-depth knowledge on web performance with additional metrics


{{<mermaid>}}
gantt
dateFormat HH-mm
axisFormat %H:%M
section 1. Monitor
30min :monitor, 00-00, 30m
section 2. Track
1h :track, after monitor, 1h
section 3. Enrich
1h :enrich, after track, 1h
section 4. Model
1h :model, after enrich, 1h
section 5. Visualize
1h :visualize, after model, 1h
section 6. Next steps
1h :next steps, after visualize, 1h

{{</mermaid >}}

***

#### Prerequisites

- It is assumed that you are already familiar with the [snowplow-web](https://hub.getdbt.com/snowplow/snowplow_web/latest/) dbt package. If not, we recommend completing the [Advanced Analytics for Web](https://docs.snowplow.io/accelerators/web) accelerator.

**Tracking and Enrichment**
- Snowplow pipeline
- Web app to implement tracking

**Modeling**
- dbt CLI installed / dbt Cloud account available
- New dbt project created and configured
- Snowflake, Databricks or BigQuery account and a user with access to create schemas and tables

{{< tableau name="SnowplowCoreWebVitals/CoreWebVitals?publish=yes" />}}
