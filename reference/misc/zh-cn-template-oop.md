---
doc_id: "mta-wiki:12704"
title: "Template : OOP ZH-CN"
source_title: "Zh-cn/Template:OOP"
source_url: "https://wiki.multitheftauto.com/wiki/Zh-cn/Template%3AOOP"
revision_id: 68577
language: "en"
categories: []
generated_at: "2026-07-26T16:16:56.650390+00:00"
---

# Template : OOP ZH-CN

文档模板

OOP模板(Object Oriented Programming)

### 用法

**OOP 语法** [什么是OOP?](https://wiki.multitheftauto.com/wiki/ZH-CN/OOP%E4%BB%8B%E7%BB%8D)

**提示**: *Set the variable to nil to execute [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md)*

**方法**: *[ped](mta://reference/misc/ped.md):warpIntoVehicle(...)*

**变量**: *.vehicle*

**对称函数**: *[getPedOccupiedVehicle](mta://scripting/shared/functions/getpedoccupiedvehicle.md)*

```
{{OOP_ZH-CN|Set the variable to nil to execute [[removePedFromVehicle]]|[[ped]]:warpIntoVehicle|vehicle|getPedOccupiedVehicle}}
```

Hey guys, here are a few "rules" in using the OOP template:

- If it's a constructor, such as [createPed](mta://scripting/shared/functions/createped.md), use "[Ped](mta://reference/misc/ped.md)" not "createPed" or "Ped.create"

- If it's a static class function or a constructor, use a capital letter for the first character. (Player not player).

- Likewise, if it's an object function such as "player:setName", use lowercase.

- Use full stops (or if you're american, "periods.") for static functions and colons (:) for object functions.
