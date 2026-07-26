---
doc_id: "mta-wiki:12829"
title: "DE/SetSoundSpeed"
source_title: "De/SetSoundSpeed"
source_url: "https://wiki.multitheftauto.com/wiki/De/SetSoundSpeed"
revision_id: 69398
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:11:20.061265+00:00"
---

# DE/SetSoundSpeed

Diese Funktion ändert die Geschwindigkeit der Wiedergabe eines [Sound](mta://reference/misc/sound.md) [Elements](mta://reference/misc/element.md).

## Syntax

```
bool setSoundSpeed ( element theSound, float speed )
```

**OOP Syntax** [Hilfe! Ich verstehe das nicht!](mta://tutorials/oop-introduction.md)

**Methode**: *[sound](mta://reference/misc/sound.md):setSpeed(...)*

**Variable**: *.speed*

**Gegenstück**: *[getSoundSpeed](mta://scripting/client/functions/getsoundspeed.md)*

### Required Arguments

- **theSound:** das [Sound](mta://reference/misc/sound.md) [Element](mta://reference/misc/element.md), von welchem du die Geschwindigkeit ändern möchtest.

- **speed:** ein [float](mta://reference/misc/float.md) Wert (Fließkommazahl), welcher die Wiedergabegeschwindigkeit repräsentiert.

### Rückgabe

Gibt ein *true* zurück, wenn die Geschwindigkeit vom [Sound](mta://reference/misc/sound.md) Element erfolgreich geändert wurde, *false* wenn nicht.

## Beispiel

```
function soundFunc()
sound = playSound ( "/sounds/jizzy.mp3",true) -- Spielt einen Sound ab
setSoundSpeed ( sound, 1.2 ) -- Spielt den Sound 20% schneller ab
end
addCommandHandler("play",soundFunc)
```

## Siehe auch

- [DE/playSoundFrontEnd](https://wiki.multitheftauto.com/wiki/DE/playSoundFrontEnd)

- [DE/getRadioChannel](https://wiki.multitheftauto.com/wiki/DE/getRadioChannel)

- [DE/getRadioChannelName](https://wiki.multitheftauto.com/wiki/DE/getRadioChannelName)

- [DE/getSoundEffects](https://wiki.multitheftauto.com/wiki/DE/getSoundEffects)

- [DE/getSoundLength](https://wiki.multitheftauto.com/wiki/DE/getSoundLength)

- [DE/getSoundMaxDistance](https://wiki.multitheftauto.com/wiki/DE/getSoundMaxDistance)

- [DE/getSoundMetaTags](https://wiki.multitheftauto.com/wiki/DE/getSoundMetaTags)

- [DE/getSoundMinDistance](https://wiki.multitheftauto.com/wiki/DE/getSoundMinDistance)

- [DE/getSoundPosition](https://wiki.multitheftauto.com/wiki/DE/getSoundPosition)

- [DE/getSoundSpeed](https://wiki.multitheftauto.com/wiki/DE/getSoundSpeed)

- [DE/getSoundVolume](https://wiki.multitheftauto.com/wiki/DE/getSoundVolume)

- [DE/isSoundPaused](https://wiki.multitheftauto.com/wiki/DE/isSoundPaused)

- [DE/playSound](https://wiki.multitheftauto.com/wiki/DE/playSound)

- [DE/playSound3D](https://wiki.multitheftauto.com/wiki/DE/playSound3D)

- [DE/setRadioChannel](https://wiki.multitheftauto.com/wiki/DE/setRadioChannel)

- [DE/setSoundEffectEnabled](https://wiki.multitheftauto.com/wiki/DE/setSoundEffectEnabled)

- [DE/setSoundMaxDistance](https://wiki.multitheftauto.com/wiki/DE/setSoundMaxDistance)

- [DE/setSoundMinDistance](https://wiki.multitheftauto.com/wiki/DE/setSoundMinDistance)

- [DE/setSoundPaused](https://wiki.multitheftauto.com/wiki/DE/setSoundPaused)

- [DE/setSoundPosition](https://wiki.multitheftauto.com/wiki/DE/setSoundPosition)

- [DE/setSoundSpeed](https://wiki.multitheftauto.com/wiki/DE/setSoundSpeed)

- [DE/setSoundVolume](https://wiki.multitheftauto.com/wiki/DE/setSoundVolume)

- [DE/stopSound](https://wiki.multitheftauto.com/wiki/DE/stopSound)
