+++
title = "Create recommenders"
weight = 1
post = ""
+++

#### **Step 1:** Update the config.yml file
Set up the configuration yaml file (`config.yaml`) that'll be used in setting up the AWS Personalize service and jobs.
   
   ```yaml
    dataset_group_base_name: 
    schema_base_name: 
    dataset_base_name: 
    import_job_base_name: 
    s3_bucket_name: 
    role_arn: 
    domains_and_datasets:
      VIDEO_ON_DEMAND:
        enable: true
        datasets: [interactions]
        recommenders: [most_popular]
      ECOMMERCE:
        enable: true
        datasets: [interactions, items, users]
        recommenders: [most_viewed, customers_who_viewed_x_also_viewed]
   ```

    The dataset/group, schema and import job names can be configured to your preference. The `s3_bucket_name` should be just the name of the S3 bucket (not the full s3 path) you created either manually or via Terraform; similarly the `role_arn` is the name of the Personalize IAM role you created, it corresponds to the Terraform variable `personalize_role_name` with a default name of `PersonalizeIAMRole`.

    You may choose which or both of the domains for Personalize to create by setting the `enabled` flag in the config file to `true` or `false`. Additionally you can choose which datasets to be created for training by Personalize by adding them to the list for the `datasets` parameter. Ensure that whichever datasets you add here are also exported by your dbt package by adding the corresponding table names to the `dbt_project.yml`'s `tables_to_export` config value. Finally you will be able to select which recommender you'd like Personalize to generate for your datasets by adding their config names in to the list parameter `recommenders` (refer to the table below for the list of available recommenders).

#### **Step 2:** Create virtual environment
Before running the script to create the recommenders with AWS personalize, use the requirements.txt file to set up the necessary packages in a virtual environment. 

#### **Step 3:** Run script to create recommenders
Run the script in the virtual environment with `python create_personalize_service.py` (assuming you are in the /aws_personalize_utilities directory). This will create the dataset group(s), schema(s), dataset(s), import job(s) and recommenders in Personalize, as well as a file of the recommender arns that will be used by the flask app. If you are creating both the ecommerce and video_on_demand recommenders at the same time, these will be created as two individual dataset groups. 

The script has been designed to be rerun and will use the same resources that have already been created rather than re-creating them (e.g. if you have already created the dataset group, it will not create it again). If you want to re-create the resources, you will need to delete them in the AWS console or using the AWS CLI. This way, if you have an error creating a recommender, e.g. not enough interactions data, you can fix the error and rerun the script without having to delete all the resources and start again.

#### **Step 4:** Monitor status of recommenders 
Once the script has run, navigate to the recommenders section in the AWS Personalize console and monitor the status of the recommenders that are being created. This can take upwards of 15 minutes to complete. Once the status of your recommenders is `Active` you can move on to the next step. If any of the recommenders fail to be created, check the status for the reason for failure. It may be due to not having enough interactions in the dataset(s). If this happens, you will need to either not use the failed recommenders, or increase the data in your dataset. If you do the latter, you will need to re-run dbt with more data, and ensure you delete the failed recommender(s) in the console before re-running the `create_personalize_service.py` script.
