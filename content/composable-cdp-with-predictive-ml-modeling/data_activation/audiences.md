+++
title = "Create an Audience"
weight = 2
+++

#### **Step 1:** Create your Models

First you need to create a [model](https://docs.getcensus.com/basics/data-models-and-entities/models) based on your out-of-the-box Snowplow modelled `snowplow_web_users` table or any custom user tables you have built.
Create another model for the user propensity scores table you created in the previous chapter, `snowplow_user_propensity_scores`.

![census_new_model](../images/census_new_model.png)

#### **Step 2:** Create Entities

Secondly you will need to create [Entities](https://docs.getcensus.com/basics/data-models-and-entities/entities) for the audiences to be built off. Base these Entities off the models you created in the previous step. Finally add a 1:1 relationship between the two, joining on `user_id`.

![census_entity_relationship](../images/census_entity_relationship.png)

#### **Step 3:** Audience Hub

Now you can build an audience using columns from your newly created Entities. In this example we are targeting users in the awareness stage based on the following criteria:
* First time on website
* Did not arrive from a marketing campaign
* **High** propensity score

{{% notice tip %}}
Marketing to high propensity to convert users (using your ML model output created in the previous [Predictive ML Models]({{< ref predictive_ml_models >}}) chapter) will lead to higher conversion for less advertising spend!
{{% /notice %}}

![census_audience_builder](../images/census_audience_builder.png)
