+++
title = "Install Recommendations dbt package"
weight = 1
post = ""
+++

> Ensure you have set up a new dbt project using [`dbt init`](https://docs.getdbt.com/reference/commands/init) and validate your connection project using [`dbt debug`](https://docs.getdbt.com/reference/commands/debug) before adding our package. All commands should be run in the directory of this project.

In this section you are going to be adding our `snowplow_recommendations` package to your fresh project. This will mean your project is able to run all our models, but will keep our package in the `dbt_packages` folder to keep your project clean and organized.

#### **Step 1:** Add the snowplow_recommendations package
Add the latest snowplow_recommendations `packages.yml` file, which you may have to create at the same level as your `dbt_project.yml` file. The latest version of our package can be found [here](https://hub.getdbt.com/snowplow/snowplow_recommendations/latest/).

```yml
packages:
  - package: snowplow/snowplow_recommendations
    version: 0.0.1
```

#### **Step 2:** Install the package
Install the package by running:

```
dbt deps
```

Once this is done, you can find our package in the `dbt_packages` folder.