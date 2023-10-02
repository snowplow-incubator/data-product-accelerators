+++
title = "Tracking"
chapter = true
weight = 2
pre = "2. "
post = ""
+++

# Tracking

{{<mermaid>}}
flowchart LR
    id1(Monitor)-->id2(Track)-->id3(Enrich)-->id4(Model)-->id5(Visualize)-->id6(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}


Get started with sending web performance events using the JavaScript tracker.

Once set-up, you will be able to send web performance data to your Snowplow pipeline.

{{% notice note %}}
Currently the web performance data collection methods and metrics are more fit towards multi-page applications. For single-page applications (_SPAs_), the required measurements will need to be refined in a different way.
**If you have questions on how single-page application web performance metrics can be measured and collected, you can reach out to us on [Discourse](https://discourse.snowplow.io/) or [Zendesk](https://snowplow.zendesk.com/) if you are on BDP Cloud or Enterprise!**

{{% /notice %}}
