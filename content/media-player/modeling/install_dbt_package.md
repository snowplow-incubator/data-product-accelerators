+++
title= "Install Snowplow dbt Package"
weight = 1
post = ""
+++

> Ensure you have set up a new dbt project using [`dbt init`](https://docs.getdbt.com/reference/commands/init) and validate your connection project using [`dbt debug`](https://docs.getdbt.com/reference/commands/debug) before adding our package. All commands should be run in the directory of this project.

In this section you are going to be adding our `snowplow_media_player` package to your fresh project. This will mean your project is able to run all our models, but will keep our package in the `dbt_packages` folder to keep your project clean and organized.

{{% notice note %}}
Our `snowplow_media_player` dbt package is licensed to you under the [Snowplow Personal and Academic License Version 1.0](https://docs.snowplow.io/personal-and-academic-license-1.0/), and you may not use this package except in compliance with the [Snowplow Personal and Academic License Version 1.0](https://docs.snowplow.io/personal-and-academic-license-1.0/).
{{% /notice %}}

#### **Step 1:** Add snowplow_media_player package

Add the snowplow_media_player package to your `packages.yml` file, which you may have to create at the same level as your `dbt_project.yml` file. The latest version of our package can be found [here](https://hub.getdbt.com/snowplow/snowplow_media_player/latest/).

```yaml
packages:
  - package: snowplow/snowplow_media_player
    version: {{< component name="snowplow_media_player_latest">}}
```

### Step 2: Install the package

Install the package by running:

```yaml
dbt deps
```

Once this is done, you can find our package in the newly created `dbt_packages` folder. You can read more about the package, including some optional features and modules not detailed within this Accelerator but checking out [our docs](https://docs.snowplow.io/docs/modeling-your-data/modeling-your-data-with-dbt/dbt-models/dbt-media-player-data-model/) .
