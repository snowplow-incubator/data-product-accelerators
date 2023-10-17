+++
title = "Set up your tracking"
weight = 1
+++

Depending on your store's front-end infrastructure and Snowplow set-up, you can use either our JavaScript tracker for a `<script>` tag option or our Browser tracker for a more modern web development set-up.

In both options, the API is similar with only minor differences in the set-up and method calls.

There are also instruction for setting up the tracker with a Shopify store and GTM.

{{< tabs groupId="select_js" >}}
{{% tab name="Browser API" %}}

#### **Step 1:** Install browser-tracker package

Install the `@snowplow/browser-tracker` and `@snowplow/browser-plugin-snowplow-ecommerce` via npm, yarn or any other package manager of your choice. Example using `npm`:

```bash
npm install @snowplow/browser-tracker @snowplow/browser-plugin-snowplow-ecommerce
```

---

#### **Step 2:** Create the tracker

In your `src` folder, create a file called `tracker.js`. Inside it create the `tracker` object using the snippet below to use it anywhere in the application:

- Tracker Name: `'sp'`
- Collector Url: `'{{Url for Collector}}'`

```javascript
import { newTracker } from "@snowplow/browser-tracker";

export const tracker = newTracker("sp", "{{Url for Collector}}", {
  /* tracker options */
});
```

In addition to the basic tracker, you can add any number of options for using Snowplow's more advanced features. <a target="_blank" href="https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/tracker-setup/initialization-options/">See more on our documentation</a>.

---

#### **Step 3:** Configure the tracker to use the `SnowplowEcommercePlugin`

To allow the tracker to use e-commerce methods from the `SnowplowEcommercePlugin`, you need to include during the initialization of the tracker. By adding it on the `plugins` array, you gain access to the full functionality:

```javascript
import { newTracker } from "@snowplow/browser-tracker";
import { SnowplowEcommercePlugin } from "@snowplow/browser-plugin-snowplow-ecommerce";

export const tracker = newTracker("sp", "{{Url for Collector}}", {
  /* tracker options */
  plugins: [SnowplowEcommercePlugin()],
});
```

Now the tracker has everything required to start collecting e-commerce action data. On the next step we are going to see how to use the available APIs.

{{% /tab %}}
{{% tab name="Javascript API" %}}

#### **Step 1:** Download sp.js

Add the `sp.js` file in your project and add it to a link-accessible server directory e.g. `public/`. The latest version can be found **[here](https://github.com/snowplow/snowplow-javascript-tracker/releases).**

---

#### **Step 2:** Add the Snowplow JavaScript snippet

Add the below snippet to all of the pages you would like to use Snowplow tracking. **Make sure to update the {{Link to the sp.js file}} variable.**

Place the `<script>` tag into the `<head>` element of your pages:

```html
<script type="text/javascript">
  (function (p, l, o, w, i, n, g) {
    if (!p[i]) {
      p.GlobalSnowplowNamespace = p.GlobalSnowplowNamespace || [];
      p.GlobalSnowplowNamespace.push(i);
      p[i] = function () {
        (p[i].q = p[i].q || []).push(arguments);
      };
      p[i].q = p[i].q || [];
      n = l.createElement(o);
      g = l.getElementsByTagName(o)[0];
      n.async = 1;
      n.src = w;
      g.parentNode.insertBefore(n, g);
    }
  })(window, document, "script", "{{Link to sp.js file}}", "snowplow");
</script>
```

---

#### **Step 3:** Configure the global `tracker` instance

You can now create the `newTracker`, with the following arguments. This creates an instance of a basic tracker without any additional context.

- Tracker Name: `'sp'`
- Collector Url: `'{{Url for Collector}}'`

```javascript
window.snowplow("newTracker", "sp", "{{Url for Collector}}", {
  /* tracker options */
});
```

In addition to the basic tracker, you can add any number of options for using Snowplow's more advanced features. <a target="_blank" href="https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/javascript-tracker/javascript-tracker-v3/tracker-setup/initialization-options/">See more on our documentation</a>.

#### **Step 4:** Configure the tracker to use the `SnowplowEcommercePlugin`

To add the `SnowplowEcommercePlugin` on the JavaScript tracker and enable the usage of the e-commerce API, you should include it as shown below:

❗❗**NOTE: The script below should be executed **before** any e-commerce API can be called successfully.**

```javascript
window.snowplow(
  "addPlugin:sp",
  "https://cdn.jsdelivr.net/npm/@snowplow/browser-plugin-snowplow-ecommerce@3/dist/index.umd.min.js",
  ["snowplowEcommerceAccelerator", "SnowplowEcommercePlugin"]
);
```

Now the tracker has everything required to start collecting e-commerce action data. On the next step we are going to see how to use the available APIs.

{{% /tab %}}
{{% tab name="Shopify" %}}

#### **Step 1:** Initialize Snowplow Tracker

Add a custom HTML tag to your GTM workspace as below. It should fire on all pages with priority 999:

``` javascript
<script type="text/javascript" >
  /* Set up tracker, plugins, link click tracking and page pings
  ** This tag is set to fire first with priority 999
  */
  ; (function (p, l, o, w, i, n, g) {
    if (!p[i]) {
      p.GlobalSnowplowNamespace = p.GlobalSnowplowNamespace || [];
      p.GlobalSnowplowNamespace.push(i); p[i] = function () {
        (p[i].q = p[i].q || []).push(arguments)
      }; p[i].q = p[i].q || []; n = l.createElement(o); g = l.getElementsByTagName(o)[0]; n.async = 1;
      n.src = w; g.parentNode.insertBefore(n, g)
    }
  } (window, document, "script", "https://cdn.jsdelivr.net/npm/@snowplow/javascript-tracker@latest/dist/sp.js", "snowplow"));
  window.snowplow('newTracker', 'sp', "{{Url for Collector}}", {
    encodeBase64: false,
    appId: '{{App ID}}',
    platform: 'web',
    contexts: {
      webPage: true,
      performanceTiming: true
    }
  });
  
  // Add ecommerce accelerator plugin
  window.snowplow(
    'addPlugin',
    'https://cdn.jsdelivr.net/npm/@snowplow/browser-plugin-snowplow-ecommerce@latest/dist/index.umd.min.js',
    ['snowplowEcommerceAccelerator', 'SnowplowEcommercePlugin']
  );
  
  // Set up heartbeats to fire every 5 seconds
  snowplow('enableActivityTracking', {
    minimumVisitLength: 5,
    heartbeatDelay: 10
  });
  // Enable link click tracking
  snowplow('enableLinkClickTracking');
  
</ script>
```

#### **Step 2:** Add shopify `.liquid` files
Additionally, add the following `.liquid` files to your Shopify Theme. You will need to add your GTM tag to the script.

##### headerDataLayer.liquid

```
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXX');</script>
<!-- End Google Tag Manager -->
    
{% comment %} Product view data layer v2.1 - part of "Shopify GA4 Kit" by Analyzify
Visit https://analyzify.com/shopify-google-analytics/ga4 for complete tutorial
{% endcomment %}

{% assign template_name = template.name %}

<script type="text/javascript">
// initialise datalayer
window.dataLayer = window.dataLayer || [];

window.appStart = function(){
  // When on a product page, send the the product info to datalayer
  window.productPageHandle = function(){
    // Note: Shopify doesn't let you get productCategory
    var productName = "{{ product.title | remove: "'" | remove: '"' }}";
    var productId = "{{ product.id }}";
    var productPrice = "{{ product.price | money_without_currency }}";
    var productBrand = "{{ product.vendor | remove: "'" | remove: '"' }}";
    var productCollection = "{{ product.collections.first.title | remove: "'" | remove: '"' }}";
    var productType = "{{ product.type | remove: "'" | remove: '"' }}";
    var productSku = "{{ product.selected_or_first_available_variant.sku | remove: "'" | remove: '"' }}";
    var productVariantId = "{{ product.selected_variant.id | default: product.variants[0].id }}";
    var productVariantTitle = "{{ product.selected_variant.title | default: product.variants[0].title }}";

    window.dataLayer.push({
      event: "shopifyProductDetail",
      productId: productId,
      productName: productName,
      productPrice: productPrice,
      productBrand: productBrand,
      productCategory: productType, //Snowplow calls productCategory what shopify calls product.type
      productCollection: productCollection,
      productSku: productSku,
      productVariantId: productVariantId,
      productVariantTitle: productVariantTitle,
      currency: "{{ shop.currency }}",
    });
  };

  // For all page_views send user information. It's different if on order page
  window.allPageHandle = function(){
    // When on the order page, the customer's order vars are populated
    {% if template == 'order' %}
    window.dataLayer.push({
      event: "shopifyUserInfo",
      contentGroup: "{{ template_name }}",
      {% if customer %}
      userType: "member",
      customer: {
        id: "{{- checkout.customer.id | json -}}",
        firstName: {{- customer.first_name  | json -}},
        lastName: {{- customer.last_name  | json -}},
        email: {{- customer.email  | json -}}
        lastOrder: "{{- customer.last_order.created_at | date: '%B %d, %Y %I:%M%p' -}}",
        orderCount: "{{- checkout.customer.orders_count | json -}}",
        totalSpent: "{{- checkout.customer.total_spent | times: 0.01 | json -}}",
        tags: {{- checkout.customer.tags | json -}}
      }
      {% else %}
        userType: "visitor",
      {% endif %}
    });
  
    // not on an order page, only track standard data
    {% else %}
    window.dataLayer.push({
      event: "shopifyUserInfo",
      contentGroup: "{{ template_name }}",
      {% if customer %}
      userType: "member",
      customer: {
        id: "{{- customer.id | json -}}",
        firstName: {{- customer.first_name  | json -}},
        lastName: {{- customer.last_name  | json -}},
        email: {{- customer.email  | json -}}
      }
      {% else %}
        userType: "visitor",
      {% endif %}
    });
    {% endif %}
  };

  // run on all pages
  allPageHandle();

  {% case template_name %}
  {% when "product" %}
    // add product info on product page
    productPageHandle();
  {% endcase %}

  // Add the cart info to datalayer
  var cartItems = [];
  var cartTotal = 0;
  {% for item in cart.items %}
    cartItems.push({
      id: {{ item.variant.id }},
      name: "{{ item.title | escape }}",
      price: {{ item.variant.price | money_without_currency | remove: ',' }},
      quantity: {{ item.quantity }}
    });
    cartTotal += {{ item.variant.price | money_without_currency | remove: ',' | times: item.quantity }};
  {% endfor %}

  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: 'cartInfo',
      cartCurrency: '{{ shop.currency }}',
      cartProducts: cartItems,
      cartTotalValue: cartTotal
  });

}

// run the datalayer script
appStart();
</script>
```

##### bodyDataLayerTracking.liquid
```
// Call the trackProductData function with the product data on page load
    document.addEventListener('DOMContentLoaded', function() {
      // Assuming we're on collection screen
      var products = {{ collection.products | json }};
      var collectionName = {{ collection.title | json }};
      
      if (products) {
        // Define the data for the event
        var eventData = {
          'event': 'productData',
          'currency': "{{ shop.currency }}",
          'products': []
        };
    
        // Loop through the product data and add each product to the array in the event data
        for (var i = 0; i < products.length; i++) {
          var product = products[i];
          var productData = {
            position: i+1,
            productId: String(product.id),
            productName: product.title,
            productPrice: (product.price * 0.01), 
            productCategory: product.type,
            productCollection: collectionName,
            productBrand: product.vendor,
            productUrl: '{{ product.url }}',
            productImageUrl: product.featured_image.src
          };
          eventData.products.push(productData);
        }
    
        // Push the event data object to the DataLayer
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push(eventData);
      }

      // Check if we are on a search results page instead
      if (window.location.pathname.startsWith('/search')) {
        // Get the search term from the URL
        var urlParams = new URLSearchParams(window.location.search);
        var products = [];
        var searchTerm = '';
        searchTerm = urlParams.get('q');
    
        // Loop through the search results and extract the product data
        var searchResults = document.querySelectorAll('.product-card-wrapper');
        for (var i = 0; i < searchResults.length; i++) {
          var searchResult = searchResults[i];
          var productData = {
            'productId': searchResult.querySelector('.card__information h3 a').id.match(/\d+/)[0],
            'productName': searchResult.querySelector('.card__information').innerText.trim(),
            'productPrice': searchResult.querySelector('.price-item--regular').innerText.match(/[\d.]+/)
          };
          products.push(productData);
        }

        if (products.length > 0 || searchTerm !== '') {
          // Define the data for the event
          var eventData = {
            'event': 'searchResults',
            'searchTerm': searchTerm,
            'products': products
          };
      
          // Push the event data object to the DataLayer
          window.dataLayer = window.dataLayer || [];
          window.dataLayer.push(eventData);
      }
    }
    });

</script>
```

{{% /tab %}}
{{< /tabs >}}
