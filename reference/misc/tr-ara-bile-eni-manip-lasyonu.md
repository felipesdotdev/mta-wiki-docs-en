---
doc_id: "mta-wiki:14480"
title: "Tr/Araç bileşeni manipülasyonu"
source_title: "Tr/Araç bileşeni manipülasyonu"
source_url: "https://wiki.multitheftauto.com/wiki/Tr/Ara%C3%A7_bile%C5%9Feni_manip%C3%BClasyonu"
revision_id: 81092
language: "en"
categories: []
generated_at: "2026-07-26T16:16:59.823387+00:00"
---

# Tr/Araç bileşeni manipülasyonu

Araç Bileşeni Manipülasyonu

Araç bileşeni hareketiyle birlikte artık her bir araç için modelin parçalarını bağımsız bir şekilde manipüle etme yeteneğine sahibiz. Bu, parçaları gizlemeyi, hareket ettirmeyi ve araçlarına göre döndürmeyi içerir.

## Yetenekler

Pozisyon: Bir bileşeni şasisine veya ebeveynine göre yeniden konumlandırabilirsiniz.

Dönme: Bileşeni kendi ekseni etrafında döndürebilirsiniz.

Gizle/Göster: Bileşeni gizleyebilir ve böylece görünmemesini sağlayabilir veya tekrar gösterebilirsiniz.

## Nasıl Çalışır

Bileşen eklemek oldukça basittir. Önceki modelleme deneyiminiz varsa, her model parçasının bir adı olabilir ve bu ad, parça için benzersiz bir tanımlayıcı olarak işlev görür.

Kullanım kolaylığı açısından, model dosyasındaki adın başına # ekleyerek varsayılan olarak gizli bileşenler eklemek mümkündür, ancak bu oyun tarafından tanınan herhangi bir şeyde çalışmaz. Örneğin, tekerlekler varsayılan olarak gizlenemez, bu nedenle eklemek istediğiniz herhangi bir şeyi başına # eklemek en iyisi olacaktır.

Şöyle:
*#*hellokitty

Bu, her zaman tekrar gösterilebilir ve gösterme bayrağı, yeniden gizlenmedikçe yayınlamada kalıcıdır.

Herhangi bir bileşenin en azından şasi kuklasının altında olması gerekir.

## Basit İşlemler

Betik işlevleri, tekerlek eklemek gibi şeyleri oldukça kolay hale getirir. Tekerleklerinizi her karede başkalarından döndürme hareketini kopyalayarak eklemek ve gerekirse orijinal tekerlekleri gizleme işlevini kullanmak oldukça kolaydır.

Bu, bir tanktaki inanılmaz sayıda tekerlek için faydalı olabilir!

Veya sadece uçaklarda iki tane prop eklemek için.

Genel olarak, dönen şeyleri yapmak oldukça kolaydır; daha karmaşık animasyonlar ise en zorlu çalışmayı gerektirir, ancak sonunda bu konuda yardımcı olacak bir animasyon kütüphanesi tamamlandığında Google Code'da bulunmalıdır.

## İlginç Bir Fikir

Teorik olarak, bir modele farklı kapı türleri eklemek mümkün olmalıdır. Örneğin, kanatlı kapılar ve makaslı kapılar şu şekilde çalışabilir:

Orijinal kapıyı gizleyin.

Normal kapınızın rotası 0 ile 45 derece arasında olduğunu varsayalım, bu hareketiniz için bir temel olarak kullanılır.

Bu rotayı alıp farklı bir kapı türü için başka bir eksende uygulayın veya her karede eksenler arasında bölüştürerek yeni kapının düzgün hareketini elde edin (BONUS: Bu, sallanan kapılarla bile çalışır!)

## James Bond Tarzı

Silahlar, silahlar ve... roketler? Günün siparişi gizli panellerde saklı roketler mi? Sorun değil!

## Daha İleri Düzey

Hareket eden, gizli veya gösterilen parça sayısı konusunda bir sınır yoktur ve gizlenen herhangi bir şey render edilmez, böylece binlerce gizli parça ekleyebilirsiniz ve bunların herhangi bir şeyi yavaşlatması konusunda endişelenmenize gerek yoktur.

Bu, bir araba ile robota dönüşen tamamen dönüşebilen bir transformer robotu yapmak için hiçbir engel olmadığı anlamına gelir, ancak bu hem modelleme hem de betik yazma tarafında çok fazla çalışma gerektirecektir.
