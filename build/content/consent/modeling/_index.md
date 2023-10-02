+++
title = "Modeling"
weight = 4
chapter = true
pre = "3. "
+++

<!-- ### Chapter 2 -->

# Modeling your Data

{{<mermaid>}}
flowchart LR
    id1(Track)-->id2(Enrich)-->id3(Model)-->id4(Visualize)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px

{{</mermaid >}}

To process raw events created by the Snowplow Enhanced Consent plugin we have included an optional module to model consent events in the [snowplow-web dbt package](https://hub.getdbt.com/snowplow/snowplow_web/latest/)

In this chapter you will learn how to enable and run the consent module within the snowplow-web package.
