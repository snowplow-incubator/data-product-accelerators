+++
title= "Explore Snowplow data"
weight = 3
post = ""
+++

Processed data should now be loaded into your warehouse. In this section we will take a closer look at the output to get familiar with the derived tables.

***

#### **Step 1:** Check the output schemas

Head to the SQL editor of your choice (e.g. Snowflake Web UI) to check the model’s output. You should be able to see three new schemas created:

1. [your_custom_schema]_***scratch***: drop and recompute models that aid the incremental run
2. [your_custom_schema]_***derived***: main output models you can use in your downstream models and reporting
3. [your_custom_schema]_***snowplow_manifest***: tables that help the integrity and core incremental logic of the model

#### **Step 2:** Explore your data

Take some time to familiarize yourself with the derived tables. You could run a few simple queries such as the ones listed below. Make sure to modify the schema to be aligned with your custom dbt schema.

**Find out the top 10 regions your content is being played using `SNOWPLOW_MEDIA_PLAYER_PLAYS_BY_PAGEVIEW`:**

```sql
SELECT
  GEO_REGION_NAME,
  COUNT(DISTINCT PAGE_VIEW_ID) AS PAGE_VIEWS
FROM
  YOUR_CUSTOM_SCHEMA_DERIVED.SNOWPLOW_MEDIA_PLAYER_PLAYS_BY_PAGEVIEW
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10
```

**Find out details about your most watched content using `SNOWPLOW_MEDIA_PLAYER_MEDIA_STATS`:**

```sql
SELECT *
FROM
  YOUR_CUSTOM_SCHEMA_DERIVED.SNOWPLOW_MEDIA_PLAYER_MEDIA_STATS
ORDER BY PLAYS DESC
LIMIT 1
```

**Count the number of sessions where an ad reached more than 75% through using `SNOWPLOW_MEDIA_PLAYER_MEDIA_AD_VIEWS`:**

```sql
SELECT
  AD_ID,
  NAME,
  COUNT(DISTINCT SESSION_IDENTIFIER) AS SESSIONS
FROM
  YOUR_CUSTOM_SCHEMA_DERIVED.SNOWPLOW_MEDIA_PLAYER_MEDIA_AD_VIEWS
WHERE PERCENT_REACHED_75
GROUP BY 1,2
ORDER BY 3 DESC
```

**Calculate the click through rate to find your best performing ads using `SNOWPLOW_MEDIA_PLAYER_MEDIA_ADS`:**

```sql
SELECT
  AD_ID,
  NAME,
  SUM(CLICKED_UNIQUE) AS TOTAL_CLICKED_UNIQUE,
  SUM(VIEWS_UNIQUE) AS TOTAL_VIEWS_UNIQUE,
  SUM(CLICKED_UNIQUE)*100/SUM(VIEWS_UNIQUE) AS CTR
FROM
  YOUR_CUSTOM_SCHEMA_DERIVED.SNOWPLOW_MEDIA_PLAYER_MEDIA_ADS
GROUP BY 1,2
ORDER BY 5 DESC
LIMIT 10
```

Check out the **database** section of the [documentation site](https://docs.snowplow.io/docs/modeling-your-data/modeling-your-data-with-dbt/reference/snowplow_media_player/models/) for a full breakdown of what the output should look like.
