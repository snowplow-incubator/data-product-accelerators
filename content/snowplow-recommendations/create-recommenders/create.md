+++
title = "Create recommenders"
weight = 1
post = ""
+++

#### **Step 1:** Update .env file
Update the `aws_personalize_utilities/.env` file with your variables. Either `ecommerce` or `vod` (video_on_demand) will be appended to the names you give below (e.g. `my_dataset_group` with the domain `ecommerce` will be named in AWS as `my_dataset_group_ecommerce`). Each dataset and import job will also have the data type (interactions, users or items) appended to the name you give, e.g. `test_dataset` will become `test_dataset_ecommerce_interactions`.
The .env file should look like this:
```
dataset_group_name = 'dataset_group' # this can be anything you like
schema_name = 'interactions_schema' # this can be anything you like
dataset_name = 'dataset' # this can be anything you like
import_job_name = 'import_job' # this can be anything you like
s3_bucket_name = 'awspersonalizebucket123' # the name of the S3 bucket that was created
role_arn = 'arn:aws:iam::485941242585:role/personalize_role' # the ARN of the role created for Personalize (Not the role created for Snowflake). If you used Terraform, this was an output variable.
domains_and_dataset_types={"ECOMMERCE": ["interactions", "items", "users"]} # add 'VIDEO_ON_DEMAND' and its dataset types to the dict if you are creating media recommenders as well, or just 'VIDEO_ON_DEMAND' with its dataset types if you are only creating media recommenders. This will just be "VIDEO_ON_DEMAND": ["interactions"] unless you have written SQL for the other dataset types.
```

#### **Step 2:** Create virtual environment
Before running the script to create the recommenders with AWS personalize, use the requirements.txt file to set up the necessary packages in a virtual environment. 

#### **Step 3:** Run script to create recommenders
Run the script in the virtual environment with `python create_personalize_service.py` (assuming you are in the /aws_personalize_utilities directory). This will create the dataset group(s), schema(s), dataset(s), import job(s) and recommenders in Personalize, as well as a file of the recommender arns that will be used by the flask app. If you are creating both the ecommerce and video_on_demand recommenders at the same time, these will be created as two individual dataset groups. 

The script has been designed to be rerun and will use the same resources that have already been created rather than re-creating them (e.g. if you have already created the dataset group, it will not create it again). If you want to re-create the resources, you will need to delete them in the AWS console or using the AWS CLI. This way, if you have an error creating a recommender, e.g. not enough interactions data, you can fix the error and rerun the script without having to delete all the resources and start again.

#### **Step 4:** Monitor status of recommenders 
Once the script has run, navigate to the recommenders section in the AWS Personalize console and monitor the status of the recommenders that are being created. This can take upwards of 15 minutes to complete. Once the status of your recommenders is `Active` you can move on to the next step. If any of the recommenders fail to be created, check the status for the reason for failure. It may be due to not having enough interactions in the dataset(s). If this happens, you will need to either not use the failed recommenders, or increase the data in your dataset. If you do the latter, you will need to re-run dbt with more data, and ensure you delete the failed recommender(s) in the console before re-running the `create_personalize_service.py` script.
