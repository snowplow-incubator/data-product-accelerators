+++
title = "Setup your tracking"
weight = 1
+++
 
There are a number of options to implement Snowplow tracking in your website or single page application.

Select the required pathway to implement tracking on your project.

{{< tabs groupId="select_js" >}}
{{% tab name="Javascript" %}}

#### **Step 1:** Download sp.js
Add the sp.js file to your project directory. The latest version can be found **[here](https://github.com/snowplow/snowplow-javascript-tracker/releases).**

***

#### **Step 2:** Add JS snippet
Add the below snippet to all of the pages you would like to track. **Make sure to update the {{Link to the sp.js file}} variable.**

Place the `<script>` tag into the `<head>` element of your page.

<!-- Typically this will be placed into the `<head>` element of your page or in a similar, suitable, location if using a Single Page Application framework. -->

```html
<script type="text/javascript" async=1 >
;(function (p, l, o, w, i, n, g) { if (!p[i]) { p.GlobalSnowplowNamespace = p.GlobalSnowplowNamespace || []; p.GlobalSnowplowNamespace.push(i); p[i] = function () { (p[i].q = p[i].q || []).push(arguments) }; p[i].q = p[i].q || []; n = l.createElement(o); g = l.getElementsByTagName(o)[0]; n.async = 1; n.src = w; g.parentNode.insertBefore(n, g) } }(window, document, "script", "{{Link to sp.js file}}", "snowplow"));
</script>
```

***

#### **Step 3:** Configure the Tracker
Call `newTracker` in the `<script>` tag, with the following arguments. This creates an instance of a basic tracker without any additional context.

- Tracker Name: `'sp'`
- Collector Url: `'{{Url for Collector}}'`

```javascript
window.snowplow('newTracker', 'sp', '{{Url for Collector}}')
```

<!-- **should we point the collector to mini/micro collector for testing??** -->

In addition to the basic tracker, add the below optional arguments to the tracker to make use of some of Snowplow's more advanced features.

<!-- **Optional Settings (JSON):** -->
  - `appId`: Identify events that occur on different applications
  - `platform`: Identify the platform the event occurred on, in this case `web`
  - `cookieSameSite`: Protects cookies from being accessed by third party domains

```javascript
window.snowplow('newTracker', 'sp', '{{Url for Collector}}', {
    appId: 'appId',
    platform: 'web',
    cookieSameSite: 'Lax',
});
```

{{% /tab %}}
{{% tab name="React" %}}

❗❗**NOTE: `react-router-dom` is required to implement tracking in a react app**

#### **Step 1:** Install browser-tracker package

Install the `@snowplow/browser-tracker` via npm by running:

```bash
npm install @snowplow/browser-tracker
```

<!-- **Have react router dom installed** -->

***

#### **Step 2:** Import the tracker package
In your `src` folder, create a file called `tracker.js`.

Import the browser tracker into `tracker.js` with the below snippet:

```javascript
import React from 'react';
import { newTracker, trackPageView, enableActivityTracking } from "@snowplow/browser-tracker";
```

***

#### **Step 3:** Configure the tracker
Create the tracker in `tracker.js` with the with the following arguments. This creates an instance of a basic tracker without any additional context.

- Tracker Name: `'sp'`
- Collector Url: `'{{Url for Collector}}'`

```javascript
let tracker = newTracker('sp', '{{Url for Collector}}')
```

In addition to the basic tracker, add the below optional arguments to the tracker to make use of some of Snowplow's more advanced features.

  - `appId`: Identify events that occur on different applications
  - `platform`: Identify the platform the event occurred on, in this case `web`
  - `cookieSameSite`: Protects cookies from being accessed by third party domains

```javascript
let tracker = newTracker('sp', '{{Url for Collector}}', {
    appId: 'appId',
    platform: 'web',
    cookieSameSite: 'Lax',
});

```

{{% /tab %}}
{{% tab name="Angular" %}}

#### **Step 1:** Install browser-tracker package

Install the `@snowplow/browser-tracker` via npm by running:

```bash
npm install @snowplow/browser-tracker
```

***

####  **Step 2:** Generate Snowplow service
Run `ng generate service snowplow` to create `snowplow.service.ts` and `snowplow.service.spec.ts` within `src/app`.

Import the browser tracker to `snowplow.service.ts` by adding the snippet below.

```javascript
import { newTracker, trackPageView, enableActivityTracking, BrowserTracker } from "@snowplow/browser-tracker";
```

***

#### **Step 3:**  Configure the tracker
Create the tracker with the with the following arguments. This creates an instance of a basic tracker without any additional context.

- Tracker Name: `'sp'`
- Collector Url: `'{{Url for Collector}}'`

Add the below snippet to `snowplow.service.ts`

```javascript
export class SnowplowService {
  tracker: BrowserTracker = newTracker('sp', '{{Url for Collector}}')
}

```

In addition to the basic tracker, add the below optional arguments to the tracker to make use of some of Snowplow's more advanced features.

  - `appId`: Identify events that occur on different applications
  - `platform`: Identify the platform the event occurred on, in this case `web`
  - `cookieSameSite`: Protects cookies from being accessed by third party domains

```javascript
export class SnowplowService {
  tracker: BrowserTracker = newTracker('sp',  '{{Url for Collector}}', {
    appId: 'appId',
    platform: 'web',
    cookieSameSite: 'Lax',
  })
}
```
{{% /tab %}}
{{% tab name="GTM" %}}

❗❗**NOTE: A Google Tag Manager Account is required for this pathway**

#### **Step 1:** Create container
Create a web container for your site.
![Create container](../images/create_container.png?classes=shadow)

#### **Step 2:** Add Tags to site
Install Google Tag Manager on your site by following the [installation guide](https://support.google.com/tagmanager/answer/6103696?hl=en#install) in the Install Tag Manager Box.

Tip: Near the top of the window, find your container ID, formatted as "GTM-XXXXXX". Click your container ID to launch the Install Tag Manager box.

![Install GTM](../images/google_tag.png)

#### **Step 3:** Add New Template Variable
Go to `Templates` and click `Search Gallery` under `Variable Templates`.
![Variable Template](../images/add_variable_template.png?classes=shadow)

Search `Snowplow V3 Settings` in the search bar.
![Variable Search](../images/variable_search.png?classes=shadow)

Add the template to your workspace.
![Add to workspace](../images/template_to_workspace.png?classes=shadow)

Navigate to Variables, click new and select `Snowplow v3 Settings`.
![Add Variable](../images/add_variable_config.png?classes=shadow)

Add your collector endpoint and link to your `sp.js` file.
![Edit Variables](../images/edit_variables.png?classes=shadow)

#### **Step 4:** Add New Tag Template
Go to `Templates` and click `Search Gallery` under `Tag Templates`.
![Tag Template](../images/add_tag_template.png?classes=shadow)

Search `Snowplow V3` in the search bar.
![Tag Search](../images/tag_search.png?classes=shadow)

Add the template to your workspace.
![Tag to workspace](../images/tag_to_workspace.png?classes=shadow)


{{% /tab %}}
{{< /tabs >}}


