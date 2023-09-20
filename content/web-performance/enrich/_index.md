+++
title = "Enrich"
date = 2022-08-16T17:24:05+01:00
weight = 3
chapter = true
pre = "3. "
+++


# Enriching your Data

{{<mermaid>}}
flowchart LR
    id1(Monitor)-->id2(Track)-->id3(Enrich)-->id4(Model)-->id5(Visualize)-->id6(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}

Snowplow offers a large number of enrichments that can be used to enhance your event data. In this chapter we showcase the specific enrichments which you need or are advised to enable in your pipeline for most effective web performance data collection and analysis.