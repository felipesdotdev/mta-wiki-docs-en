---
doc_id: "mta-wiki:7855"
title: "Vector"
source_title: "Vector"
source_url: "https://wiki.multitheftauto.com/wiki/Vector"
revision_id: 58847
language: "en"
categories: ["OOP"]
generated_at: "2026-07-26T16:17:02.862183+00:00"
---

# Vector

A **vector** represents a [Euclidean vector](http://en.wikipedia.org/wiki/Euclidean_vector), which can be used to work with positions or directions in a 2D plane or 3D space. The classes of vectors available in MTA are:

- [Vector2](mta://reference/misc/vector-vector2.md)

- [Vector3](mta://reference/misc/vector-vector3.md)

- [Vector4](mta://reference/misc/vector-vector4.md)

**Tip**: if you are using vectors a lot, you can use *collectgarbage("setpause",100)* to tell Lua to garbage collect intermediary vectors frequently. Run that once per resource (or just in the resource you need it for). This has other performance implications as Lua will be stopping the world more frequently.

## See also

- [OOP](mta://tutorials/oop.md)

- [OOP Introduction](mta://tutorials/oop-introduction.md)

- [Matrix](mta://reference/misc/matrix.md)
