+++
title = "Interact with Recommenders"
date = 2023-09-26T17:24:05+01:00
weight = 5
chapter = true
pre = "5. "
+++

# Interact with recommenders

{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Create Supporting Infrastructure)-->id3(Model)-->id4(Create Recommenders)-->id5(Interact with Recommenders)-->id6(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}


In this chapter you will run a local Flask app that demonstrates how to interact with the recommenders created in AWS Personalize. You can send requests to the app via curl or python, or alternatively, you can use the provided html form. 