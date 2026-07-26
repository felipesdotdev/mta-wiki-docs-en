---
doc_id: "mta-wiki:8228"
title: "Category : Эффект"
source_title: "Эффект"
source_url: "https://wiki.multitheftauto.com/wiki/%D0%AD%D1%84%D1%84%D0%B5%D0%BA%D1%82"
revision_id: 70640
language: "en"
categories: ["Изменения_в_версии_1.4.0", "Элемент"]
generated_at: "2026-07-26T16:16:58.004524+00:00"
---

# Category : Эффект

ДОБАВЛЕНО/ОБНОВЛЕНО В ВЕРСИИ 1.4.0 :

Класс *Effect* представляет такие элементы эффектов в игровом мире, как дым, искры, огонь и так далее.

Тип элемента этого класса - **"effect"**.

## Список эффектов

Всего существует 82 эффекта.

```
--Таблица, содержащая названия всех эффектов.
local effectNames = {
"blood_heli","boat_prop","camflash","carwashspray","cement","cloudfast","coke_puff","coke_trail","cigarette_smoke",
"explosion_barrel","explosion_crate","explosion_door","exhale","explosion_fuel_car","explosion_large","explosion_medium",
"explosion_molotov","explosion_small","explosion_tiny","extinguisher","flame","fire","fire_med","fire_large","flamethrower",
"fire_bike","fire_car","gunflash","gunsmoke","insects","heli_dust","jetpack","jetthrust","nitro","molotov_flame",
"overheat_car","overheat_car_electric","prt_blood","prt_boatsplash","prt_bubble","prt_cardebris","prt_collisionsmoke",
"prt_glass","prt_gunshell","prt_sand","prt_sand2","prt_smokeII_3_expand","prt_smoke_huge","prt_spark","prt_spark_2",
"prt_splash","prt_wake","prt_watersplash","prt_wheeldirt","petrolcan","puke","riot_smoke","spraycan","smoke30lit","smoke30m",
"smoke50lit","shootlight","smoke_flare","tank_fire","teargas","teargasAD","tree_hit_fir","tree_hit_palm","vent","vent2",
"water_hydrant","water_ripples","water_speed","water_splash","water_splash_big","water_splsh_sml","water_swim","waterfall_end",
"water_fnt_tme","water_fountain","wallbust","WS_factorysmoke"
}
```

| Имя | Описание |
| --- | --- |
| blood_heli | кровавый взрыв |
| boat_prop | прибой |
| camflash | небольшая вспышка |
| carwashspray | пар, как на автомойке |
| cement | цемент |
| cloudfast | быстрые облака |
| coke_puff | слойка кокса |
| coke_trail | льющаяся вода |
| cigarette_smoke | дым от сигареты |
| explosion_barrel | взрыв и осколки ящика |
| explosion_crate | взрыв и осколки большого ящика |
| explosion_door | дым с щепками |
| exhale | маленький дым |
| explosion_fuel_car | взрыв машины |
| explosion_large | большой взрыв |
| explosion_medium | средний взрыв |
| explosion_molotov | взрыв от коктейля Молотова |
| explosion_small | маленький взрыв |
| explosion_tiny | очень маленький взрыв |
| extinguisher | пена огнетушителя |
| flame | небольшой огонь |
| fire | огонь |
| fire_med | средний огонь |
| fire_large | большой огонь |
| flamethrower | огонь огнемета |
| fire_bike | огонь, как от горящего мотоцикла |
| fire_car | огонь, как от горящей машины |
| gunflash | как вылетает пуля из ствола |
| gunsmoke | дым от оружия |
| insects | насекомые |
| heli_dust | пыль, как от вертолёта |
| jetpack | пламя джетпака |
| jetthrust | пламя из глушителя машины |
| nitro | нитро |
| molotov_flame | огонь от коктейля Молотова |
| overheat_car | дым от поврежденной машины |
| overheat_car_electric | разбитая электромашина |
| prt_blood | маленький всплеск крови |
| prt_boatsplash | пена |
| prt_bubble | пузырь |
| prt_cardebris | осколки от ящика |
| prt_collisionsmoke | плотный белый дым |
| prt_glass | ломающееся стекло |
| prt_gunshell | снаряды |
| prt_sand | рассеянный песок |
| prt_sand2 | чуть меньше песка |
| prt_smokeII_3_expand | серый дым |
| prt_smoke_huge | много серого дыма |
| prt_spark | искры |
| prt_spark_2 | большие искры |
| prt_splash | взрыв |
| prt_wake | волна |
| prt_watersplash | всплеск |
| prt_wheeldirt | искры от колёс машины |
| petrolcan | струя |
| puke | рвота |
| riot_smoke | много дыма |
| spraycan | спрей |
| smoke30lit | дым |
| smoke30m | густой дым |
| smoke50lit | более насыщенный дым |
| shootlight | выстреливаемый свет (используется для прожекторов), искры и стекло |
| smoke_flare | выстреливаемый свет, искры и стекло создают хороший эффект фейерверка |
| tank_fire | выстрел из танка |
| teargas | газ, как от газовой гранаты |
| teargasAD | газ, как от маленькой газовой гранаты |
| tree_hit_fir | листопад |
| tree_hit_palm | падение пары больших листьев |
| vent | медленно рассеиваемый дым |
| vent2 | практически тоже самое, что и выше |
| water_hydrant | большой поток воды |
| water_ripples | круги на воде |
| water_speed | большие искры из воды |
| water_splash | маленькие искры из воды |
| water_splash_big | средние искры |
| water_splsh_sml | искры, только их почти не видно |
| water_swim | маленькие искры при навигации |
| waterfall_end | много пара |
| water_fnt_tme | большой поток воды |
| water_fountain | фонтан воды |
| wallbust | исчезающая пара кучи |
| WS_factorysmoke | дым |
