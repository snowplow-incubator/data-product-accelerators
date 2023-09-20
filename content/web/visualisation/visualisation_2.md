+++
title = "Databricks Notebook"
post = ""
weight = 2
+++

You can create custom visualisations including dashboards using a Datrabricks notebook.



#### **Step 1:** Clone repository

Download the databricks notebook file from our repo to get started.


```bash
git clone --depth 1  --filter=blob:none --sparse https://github.com/snowplow-incubator/snowplow-accelerator-resources.git ; 
cd snowplow-accelerator-resources
git sparse-checkout set advanced-analytics-web-accelerator/databricks-notebook
```


#### **Step 2:** Import the notebook
Go to your Databricks `Workspace` and click on the Down Arrowhead sign then select `Import`.
Browse to the downloaded `snowplow_advanced_analytics_for_web.ipynb` notebook and click `Import`.

![image alt text](https://docs.databricks.com/_images/import-notebook.png)

For further information on this, check out the official Databricks [documentation](https://docs.databricks.com/notebooks/notebooks-manage.html)

#### **Step 3:** Attach the notebook to your cluster
Before you can do any work, you must first attach the notebook to a cluster.

To attach a notebook to a cluster:

1. In the notebook toolbar, click `Detached`.

![sql_workspace](../images/toolbar.png)

2. From the drop-down, select a cluster.

#### **Step 4:** Change source table schemas and or variables
The predefined SQL statements all refer to the `derived` schema. Make sure to update this to your own schema before attempting to run the notebook. It should be `[your_dbt_schema]_derived`.

{{% notice info %}}

You can do this quickly by using the `Edit / Find and replace` functionality.

{{% /notice %}}

#### **Step 5:** Run the notebook
Click on `Run all` which you can find in the toolbar at the top of the page. It should take a minute or so to have everything refreshed. Once finished you can go to `View` and click on `Results only` to see the outcome without the code snippets.

#### **Step 6:** Check out the dashboard
Head over to `Views/web_accelerator` under dashboards to open the corresponding dashboard as well.
