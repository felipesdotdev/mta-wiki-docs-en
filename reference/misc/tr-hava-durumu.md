---
doc_id: "mta-wiki:14482"
title: "Tr/Hava Durumu"
source_title: "Tr/Hava Durumu"
source_url: "https://wiki.multitheftauto.com/wiki/Tr/Hava_Durumu"
revision_id: 81096
language: "en"
categories: ["ID_Lists"]
generated_at: "2026-07-26T16:17:00.048570+00:00"
---

# Tr/Hava Durumu

Hava durumu, [setWeather](mta://scripting/shared/functions/setweather.md) ve [setWeatherBlended](mta://scripting/shared/functions/setweatherblended.md) işlevleri kullanılarak değiştirilebilir. GTA: SA'da, her hava durumu türünün güneşin doğuşu, sabah, öğle, öğleden sonra, akşam, gün batımı, gece ve gece yarısı için farklı parametreleri vardır, bu yüzden bir hava durumu, günün saatine bağlı olarak çok değişebilir.

20 ile 255 arasındaki standart dışı hava durumu ID'leri de desteklenmektedir, ancak bunlar günün bazı saatlerinde hatalı olabilir.

MTA: SA, hava durumunun nasıl görüntüleneceğini değiştirebilen özel hava durumu işlevlerine sahiptir, ancak bu listede hava durumları bu özellikler dikkate alınarak tanımlanmıştır. Ayrıca, [setWeatherBlended](mta://scripting/shared/functions/setweatherblended.md) kullanmak, daha fazla belgelenmemiş etkiye olanak tanır.

Her hava durumu ID'sinin (0'dan 255'e kadar) her oyun içi saatte çekilmiş görüntülerini içeren tam hava durumu galerisi için [bu sayfayı](http://dev.prineside.com/en/gtasa_weather_id/) ziyaret edebilirsiniz.

## Default GTA: SA weathers (registered in timecyc.dat)

| Weather ID | Name from timecyc.dat | Screenshots at 12:00 PM | Description |
| --- | --- | --- | --- |
| 0 | EXTRASUNNY_LA | Applies a heat haze effect | Tek oyunculu oyun modunda, bunlar Los Santos'a özel hava durumlarıdır . Bunlar, mavi gökyüzü ve az sayıda bulut bulunan açık hava durumlarıdır. |
| 1 | SUNNY_LA |  |  |
| 2 | EXTRASUNNY_SMOG_LA |  |  |
| 3 | SUNNY_SMOG_LA |  |  |
| 4 | CLOUDY_LA |  |  |
| 5 | SUNNY_SF |  | Tek oyunculu oyun modunda, bunlar San Fierro'ya özel hava durumlarıdır . Los Santos'a göre daha çeşitlidirler: bazılarında hava açıktır, ancak diğerleri yağmurlu veya sisli olabilir. |
| 6 | EXTRASUNNY_SF |  |  |
| 7 | CLOUDY_SF |  |  |
| 8 | RAINY_SF | Starts a thunderstorm, with rain and lightnings |  |
| 9 | FOGGY_SF | Starts a cloudy, dense fog |  |
| 10 | SUNNY_VEGAS |  | Tek oyunculu oyun modunda, bunlar Las Venturas'a özel hava durumlarıdır . Bunlar, açık ve kuru hava durumlarıdır. |
| 11 | EXTRASUNNY_VEGAS | Applies scorching hot weather, with a heat haze effect |  |
| 12 | CLOUDY_VEGAS |  |  |
| 13 | EXTRASUNNY_COUNTRYSIDE |  | Tek oyunculu oyun modunda, bunlar Los Santos kırsalına özgü hava durumlarıdır . Bunlar, kasvetli, puslu ve çeşitli hava durumlardır, bazıları yağmurludur. |
| 14 | SUNNY_COUNTRYSIDE |  |  |
| 15 | CLOUDY_COUNTRYSIDE |  |  |
| 16 | RAINY_COUNTRYSIDE | Starts a thunderstorm |  |
| 17 | EXTRASUNNY_DESERT | Apply a heat haze effect | Tek oyunculu oyun modunda, bunlar Bone County'ye özgü hava durumlarıdır . Bunlar, açık, kuru ve kavurucu sıcak hava durumlardır. |
| 18 | SUNNY_DESERT | Apply a heat haze effect |  |
| 19 | SANDSTORM_DESERT | Starts a dense sandstorm |  |
| 20 | UNDERWATER |  | Tek oyunculu oyun modunda, bu muhtemelen kameranın su altındayken içsel olarak kullanılan hava durumudur . Yeşilimsi ve bulutlu olup, kirlenmiş bir hava durumu izlenimi verir. |
| 21 | EXTRACOLOURS_1 | Adds a purple-ish color to the sky and objects | Tek oyunculu oyun modunda, bunlar iç mekanlarda kullanılan hava durumlarıdır . Biraz garip, karanlık hava durumlarıdır ve gökyüzü renklerinde gradyanlar bulunur. |
| 22 | EXTRACOLOURS_2 | Adds a black-white sky and a uniform light to objects |  |

## Diğer hava durumu ID'leri

- **23 ile 26:** Soluk turuncu hava durumu.

- **27 ile 29:** Taze mavi hava durumu.

- **30 ile 32:** Koyu, bulutlu, yeşilimsi mavi hava durumu.

- **33:** Koyu, bulutlu, kahverengi hava durumu.

- **34:** Mavi/mor, normal hava durumu.

- **35:** Donuk kahverengi hava durumu.

- **36 ile 38:** Parlak, sisli, turuncu hava durumu.

- **39:** Çok parlak hava durumu. Gece gündüz gibi görünür.

- **40 ile 42:** Mavi/mor, bulutlu hava durumu.

- **43:** Zehirli, kirli bulutlar hava durumu.

- **44:** Siyah/beyaz gökyüzü hava durumu, **22'**ye benzer.

- **45 ile 60:** Akşamları grafik hatalarıyla normal görünen hava durumu.

- **100:** Nesnelerin kaybolmasına neden olan garip hava durumu.

- **118:** Pembe gökyüzü ve kristal su ile fırtınalı hava durumu.

- **126 ile 150:** Korkunç yanıp sönen kırmızı hatalı hava durumu.

- **151 ile 175:** Pembe, mor ve turkuaz bulutlarla uzak görüş mesafesi hava durumu.

## See also

- [ID lists](mta://reference/misc/id--474ae526.md)
