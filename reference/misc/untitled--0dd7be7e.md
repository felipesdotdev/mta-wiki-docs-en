---
doc_id: "mta-wiki:6528"
title: "Причины смерти"
source_title: "Причины смерти"
source_url: "https://wiki.multitheftauto.com/wiki/%D0%9F%D1%80%D0%B8%D1%87%D0%B8%D0%BD%D1%8B_%D1%81%D0%BC%D0%B5%D1%80%D1%82%D0%B8"
revision_id: 74855
language: "en"
categories: ["Списки_ID"]
generated_at: "2026-07-26T16:17:09.438955+00:00"
---

# Причины смерти

Следующие причины смерти используются такими событиями, как [onPlayerDamage](https://wiki.multitheftauto.com/wiki/RU/onPlayerDamage) или [onPlayerWasted](https://wiki.multitheftauto.com/wiki/RU/onPlayerWasted) для аргумента **оружие**, чтобы описать причину, по которой [пешеход](https://wiki.multitheftauto.com/wiki/RU/Element/Ped) был повреждён или убит.
Если игрок был ранен из оружия, то соответствующий ID оружия является идентификатором типа урона. ID оружия можно найти [здесь](mta://reference/misc/untitled--b1408b63.md).

| ID | Причина смерти | Дополнительная информация |
| --- | --- | --- |
| 19 | Rocket (ракета) | Фактический тип повреждения при повреждении из ракетной установки |
| 37 | Burnt (сгорел) | Используется при смерти от огня, даже если он был создан от взрыва ракеты или коктейля Молотова |
| 49 | Rammed (задавлен) |  |
| 50 | Ranover (сбит) | Также вызывается при смерти от винта вертолёта |
| 51 | Explosion (взрыв) | Иногда может использоваться при смерти, вызванный взрывом ракеты |
| 52 | Driveby (застрелен из ТС) | НЕ используется для драйв-бай убийств от, например, ресурса 'realdriveby' |
| 53 | Drowned (утонул) |  |
| 54 | Fall (разбился) |  |
| 55 | Unknown (неизвестно) | Информации по данной причине нет |
| 56 | Melee (в рукопашной схватке) | Похоже, никогда не появляется (?); при фактической смерти от рукопашной схватки используется ID оружия-кулака (0) (см. здесь ) |
| 57 | Weapon | Похоже, никогда не появляется (?) |
| 59 | Tank Grenade (танковый снаряд) |  |
| 63 | Blown (взорвался) | Фактическая причина смерти при смерти, вызванной взрывом ТС |

Причины смертей в lua-таблице

```
local damageTypes = {
	[19] = "Rocket",
	[37] = "Burnt",
	[49] = "Rammed",
	[50] = "Ranover/Helicopter Blades",
	[51] = "Explosion",
	[52] = "Driveby",
	[53] = "Drowned",
	[54] = "Fall",
	[55] = "Unknown",
	[56] = "Melee",
	[57] = "Weapon",
	[59] = "Tank Grenade",
	[63] = "Blown"
}
```

## Смотрите также

- [Списки ID](https://wiki.multitheftauto.com/wiki/RU/Id)

### Связанные события

- [onPlayerDamage](https://wiki.multitheftauto.com/wiki/RU/onPlayerDamage) - *срабатывает, когда игрок получает урон любым способом*

- [onPlayerWasted](https://wiki.multitheftauto.com/wiki/RU/onPlayerWasted) - *срабатывает, когда игрок убит или умирает*
