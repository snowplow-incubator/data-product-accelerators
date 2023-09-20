+++
title = "Modeling"
date = 2022-08-16T17:24:05+01:00
weight = 4
chapter = true
pre = "4. "
+++


# Modeling your Data

{{<mermaid>}}
flowchart LR
    id1(Monitor)-->id2(Track)-->id3(Enrich)-->id4(Model)-->id5(Visualize)-->id6(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}


To process raw events created by the Snowplow Web Vitals plugin (@snowplow/browser-plugin-web-vitals) we have included an optional module to model core web vital events in the [snowplow-web dbt package](https://hub.getdbt.com/snowplow/snowplow_web/latest/).

In this chapter you will learn how to enable and run the core web vitals module within the snowplow-web package.
