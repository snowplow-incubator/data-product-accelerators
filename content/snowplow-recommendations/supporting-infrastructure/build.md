+++
title = "Create Supporting Infrastructure"
weight = 2
post = ""
+++

For this step, you have two options:
#### **Option 1:** Manual
Follow the linked Snowflake and AWS documentation and create the necessary resources manually.

or

#### **Option 2:** Terraform
Use the provided Terraform script to create the resources. This is the recommended option as it is significantly faster (assuming you're familiar with Terraform).
{{< tabs >}}
{{% tab name="Manual" %}}
#### Option 1: Manual instructions
**I**. Create an S3 bucket for the data from Snowflake - https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html

**II**. Follow the instructions in the following link to configure a storage integration between Snowflake and S3 - https://docs.snowflake.com/en/user-guide/data-load-s3-config-storage-integration.html. You will need either global CREATE STORAGE INTEGRATION permissions or to be an ACCOUNTADMIN in Snowflake for this step, as well as permissions in AWS to create and manage IAM policies and roles. 
**Note: The data from Snowflake will be loaded to the root of your bucket, so don't add any prefixes to the resource name when creating the policies.**

**III**. Create a policy and role for AWS personalize - follow instructions here https://docs.aws.amazon.com/personalize/latest/dg/set-up-required-permissions.html 

- Also follow the instructions here https://docs.aws.amazon.com/personalize/latest/dg/cross-service-confused-deputy-prevention.html to prevent the confused deputy problem, by modifying the trust policy for the role you created in the previous step.

**IV**. We then need to create two more policies - one that is attached to the personalize role, and another that is attached to the bucket. These allow the personalize service to access your S3 bucket: https://docs.aws.amazon.com/personalize/latest/dg/granting-personalize-s3-access.html 
There are a few headings in this document that aren't relevant; the ones to follow are:
- Beneath the heading `Attaching an Amazon S3 policy to your Amazon Personalize service role` follow instructions for `Service role policy for batch workflows` (the only difference between the two policies in this section is the addition of the `"s3:PutObject"` action for the batch workflows).
- Beneath the heading `Attaching an Amazon Personalize access policy to your Amazon S3 bucket` follow instructions for `Amazon S3 bucket policy for batch workflows` (once again the only difference is the addition of the `"s3:PutObject"` action).
{{% /tab %}}

{{% tab name="Terraform" %}}
#### Option 2: Use supplied Terraform script

**I**. Set up AWS and Terraform if not already done: https://developer.hashicorp.com/terraform/tutorials/aws-get-started/aws-build

**II**. Create a file called `terraform.tfvars` in the `terraform_utilities` directory. This file will contain the variables that are used in the terraform script. The file should look like this:
```
aws_region           = "region"
bucket_name          = "bucket_name"
snowflake_username   = "username"
aws_account_id       = "111111111111"
snowflake_account_id = "ID-COMPANYNAME"
snowflake_database   = "DATABASE"
snowflake_schema     = "SCHEMA"
# Below variables are optional, defaults are provided in variables.tf
personalize_policy_name = "PersonalizeIAMPolicy_123"
personalize_role_name = "PersonalizeIAMRole_123"  
personalize_s3_bucket_access_policy_name = "PersonalizeS3BucketAccessPolicy_123"  
personalize_s3_access_policy_name = "PersonalizeS3AccessPolicy_123"  
snowflake_policy_name = "SnowflakeIAMPolicy_123"  
snowflake_role_name = "SnowflakeIAMRole_123"  
snowflake_storage_integration_name = "PersonalizeS3StorageIntegration_123"
snowflake_personalize_stage_name = "PersonalizeS3Stage_123"
```

**III**. Export your snowflake password in your environment. You can do this by running `export SNOWFLAKE_PASSWORD=your_password` in your terminal.

**IV**. Run `terraform init` in the `terraform_utilities` directory. This will initialise terraform and download the necessary providers.

**V**. Run `terraform apply` in the `terraform_utilities` directory. This will create the necessary resources in AWS and Snowflake. You will need to enter `yes` when prompted to confirm the creation of the resources.
{{% /tab %}}
{{< /tabs >}}