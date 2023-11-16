+++
title = "Connect Data Warehouse to Census"
weight = 1
+++

You can easily connect to Census from your data warehouse using either [Databricks Partner Connect](https://docs.databricks.com/integrations/partner-connect/reverse-etl.html) or [Snowflake Partner Connect](https://www.getcensus.com/blog/snowflake-partner-connect).

1. Make sure your data warehouse account, workspace, and the signed-in user all meet the necessary requirements for Partner Connect.
2. In the sidebar, click **Partner Connect**.
3. Find the Census tile. If the tile has a check mark icon, stop here, as your workspace is already connected. Otherwise, follow the on-screen directions to finish creating the connection.

![census_partner_connect](../images/census_partner_connect.png?width=40pc)

Once set-up you should see your new connection under the Sources tab in Census:

![census_sources](../images/census_sources.png?width=40pc)

Alternatively you can connect to Census manually with [Databricks](https://docs.getcensus.com/sources/databricks) or [Snowflake](https://docs.getcensus.com/sources/snowflake).
