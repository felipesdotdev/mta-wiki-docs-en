---
doc_id: "mta-wiki:3500"
title: "Weather"
source_title: "Weather"
source_url: "https://wiki.multitheftauto.com/wiki/Weather"
revision_id: 73230
language: "en"
categories: ["ID_Lists"]
generated_at: "2026-07-26T16:17:06.929462+00:00"
---

# Weather

Weather can be changed using [setWeather](mta://scripting/shared/functions/setweather.md) and [setWeatherBlended](mta://scripting/shared/functions/setweatherblended.md) functions. In GTA: SA, every weather has different parameters for the sunrise, morning, midday, noon, afternoon, sunset, night and midnight, so a weather can vary a lot deppending of the time of the day.

Non-standard weather ID's between 20 and 255 are also supported, but they might be buggy at some moments of the day.

MTA: SA has custom weather functions which can modify how a weather is rendered, but in this list the weathers are described without taking that into account. Also, using [setWeatherBlended](mta://scripting/shared/functions/setweatherblended.md) allows for more undocumented effects.

For a complete weather gallery, containing images of every weather ID (0 to 255) shot at every in-game hour, visit [this page](http://dev.prineside.com/en/gtasa_weather_id/).

## Default GTA: SA weathers (registered in timecyc.dat)

| Weather ID | Name from timecyc.dat | Screenshots at 12:00 PM | Description |
| --- | --- | --- | --- |
| 0 | EXTRASUNNY_LA | Applies a heat haze effect | In singleplayer, these are Los Santos specific weathers . They are clear weathers, with blue sky and few clouds. |
| 1 | SUNNY_LA |  |  |
| 2 | EXTRASUNNY_SMOG_LA |  |  |
| 3 | SUNNY_SMOG_LA |  |  |
| 4 | CLOUDY_LA |  |  |
| 5 | SUNNY_SF |  | In singleplayer, these are San Fierro specific weathers . They are more diverse than Los Santos': some of them are clear, but others are rainy or foggy. |
| 6 | EXTRASUNNY_SF |  |  |
| 7 | CLOUDY_SF |  |  |
| 8 | RAINY_SF | Starts a thunderstorm, with rain and lightnings |  |
| 9 | FOGGY_SF | Starts a cloudy, dense fog |  |
| 10 | SUNNY_VEGAS |  | In singleplayer, these are Las Venturas specific weathers . They are clear, dry weathers. |
| 11 | EXTRASUNNY_VEGAS | Applies scorching hot weather, with a heat haze effect |  |
| 12 | CLOUDY_VEGAS |  |  |
| 13 | EXTRASUNNY_COUNTRYSIDE |  | In singleplayer, these are Los Santos countryside specific weathers . They are dull, hazy, diverse weathers, with rainy ones. |
| 14 | SUNNY_COUNTRYSIDE |  |  |
| 15 | CLOUDY_COUNTRYSIDE |  |  |
| 16 | RAINY_COUNTRYSIDE | Starts a thunderstorm |  |
| 17 | EXTRASUNNY_DESERT | Apply a heat haze effect | In singleplayer, these are Bone County specific weathers . They are clear, dry, scorching hot weathers. |
| 18 | SUNNY_DESERT | Apply a heat haze effect |  |
| 19 | SANDSTORM_DESERT | Starts a dense sandstorm |  |
| 20 | UNDERWATER |  | In singleplayer, this is probably the weather used internally when camera is underwater . It is greenish and cloudy, so it appears to be a kind of contaminated weather. |
| 21 | EXTRACOLOURS_1 | Adds a purple-ish color to the sky and objects | In singleplayer, these are weathers used in interiors . They are somewhat strange, dark weathers with gradiented skyline colors. |
| 22 | EXTRACOLOURS_2 | Adds a black-white sky and a uniform light to objects |  |

## Other weather IDs

- **23 to 26:** Pale orange weather.

- **27 to 29:** Fresh blue weather.

- **30 to 32:** Dark, cloudy, teal weather.

- **33:** Dark, cloudy, brown weather.

- **34:** Blue/purple, regular weather.

- **35:** Dull brown weather.

- **36 to 38:** Bright, foggy, orange weather.

- **39:** Very bright weather. Night looks like day.

- **40 to 42:** Blue/purple, cloudy weather.

- **43:** Toxic, contaminated clouds weather.

- **44:** Black/white sky weather, similar to **22**.

- **45 to 60:** Normal seeming weather with graphical bugs at evening.

- **100:** Strange weather which makes objects disappear.

- **118:** Stormy weather with pink sky and crystal water.

- **126 to 150:** Horrible flashing red bugged weather.

- **151 to 175:** Far draw distance weather with pink, purple and turquoise clouds.

## See also

- [ID lists](mta://reference/misc/id--474ae526.md)
