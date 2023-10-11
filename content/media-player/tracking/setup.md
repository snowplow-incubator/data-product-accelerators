+++
title = "Set-up your tracking"
weight = 1
post = ""
+++

#### **Step 1:** Choose your tracking SDK

Snowplow provides a range of tracking SDKs to address different media players and platforms that you may be collecting your data from. Choosing the right SDK for you depends on the following questions:

1. Do you want to collect data from a Web app or a mobile app?
2. What media player do you use to play media in your app?
3. Do you prefer our tracking SDK to automatically subscribe to and track events from the media player or do you prefer to track the events manually by calling track event functions in our tracking SDK (e.g., you have a wrapper around the media player which listens to the player events and can send them to Snowplow)?
4. What data do you want to track? This will have an effect on whether you can choose a tracking SDK that tracks version 1 of our media schemas or should only look for SDKs that track version 2 Snowplow media schemas (see the explainer below to understand the difference between version 1 and 2 media schemas).

> **❓ Version 1 vs Version 2 media schemas**
>
> There are two versions of schemas for media events that our trackers may use to track media events. We recommend adopting the v2 schemas, but you may choose v1 schemas in case you want use a tracking SDK that doesn’t yet support v2 schemas and you don’t need the additional features of v2 schemas.
>
> They differ in the following ways:
>
> 1. V2 schemas enable more accurate metrics about the playback (e.g., played duration, average playback rate) that are computed on the tracker instead of estimated in modeling.
> 2. V2 schemas enable tracking ads played during media playback.
> 3. V2 schemas provide additional events to track playback quality and periodic media pings during playback.
> 4. V2 schemas support live streaming video (in addition to VOD).

| Tracking SDK | Platform | Media schemas version | Provides auto-tracking? | Player |
| --- | --- | --- | --- | --- |
| [Media Plugin for JS tracker](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/) | Web | v2 | No | Any |
| [Vimeo Plugin for JS tracker](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/vimeo-tracking/) | Web  | v2 | Yes | Vimeo |
| [iOS tracker](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/) | Mobile (iOS) | v2 | No | Any |
| [iOS tracker](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/) | Mobile (iOS) | v2 | Yes | AVPlayer |
| [Android tracker](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/) | Mobile (Android) | v2 | No | Any |
| [HTML5 Media Tracking Plugin for JS tracker](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media-tracking/) | Web | v1 | Yes | HTML5 media or video |
| [YouTube Plugin for JS tracker](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/youtube-tracking/) | Web | v1 | Yes | YouTube |

#### **Step 2:** Install the tracking SDK in your app

Once you have chosen the tracking SDK to use, the next step is to install it in your app.

{{< tabs groupId="tracking sdk" >}}

{{% tab name="Media JS plugin" %}}

Install the `@snowplow/browser-tracker` and `@snowplow/browser-plugin-media` via npm, yarn or any other package manager of your choice. Example using `npm`:

```bash
npm install @snowplow/browser-tracker @snowplow/browser-plugin-media
```
{{% /tab %}}

{{% tab name="Vimeo JS plugin" %}}
Install the `@snowplow/browser-tracker` and `@snowplow/browser-plugin-vimeo-tracking` via npm, yarn or any other package manager of your choice. Example using `npm`:

```bash
npm install @snowplow/browser-tracker @snowplow/browser-plugin-vimeo-tracking
```
{{% /tab %}}

{{% tab name="YouTube JS plugin" %}}
Install the `@snowplow/browser-tracker` and `@snowplow/browser-plugin-youtube-tracking` via npm, yarn or any other package manager of your choice. Example using `npm`:

```bash
npm install @snowplow/browser-tracker @snowplow/browser-plugin-youtube-tracking
```
{{% /tab %}}

{{% tab name="HTML5 media tracking JS plugin" %}}
Install the `@snowplow/browser-tracker` and `@snowplow/browser-plugin-media-tracking` via npm, yarn or any other package manager of your choice. Example using `npm`:

```bash
npm install @snowplow/browser-tracker @snowplow/browser-plugin-media-tracking
```
{{% /tab %}}

{{% tab name="iOS" %}}
You can install the tracker using SPM as follows:

1. In Xcode, select File > Swift Packages > Add Package Dependency.
2. Add the URL where to download the library: [https://github.com/snowplow/snowplow-ios-tracker](https://github.com/snowplow/snowplow-ios-tracker)

To learn about other options for installing the tracker (e.g. using CocoaPods or Carthage), [see the mobile tracker documentation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/installation-and-set-up/) .

{{% /tab %}}

{{% tab name="Android" %}}
The tracker can be installed using Gradle. Add the following to your `build.gradle` file:

```jsx
dependencies {
  ...
  // Snowplow Android Tracker
  implementation 'com.snowplowanalytics:snowplow-android-tracker:5.+'
  // In case 'lifecycleAutotracking' is enabled
  implementation 'androidx.lifecycle-extensions:2.2.+'
  ...
}
```
{{% /tab %}}

{{< /tabs >}}

{{% notice note %}}
It is also possible to integrate the plugins using a JavaScript script tag. For instructions, [please visit the documentation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/javascript-tracker/javascript-tracker-v3/plugins/media/).
{{% /notice %}}


#### **Step 3:** Create and configure the tracker

Next, you will need to create a configured tracker instance.

{{< tabs groupId="tracking sdk" >}}

{{% tab name="Media JS plugin" %}}

To add the `SnowplowMediaPlugin` on the JavaScript tracker, you should include it as shown below:

```jsx
import { newTracker } from '@snowplow/browser-tracker';
import { SnowplowMediaPlugin } from '@snowplow/browser-plugin-media';

newTracker('sp1', '{{collector_url}}', { 
    appId: 'my-app-id', 
    plugins: [ SnowplowMediaPlugin() ],
});
```


{{% /tab %}}

{{% tab name="Vimeo JS plugin" %}}

To add the `VimeoTrackingPlugin` on the JavaScript tracker, you should include it as shown below:

```jsx
import { newTracker } from '@snowplow/browser-tracker';
import { VimeoTrackingPlugin, enableYouTubeTracking } from '@snowplow/browser-plugin-youtube-tracking';

newTracker('sp1', '{{collector_url}}', {
    appId: 'my-app-id',
    plugins: [ VimeoTrackingPlugin() ],
});
```

{{% /tab %}}

{{% tab name="YouTube JS plugin" %}}

To add the `YouTubeTrackingPlugin` on the JavaScript tracker, you should include it as shown below:

```jsx
import { newTracker } from '@snowplow/browser-tracker';
import { YouTubeTrackingPlugin, enableYouTubeTracking } from '@snowplow/browser-plugin-youtube-tracking';

newTracker('sp1', '{{collector_url}}', {
    appId: 'my-app-id',
    plugins: [ YouTubeTrackingPlugin() ],
});
```

{{% /tab %}}

{{% tab name="HTML5 media tracking JS plugin" %}}

To add the `MediaTrackingPlugin` on the JavaScript tracker, you should include it as shown below:

```jsx
import { newTracker } from '@snowplow/browser-tracker';
import { MediaTrackingPlugin, enableMediaTracking } from '@snowplow/browser-plugin-media-tracking';

newTracker('sp1', '{{collector_url}}', {
    appId: 'my-app-id',
    plugins: [ MediaTrackingPlugin() ],
});
```

{{% /tab %}}

{{% tab name="iOS" %}}

We recommend creating a class or a file with helper functions (e.g., `Tracker.swift`) to manage all the Snowplow related code in your project. Import the Snowplow tracker package in the file as follows:

```jsx
import SnowplowTracker
```

The next step is to initialize the tracker instances in your app. Tracker instances are initialized given configuration that includes network settings, tracker feature settings, session settings, and more.

The following snippets show how to initialize tracker instances using the default settings. They call the `createTracker` function and with some arguments:

1. The tracker namespace which uniquely identifies the tracker within the app (`ns` in the snippet).
2. Network configuration with the endpoint address of the Snowplow Collector (e.g. [Snowplow Micro](https://docs.snowplowanalytics.com/docs/understanding-your-pipeline/what-is-snowplow-micro/) or [Snowplow Mini](https://docs.snowplowanalytics.com/docs/understanding-your-pipeline/what-is-snowplow-mini/) ) to send events to. We will update this with a testing endpoint later when we discuss the testing setup .
3. Tracker configuration with the application ID that identifies events across different applications (`appId` in the snippet).

```jsx
let networkConfig = NetworkConfiguration(endpoint: "{{URL for Collector}}")
let trackerConfig = TrackerConfiguration()
    .appId("appId")
let tracker = Snowplow.createTracker(
    namespace: "ns",
    network: networkConfig,
    configurations: [trackerConfig]
)
```

{{% /tab %}}

{{% tab name="Android" %}}

We recommend creating a class or a file with helper functions (e.g., `Tracker.kt`) to manage all the Snowplow related code in your project. Import the Snowplow tracker package in the file as follows:

```kotlin
import com.snowplowanalytics.snowplow.configuration.NetworkConfiguration
import com.snowplowanalytics.snowplow.configuration.TrackerConfiguration
import com.snowplowanalytics.snowplow.controller.TrackerController
import com.snowplowanalytics.snowplow.Snowplow.createTracker
```

The next step is to initialize the tracker instances in your app. Tracker instances are initialized given configuration that includes network settings, tracker feature settings, session settings, and more.

The following snippets show how to initialize tracker instances using the default settings. They call the `createTracker` function and with some arguments:

1. The tracker namespace which uniquely identifies the tracker within the app (`ns` in the snippet).
2. Network configuration with the endpoint address of the Snowplow Collector (e.g. [Snowplow Micro](https://docs.snowplowanalytics.com/docs/understanding-your-pipeline/what-is-snowplow-micro/) or [Snowplow Mini](https://docs.snowplowanalytics.com/docs/understanding-your-pipeline/what-is-snowplow-mini/) ) to send events to. We will update this with a testing endpoint later when we discuss the testing setup .
3. Tracker configuration with the application ID that identifies events across different applications (`appId` in the snippet).

```kotlin
val networkConfig = NetworkConfiguration("{{URL for Collector}}")
val trackerConfig = TrackerConfiguration("appId")
val tracker = createTracker(
    context,
    "ns",
    networkConfig,
    trackerConfig
)
```

{{% /tab %}}

{{< /tabs >}}

#### **Step 4:** Start tracking events

Having created a tracker, we can now start tracking media events.

{{< tabs groupId="tracking sdk" >}}

{{% tab name="Media JS plugin" %}}

Media tracking instances are identified by a unique ID. This is an identifier that you provide. Make sure that each media player and content tracked have a different ID.

```jsx
const id = 'XXXXX'; // randomly generated ID
```

To start tracking media events, call the `startMediaTracking` function with the ID.

```jsx
import { startMediaTracking } from "@snowplow/browser-plugin-media";
startMediaTracking({
  id,
  player: {
      duration: 150, // A double-precision floating-point value indicating the duration of the media in seconds
      label: 'Sample video', // A human-readable title for the media
      playerType: 'html5', // The type of player
  },
  boundaries: [10, 25, 50, 75] // Percentage progress events will be tracked when playback reaches the boundaries
});
```

See [the documentation for the full list](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#media-player-properties) of options.

Subscribe for playback position changes on the media player and make sure to update the player properties as follows.

```jsx
import { updateMediaTracking } from "@snowplow/browser-plugin-media";
updateMediaTracking({
  id,
  player: { currentTime: 10 }
});
```

Subscribe to the player events that you are interested in and use the relevant functions to track the events (see the [documentation for the full list](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#tracking-media-events)), for example:

- `trackMediaPlay` – player changes state to playing from previously being paused.
- `trackMediaPause` – user pauses the playback.
- `trackMediaEnd` – playback stops when end of the media is reached.
- `trackMediaSeekStart` – seek operation begins.
- `trackMediaSeekEnd` – seek operation completes.
- `trackMediaPlaybackRateChange` – playback rate has changed ([accepts a `newRate` parameter](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#playback-rate-change) with the new playback rate).
- `trackMediaVolumeChange` – volume has changed ([accepts a `newVolume` parameter](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#volume-change) with the new volume).
- `trackMediaBufferStart` – player goes into the buffering state and begins to buffer content.
- `trackMediaBufferEnd` – player finishes buffering content and resumes playback.
- `trackMediaQualityChange` – video playback quality changes ([accepts `newQuality`, `bitrate`, `framesPerSecond`, `automatic` optional parameters](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#quality-change) to describe the new setting).
- in case you are interested in tracking ads during playback, see the [relevant ad events in the documetation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#events-for-ad-events).

To track the events, simply provide the media tracking ID to the respective tracking function:

```jsx
import { trackMediaPlay } from "@snowplow/browser-plugin-media";
trackMediaPlay({ id });
```

You can also pass additional optional information to the track methods [as documented here](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#providing-additional-information).

Finally, use the `endMediaTracking` call to end media tracking. This will clear the local state for the media tracking and stop any background updates.

```jsx
import { endMediaTracking } from "@snowplow/browser-plugin-media";
endMediaTracking({ id });
```

{{% /tab %}}

{{% tab name="Vimeo JS plugin" %}}

Vimeo tracking instances are identified by a unique ID. This is an identifier that you provide. Make sure that each media player and content tracked have a different ID.

```jsx
const id = 'XXXXX'; // randomly generated ID
```

To start tracking media events, call the `startVimeoTracking` function. The function takes a `video` attribute that accepts either:

- an `iframe` element,
- or an instance of `Vimeo.Player`, created with the [Vimeo Player SDK](https://developer.vimeo.com/player/sdk).

In case of using an `iframe` element for the attribute, call the function as follows.

```jsx
import { startVimeoTracking } from '@snowplow/browser-plugin-vimeo-tracking'

const video = document.getElementById('vimeo-iframe')

startVimeoTracking({ id, video })
```

In case of passing an instance of `Vimeo.Player`, created with the [Vimeo Player SDK](https://developer.vimeo.com/player/sdk), you can call `startVimeoTracking` as follows.

```jsx
import { Player } from '@vimeo/player'
import { startVimeoTracking } from '@snowplow/browser-plugin-vimeo-tracking'

const video = new Player('vimeo-player', {
  videoId: 'zSM4ZyVe8xs'
});

startVimeoTracking({ id, video })
```

After the video player disappears (particularly important in single page apps), it's important to call `endVimeoTracking` as this will end any recurring ping events, clear all listeners set by the Vimeo plugin, along with resetting statistics counters.

```jsx
import { endVimeoTracking } from '@snowplow/browser-plugin-vimeo-tracking'

endVimeoTracking(id)
```

For more configuration and tracking options, [visit the documentation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/vimeo-tracking/#advanced-usage).

{{% /tab %}}

{{% tab name="YouTube JS plugin" %}}

To start tracking media events, call the  `enableYouTubeTracking` function. To find the YouTube player, this function takes an `id` parameter which is the HTML id attribute of the media element.

```jsx
enableYouTubeTracking({
  id: 'my-video',
  options: {
    label: 'My Video Name',
  }
})
```

For more configuration options, [see the documentation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/youtube-tracking/#the-enableyoutubetracking-function).

{{% /tab %}}

{{% tab name="HTML5 media tracking JS plugin" %}}

To start tracking media events, call the  `enableMediaTracking` function. To find your media element, this function takes an `id` parameter which can either be:

1. the id of the `<audio>` or `<video>` HTML element,
2. or the id of the parent element of the `<audio>` or `<video>` element (the parent can only have one child element).

It is also a good practice to set the `label` of the media being played. This may be the title of the video.

```jsx
import { enableMediaTracking } from '@snowplow/browser-plugin-media-tracking'

enableMediaTracking({
  id: 'my-video',
  options: {
    label: 'My Video Name'
  }
})
```

For more configuration options, [see the documentation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media-tracking/#the-enablemediatracking-function).

{{% /tab %}}

{{% tab name="iOS" %}}

Media tracking instances are identified by a unique ID. This is an identifier that you provide. Make sure that each media player and content tracked have a different ID.

```swift
let id = "XXXXX" // randomly generated ID
```

To start tracking media events, call the `startMediaTracking` function with the ID, which return an instance of `MediaTracking` that you will use to track events and manage the media tracking.

```swift
let tracker = Snowplow.defaultTracker()
let player = MediaPlayerEntity()
    .duration(150.0) // A double-precision floating-point value indicating the duration of the media in seconds
    .label("Sample video") // A human-readable title for the media
let configuration = MediaTrackingConfiguration(id: id)
    .player(player)
    .boundaries([10, 25, 50, 75])
let mediaTracking = tracker.media.startMediaTracking(configuration: configuration)
```


See [the documentation for the full list](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/#media-player-properties) of options.

Subscribe for playback position changes on the media player and make sure to update the player properties as follows.

```swift
mediaTracking.update(player: MediaPlayerEntity().currentTime(10.0))
```

Subscribe to the player events that you are interested in and use the relevant media event classes to track the events (see the [documentation for the full list](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/?platform=android#tracking-media-events)), for example:

- `MediaPlayEvent` – player changes state to playing from previously being paused.
- `MediaPauseEvent` – user pauses the playback.
- `MediaEndEvent` – playback stops when end of the media is reached.
- `MediaSeekStartEvent` – seek operation begins.
- `MediaSeekEndEvent` – seek operation completes.
- `MediaPlaybackRateChangeEvent` – playback rate has changed ([accepts a `newRate` parameter](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#playback-rate-change) with the new playback rate).
- `MediaVolumeChangeEvent` – volume has changed ([accepts a `newVolume` parameter](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#volume-change) with the new volume).
- `MediaBufferStartEvent` – player goes into the buffering state and begins to buffer content.
- `MediaBufferEndEvent` – player finishes buffering content and resumes playback.
- `MediaQualityChangeEvent` – video playback quality changes ([accepts `newQuality`, `bitrate`, `framesPerSecond`, `automatic`](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#quality-change) [optional parameters](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/?platform=android#quality-change) to describe the new setting).
- in case you are interested in tracking ads during playback, see the [relevant ad events in the documetation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/?platform=android#events-for-ad-events).

To track the events, simply provide the media tracking ID to the respective tracking function:

```swift
mediaTracking.track(MediaPlayEvent())
```

You can also pass additional optional information to the track methods [as documented here](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/?platform=ios#providing-additional-information).

Finally, use the `endMediaTracking` call to end media tracking. This will clear the local state for the media tracking and stop any background updates.

```swift
tracker.media.endMediaTracking(id: id)
```

{{% /tab %}}

{{% tab name="Android" %}}

Media tracking instances are identified by a unique ID. This is an identifier that you provide. Make sure that each media player and content tracked have a different ID.

```kotlin
val id = "XXXXX" // randomly generated ID
```

To start tracking media events, call the `startMediaTracking` function with the ID, which return an instance of `MediaTracking` that you will use to track events and manage the media tracking.

```kotlin
val tracker = Snowplow.defaultTracker
val player = MediaPlayerEntity(
    duration = 150.0, // A double-precision floating-point value indicating the duration of the media in seconds
    label = "Sample video", // A human-readable title for the media
)
val configuration = MediaTrackingConfiguration(
    id = id,
    player = player,
    boundaries = listOf(10, 25, 50, 75) // Percentage progress events will be tracked when playback reaches the boundaries
)
val mediaTracking = tracker?.media?.startMediaTracking(configuration)
```

See [the documentation for the full list](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/#media-player-properties) of options.

Subscribe for playback position changes on the media player and make sure to update the player properties as follows.

```kotlin
mediaTracking?.update(player = MediaPlayerEntity(currentTime = 10.0))
```


Subscribe to the player events that you are interested in and use the relevant media event classes to track the events (see the [documentation for the full list](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/?platform=android#tracking-media-events)), for example:

- `MediaPlayEvent` – player changes state to playing from previously being paused.
- `MediaPauseEvent` – user pauses the playback.
- `MediaEndEvent` – playback stops when end of the media is reached.
- `MediaSeekStartEvent` – seek operation begins.
- `MediaSeekEndEvent` – seek operation completes.
- `MediaPlaybackRateChangeEvent` – playback rate has changed ([accepts a `newRate` parameter](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#playback-rate-change) with the new playback rate).
- `MediaVolumeChangeEvent` – volume has changed ([accepts a `newVolume` parameter](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#volume-change) with the new volume).
- `MediaBufferStartEvent` – player goes into the buffering state and begins to buffer content.
- `MediaBufferEndEvent` – player finishes buffering content and resumes playback.
- `MediaQualityChangeEvent` – video playback quality changes ([accepts `newQuality`, `bitrate`, `framesPerSecond`, `automatic`](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/browser-tracker/browser-tracker-v3-reference/plugins/media/#quality-change) [optional parameters](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/?platform=android#quality-change) to describe the new setting).
- in case you are interested in tracking ads during playback, see the [relevant ad events in the documetation](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/?platform=android#events-for-ad-events).

To track the events, simply provide the media tracking ID to the respective tracking function:

```kotlin
mediaTracking?.track(MediaPlayEvent())
```

You can also pass additional optional information to the track methods [as documented here](https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/media-tracking/?platform=ios#providing-additional-information).

Finally, use the `endMediaTracking` call to end media tracking. This will clear the local state for the media tracking and stop any background updates.

```kotlin
tracker?.media?.endMediaTracking(id)
```

{{% /tab %}}

{{< /tabs >}}
