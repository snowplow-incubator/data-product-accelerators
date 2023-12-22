+++
title = "Initial Setup"
weight = 1
post = ""
+++

#### **Step 1:** Install SDK
Install the AWS SDK for Python (Boto3) if you don't already have it - https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

#### **Step 2:** Set up AWS credentials 
In your AWS account, create an access key for your user - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey. Copy the access key id and secret access key to a file called credentials in the .aws folder in your home directory. The file should look like this:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

You can also ensure that if you have a config file in the .aws folder that it has the correct region in it. The file should look like this:
```
[default]
region=YOUR_REGION
```