+++
title = "Run snowplow_recommendations dbt package"
weight = 2
post = ""
+++

This dbt package gives you the option of creating tables for either Ecommerce or Media (video_on_demand) data, or both, if you have both types of data. You will need to specify in the `dbt_project.yml` file which tables you would like to create (instructions below).

For ecommerce, we will use the `snowplow_ecommerce_product_interactions` table created by the dbt-snowplow-ecommerce package to create the ecommerce dataset for AWS Personalize. 

For media, we will use the `snowplow_media_player_base` table created by the dbt-snowplow-media-player package to create the video_on_demand dataset for AWS Personalize.

By default, the items, users and interactions tables can be created for ecommerce, but only the interactions table can be created for video_on_demand. This is because the video_on_demand items table has required fields (e.g. genres) that aren't tracked in the media tracking plugins by default. You can write custom SQL to create the items and users tables for media if you have the [required fields](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-datasets-and-schemas.html) either in your snowplow events table or in a separate table. 
See expandable section for further instructions.

{{% expand "Creating items and users for video_on_demand" %}}
*Creating the items and users models for Video on Demand recommenders*

These instructions are for both items and users, but you can create just one if you only have the requirements for one.
1. Create macros in the macros folder of your project, called `create_media_items` and `create_media_users`. You can copy the formatting of the macros for ecommerce. 
2. Within the macros, write the SQL that will output tables with the required fields for items and/or users. You can find the required fields [here](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-datasets-and-schemas.html). The models are already set up to use the macros that you create.
3. Change the relevant models in the models section of your `dbt_project.yml` file to `+enabled: true`:
```
      snowplow_aws_personalize_media_items:
        +enabled: true
      snowplow_aws_personalize_media_users:
        +enabled: true
```
4. You will also need to add the model name(s) to the list of tables to export:
```
vars:
...
tables_to_export: ["snowplow_aws_personalize_media_interactions", "snowplow_aws_personalize_media_items"] # Add all tables that you want to export to AWS Personalize
```
5. Create a schema for each model in the aws_personalize_utilities/schemas/ folder. They must be named `media_items.avro` and `media_users.avro` for the python script that creates the recommenders to read them. You can copy the formatting of the ecommerce schemas or see the documentation [here](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-datasets-and-schemas.html).
{{% /expand %}}

#### **Step 1:** Update the vars in your `dbt_project.yml` file:
<!-- TODO: update these after media model finalised -->
```
vars:
  snowflake_stage_name: "SNOWFLAKE_STAGE_NAME_HERE"  # The name of the stage created in Snowflake - if you used Terraform, this was an output variable.
  tables_to_export: ["snowplow_aws_personalize_ecommerce_interactions", "snowplow_aws_personalize_ecommerce_items", "snowplow_aws_personalize_ecommerce_users"] # Add all tables that you want to export to AWS Personalize
  
  # Below are only for ecommerce
  ecommerce_product_source: "{{ source('ecommerce', 'snowplow_ecommerce_product_interactions') }}" # you will need to update the source in the schema.yml file to use your schema (and table if named differently).
  ecommerce_start_date: '2023-01-01' # Add the date that you want to start from (leave as '' if you want to use the look_back_days variable)
  ecommerce_end_date: '2023-01-31' # Add the date that you want to end on (leave as '' if you want to use the look_back_days variable)
  look_back_days: 31 # This is only used if no dates are specified, and it processes data from (current date - 1) minus the number of days specified here.
  ecommerce_product_categories_separator: '/' # The separator used in the product_category field in the ecommerce table
    
  # Below are only for media (video_on_demand) 
  snowplow__enable_youtube: true # set to true if the YouTube context schema is enabled
  snowplow__enable_whatwg_media: true # set to true if the HTML5 media element context schema is enabled
  media_start_date: '2003-11-23'
  media_end_date: '2023-08-31'
  media_look_back_days: 31

```

Update the models in your `dbt_project.yml` file, depending on which tables you want to create. The following configuration will create the ecommerce interactions, users and items tables, but no media tables:
```
models:
  snowplow_recommendations:
    # +schema: "recommendations"
    +materialized: table
    snowflake:
      enabled: "{{ target.type == 'snowflake' | as_bool() }}"
      snowplow_aws_personalize_ecommerce_interactions:
        +enabled: true
      snowplow_aws_personalize_ecommerce_items:
        +enabled: true
      snowplow_aws_personalize_ecommerce_users:
        +enabled: true
      snowplow_aws_personalize_media_interactions:
        +enabled: false
      snowplow_aws_personalize_media_items:
        +enabled: false
      snowplow_aws_personalize_media_users:
        +enabled: false
``` 

Run `dbt deps` followed by `dbt run` in your project directory. This will create the table(s) in Snowflake and copy it/them to S3.