+++
title = "Introduction"
menuTitle = "Introduction"
pre = "<i class='fas fa-rocket'></i> "
chapter = false
weight = 1
+++

### Recommendations Accelerator

#### Introduction

This accelerator will show you how to use the [AWS Personalize service](https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html) to create recommenders based on your Snowplow data, enabling you to provide personalized recommendations to your users. There are two domain use cases that are covered in this accelerator: ecommerce and video_on_demand. Although the instructions will generally reference both use cases, you can choose to do one or the other, or both.



In this accelerator, we will enable you to:

* Run dbt to transform your Snowplow data into a format that can be used by AWS Personalize
* Set up the infrastructure required to run AWS Personalize, including the necessary IAM roles and policies
* Create ecommerce and/or media (video_on_demand) recommenders in AWS Personalize
* Run a local Flask application to interact with AWS Personalize 
***

#### Who is this guide for?

- Data practitioners who are already familiar with dbt and Python, as well as running commands in the command line.
- Data practitioners who want to use AWS Personalize to create recommenders for either ecommerce or media (video_on_demand) based on their Snowplow data.
- Data practitioners who would like to learn with a hands-on approach about AWS Personalize and how it can be used to create recommenders, using sample data.
***

#### What will be covered

In an estimated minimum of 5.5 hours, you can achieve the following:

- **Upload -** Upload some sample data (optional)
- **Create Supporting Infrastructure -** Create the supporting infrastructure needed move your data from your warehouse to S3, including the necessary IAM roles and policies
- **Model -** Run dbt to transform your Snowplow data into a format that can be used by AWS Personalize
- **Create Recommenders -** Create recommenders in AWS Personalize
- **Interact with Recommenders -** Run a local Flask application to interact with AWS Personalize
- **Next Steps -** Learn about the next steps you can take to continue your journey with AWS Personalize
***

#### What will not be covered

- We will not be covering how to implement ecommerce or media tracking in this accelerator. We will also not be covering how to run the ecommerce or media dbt packages. If you would like to learn more about these, the [quickstart](https://docs.snowplow.io/docs/modeling-your-data/modeling-your-data-with-dbt/dbt-quickstart/ecommerce/) or [accelerator](https://docs.snowplow.io/accelerators/ecommerce/) for ecommerce or the [quickstart](https://docs.snowplow.io/docs/modeling-your-data/modeling-your-data-with-dbt/dbt-quickstart/media-player/) for media could be a good place to start (media accelerator coming soon).

<!-- TODO fix gantt chart styling - Section names overlap chart -->
{{<mermaid>}} 
gantt
        dateFormat  HH:mm
        axisFormat %H:%M
        section 1. Upload
        30min       :s1, 00:00, 00:30
        section 2. Create Supporting Infrastructure
        2h          :s2, after s1, 02:30
        section 3. Model
        30min       :s3, after s2, 03:00
        section 4. Create Recommenders
        1h          :s4, after s3, 04:00
        section 5. Interact with Recommenders
        1h          :s5, after s4, 05:00
        section 6. Next steps
        30min       :s6, after s5, 05:30
{{</mermaid>}}

{{% notice info %}}
The time guides are only a rough estimation. For example, if you use Terraform for Step 2, it will take significantly less time than if you follow the manual instructions.
{{% /notice %}}
***

#### Prerequisites

- If using Snowflake, you have ACCOUNTADMIN or the global CREATE STORAGE INTEGRATION privilege in your Snowflake account.
- You have the necessary permissions in AWS to create/update IAM roles and policies, create an S3 bucket, and create AWS personalize resources.

If you are not using the sample data: 
- An implementation of the dbt-snowplow-ecommerce package. This will have created the `snowplow_ecommerce_product_interactions` table, which is used by this dbt package to create the ecommerce dataset for AWS Personalize. If you don't have this table, you can create it by following the instructions [here](https://docs.snowplow.io/docs/modeling-your-data/modeling-your-data-with-dbt/dbt-quickstart/ecommerce/).
  
And/or

- An implementation of the dbt-snowplow-media-player package (>= 0.6.0). This will have created the `snowplow_media_player_base` table, which is used by this dbt package to create the video_on_demand dataset for AWS Personalize. If you don't have this table, you can create it by following the instructions [here](https://docs.snowplow.io/docs/modeling-your-data/modeling-your-data-with-dbt/dbt-quickstart/media-player/).

