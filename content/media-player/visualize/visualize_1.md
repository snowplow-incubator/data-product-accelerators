+++
title = "Visualize your data"
weight = 1
post = ""
+++

Now that you have modeled data you would probably want to see the results in a visual way as well to be able to easily to identify patterns and trends in your data.

We have created a Tableau workbook to showcase how you could do that, using csvs that were exported from the derived core web vitals tables (`snowplow_media_player_media_stats`, `snowplow_media_player_plays_by_pageview`, `snowplow_media_player_media_ads`, `snowplow_media_player_media_ad_views`).

If you would like to see your own modeled data you can simply change the data sources and then you will be able to look at the visualizations to get inspiration of what you can build with your connector of choice (based on the warehouse you have).

#### Accessing the sample Tableau workbook

You can download the file [here](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/media_player/snowplow_media_player_tableau_demo.twbx).

In case you need the source csvs, you can access them here:
* [snowplow_media_player_media_stats](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/media_player/snowplow_media_player_media_stats.csv)
* [snowplow_media_player_plays_by_pageview](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/media_player/snowplow_media_player_plays_by_pageview.csv)
* [snowplow_media_player_media_ads](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/media_player/snowplow_media_player_media_ads.csv)
* [snowplow_media_player_media_ad_views](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/media_player/snowplow_media_player_media_ad_views.csv)

Once you have the file locally, you can open it in several ways: with Tableau Public, Tableau Reader (free) or by uploading it to Tableau Online, if you have access.

#### Change the dashboard data source

1. Export your `snowplow_media_player_media_stats`, `snowplow_media_player_plays_by_pageview`, `snowplow_media_player_media_ads` and `snowplow_media_player_media_ad_views` derived tables as csvs with your sql editor of choice.

2. In Tableau Public or Tableau Online open the sample twbx file.
3. Right-click the data source you wish to edit in the data pane.
4. From the menu, select Edit Connection.
5. In the Edit Connection dialog box, you have two options:
    - Navigate to the new location of the data source by browsing your computer's file system.
    - Select a new data source altogether by clicking on the Browse button and choosing a different file.
6. After you have selected the new location or data source, select OK to save the changes.

You should have a working dashboard with your own data! Feel free to pick and choose visualizations and dashboards to make your custom one.

{{< tableau name="MediaPlayerAccelerator/Overview?publish=yes" />}}
