+++
title = "Run snowplow_recommendations dbt package"
weight = 2
post = ""
+++

This dbt package gives you the option of creating tables for either Ecommerce or Media (video_on_demand) data, or both, if you have both types of data. You will need to specify in the `dbt_project.yml` file which tables you would like to create (instructions below).

For ecommerce, we will use the `snowplow_ecommerce_product_interactions` table created by the dbt-snowplow-ecommerce package to create the E-commerce dataset for AWS Personalize. 

For media, we will use the `snowplow_media_player_base` table created by the dbt-snowplow-media-player package to create the Video On Demand dataset for AWS Personalize.

By default, the items, users and interactions tables can be created for E-commerce, but only the interactions table can be created for Video On Demand. This is because the VOD items table has required fields (e.g. genres) that aren't tracked in the media tracking plugins by default. You can write custom SQL to create the items and users tables for media if you have the [required fields](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-datasets-and-schemas.html) either in your snowplow events table or in a separate table. 
See expandable section for further instructions.

{{% expand "Creating items and users for video_on_demand" %}}
*Creating the items and users models for Video on Demand recommenders*

These instructions are for both items and users, but you can create just one if you only have the requirements for one.
1. Create macros in the macros folder of your project, called `create_media_items` and `create_media_users`. You can copy the formatting of the macros for E-commerce. 
2. Within the macros, write the SQL that will output tables with the required fields for items and/or users. You can find the required fields [here](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-datasets-and-schemas.html). Create the models under the 'media' folder at `models/media/`.

    This is an example of a media users dbt model:
    ```sql
    {{
      config(
        sql_header=snowplow_utils.set_query_tag(var('snowplow__query_tag', 'snowplow_dbt'))
      )
    }}

    {{ external_table_config(this.name) }}


    {{ create_media_users() }}
    ```

    The macro `create_media_users()` should contain the sql to output the fields of the users dataset for Video On Demand.
    
3. You will also need to add the model name(s) to the list parameter in the config file (i.e. `tables_to_export`).
4. Create a schema for each model in the `aws_personalize_utilities/schemas/` folder. They must be named `media_items.avro` and `media_users.avro` for the python script that creates the recommenders to read them. You can copy the formatting of the ecommerce schemas or see the documentation [here](https://docs.aws.amazon.com/personalize/latest/dg/VIDEO-ON-DEMAND-datasets-and-schemas.html).
{{% /expand %}}

#### **Step 1:** Update the vars in your `dbt_project.yml` file:

The current version of this package will only build the models (datasets) for the E-commerce domain (i.e. 'interactions', 'items' and 'users') whereas for the Video On Demand domain only the 'interactions' model will be created. This is due to the fact that the current media tracking available doesn't capture some data that are required fields for the 'items' and 'users' datasets for VOD. You are able to create them yourself if you have the available fields in other tables.
   
You may wish to only run the models for a specific domain (or both) by enabling them in the project config file via:
```yaml
models:
  snowplow_recommendations:
    +materialized: table
    ecommerce:
      enabled: true
    media:
      enabled: true
```

You may need to further update some variables in your `dbt_project.yml` file:
- `tables_to_export`: When a domain type is enabled in the config file then all the models for that domain will be built, but you may list which tables (models) to be exported to S3 with this variable here. Enter the name of the model in this array if you'd like a table to be exported to S3 to be trained by AWS Personalize (note that the 'interaction' models are required datasets but the 'items' and 'users' datasets are optional).
- `snowflake_stage_name`: This will be the name of the external Stage in your Snowflake account to load data to AWS S3. If you used Terraform to create this stage then the name can be found in the TF variable files.
- `external_catalog`: This is the name of the external catalog on your Databricks account. In order to create external tables the query must be executed from an external catalog. If you used Terraform to create this stage then the name can be found in the TF variable files.
- `s3_bucket`: This is the S3 path (i.e. `s3://<bucket name>/`) for which your Databricks' external location is configured to. If you used Terraform to create this stage then the name can be found in the TF variable files.

The other variables behave similarly to all the other Snowplow dbt packages and their configurable variables for running the models.

Run `dbt deps` followed by `dbt run` in the `dbt-snowplow-recommendations` directory. This will create the table(s) in your data warehouse and export the models as csv files to the S3 bucket.