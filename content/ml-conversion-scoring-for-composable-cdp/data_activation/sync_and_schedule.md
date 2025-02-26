+++
title = "Sync and Schedule"
weight = 3
+++

#### **Step 1:** Sync your audiences to your destinations

After setting up your required [destinations](https://docs.getcensus.com/destinations/overview) in Census you can sync up your new audiences.

![census_syncs](../images/census_syncs.png?width=40pc)


#### **Step 2:** Schedule your audience syncs

It is important that your audiences connected to these third party tools are always up to date and in sync with your Snowplow web data in the data warehouse.

One way you can ensure this is by using the [dbt Cloud sync trigger](https://docs.getcensus.com/basics/core-concept/triggering-syncs#dbt-cloud) to trigger syncs after the dbt Snowplow web model job finishes and the derived tables are updated.

![census_dbt_cloud_trigger](../images/census_dbt_cloud_trigger.png?width=40pc)
