---
doc_id: "mta-wiki:8889"
title: "Pl/GetClothesTypeName"
source_title: "Pl/GetClothesTypeName"
source_url: "https://wiki.multitheftauto.com/wiki/Pl/GetClothesTypeName"
revision_id: 48169
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:16:29.027530+00:00"
---

# Pl/GetClothesTypeName

Ta funkcja pozwala na pobranie nazwy wybranego typu ubrań.

## Składnia

```
string getClothesTypeName ( int clothesType )
```

### Wymagane argumenty

- **clothesType**: Liczba całkowita reprezentująca typ ubrań którego nazwę chcesz pobrać

## Wartości zwrotne

Funkcja zwraca ciąg znaków (nazwę typu ubrań) jeśli wyszukiwanie się powiodło, w innym przypadku *false*.

## Przykład

Ten przykład dodaje komendę /clothes która wyświetla graczu informacje o jego obecnym ubiorze.

```
function getClothes ( thePlayer, key, clothesType )
  local texture, model = getPedClothes ( source, clothesType )
  if ( texture and model ) then
    outputChatBox ( getPlayerName ( thePlayer ) .. " ubiera " .. texture .. " " .. model .. " na jego " .. getClothesTypeName ( clothesType ) )
  end
end
addCommandHandler ( "clothes", getClothes )
```

## Zobacz także

- [getBodyPartName](mta://scripting/shared/functions/getbodypartname.md)

- [getClothesByTypeIndex](mta://scripting/shared/functions/getclothesbytypeindex.md)

- [getClothesTypeName](mta://scripting/shared/functions/getclothestypename.md)

- [getTypeIndexFromClothes](mta://scripting/shared/functions/gettypeindexfromclothes.md)

[BETA](mta://reference/misc/beta-features.md): NEW FEATURE (BUILD: 1.6.0 [r23124](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=23124))

- [addClothingModel](mta://scripting/client/functions/addclothingmodel.md)
