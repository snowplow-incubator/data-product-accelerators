---
title: Install Snowplow dbt Package
description: Install Snowplow dbt Package
weight: 3
lastmod: 2022-11-20T10:23:30-09:00
draft: false
chapter_start: Modelling
free: true 
---


#### **Step 1:** Add snowplow-mobile package

Add the snowplow-web package to your packages.yml file. The latest version can be found [here](https://hub.getdbt.com/snowplow/snowplow_web/latest/)

```yml
packages:
  - package: snowplow/snowplow_mobile
    version: {{<component name="snowplow_mobile_latest">}}
```

***

#### **Step 2:** Install the package

Install the package by running:

```sh
dbt deps
```
