+++
title = "Data upload"
weight = 1
post = ""
+++


In this section we are going to load the sample Snowplow data to your warehouse.

{{< tabs groupId="select_upload" >}}

{{% tab name="Snowflake" %}}

We have provided a public S3 bucket where we store the sample data in a csv format through [this link](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/Hybrid_Apps/Hybrid_sample_events.csv).

You will be able to load this file to your Snowflake warehouse with a few simple steps explained below.

#### **Step 1:**  Create the ATOMIC schema

If the ATOMIC schema doesn't exist, create it in your target database.

```sql
CREATE SCHEMA IF NOT EXISTS TARGET_DB.ATOMIC
```

***

#### **Step 2:**   Create the **ATOMIC.SAMPLE_EVENTS_HYBRID_BASE** table

This is where you will load the sample data to. You will need to modify the TARGET_DB according to your own database.

```sql
CREATE OR REPLACE TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_HYBRID_BASE (

	APP_ID VARCHAR(255),
	PLATFORM VARCHAR(255),
	ETL_TSTAMP TIMESTAMP_NTZ(9),
	COLLECTOR_TSTAMP TIMESTAMP_NTZ(9) NOT NULL,
	DVCE_CREATED_TSTAMP TIMESTAMP_NTZ(9),
	EVENT VARCHAR(128),
	EVENT_ID VARCHAR(36) NOT NULL,
	TXN_ID NUMBER(38,0),
	NAME_TRACKER VARCHAR(128),
	V_TRACKER VARCHAR(100),
	V_COLLECTOR VARCHAR(100) NOT NULL,
	V_ETL VARCHAR(100) NOT NULL,
	USER_ID VARCHAR(255),
	USER_IPADDRESS VARCHAR(128),
	USER_FINGERPRINT VARCHAR(128),
	DOMAIN_USERID VARCHAR(128),
	DOMAIN_SESSIONIDX NUMBER(38,0),
	NETWORK_USERID VARCHAR(128),
	GEO_COUNTRY VARCHAR(2),
	GEO_REGION VARCHAR(3),
	GEO_CITY VARCHAR(75),
	GEO_ZIPCODE VARCHAR(15),
	GEO_LATITUDE FLOAT,
	GEO_LONGITUDE FLOAT,
	GEO_REGION_NAME VARCHAR(100),
	IP_ISP VARCHAR(100),
	IP_ORGANIZATION VARCHAR(128),
	IP_DOMAIN VARCHAR(128),
	IP_NETSPEED VARCHAR(100),
	PAGE_URL VARCHAR(4096),
	PAGE_TITLE VARCHAR(2000),
	PAGE_REFERRER VARCHAR(4096),
	PAGE_URLSCHEME VARCHAR(16),
	PAGE_URLHOST VARCHAR(255),
	PAGE_URLPORT NUMBER(38,0),
	PAGE_URLPATH VARCHAR(3000),
	PAGE_URLQUERY VARCHAR(6000),
	PAGE_URLFRAGMENT VARCHAR(3000),
	REFR_URLSCHEME VARCHAR(16),
	REFR_URLHOST VARCHAR(255),
	REFR_URLPORT NUMBER(38,0),
	REFR_URLPATH VARCHAR(6000),
	REFR_URLQUERY VARCHAR(6000),
	REFR_URLFRAGMENT VARCHAR(3000),
	REFR_MEDIUM VARCHAR(25),
	REFR_SOURCE VARCHAR(50),
	REFR_TERM VARCHAR(255),
	MKT_MEDIUM VARCHAR(255),
	MKT_SOURCE VARCHAR(255),
	MKT_TERM VARCHAR(255),
	MKT_CONTENT VARCHAR(500),
	MKT_CAMPAIGN VARCHAR(255),
	SE_CATEGORY VARCHAR(1000),
	SE_ACTION VARCHAR(1000),
	SE_LABEL VARCHAR(4096),
	SE_PROPERTY VARCHAR(1000),
	SE_VALUE FLOAT,
	TR_ORDERID VARCHAR(255),
	TR_AFFILIATION VARCHAR(255),
	TR_TOTAL NUMBER(18,2),
	TR_TAX NUMBER(18,2),
	TR_SHIPPING NUMBER(18,2),
	TR_CITY VARCHAR(255),
	TR_STATE VARCHAR(255),
	TR_COUNTRY VARCHAR(255),
	TI_ORDERID VARCHAR(255),
	TI_SKU VARCHAR(255),
	TI_NAME VARCHAR(255),
	TI_CATEGORY VARCHAR(255),
	TI_PRICE NUMBER(18,2),
	TI_QUANTITY NUMBER(38,0),
	PP_XOFFSET_MIN NUMBER(38,0),
	PP_XOFFSET_MAX NUMBER(38,0),
	PP_YOFFSET_MIN NUMBER(38,0),
	PP_YOFFSET_MAX NUMBER(38,0),
	USERAGENT VARCHAR(1000),
	BR_NAME VARCHAR(50),
	BR_FAMILY VARCHAR(50),
	BR_VERSION VARCHAR(50),
	BR_TYPE VARCHAR(50),
	BR_RENDERENGINE VARCHAR(50),
	BR_LANG VARCHAR(255),
	BR_FEATURES_PDF BOOLEAN,
	BR_FEATURES_FLASH BOOLEAN,
	BR_FEATURES_JAVA BOOLEAN,
	BR_FEATURES_DIRECTOR BOOLEAN,
	BR_FEATURES_QUICKTIME BOOLEAN,
	BR_FEATURES_REALPLAYER BOOLEAN,
	BR_FEATURES_WINDOWSMEDIA BOOLEAN,
	BR_FEATURES_GEARS BOOLEAN,
	BR_FEATURES_SILVERLIGHT BOOLEAN,
	BR_COOKIES BOOLEAN,
	BR_COLORDEPTH VARCHAR(12),
	BR_VIEWWIDTH NUMBER(38,0),
	BR_VIEWHEIGHT NUMBER(38,0),
	OS_NAME VARCHAR(50),
	OS_FAMILY VARCHAR(50),
	OS_MANUFACTURER VARCHAR(50),
	OS_TIMEZONE VARCHAR(255),
	DVCE_TYPE VARCHAR(50),
	DVCE_ISMOBILE BOOLEAN,
	DVCE_SCREENWIDTH NUMBER(38,0),
	DVCE_SCREENHEIGHT NUMBER(38,0),
	DOC_CHARSET VARCHAR(128),
	DOC_WIDTH NUMBER(38,0),
	DOC_HEIGHT NUMBER(38,0),
	TR_CURRENCY VARCHAR(3),
	TR_TOTAL_BASE NUMBER(18,2),
	TR_TAX_BASE NUMBER(18,2),
	TR_SHIPPING_BASE NUMBER(18,2),
	TI_CURRENCY VARCHAR(3),
	TI_PRICE_BASE NUMBER(18,2),
	BASE_CURRENCY VARCHAR(3),
	GEO_TIMEZONE VARCHAR(64),
	MKT_CLICKID VARCHAR(128),
	MKT_NETWORK VARCHAR(64),
	ETL_TAGS VARCHAR(500),
	DVCE_SENT_TSTAMP TIMESTAMP_NTZ(9),
	REFR_DOMAIN_USERID VARCHAR(128),
	REFR_DVCE_TSTAMP TIMESTAMP_NTZ(9),
	DOMAIN_SESSIONID VARCHAR(128),
	DERIVED_TSTAMP TIMESTAMP_NTZ(9),
	EVENT_VENDOR VARCHAR(1000),
	EVENT_NAME VARCHAR(1000),
	EVENT_FORMAT VARCHAR(128),
	EVENT_VERSION VARCHAR(128),
	EVENT_FINGERPRINT VARCHAR(128),
	TRUE_TSTAMP TIMESTAMP_NTZ(9),
	LOAD_TSTAMP TIMESTAMP_NTZ(9),
	CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_1 VARCHAR,
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1 VARCHAR,
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT_1 VARCHAR,
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MOBILE_CONTEXT_1 VARCHAR,
	CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_APPLICATION_1 VARCHAR,
	UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW_1 VARCHAR,
	constraint EVENT_ID_PK primary key (EVENT_ID)
);
```
***

#### **Step 3:** Create stage


```sql
CREATE OR REPLACE STAGE snowplow_hybrid_sample_stage
url = 's3://snowplow-demo-datasets/Hybrid_Apps/Hybrid_sample_events.csv'
file_format = (TYPE=csv field_delimiter=',' skip_header=1, FIELD_OPTIONALLY_ENCLOSED_BY='"')
```

***
#### **Step 4:** Copy into base table from stage

```sql
COPY INTO TARGET_DB.ATOMIC.SAMPLE_EVENTS_HYBRID_BASE
FROM @snowplow_hybrid_sample_stage
```
***

#### **Step 5:** Create the **ATOMIC.SAMPLE_EVENTS_HYBRID** table

```sql
CREATE OR REPLACE TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_HYBRID AS (

SELECT
	APP_ID,
	PLATFORM,
	ETL_TSTAMP,
	COLLECTOR_TSTAMP,
	DVCE_CREATED_TSTAMP,
	EVENT,
	EVENT_ID,
	TXN_ID,
	NAME_TRACKER,
	V_TRACKER,
	V_COLLECTOR,
	V_ETL,
	USER_ID,
	USER_IPADDRESS,
	USER_FINGERPRINT,
	DOMAIN_USERID,
	DOMAIN_SESSIONIDX,
	NETWORK_USERID,
	GEO_COUNTRY,
	GEO_REGION,
	GEO_CITY,
	GEO_ZIPCODE,
	GEO_LATITUDE,
	GEO_LONGITUDE,
	GEO_REGION_NAME,
	IP_ISP,
	IP_ORGANIZATION,
	IP_DOMAIN,
	IP_NETSPEED,
	PAGE_URL,
	PAGE_TITLE,
	PAGE_REFERRER,
	PAGE_URLSCHEME,
	PAGE_URLHOST,
	PAGE_URLPORT,
	PAGE_URLPATH,
	PAGE_URLQUERY,
	PAGE_URLFRAGMENT,
	REFR_URLSCHEME,
	REFR_URLHOST,
	REFR_URLPORT,
	REFR_URLPATH,
	REFR_URLQUERY,
	REFR_URLFRAGMENT,
	REFR_MEDIUM,
	REFR_SOURCE,
	REFR_TERM,
	MKT_MEDIUM,
	MKT_SOURCE,
	MKT_TERM,
	MKT_CONTENT,
	MKT_CAMPAIGN,
	SE_CATEGORY,
	SE_ACTION,
	SE_LABEL,
	SE_PROPERTY,
	SE_VALUE,
	TR_ORDERID,
	TR_AFFILIATION,
	TR_TOTAL,
	TR_TAX,
	TR_SHIPPING,
	TR_CITY,
	TR_STATE,
	TR_COUNTRY,
	TI_ORDERID,
	TI_SKU,
	TI_NAME,
	TI_CATEGORY,
	TI_PRICE,
	TI_QUANTITY,
	PP_XOFFSET_MIN,
	PP_XOFFSET_MAX,
	PP_YOFFSET_MIN,
	PP_YOFFSET_MAX,
	REPLACE(USERAGENT, '\"', '') as USERAGENT,
	BR_NAME,
	BR_FAMILY,
	BR_VERSION,
	BR_TYPE,
	BR_RENDERENGINE,
	BR_LANG,
	BR_FEATURES_PDF,
	BR_FEATURES_FLASH,
	BR_FEATURES_JAVA,
	BR_FEATURES_DIRECTOR,
	BR_FEATURES_QUICKTIME,
	BR_FEATURES_REALPLAYER,
	BR_FEATURES_WINDOWSMEDIA,
	BR_FEATURES_GEARS,
	BR_FEATURES_SILVERLIGHT,
	BR_COOKIES,
	BR_COLORDEPTH,
	BR_VIEWWIDTH,
	BR_VIEWHEIGHT,
	OS_NAME,
	OS_FAMILY,
	OS_MANUFACTURER,
	OS_TIMEZONE,
	DVCE_TYPE,
	DVCE_ISMOBILE,
	DVCE_SCREENWIDTH,
	DVCE_SCREENHEIGHT,
	DOC_CHARSET,
	DOC_WIDTH,
	DOC_HEIGHT,
	TR_CURRENCY,
	TR_TOTAL_BASE,
	TR_TAX_BASE,
	TR_SHIPPING_BASE,
	TI_CURRENCY,
	TI_PRICE_BASE,
	BASE_CURRENCY,
	GEO_TIMEZONE,
	MKT_CLICKID,
	MKT_NETWORK,
	ETL_TAGS,
	DVCE_SENT_TSTAMP,
	REFR_DOMAIN_USERID,
	REFR_DVCE_TSTAMP,
	DOMAIN_SESSIONID,
	DERIVED_TSTAMP,
	EVENT_VENDOR,
	EVENT_NAME,
	EVENT_FORMAT,
	EVENT_VERSION,
	EVENT_FINGERPRINT,
	TRUE_TSTAMP,
	LOAD_TSTAMP,
    PARSE_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_1) as CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_1,
    PARSE_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1) as CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1,
    PARSE_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT_1) as CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT_1,
    PARSE_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MOBILE_CONTEXT_1) as CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MOBILE_CONTEXT_1,
    PARSE_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_APPLICATION_1) as CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_APPLICATION_1,
    PARSE_JSON(UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW_1) as UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW_1

FROM ATOMIC.SAMPLE_EVENTS_HYBRID_BASE )

```

***

#### **Step 6:** Drop the **SAMPLE_EVENTS_HYBRID_BASE** table

```sql
DROP TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_HYBRID_BASE
```
You will now have the `ATOMIC.SAMPLE_EVENTS_HYBRID` created and loaded with sample data.

{{% /tab %}}

{{% tab name="Databricks" %}}


We have provided a public S3 bucket where we store the sample data in a csv format through [this link](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/Hybrid_Apps/Hybrid_sample_events_tab_separated.csv).

You can load the sample data to the warehouse using your `Databricks Workspace` as described in the below steps.

For more details please check out the official [Databricks documentation](https://docs.databricks.com/ingestion/add-data/index.html).

#### **Step 1:**   Create the ATOMIC schema
If the ATOMIC schema doesn't exist, create it in your target database.

```sql
CREATE SCHEMA IF NOT EXISTS TARGET_DB.ATOMIC
```

#### **Step 2:**  Upload the csv file
2.1 Log into your Databricks workspace.

2.2 Select `+New` -> `File upload` to get started.

2.3 Click `Browse` and locate the `Hybrid_sample_events_tab_separated.csv` file and click `Open`. It should take a minute or two to load.

2.4 Once you see the preview, specify the catalog, the schema (atomic) and change the name to **sample_events_hybrid_base**.

2.5 Go to `advanced attributes` and change the column delimiter to `tab` then X out of the window. After this the data reloads, which will now be separated correctly column by column.

2.6 Click create table.
#### **Step 3:** Create the **ATOMIC.SAMPLE_EVENTS_HYBRID** table

The Snowplow pipeline creates context fields as arrays but uploading the test data can be achieved through string/varchar data type first. Run the below DDL statement in your SQL editor to create the `sample_events_hybrid` table from the base table including the necessary conversions:

```sql


CREATE OR REPLACE TABLE ATOMIC.SAMPLE_EVENTS_HYBRID AS (

  WITH PREP AS (

  SELECT
   *,
   FROM_JSON(UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW_1, 'ARRAY<STRUCT<ID:STRING, NAME:STRING, PREVIOUS_ID:STRING, PREVIOUS_NAME:STRING, PREVIOUS_TYPE:STRING, TRANSITION_TYPE:STRING, TYPE:STRING>>') AS UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW

  FROM TARGET_DB.ATOMIC.SAMPLE_EVENTS_HYBRID_BASE
 )

 , STRUCT_BASE AS (

   SELECT
   *
   EXCEPT(UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW_1, UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW),
   UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW[0].ID::STRING AS ID,
   UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW[0].NAME::STRING AS NAME,
   UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW[0].PREVIOUS_ID::STRING AS PREVIOUS_ID,
   UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW[0].PREVIOUS_NAME::STRING AS PREVIOUS_NAME,
   UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW[0].PREVIOUS_TYPE::STRING AS PREVIOUS_TYPE,
   UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW[0].TRANSITION_TYPE::STRING AS TRANSITION_TYPE,
   UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW[0].TYPE::STRING AS TYPE

   FROM PREP
 )


  SELECT
    APP_ID,
    PLATFORM,
    ETL_TSTAMP,
    COLLECTOR_TSTAMP,
    DVCE_CREATED_TSTAMP,
    EVENT,
    EVENT_ID,
    TXN_ID,
    NAME_TRACKER,
    V_TRACKER,
    V_COLLECTOR,
    V_ETL,
    USER_ID,
    USER_IPADDRESS,
    USER_FINGERPRINT,
    DOMAIN_USERID,
    DOMAIN_SESSIONIDX,
    NETWORK_USERID,
    GEO_COUNTRY,
    GEO_REGION,
    GEO_CITY,
    GEO_ZIPCODE,
    GEO_LATITUDE,
    GEO_LONGITUDE,
    GEO_REGION_NAME,
    IP_ISP,
    IP_ORGANIZATION,
    IP_DOMAIN,
    IP_NETSPEED,
    PAGE_URL,
    PAGE_TITLE,
    PAGE_REFERRER,
    PAGE_URLSCHEME,
    PAGE_URLHOST,
    PAGE_URLPORT,
    PAGE_URLPATH,
    PAGE_URLQUERY,
    PAGE_URLFRAGMENT,
    REFR_URLSCHEME,
    REFR_URLHOST,
    REFR_URLPORT,
    REFR_URLPATH,
    REFR_URLQUERY,
    REFR_URLFRAGMENT,
    REFR_MEDIUM,
    REFR_SOURCE,
    REFR_TERM,
    MKT_MEDIUM,
    MKT_SOURCE,
    MKT_TERM,
    MKT_CONTENT,
    MKT_CAMPAIGN,
    SE_CATEGORY,
    SE_ACTION,
    SE_LABEL,
    SE_PROPERTY,
    SE_VALUE,
    TR_ORDERID,
    TR_AFFILIATION,
    TR_TOTAL,
    TR_TAX,
    TR_SHIPPING,
    TR_CITY,
    TR_STATE,
    TR_COUNTRY,
    TI_ORDERID,
    TI_SKU,
    TI_NAME,
    TI_CATEGORY,
    TI_PRICE,
    TI_QUANTITY,
    PP_XOFFSET_MIN,
    PP_XOFFSET_MAX,
    PP_YOFFSET_MIN,
    PP_YOFFSET_MAX,
    USERAGENT,
    BR_NAME,
    BR_FAMILY,
    BR_VERSION,
    BR_TYPE,
    BR_RENDERENGINE,
    BR_LANG,
    BR_FEATURES_PDF,
    BR_FEATURES_FLASH,
    BR_FEATURES_JAVA,
    BR_FEATURES_DIRECTOR,
    BR_FEATURES_QUICKTIME,
    BR_FEATURES_REALPLAYER,
    BR_FEATURES_WINDOWSMEDIA,
    BR_FEATURES_GEARS,
    BR_FEATURES_SILVERLIGHT,
    BR_COOKIES,
    BR_COLORDEPTH,
    BR_VIEWWIDTH,
    BR_VIEWHEIGHT,
    OS_NAME,
    OS_FAMILY,
    OS_MANUFACTURER,
    OS_TIMEZONE,
    DVCE_TYPE,
    DVCE_ISMOBILE,
    DVCE_SCREENWIDTH,
    DVCE_SCREENHEIGHT,
    DOC_CHARSET,
    DOC_WIDTH,
    DOC_HEIGHT,
    TR_CURRENCY,
    TR_TOTAL_BASE,
    TR_TAX_BASE,
    TR_SHIPPING_BASE,
    TI_CURRENCY,
    TI_PRICE_BASE,
    BASE_CURRENCY,
    GEO_TIMEZONE,
    MKT_CLICKID,
    MKT_NETWORK,
    ETL_TAGS,
    DVCE_SENT_TSTAMP,
    REFR_DOMAIN_USERID,
    REFR_DVCE_TSTAMP,
    DOMAIN_SESSIONID,
    DERIVED_TSTAMP,
    EVENT_VENDOR,
    EVENT_NAME,
    EVENT_FORMAT,
    EVENT_VERSION,
    EVENT_FINGERPRINT,
    TRUE_TSTAMP,
    STRUCT(ID, NAME, PREVIOUS_ID, PREVIOUS_NAME, PREVIOUS_TYPE, TRANSITION_TYPE, TYPE) AS UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW_1,
   FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1, 'ARRAY<STRUCT<SESSION_ID:STRING, SESSION_INDEX:STRING, PREVIOUS_SESSION_ID:STRING, USER_ID:STRING, FIRST_EVENT_ID:STRING, EVENT_INDEX:STRING, STORAGE_MECHANISM:STRING, FIRST_EVENT_TIMESTAMP:STRING>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION,
   FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT_1, 'ARRAY<STRUCT<LATITUDE:FLOAT, LONGITUDE:FLOAT, LATITUDE_LONGITUDE_ACCURACY:FLOAT, ALTITUDE:FLOAT, ALTITUDE_ACCURACY:FLOAT, BEARING:FLOAT, SPEED:FLOAT, TIMESTAMP:INT>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT


  FROM STRUCT_BASE

)
```

#### **Step 4:**  Drop the **SAMPLE_EVENTS_HYBRID_BASE** table

```sql
DROP TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_HYBRID_BASE
```
You will now have the `ATOMIC.SAMPLE_EVENTS_HYBRID` created and loaded with sample data.

{{% /tab %}}

{{% tab name="BigQuery" %}}

We have provided a public S3 bucket where we store the sample data in a csv format, you should be able to download it locally through this [link](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/Hybrid_Apps/Hybrid_sample_events.csv).

You can load the sample data to the warehouse using your [Google Cloud console](https://console.cloud.google.com/) as described in the below steps.

For more details please check out the official [BigQuery documentation](https://cloud.google.com/bigquery/docs/batch-loading-data#console).


#### **Step 1:**  Create the ATOMIC schema
If the ATOMIC schema doesn't exist, create it in your target database.

```sql
CREATE SCHEMA IF NOT EXISTS ATOMIC

```
***

#### **Step 2:**  Upload the csv file

2.1 Open the `BigQuery` page in the [Google Cloud console](https://console.cloud.google.com/).

2.2 In the `Explorer` panel, expand your project and select the `atomic` schema/dataset. You should see the details panel open, if not, expand the `Actions` option (click on the three vertical dots) and click `Open`.

2.3 In the `Details` panel, click `Create table`.

2.4 On the `Create table` page fill out the sections:

In the `Source` section:

- For `Create table from`, select `Upload`.
- For `Select file`, click `Browse`. Navigate to the `Hybrid_sample_events.csv` and open it.
- Make sure `CSV` is selected for `File format`

In the `Destination` section:

On the `Create table` page,

- For `Project`, choose the appropriate project (should be auto-populated).
- For `Dataset` make sure it is `atomic` (should be auto-populated).
- In the `Table` field put: `SAMPLE_EVENTS_HYBRID_BASE`
Verify that Table type is set to `Native table`.

On the `Schema` section:

- Click `Auto-detect`

Expand the `Advanced options` and put 1 for `Header rows to skip` and tick the box for `Quoted newlines`

- Click `Create table`. Wait for a minute or two and the table should be created.

#### **Step 3:** Create the **ATOMIC.SAMPLE_EVENTS_HYBRID** table

The Snowplow pipeline creates context fields as REPEATED fields but uploading the test data can be achieved through string/varchar data type first. Run the below DDL statement in your SQL editor to create the `sample_events_hybrid` table from the base table including the necessary conversions:

```sql
CREATE OR REPLACE TABLE ATOMIC.SAMPLE_EVENTS_HYBRID AS (


WITH PREP AS (
SELECT
  *
  EXCEPT(UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW_1, CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1, CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT_1),
  JSON_EXTRACT_ARRAY(UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW_1) AS UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW,
  JSON_EXTRACT_ARRAY(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION,
  JSON_EXTRACT_ARRAY(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT_1) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT

FROM TARGET_DB.ATOMIC.SAMPLE_EVENTS_HYBRID_BASE
)


SELECT
  * EXCEPT(UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW, CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION, CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT),
  ARRAY(
    SELECT AS STRUCT JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.ID') AS ID,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.NAME') AS NAME,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.PREVIOUS_ID') AS PREVIOUS_ID,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.PREVIOUS_NAME') AS PREVIOUS_NAME,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.PREVIOUS_TYPE') AS PREVIOUS_TYPE,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.TRANSITION_TYPE') AS TRANSITION_TYPE,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.TYPE') AS TYPE
    FROM UNNEST(UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW) AS JSON_ARRAY
    ) AS UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_VIEW_1_0_0,
  ARRAY(
    SELECT AS STRUCT JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.SESSION_ID') AS SESSION_ID,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.USER_ID') AS USER_ID,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.SESSION_INDEX') AS SESSION_INDEX,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.FIRST_EVENT_ID') AS FIRST_EVENT_ID,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.PREVIOUS_SESSION_ID') AS PREVIOUS_SESSION_ID,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.EVENT_INDEX') AS EVENT_INDEX,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.STORAGE_MECHANISM') AS STORAGE_MECHANISM,
                    JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.FIRST_EVENT_TIMESTAMP') AS FIRST_EVENT_TIMESTAMP
    FROM UNNEST(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION) AS JSON_ARRAY
    ) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1_0_1,
  ARRAY(
    SELECT AS STRUCT CAST(JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.LATITUDE') AS FLOAT64) AS LATITUDE,
                    CAST(JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.LONGITUDE') AS FLOAT64) AS LONGITUDE,
                    CAST(JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.LATITUDE_LONGITUDE_ACCURACY') AS FLOAT64) AS LATITUDE_LONGITUDE_ACCURACY,
                    CAST(JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.ALTITUDE') AS FLOAT64) AS ALTITUDE,
                    CAST(JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.ALTITUDE_ACCURACY')  AS FLOAT64)AS ALTITUDE_ACCURACY,
                    CAST(JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.BEARING')  AS FLOAT64)AS BEARING,
                    CAST(JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.SPEED') AS FLOAT64) AS SPEED,
                    CAST(JSON_EXTRACT_SCALAR(JSON_ARRAY,'$.TIMESTAMP') AS INTEGER) AS TIMESTAMP
    FROM UNNEST(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT) AS JSON_ARRAY
    ) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_GEOLOCATION_CONTEXT_1_1_0

FROM PREP
```

)

#### **Step 4:**  Drop the SAMPLE_EVENTS_HYBRID_BASE table

```sql
DROP TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_HYBRID_BASE
```
You will now have the `ATOMIC.SAMPLE_EVENTS_HYBRID` created and loaded with sample data.

{{% /tab %}}

{{< /tabs >}}