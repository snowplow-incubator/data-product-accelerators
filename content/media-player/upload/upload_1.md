+++
title = "Data upload"
weight = 1
post = ""
+++

There are a number of options to load the sample Snowplow data to your warehouse. Select the most suitable for your project below.

{{< tabs groupId="select_upload" >}}

{{% tab name="Snowflake" %}}

We have provided a public S3 bucket where we store the sample data in a csv format:

url = https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/media_player/snowplow_media_player_sample_events_snowflake.csv

You will be able to load this file to your Snowflake warehouse with a few simple steps explained below.

#### **Step 1:**  Create the ATOMIC schema
If the ATOMIC schema doesn't exist, create it in your target database.

```sql
CREATE SCHEMA IF NOT EXISTS TARGET_DB.ATOMIC
```

***

#### **Step 2:**  Create the SAMPLE_EVENTS_MEDIA_PLAYER_BASE table
This is where you will load the sample data to. You will need to modify the TARGET_DB according to your own database.


```sql
CREATE OR REPLACE TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER_BASE (
	APP_ID VARCHAR(255),
	PLATFORM VARCHAR(255),
	ETL_TSTAMP TIMESTAMP_NTZ(9),
	COLLECTOR_TSTAMP TIMESTAMP_NTZ(9),
	DVCE_CREATED_TSTAMP TIMESTAMP_NTZ(9),
	EVENT VARCHAR(128),
	EVENT_ID VARCHAR(36),
	TXN_ID NUMBER(38,0),
	NAME_TRACKER VARCHAR(128),
	V_TRACKER VARCHAR(100),
	V_COLLECTOR VARCHAR(100),
	V_ETL VARCHAR(100),
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
	SE_LABEL VARCHAR(1000),
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
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_WEB_PAGE_1 ARRAY,
	CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_1 ARRAY,
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1 ARRAY,
	CONTEXTS_ORG_WHATWG_VIDEO_ELEMENT_1 ARRAY,
	CONTEXTS_ORG_WHATWG_MEDIA_ELEMENT_1 ARRAY,
	CONTEXTS_COM_YOUTUBE_YOUTUBE_1 ARRAY,
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_1 ARRAY,
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_2 ARRAY,
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_SESSION_1 ARRAY,
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_1 ARRAY,
	CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_BREAK_1 ARRAY,
	UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_EVENT_1 OBJECT,
	UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_QUARTILE_EVENT_1 OBJECT
);
```

***

#### **Step 3:** Create stage


```sql
CREATE OR REPLACE STAGE snowplow_sample_media_player_events_stage
URL = 'https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/media_player/snowplow_media_player_sample_events_snowflake.csv'
FILE_FORMAT = (TYPE=CSV FIELD_DELIMITER=',' SKIP_HEADER=1, FIELD_OPTIONALLY_ENCLOSED_BY='"')
```

***
#### **Step 4:** Copy into base table FROM stage

```sql
COPY INTO TARGET_DB.ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER_BASE
FROM @snowplow_sample_media_player_events_stage
```
***

#### **Step 5:** Create the **ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER** table

```sql
CREATE OR REPLACE TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER AS (

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
    LOAD_TSTAMP,
    PARSE_JSON(EV.CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_WEB_PAGE_1) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_WEB_PAGE_1,
    PARSE_JSON(EV.CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_1) AS CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_1,
    PARSE_JSON(EV.CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1,
    PARSE_JSON(EV.CONTEXTS_ORG_WHATWG_VIDEO_ELEMENT_1) AS CONTEXTS_ORG_WHATWG_VIDEO_ELEMENT_1,
    PARSE_JSON(EV.CONTEXTS_ORG_WHATWG_MEDIA_ELEMENT_1) AS CONTEXTS_ORG_WHATWG_MEDIA_ELEMENT_1,
    PARSE_JSON(EV.CONTEXTS_COM_YOUTUBE_YOUTUBE_1) AS CONTEXTS_COM_YOUTUBE_YOUTUBE_1,
    PARSE_JSON(EV.CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_1) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_1,
    PARSE_JSON(EV.CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_2) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_2,
    PARSE_JSON(EV.CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_SESSION_1) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_SESSION_1,
    PARSE_JSON(EV.CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_1) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_1,
    PARSE_JSON(EV.CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_BREAK_1) AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_BREAK_1,
    PARSE_JSON(EV.UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_EVENT_1) AS UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_EVENT_1,
    PARSE_JSON(EV.UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_QUARTILE_EVENT_1) AS UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_QUARTILE_EVENT_1

FROM ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER_BASE )

```

***

#### **Step 6:**  Drop the **SAMPLE_EVENTS_MEDIA_PLAYER_BASE** table

```sql
DROP TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER_BASE
```
You will now have the ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER created and loaded with sample data.

{{% /tab %}}

{{% tab name="Databricks" %}}

We have provided a public S3 bucket where we store the sample data in a csv format, you should be able to download it locally through this [link](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/media_player/snowplow_media_player_sample_events.csv).

You can load the sample data to the warehouse using your `Databricks Workspace` AS described in the below steps.

For more details please check out the official [Databricks documentation](https://docs.databricks.com/ingestion/add-data/index.html).


#### **Step 1:**  Create the ATOMIC schema
If the ATOMIC schema doesn't exist, create it in your target database.

```sql
CREATE SCHEMA IF NOT EXISTS ATOMIC

```

***

#### **Step 2:**  Upload the csv file
2.1 Navigate to the `Catalog Explorer` page.

2.2 Select `+Add` -> `Add data` to get started.

2.3 Under `From local files` click `Create or modify table` and drop in the `snowplow_media_player_sample_events.csv` file. It should take a minute or two to load.

2.4 Once you see the preview, specify the catalog, the schema (atomic) and change the name to **sample_events_media_player_base**.

2.5 Under `Advanced attributes` tick `Rows span multiple lines`.

2.6 Click create table.


***

#### **Step 3:** Create the **ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER** table

The Snowplow pipeline creates context fields AS arrays but uploading the test data can be achieved through string/varchar data type first. Run the below DDL statement in your SQL editor to create the `sample_events_media_plauer` table FROM the base table including the necessary conversions:

```sql
CREATE OR REPLACE TABLE TARGET_DB.ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER AS (

SELECT
    APP_ID,
    PLATFORM,
    CAST(ETL_TSTAMP AS TIMESTAMP) AS ETL_TSTAMP,
    CAST(COLLECTOR_TSTAMP AS TIMESTAMP) AS COLLECTOR_TSTAMP,
    CAST(DVCE_CREATED_TSTAMP AS TIMESTAMP) AS DVCE_CREATED_TSTAMP,
    EVENT,
    EVENT_ID,
    CAST(TXN_ID AS BIGINT) AS TXN_ID,
    NAME_TRACKER,
    V_TRACKER,
    V_COLLECTOR,
    V_ETL,
    USER_ID,
    USER_IPADDRESS,
    CAST(USER_FINGERPRINT AS BIGINT) AS USER_FINGERPRINT,
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
    CAST(TR_TOTAL AS FLOAT) AS TR_TOTAL,
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
    CAST(PP_XOFFSET_MIN AS BIGINT) AS PP_XOFFSET_MIN,
    CAST(PP_XOFFSET_MAX AS BIGINT) AS PP_XOFFSET_MAX,
    CAST(PP_YOFFSET_MIN AS BIGINT) AS PP_YOFFSET_MIN,
    CAST(PP_YOFFSET_MAX AS BIGINT) AS PP_YOFFSET_MAX,
    REPLACE(USERAGENT, '\"', '') AS USERAGENT,
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
    CAST(BR_VIEWWIDTH AS BIGINT) AS BR_VIEWWIDTH,
    CAST(BR_VIEWHEIGHT AS BIGINT) AS BR_VIEWHEIGHT,
    OS_NAME,
    OS_FAMILY,
    OS_MANUFACTURER,
    OS_TIMEZONE,
    DVCE_TYPE,
    DVCE_ISMOBILE,
    CAST(DVCE_SCREENWIDTH AS BIGINT) AS DVCE_SCREENWIDTH,
    CAST(DVCE_SCREENHEIGHT AS BIGINT) AS DVCE_SCREENHEIGHT,
    DOC_CHARSET,
    CAST(DOC_WIDTH AS BIGINT) AS DOC_WIDTH,
    CAST(DOC_HEIGHT AS BIGINT) AS DOC_HEIGHT,
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
    CAST(DVCE_SENT_TSTAMP AS TIMESTAMP) AS DVCE_SENT_TSTAMP,
    REFR_DOMAIN_USERID,
    CAST(REFR_DVCE_TSTAMP AS TIMESTAMP) AS REFR_DVCE_TSTAMP,
    DOMAIN_SESSIONID,
    CAST(DERIVED_TSTAMP AS TIMESTAMP) AS DERIVED_TSTAMP,
    EVENT_VENDOR,
    EVENT_NAME,
    EVENT_FORMAT,
    EVENT_VERSION,
    EVENT_FINGERPRINT,
    CAST(TRUE_TSTAMP AS TIMESTAMP) AS TRUE_TSTAMP,
    CAST(LOAD_TSTAMP AS TIMESTAMP) AS LOAD_TSTAMP,
    FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_WEB_PAGE_1, 'array<struct<id:string>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_WEB_PAGE_1,
    FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_1, 'array<struct<name:string, type:string, id:string, view_controller:string, top_view_controller:string, activity:string, fragment:string>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_MOBILE_SCREEN_1,
    FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1, 'array<struct<user_id:string, session_id:string, session_index:integer, event_index:integer, previous_session_id:string, storage_mechanism:string, first_event_id:string, first_event_timestamp:string>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_CLIENT_SESSION_1,
    FROM_JSON(CONTEXTS_ORG_WHATWG_VIDEO_ELEMENT_1, 'array<struct<video_height:integer, video_width:integer, auto_picture_in_picture:boolean, disable_picture_in_picture:boolean, poster:string >>') AS CONTEXTS_ORG_WHATWG_VIDEO_ELEMENT_1,
    FROM_JSON(CONTEXTS_ORG_WHATWG_MEDIA_ELEMENT_1, 'array<struct<auto_play:boolean, current_src:string, default_muted:boolean, default_playback_rate:double ,html_id:string,media_type:string,network_state:string,preload:string,ready_state:string,seeking:boolean,cross_origin:string,disable_remote_playback:boolean,error:string,file_extension:string,fullscreen:boolean,picture_in_picture:boolean,src:string>>') AS CONTEXTS_ORG_WHATWG_MEDIA_ELEMENT_1,
    FROM_JSON(CONTEXTS_COM_YOUTUBE_YOUTUBE_1, 'array<struct<auto_play:boolean, buffering:boolean, controls:boolean, cued:boolean, loaded:integer, playback_quality:string, player_id:string, unstarted:boolean, url:string, error:string, fov:double, origin:string, pitch:double, playlist_index:double, roll:double, yaw:double>>') AS CONTEXTS_COM_YOUTUBE_YOUTUBE_1,
    FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_1, 'array<struct<current_time:double, ended:boolean, loop:boolean, muted:boolean, paused:boolean, playback_rate:double, volume:integer, duration:double, is_live:boolean, percent_progress:integer>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_1,
    FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_2, 'array<struct<current_time:double, duration:double, ended: boolean, fullscreen:boolean, livestream:boolean, label:string, loop:boolean, media_type:string, muted:boolean, paused:boolean, picture_in_picture:boolean, playback_rate:double, player_type:string, quality:string, volume:integer>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_2,
    FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_SESSION_1, 'array<struct<media_session_id:string, started_at:string, ping_interval:integer, time_played:double, time_played_muted:double, time_paused:double, content_watched:double, time_buffering:double, time_spent_ads:double, ads:integer, ads_clicked:integer, ads_skipped:integer, ad_breaks:integer, avg_playback_rate:double>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_SESSION_1,
    FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_1, 'array<struct<name:string, ad_id:string, creative_id:string, pod_position:integer, duration:double, skippable:boolean>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_1,
    FROM_JSON(CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_BREAK_1, 'array<struct<name:string, break_id:string, start_time:string, break_type:string, pod_size:integer>>') AS CONTEXTS_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_BREAK_1,
    FROM_JSON(UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_EVENT_1, 'struct<type:string, label:string>') AS UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_PLAYER_EVENT_1,
    FROM_JSON(UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_QUARTILE_EVENT_1, 'struct<percent_progress:integer>') AS UNSTRUCT_EVENT_COM_SNOWPLOWANALYTICS_SNOWPLOW_MEDIA_AD_QUARTILE_EVENT_1

FROM ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER_BASE )
```

***

#### **Step 4:**  Drop the **SAMPLE_EVENTS_MEDIA_PLAYER_BASE** table

```sql
DROP TABLE ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER_BASE
```
You will now have the ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER created and loaded with sample data.


{{% /tab %}}

{{% tab name="BigQuery" %}}

We have provided a public S3 bucket where we store the sample data in a csv format, you should be able to download it locally through this [link](https://snowplow-demo-datasets.s3.eu-central-1.amazonaws.com/media_player/snowplow_media_player_sample_events.csv).

You can load the sample data to the warehouse using your [Google Cloud console](https://console.cloud.google.com/) AS described in the below steps.

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

- For `Create table from`, SELECT `Upload`.
- For `Select file`, click `Browse`. Navigate to the `snowplow_meida_player_sample_events.csv` and open it.
- Make sure `CSV` is selected for `File format`

In the `Destination` section:

- For `Project`, choose the appropriate project (should be auto-populated).
- For `Dataset` make sure it is `atomic` (should be auto-populated).
- In the `Table` field put: `SAMPLE_EVENTS_MEDIA_PLAYER_BASE`.
- Verify that Table type is set to `Native table`.

On the `Schema` section:

- Click `Auto-detect`

Expand the `Advanced options`:

- Put 1 for `Header rows to skip`.
- Tick `Quoted newlines`.

Click `Create table`. Wait for a minute or two and the table should be created.

#### **Step 3:** Create the **ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER** table

The Snowplow pipeline creates context fields AS REPEATED fields but uploading the test data can be achieved through string/varchar data type first. Run the below DDL statement in your SQL editor to create the `SAMPLE_EVENTS_MEDIA_PLAYER` table FROM the base table including the necessary conversions:

```
CREATE OR REPLACE TABLE ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER AS (

WITH prep AS (

    SELECT
        *
        EXCEPT(
          contexts_com_snowplowanalytics_snowplow_web_page_1,
          contexts_com_snowplowanalytics_mobile_screen_1,
          contexts_com_snowplowanalytics_snowplow_client_session_1,
          contexts_org_whatwg_video_element_1,
          contexts_org_whatwg_media_element_1,
          contexts_com_youtube_youtube_1,
          contexts_com_snowplowanalytics_snowplow_media_player_1,
          contexts_com_snowplowanalytics_snowplow_media_player_2,
          contexts_com_snowplowanalytics_snowplow_media_session_1,
          contexts_com_snowplowanalytics_snowplow_media_ad_1,
          contexts_com_snowplowanalytics_snowplow_media_ad_break_1,
          unstruct_event_com_snowplowanalytics_snowplow_media_player_event_1,
          unstruct_event_com_snowplowanalytics_snowplow_media_ad_quartile_event_1
        ),
        JSON_EXTRACT_ARRAY(contexts_com_snowplowanalytics_snowplow_web_page_1) AS contexts_com_snowplowanalytics_snowplow_web_page_1,
        JSON_EXTRACT_ARRAY(contexts_com_snowplowanalytics_mobile_screen_1) AS contexts_com_snowplowanalytics_mobile_screen_1,
        JSON_EXTRACT_ARRAY(contexts_com_snowplowanalytics_snowplow_client_session_1) AS contexts_com_snowplowanalytics_snowplow_client_session_1,
        JSON_EXTRACT_ARRAY(contexts_org_whatwg_video_element_1) AS contexts_org_whatwg_video_element_1,
        JSON_EXTRACT_ARRAY(contexts_org_whatwg_media_element_1) AS contexts_org_whatwg_media_element_1,
        JSON_EXTRACT_ARRAY(contexts_com_youtube_youtube_1) AS contexts_com_youtube_youtube_1,
        JSON_EXTRACT_ARRAY(contexts_com_snowplowanalytics_snowplow_media_player_1) AS contexts_com_snowplowanalytics_snowplow_media_player_1,
        JSON_EXTRACT_ARRAY(contexts_com_snowplowanalytics_snowplow_media_player_2) AS contexts_com_snowplowanalytics_snowplow_media_player_2,
        JSON_EXTRACT_ARRAY(contexts_com_snowplowanalytics_snowplow_media_session_1) AS contexts_com_snowplowanalytics_snowplow_media_session_1,
        JSON_EXTRACT_ARRAY(contexts_com_snowplowanalytics_snowplow_media_ad_1) AS contexts_com_snowplowanalytics_snowplow_media_ad_1,
        JSON_EXTRACT_ARRAY(contexts_com_snowplowanalytics_snowplow_media_ad_break_1) AS contexts_com_snowplowanalytics_snowplow_media_ad_break_1,
        PARSE_JSON(unstruct_event_com_snowplowanalytics_snowplow_media_player_event_1) AS unstruct_event_com_snowplowanalytics_snowplow_media_player_event_1,
        PARSE_JSON(unstruct_event_com_snowplowanalytics_snowplow_media_ad_quartile_event_1) AS unstruct_event_com_snowplowanalytics_snowplow_media_ad_quartile_event_1

    FROM ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER_BASE
)

SELECT
    APP_ID,
    PLATFORM,
    CAST(ETL_TSTAMP AS TIMESTAMP) AS ETL_TSTAMP,
    CAST(COLLECTOR_TSTAMP AS TIMESTAMP) AS COLLECTOR_TSTAMP,
    CAST(DVCE_CREATED_TSTAMP AS TIMESTAMP) AS DVCE_CREATED_TSTAMP,
    EVENT,
    EVENT_ID,
    CAST(TXN_ID AS INT64) AS TXN_ID,
    NAME_TRACKER,
    V_TRACKER,
    V_COLLECTOR,
    V_ETL,
    USER_ID,
    USER_IPADDRESS,
    CAST(USER_FINGERPRINT AS INT64) AS USER_FINGERPRINT,
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
    CAST(TR_TOTAL AS FLOAT64) AS TR_TOTAL,
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
    CAST(PP_XOFFSET_MIN AS INT64) AS PP_XOFFSET_MIN,
    CAST(PP_XOFFSET_MAX AS INT64) AS PP_XOFFSET_MAX,
    CAST(PP_YOFFSET_MIN AS INT64) AS PP_YOFFSET_MIN,
    CAST(PP_YOFFSET_MAX AS INT64) AS PP_YOFFSET_MAX,
    REPLACE(USERAGENT, '\"', '') AS USERAGENT,
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
    CAST(BR_VIEWWIDTH AS INT64) AS BR_VIEWWIDTH,
    CAST(BR_VIEWHEIGHT AS INT64) AS BR_VIEWHEIGHT,
    OS_NAME,
    OS_FAMILY,
    OS_MANUFACTURER,
    OS_TIMEZONE,
    DVCE_TYPE,
    DVCE_ISMOBILE,
    CAST(DVCE_SCREENWIDTH AS INT64) AS DVCE_SCREENWIDTH,
    CAST(DVCE_SCREENHEIGHT AS INT64) AS DVCE_SCREENHEIGHT,
    DOC_CHARSET,
    CAST(DOC_WIDTH AS INT64) AS DOC_WIDTH,
    CAST(DOC_HEIGHT AS INT64) AS DOC_HEIGHT,
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
    CAST(DVCE_SENT_TSTAMP AS TIMESTAMP) AS DVCE_SENT_TSTAMP,
    REFR_DOMAIN_USERID,
    CAST(REFR_DVCE_TSTAMP AS TIMESTAMP) AS REFR_DVCE_TSTAMP,
    DOMAIN_SESSIONID,
    CAST(DERIVED_TSTAMP AS TIMESTAMP) AS DERIVED_TSTAMP,
    EVENT_VENDOR,
    EVENT_NAME,
    EVENT_FORMAT,
    EVENT_VERSION,
    EVENT_FINGERPRINT,
    CAST(TRUE_TSTAMP AS TIMESTAMP) AS TRUE_TSTAMP,
    CAST(LOAD_TSTAMP AS TIMESTAMP) AS LOAD_TSTAMP,
    ARRAY(
      SELECT AS struct JSON_EXTRACT_SCALAR(json_array,'$.id') AS id
      FROM unnest(contexts_com_snowplowanalytics_snowplow_web_page_1) AS json_array
    ) AS contexts_com_snowplowanalytics_snowplow_web_page_1,
    ARRAY(
      SELECT AS struct JSON_EXTRACT_SCALAR(json_array,'$.name') AS name,
                      JSON_EXTRACT_SCALAR(json_array,'$.type') AS type,
                      JSON_EXTRACT_SCALAR(json_array,'$.id') AS id,
                      JSON_EXTRACT_SCALAR(json_array,'$.view_controller') AS view_controller,
                      JSON_EXTRACT_SCALAR(json_array,'$.top_view_controller') AS top_view_controller,
                      JSON_EXTRACT_SCALAR(json_array,'$.activity') AS activity,
                      JSON_EXTRACT_SCALAR(json_array,'$.fragment') AS fragment
      FROM unnest(contexts_com_snowplowanalytics_mobile_screen_1) AS json_array
    ) AS contexts_com_snowplowanalytics_mobile_screen_1,
    ARRAY(
      SELECT AS struct JSON_EXTRACT_SCALAR(json_array,'$.user_id') AS user_id,
                      JSON_EXTRACT_SCALAR(json_array,'$.session_id') AS session_id,
                      JSON_EXTRACT_SCALAR(json_array,'$.session_index') AS session_index,
                      JSON_EXTRACT_SCALAR(json_array,'$.event_index') AS event_index,
                      JSON_EXTRACT_SCALAR(json_array,'$.previous_session_id') AS previous_session_id,
                      JSON_EXTRACT_SCALAR(json_array,'$.storage_mechanism') AS storage_mechanism,
                      JSON_EXTRACT_SCALAR(json_array,'$.first_event_id') AS first_event_id,
                      JSON_EXTRACT_SCALAR(json_array,'$.first_event_timestamp') AS first_event_timestamp
      FROM unnest(contexts_com_snowplowanalytics_snowplow_client_session_1) AS json_array
    ) AS contexts_com_snowplowanalytics_snowplow_client_session_1,
    ARRAY(
      SELECT AS struct JSON_EXTRACT_SCALAR(json_array,'$.video_height') AS video_height,
                      JSON_EXTRACT_SCALAR(json_array,'$.video_width') AS video_width,
                      JSON_EXTRACT_SCALAR(json_array,'$.auto_picture_in_picture') AS auto_picture_in_picture,
                      JSON_EXTRACT_SCALAR(json_array,'$.disable_picture_in_picture') AS disable_picture_in_picture,
                      JSON_EXTRACT_SCALAR(json_array,'$.poster') AS poster
      FROM unnest(contexts_org_whatwg_video_element_1) AS json_array
    ) AS contexts_org_whatwg_video_element_1,
    ARRAY(
      SELECT AS struct JSON_EXTRACT_SCALAR(json_array,'$.auto_play') AS auto_play,
                      JSON_EXTRACT_SCALAR(json_array,'$.current_src') AS current_src,
                      JSON_EXTRACT_SCALAR(json_array,'$.default_muted') AS default_muted,
                      JSON_EXTRACT_SCALAR(json_array,'$.default_playback_rate') AS default_playback_rate,
                      JSON_EXTRACT_SCALAR(json_array,'$.html_id') AS html_id,
                      JSON_EXTRACT_SCALAR(json_array,'$.media_type') AS media_type,
                      JSON_EXTRACT_SCALAR(json_array,'$.network_state') AS network_state,
                      JSON_EXTRACT_SCALAR(json_array,'$.preload') AS preload,
                      JSON_EXTRACT_SCALAR(json_array,'$.ready_state') AS ready_state,
                      JSON_EXTRACT_SCALAR(json_array,'$.seeking') AS seeking,
                      JSON_EXTRACT_SCALAR(json_array,'$.cross_origin') AS cross_origin,
                      JSON_EXTRACT_SCALAR(json_array,'$.disable_remote_playback') AS disable_remote_playback,
                      JSON_EXTRACT_SCALAR(json_array,'$.error') AS error,
                      JSON_EXTRACT_SCALAR(json_array,'$.file_extension') AS file_extension,
                      JSON_EXTRACT_SCALAR(json_array,'$.fullscreen') AS fullscreen,
                      JSON_EXTRACT_SCALAR(json_array,'$.picture_in_picture') AS picture_in_picture,
                      JSON_EXTRACT_SCALAR(json_array,'$.played') AS played,
                      JSON_EXTRACT_SCALAR(json_array,'$.src') AS src,
                      JSON_EXTRACT_SCALAR(json_array,'$.text_tracks') AS text_tracks
      FROM unnest(contexts_org_whatwg_media_element_1) AS json_array
    ) AS contexts_org_whatwg_media_element_1,
    ARRAY(
      SELECT AS struct JSON_EXTRACT_SCALAR(json_array,'$.auto_play') AS auto_play,
                      JSON_EXTRACT_SCALAR(json_array,'$.available_playback_rates') AS available_playback_rates,
                      JSON_EXTRACT_SCALAR(json_array,'$.buffering') AS buffering,
                      JSON_EXTRACT_SCALAR(json_array,'$.controls') AS controls,
                      JSON_EXTRACT_SCALAR(json_array,'$.cued') AS cued,
                      JSON_EXTRACT_SCALAR(json_array,'$.loaded') AS loaded,
                      JSON_EXTRACT_SCALAR(json_array,'$.playback_quality') AS playback_quality,
                      JSON_EXTRACT_SCALAR(json_array,'$.player_id') AS player_id,
                      JSON_EXTRACT_SCALAR(json_array,'$.unstarted') AS unstarted,
                      JSON_EXTRACT_SCALAR(json_array,'$.url') AS url,
                      JSON_EXTRACT_SCALAR(json_array,'$.error') AS error,
                      JSON_EXTRACT_SCALAR(json_array,'$.fov') AS fov,
                      JSON_EXTRACT_SCALAR(json_array,'$.origin') AS origin,
                      JSON_EXTRACT_SCALAR(json_array,'$.pitch') AS pitch,
                      JSON_EXTRACT_SCALAR(json_array,'$.playlist') AS playlist,
                      JSON_EXTRACT_SCALAR(json_array,'$.playlist_index') AS playlist_index,
                      JSON_EXTRACT_SCALAR(json_array,'$.roll') AS roll,
                      JSON_EXTRACT_SCALAR(json_array,'$.yaw') AS yaw
      FROM unnest(contexts_com_youtube_youtube_1) AS json_array
      ) AS contexts_com_youtube_youtube_1,
    ARRAY(
      SELECT AS struct cast(JSON_EXTRACT_SCALAR(json_array,'$.current_time') AS float64) AS current_time,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.ended') AS boolean) AS ended,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.loop') AS boolean) AS loop,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.muted') AS boolean) AS muted,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.paused') AS boolean) AS paused,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.playback_rate') AS float64) AS playback_rate,
                      JSON_EXTRACT_SCALAR(json_array,'$.volume') AS volume,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.duration') AS float64) AS duration,
                      JSON_EXTRACT_SCALAR(json_array,'$.is_live') AS is_live,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.percent_progress') AS integer) AS percent_progress
      FROM unnest(contexts_com_snowplowanalytics_snowplow_media_player_1) AS json_array
    ) AS contexts_com_snowplowanalytics_snowplow_media_player_1,
    ARRAY(
      SELECT AS struct cast(JSON_EXTRACT_SCALAR(json_array,'$.current_time') AS float64) AS current_time,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.duration') AS float64) AS duration,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.ended') AS boolean) AS ended,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.fullscreen') AS boolean) AS fullscreen,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.livestream') AS boolean) AS livestream,
                      JSON_EXTRACT_SCALAR(json_array,'$.label') AS label,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.loop') AS boolean) AS loop,
                      JSON_EXTRACT_SCALAR(json_array,'$.media_type') AS media_type,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.muted') AS boolean) AS muted,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.paused') AS boolean) AS paused,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.picture_in_picture') AS boolean) AS picture_in_picture,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.playback_rate') AS float64) AS playback_rate,
                      JSON_EXTRACT_SCALAR(json_array,'$.player_type') AS player_type,
                      JSON_EXTRACT_SCALAR(json_array,'$.quality') AS quality,
                      JSON_EXTRACT_SCALAR(json_array,'$.volume') AS volume

      FROM unnest(contexts_com_snowplowanalytics_snowplow_media_player_2) AS json_array
    ) AS contexts_com_snowplowanalytics_snowplow_media_player_2,
    ARRAY(
      SELECT AS struct JSON_EXTRACT_SCALAR(json_array,'$.media_session_id') AS media_session_id,
                      JSON_EXTRACT_SCALAR(json_array,'$.started_at') AS started_at,
                      JSON_EXTRACT_SCALAR(json_array,'$.ping_interval') AS ping_interval,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.time_played') AS float64) AS time_played,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.time_played_muted') AS float64) AS time_played_muted,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.time_paused') AS float64) AS time_paused,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.content_watched') AS float64) AS content_watched,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.time_buffering') AS float64) AS time_buffering,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.time_spent_ads') AS float64) AS time_spent_ads,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.ads') AS integer) AS ads,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.ads_clicked') AS integer) AS ads_clicked,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.ads_skipped') AS integer) AS ads_skipped,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.ad_breaks') AS integer) AS ad_breaks,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.avg_playback_rate') AS float64) AS avg_playback_rate

      FROM unnest(contexts_com_snowplowanalytics_snowplow_media_session_1) AS json_array
    ) AS contexts_com_snowplowanalytics_snowplow_media_session_1,
    ARRAY(
      SELECT AS struct JSON_EXTRACT_SCALAR(json_array,'$.name') AS name,
                      JSON_EXTRACT_SCALAR(json_array,'$.ad_id') AS ad_id,
                      JSON_EXTRACT_SCALAR(json_array,'$.creative_id') AS creative_id,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.pod_position') AS integer) AS pod_position,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.duration') AS float64) AS duration,
                      cast(JSON_EXTRACT_SCALAR(json_array,'$.skippable') AS boolean) AS skippable

      FROM unnest(contexts_com_snowplowanalytics_snowplow_media_ad_1) AS json_array
    ) AS contexts_com_snowplowanalytics_snowplow_media_ad_1,
    ARRAY(
      SELECT AS struct JSON_EXTRACT_SCALAR(json_array,'$.name') AS name,
                      JSON_EXTRACT_SCALAR(json_array,'$.break_id') AS break_id,
                      JSON_EXTRACT_SCALAR(json_array,'$.start_time') AS start_time,
                      JSON_EXTRACT_SCALAR(json_array,'$.break_type') AS break_type,
                      JSON_EXTRACT_SCALAR(json_array,'$.pod_size') AS pod_size

      FROM unnest(contexts_com_snowplowanalytics_snowplow_media_ad_break_1) AS json_array
    ) AS contexts_com_snowplowanalytics_snowplow_media_ad_break_1,

    struct(
      JSON_EXTRACT_SCALAR(unstruct_event_com_snowplowanalytics_snowplow_media_player_event_1,'$.type') AS type,
      JSON_EXTRACT_SCALAR(unstruct_event_com_snowplowanalytics_snowplow_media_player_event_1,'$.label') AS label
    ) AS unstruct_event_com_snowplowanalytics_snowplow_media_player_event_1,

    struct(
      cast(JSON_EXTRACT_SCALAR(unstruct_event_com_snowplowanalytics_snowplow_media_ad_quartile_event_1,'$.percent_progress') AS integer) AS percent_progress
    ) AS unstruct_event_com_snowplowanalytics_snowplow_media_ad_quartile_event_1


FROM prep

)

```

***

#### **Step 4:**  Drop the **SAMPLE_EVENTS_MEDIA_PLAYER_BASE** table

```sql
DROP TABLE ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER_BASE
```
You will now have the ATOMIC.SAMPLE_EVENTS_MEDIA_PLAYER created and loaded with sample data.

{{% /tab %}}

{{< /tabs >}}
