+++
title = "Create Supporting Infrastructure"
date = 2023-09-26T17:24:05+01:00
weight = 2
chapter = true
pre = "2. "
+++

# Create the infrastructure needed to run AWS Personalize

{{<mermaid>}}
flowchart LR
    id1(Upload)-->id2(Create Supporting Infrastructure)-->id3(Model)-->id4(Create Recommenders)-->id5(Interact with Recommenders)-->id6(Next steps)
    style id1 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id2 fill:#f5f5f5,stroke:#6638B8,stroke-width:3px
    style id3 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id4 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id5 fill:#f5f5f5,stroke:#333,stroke-width:1px
    style id6 fill:#f5f5f5,stroke:#333,stroke-width:1px
{{</mermaid >}}


In this chapter you will create the AWS infrastructure needed to run AWS Personalize, including the necessary IAM roles and policies. 
You will also create a bucket in S3 to store your data. You will also create the storage integration and stage in Snowflake, if using.