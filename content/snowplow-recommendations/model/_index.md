+++
title = "Model"
date = 2023-09-26T17:24:05+01:00
weight = 3
chapter = true
pre = "3. "
+++

# Model the data for AWS Personalize

{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Create Supporting Infrastructure)-->id3(Model)-->id4(Create Recommenders)-->id5(Interact with Recommenders)-->id6(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}


In this chapter you will create the data needed for AWS Personalize using the dbt-snowplow-recommendations package. This package, as well as creating the data needed, also stages the data in S3 using an on-run-end hook. This means that you don't have to manually load the data to S3.