+++
title = "Databricks - Using your Model"
weight = 3
url= '/ml-conversion-scoring-for-composable-cdp/predictive_ml_models/databricks/using_your_model'

+++

#### Predicting user's propensity to convert

Now that your model is built and saved in MLflow registry, here is how you might load and use your model in a Databricks notebook.

{{< jupyter databricks_deploying_model 500 >}}

Now you are ready to use your model output for activation via Census. The next chapter, [Data Activation]({{< ref data_activation >}}), guides you through how to target high propensity visitors to optimize ad spend.
