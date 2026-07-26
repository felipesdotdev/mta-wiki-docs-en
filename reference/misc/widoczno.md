---
doc_id: "mta-wiki:13615"
title: "Widoczność"
source_title: "Widoczność"
source_url: "https://wiki.multitheftauto.com/wiki/Widoczno%C5%9B%C4%87"
revision_id: 74153
language: "en"
categories: ["Scripting_Concepts"]
generated_at: "2026-07-26T16:17:06.954796+00:00"
---

# Widoczność

System widoczności markerów i znaczników działa według następującej zasady: jeśli coś jest widoczne dla określonego elementu, to jest również widoczne dla wszystkich elementów potomnych tego elementu. Ponadto domyślnie wszystko jest widoczne dla elementu głównego.

Oznacza to, że jeśli chcesz zrobić m.in. znacznik widoczny tylko dla kilku konkretnych graczy, musisz zrobić dwie rzeczy:

- Ustaw znacznik niewidoczny dla elementu głównego (roota), używając [setElementVisibleTo](mta://scripting/server/functions/setelementvisibleto.md). Znacznik jest teraz ukryty dla wszystkich graczy.

- Spraw, aby znacznik był ponownie widoczny dla wybranych graczy.

To samo dotyczy markerów.

**Wskazówka:** Jeśli chcesz, aby coś było widoczne tylko dla niektórych graczy, najodpowiedniejszym sposobem będzie ustawienie domyślnej widoczności elementu na resourceRoot (żaden gracz tego nie zobaczy, ponieważ żaden gracz nie jest elementem podrzędnym danego zasobu), a następnie użyj [setElementVisibleTo](mta://scripting/server/functions/setelementvisibleto.md) na określonych graczach. W przeciwnym razie istnieje szansa, że gracze zobaczą znacznik przez ułamek sekundy, ponieważ znacznik jest tworzony, ale zaraz potem zostaje niewidoczny.

**Źle**:

```
local blip = createBlip(0, 0, 0, 41)
setElementVisibleTo(blip, root, false)
setElementVisibleTo(blip, somePlayer, true)
```

**Dobrze**:

```
local blip = createBlip(0, 0, 0, 41, 1, 2, 3, 4, 5, 6, 9999, resourceRoot)
setElementVisibleTo(blip, somePlayer, true)
```
