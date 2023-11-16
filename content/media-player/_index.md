+++
title = "Advanced Analytics for Media Player"
menuTitle = "Introduction"
pre = "<i class='fas fa-rocket'></i> "
chapter = false
weight = 1
+++

Welcome to the **Video and Media Analytics** accelerator. Once finished, you will be able to build a deeper understanding of user behavior across your media players and use your data to influence business decisions.

Here you will learn to:

* Model and Visualize Snowplow data
  - using the [snowplow-media-player](https://hub.getdbt.com/snowplow/snowplow_media_player/latest/) dbt package and Tableau
  - using our sample data for Snowflake, Databricks or BigQuery (no need to have a working pipeline)
* Set-up Snowplow Tracking
* Apply what you have learned on your own pipeline to gain insights

***

#### Who is this guide for?

- Data practitioners who would like to get familiar with Snowplow data.
- Data practitioners who want to learn how to use the snowplow-media-player dbt package and set-up tracking using their media players, to gain insight from their users' behavioral data as quickly as possible.

***

#### What you will learn

In approximately 8 working hours you can achieve the following:

- **Upload data -** Upload a sample Snowplow events dataset to your warehouse
- **Model -** Configure and run the snowplow-media-player data model
- **Visualize -** Visualize the modeled data with Tableau
- **Track -** Set-up and deploy tracking across your media players
- **Next steps -** Gain value from your own pipeline data through modeling and visualization


{{<mermaid>}}
gantt
        dateFormat  HH-mm
        axisFormat %M
        section 1. Upload
        1h          :upload, 00-00, 1m
        section 2. Model
        1h          :model, after upload, 1m
        section 3. Visualize
        1h          :visualize, after model, 1m
        section 4. Track
        2h          :track, after visualize, 2m
        section 5. Next steps
        2h          :next steps, after track, 2m

{{</mermaid >}}

***

#### Prerequisites

**Modeling**
- dbt CLI installed / dbt Cloud account available
- New dbt project created and configured
- Snowflake, Databricks or BigQuery account and a user with access to create schemas and tables

**Tracking**
- Snowplow pipeline
- Media player to implement tracking

#### What you will build

**Video and Media Analytics Dashboard** - with Tableau

{{< tableau name="MediaPlayerAccelerator/Overview?publish=yes" />}}
