+++
title = "Connect Snowplow to your CMP events"
weight = 2
+++

Most companies use consent management platforms to manage consent selection for their website visitors. A CMP allows users to understand how and why data is collected from a website and then accept, deny or configure which scopes they consent to.

We will demonstrate how you can use [Cookiebot](https://www.cookiebot.com/) methods to hook into consent preference selection programmatically and send this data to Snowplow. Most CMPs have similar functionality so everything shown in this guide can be adjusted to suit your needs.

![cookiebot](../images/cookiebot.png?width=50pc)


#### Subscribe to consent selection events

Based on the Cookiebot developer [documentation](https://www.cookiebot.com/en/developer/#h-event-handling) you can subscribe to many different events relating to user actions. The ones we are interested in for preference selection are the `CookiebotOnAccept` and `CookiebotOnDecline`. These events fire when a visitor selects to deny or accept, partially or completely, all optional data collection scopes on a website.

To do that we are going to create a function called `trackConsent` and listen to both of the events listed above.

```js
window.addEventListener("CookiebotOnAccept", trackConsent, false);
window.addEventListener("CookiebotOnDecline", trackConsent, false);
```

Any other consent management platform will have similar capabilities to hook into these events.

#### Send consent preference selection events to Snowplow

The `trackConsent` function will try to discern the cases in which the visitor denied, accepted or partially accepted data collection scopes and send the appropriate action to Snowplow.

{{< tabs groupId="select_js" >}}
{{% tab name="Browser API" %}}

```js
function trackConsent() {
  /*
   * Use window.Cookiebot.consent which contains the selected scopes.
   */
  const availableScopes = Object.keys(window.Cookiebot.consent).filter(
    (key) => typeof window.Cookiebot.consent[key] === "boolean"
  );
  const consentScopes = availableScopes.filter(
    (key) => window.Cookiebot.consent[key]
  );

  /*
   * Build the enhanced consent object to send to Snowplow.
   */
  const enhancedConsent = {
    consentScopes,
    basisForProcessing: "consent",
    consentUrl: "https://www.example.com/",
    consentVersion: "1.0",
    domainsApplied: ["https://www.example.com/"],
    gdprApplies: window.Cookiebot.regulations.gdprApplies
  };

  /* If it is a selection and not a page load. */
  if (window.Cookiebot.changed) {
    /* Necessary cookies are always included. */
    if (consentScopes.length === 1) {
      trackConsentDeny(enhancedConsent);
    } else if (
      /* Not all scopes are consented to. */
      consentScopes.length !== availableScopes.length
    ) {
      trackConsentSelected(enhancedConsent);
    } else {
      trackConsentAllow(enhancedConsent);
    }
  }
}
```

{{% /tab %}}
{{% tab name="JavaScript API" %}}

```js
function trackConsent() {
  /*
   * Use window.Cookiebot.consent which contains the selected scopes.
   */
  const availableScopes = Object.keys(window.Cookiebot.consent).filter(
    (key) => typeof window.Cookiebot.consent[key] === "boolean"
  );
  const consentedScopes = availableScopes.filter(
    (key) => window.Cookiebot.consent[key]
  );

  /*
   * Build the enhanced consent object to send to Snowplow.
   */
  const enhancedConsent = {
    consentedScopes,
    basisForProcessing: "consent",
    consentUrl: "https://www.example.com/",
    consentVersion: "1.0",
    domainsApplied: ["https://www.example.com/"],
  };

  /* If it is a selection and not a page load. */
  if (window.Cookiebot.changed) {
    /* Necessary cookies are always included. */
    if (consentedScopes.length === 1) {
      window.snowplow("trackConsentDeny:{trackerName}", enhancedConsent);
    } else if (
      /* Not all scopes are consented to. */
      consentedScopes.length !== availableScopes.length
    ) {
      window.snowplow("trackConsentSelected:{trackerName}", enhancedConsent);
    } else {
      window.snowplow("trackConsentAllow:{trackerName}", enhancedConsent);
    }
  }
}
```

{{% /tab %}}

{{< /tabs >}}

{{% notice info %}}
The example above assumes that `partial consent` is when the visitor does not accept all the available scopes, but a selection of them. The use case for your application could as well be targeting the type of button that was pressed which reveals different intent. The API is designed to fit a variety of use-cases, you just need to add the code modified for your selected consent management platform.
{{% /notice %}}