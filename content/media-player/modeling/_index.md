+++
title = "Modeling"
weight = 3
chapter = true
pre = "2. "
+++

# Modeling your Data

{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Model)-->id3(Visualize)-->id4(Track)-->id5(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}

The [snowplow-media-player](https://github.com/snowplow/dbt-snowplow-media-player) dbt package transforms and aggregates the raw media event data collected by the Snowplow JavaScript tracker or iOS and Android trackers in combination with media tracking specific plugins: [Media plugin](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/javascript-tracker/javascript-tracker-v3/plugins/media/), [HTML5 media player plugin](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/javascript-tracker/javascript-tracker-v3/plugins/media-tracking/), [YouTube plugin](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/javascript-tracker/javascript-tracker-v3/plugins/youtube-tracking/), [Vimeo plugin](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/javascript-tracker/javascript-tracker-v3/plugins/vimeo-tracking/) or the [iOS and Android media APIs](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/).

In this chapter you will learn how to enable and run the snowplow-meida-player package.
