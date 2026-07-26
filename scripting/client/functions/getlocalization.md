---
doc_id: "mta-wiki:7660"
title: "GetLocalization"
source_title: "GetLocalization"
source_url: "https://wiki.multitheftauto.com/wiki/GetLocalization"
revision_id: 77221
language: "en"
categories: ["Client_functions"]
generated_at: "2026-07-26T16:15:15.164751+00:00"
---

# GetLocalization

This function gets the player's localization setting as set in the MTA client.

## Syntax

```
table getLocalization ( )
```

### Returns

Returns a [table](mta://reference/misc/table.md) with the following entries:

- **code :** The language code *(eg. "en_US" for "English (United States)" or "ar" for "Arabic")*.

- **name :** The name of the language *(eg. "English (United States)" or "Arabic")*.

## Example

This example outputs simple *Welcome* message at the resource start (also when player joins the game if the resource is already running).

```
local msg = {cs = "Vítejte", fr = "Accueil", de = "Willkommen", pl = "Powitanie", hu = "Üdv"}

addEventHandler("onClientResourceStart", resourceRoot, 
	function ()
		local languageCode = getLocalization()["code"]
		if msg[languageCode] then --Check if the message is avaible in client's language
			outputChatBox(msg[languageCode] .. "!") --Output it
		else
			outputChatBox("Welcome!") --Output English for any other language
		end
	end)
```

This is a list of all the language codes used in MTA in a table with the full name of the language.

```
langTable = {
	["ar_SA"] = "Arabic",
	["az_AZ"] = "Azerbaijani",
	["bg_BG"] = "Bulgarian",
	["bs_BA"] = "Bosnian",
	["cs_CZ"] = "Czech",
	["da_DK"] = "Danish",
	["de_DE"] = "German",
	["en_US"] = "English",
	["el_GR"] = "Greek",
	["es_ES"] = "Spanish",
	["et_EE"] = "Estonian",
	["fa_IR"] = "Persian",
	["fi_FI"] = "Finnish",
	["fil_PH"] = "Filipino",
	["fr_FR"] = "French",
	["he_IL"] = "Hebrew",
	["hi_IN"] = "Hindi",
	["hr_HR"] = "Croatian",
	["hu_HU"] = "Hungarian",
	["id_ID"] = "Indonesian",
	["it_IT"] = "Italian",
	["ja_JP"] = "Japanese",
	["ka_GE"] = "Georgian",
	["ko_KR"] = "Korean",
	["lt_LT"] = "Lithuanian",
	["lv_LV"] = "Latvian",
	["mk_MK"] = "Macedonian",
	["nb_NO"] = "Norwegian",
	["nl_NL"] = "Dutch",
	["pt_BR"] = "Portuguese, Brazilian",
	["pt_PT"] = "Portuguese",
	["pl_PL"] = "Polish",
	["ru_RU"] = "Russian",
	["ro_RO"] = "Romanian",
	["sl_SL"] = "Slovenian",
	["sv_SE"] = "Swedish",
	["sk_SK"] = "Slovak",
	["srp"] = "Serbian",
	["tr_TR"] = "Turkish",
	["uk_UA"] = "Ukrainian",
	["vi_VN"] = "Vietnamese",
	["zh_CN"] = "Chinese Simplified",
	["zh_TW"] = "Chinese Traditional",

}
```

This function is useful for fixing any scripts that were made before MTA 1.6 as some of the language codes were changed.

```
local languageCodes = {
	['ar_SA'] = 'ar',
	['bg_BG'] = 'bg',
	['da_DK'] = 'da',
	['de_DE'] = 'de',
	['el_GR'] = 'el',
	['es_ES'] = 'es',
	['fr_FR'] = 'fr',
	['hr_HR'] = 'hr',
	['hu_HU'] = 'hu',
	['id_ID'] = 'id',
	['it_IT'] = 'it',
	['lt_LT'] = 'lt',
	['nb_NO'] = 'nb',
	['nl_NL'] = 'nl',
	['pl_PL'] = 'pl',
	['pt_PT'] = 'pt_BR',
	['ro_RO'] = 'ro',
	['ru_RU'] = 'ru',
	['sl_SL'] = 'sl',
	['sv_SE'] = 'sv',
	['tr_TR'] = 'tr',
	['uk_UA'] = 'uk',
	['vi_VN'] = 'vi',
}

function getLanguageCode(c)
	return languageCodes[c] or c
end

code = getLanguageCode(getLocalization().code)
```

## See Also

- [createTrayNotification](mta://scripting/client/functions/createtraynotification.md)

- [downloadFile](mta://scripting/client/functions/downloadfile.md)

- [getKeyboardLayout](mta://scripting/client/functions/getkeyboardlayout.md)

- getLocalization

ADDED/UPDATED IN VERSION 1.6.0 [r22890](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22890):

- [getServerIp](mta://scripting/client/functions/getserverip.md)

- [isShowCollisionsEnabled](mta://scripting/client/functions/isshowcollisionsenabled.md)

- [isShowSoundEnabled](mta://scripting/client/functions/isshowsoundenabled.md)

- [isTransferBoxAlwaysVisible](mta://scripting/client/functions/istransferboxalwaysvisible.md)

- [isTrayNotificationEnabled](mta://scripting/client/functions/istraynotificationenabled.md)

- [setClipboard](mta://scripting/client/functions/setclipboard--f18b656d.md)

- [setWindowFlashing](mta://scripting/client/functions/setwindowflashing.md)

- [showCol](mta://scripting/client/functions/showcol.md)

- [showSound](mta://scripting/client/functions/showsound.md)
  

- **Shared**

- [addDebugHook](mta://scripting/shared/functions/adddebughook.md)

- [debugSleep](mta://scripting/shared/functions/debugsleep.md)

- [decodeString](mta://scripting/shared/functions/decodestring.md)

- [encodeString](mta://scripting/shared/functions/encodestring.md)

- [fromJSON](mta://scripting/shared/functions/fromjson.md)

- [generateKeyPair](mta://scripting/shared/functions/generatekeypair.md)

- [getColorFromString](mta://scripting/shared/functions/getcolorfromstring.md)

- [getDevelopmentMode](mta://scripting/shared/functions/getdevelopmentmode.md)

- [getDistanceBetweenPoints2D](mta://scripting/shared/functions/getdistancebetweenpoints2d.md)

- [getDistanceBetweenPoints3D](mta://scripting/shared/functions/getdistancebetweenpoints3d.md)

- [getEasingValue](mta://scripting/shared/functions/geteasingvalue.md)

- [getNetworkStats](mta://scripting/shared/functions/getnetworkstats.md)

- [getNetworkUsageData](mta://scripting/shared/functions/getnetworkusagedata.md)

- [getPerformanceStats](mta://scripting/shared/functions/getperformancestats.md)

- [getRealTime](mta://scripting/shared/functions/getrealtime.md)

- [getTickCount](mta://scripting/shared/functions/gettickcount.md)

- [getTimerDetails](mta://scripting/shared/functions/gettimerdetails.md)

- [getTimers](mta://scripting/shared/functions/gettimers.md)

- [getFPSLimit](mta://scripting/shared/functions/getfpslimit.md)

- [getUserdataType](mta://scripting/shared/functions/getuserdatatype.md)

- [getVersion](mta://scripting/shared/functions/getversion.md)

- [gettok](mta://scripting/shared/functions/gettok.md)

- [isTransferBoxVisible](mta://scripting/shared/functions/istransferboxvisible.md)

- [setTransferBoxVisible](mta://scripting/shared/functions/settransferboxvisible.md)

- [hash](mta://scripting/shared/functions/hash.md)

- [inspect](mta://scripting/shared/functions/inspect.md)

- [interpolateBetween](mta://scripting/shared/functions/interpolatebetween.md)

- [iprint](mta://scripting/shared/functions/iprint.md)

- [isOOPEnabled](mta://scripting/shared/functions/isoopenabled.md)

- [isTimer](mta://scripting/shared/functions/istimer.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22701](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22701):

- [isTimerPaused](mta://scripting/shared/functions/istimerpaused.md)

- [setTimerPaused](mta://scripting/shared/functions/settimerpaused.md)

- [killTimer](mta://scripting/shared/functions/killtimer.md)

- [md5](mta://scripting/shared/functions/md5.md)

- [passwordHash](mta://scripting/shared/functions/passwordhash.md)

- [passwordVerify](mta://scripting/shared/functions/passwordverify.md)

- [pregFind](mta://scripting/shared/functions/pregfind.md)

- [pregMatch](mta://scripting/shared/functions/pregmatch.md)

- [pregReplace](mta://scripting/shared/functions/pregreplace.md)

- [removeDebugHook](mta://scripting/shared/functions/removedebughook.md)

- [resetTimer](mta://scripting/shared/functions/resettimer.md)

- [setDevelopmentMode](mta://scripting/shared/functions/setdevelopmentmode.md)

- [setFPSLimit](mta://scripting/shared/functions/setfpslimit.md)

- [setTimer](mta://scripting/shared/functions/settimer.md)

- [ref](mta://scripting/shared/functions/ref.md)

- [deref](mta://scripting/shared/functions/deref.md)

- [sha256](mta://scripting/shared/functions/sha256.md)

- [split](mta://scripting/shared/functions/split.md)

- [teaDecode](mta://scripting/shared/functions/teadecode.md)

- [teaEncode](mta://scripting/shared/functions/teaencode.md)

- [toJSON](mta://scripting/shared/functions/tojson.md)

- [tocolor](mta://scripting/shared/functions/tocolor.md)

- [getProcessMemoryStats](mta://scripting/shared/functions/getprocessmemorystats.md)

- [utfChar](mta://scripting/shared/functions/utfchar.md)

- [utfCode](mta://scripting/shared/functions/utfcode.md)

- [utfLen](mta://scripting/shared/functions/utflen.md)

- [utfSeek](mta://scripting/shared/functions/utfseek.md)

- [utfSub](mta://scripting/shared/functions/utfsub.md)

- [bitAnd](mta://scripting/shared/functions/bitand.md)

- [bitNot](mta://scripting/shared/functions/bitnot.md)

- [bitOr](mta://scripting/shared/functions/bitor.md)

- [bitXor](mta://scripting/shared/functions/bitxor.md)

- [bitTest](mta://scripting/shared/functions/bittest.md)

- [bitLRotate](mta://scripting/shared/functions/bitlrotate.md)

- [bitRRotate](mta://scripting/shared/functions/bitrrotate.md)

- [bitLShift](mta://scripting/shared/functions/bitlshift.md)

- [bitRShift](mta://scripting/shared/functions/bitrshift.md)

- [bitArShift](mta://scripting/shared/functions/bitarshift.md)

- [bitExtract](mta://scripting/shared/functions/bitextract.md)

- [bitReplace](mta://scripting/shared/functions/bitreplace.md)
