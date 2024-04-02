+++
title = "Next Steps"
date = 2023-09-26T17:24:05+01:00
weight = 6
chapter = true
pre = "6. "
+++

# Next steps

{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Create Supporting Infrastructure)-->id3(Model)-->id4(Create Recommenders)-->id5(Interact with Recommenders)-->id6(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
{{</mermaid >}}

You may wish to keep your training dataset up to date with new users interactions and or new items that are added to your catalog. You may do this by either bulk uploading new data for the recommendation engine to train on or set up individual data import operations with event tracker. More information can be found [here](https://docs.aws.amazon.com/personalize/latest/dg/maintaining-relevance.html).