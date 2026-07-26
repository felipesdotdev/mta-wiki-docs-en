---
doc_id: "mta-wiki:9052"
title: "GetUserdataType"
source_title: "GetUserdataType"
source_url: "https://wiki.multitheftauto.com/wiki/GetUserdataType"
revision_id: 76247
language: "en"
categories: ["Server_functions", "Client_functions", "Changes_in_1.5.3"]
generated_at: "2026-07-26T16:15:26.633176+00:00"
---

# GetUserdataType

This function gets the type of a userdata value, which is not always a [element](mta://reference/misc/element.md) in the element tree.

## Syntax

```
string getUserdataType ( userdata value )
```

### Required Arguments

- **value**: A userdata value to get the type of. Userdata types can be:

- **Shared**

- *resource-data*: a [resource pointer](mta://reference/misc/resource.md).

- *xml-node*: a [XML node](mta://reference/misc/xmlnode.md).

- *lua-timer*: a [timer](mta://reference/misc/timer.md).

- *vector2*: a 2D vector, used in the [Vector2](mta://reference/misc/vector-vector2.md) class.

- *vector3*: a 3D vector, used in the [Vector3](mta://reference/misc/vector-vector3.md) class.

- *vector4*: a 4D vector, used in the [Vector4](mta://reference/misc/vector-vector4.md) class.

- *matrix*: a matrix, used in the [Matrix](mta://reference/misc/matrix.md) class.

- *request*: a userdata type returned via [fetchRemote](mta://scripting/shared/functions/fetchremote.md) (since [r21436](https://buildinfo.mtasa.com/?Revision=21436&Branch=))

- *userdata*: a fallback userdata type return value, when no other type could be found for the object.

- **Server only**

- *account*: a [player account](mta://reference/misc/account.md).

- *db-query*: a [database query handle](mta://scripting/server/functions/dbquery.md).

- *acl*: an [ACL entry](mta://tutorials/acl.md).

- *acl-group*: an [ACL group](mta://reference/misc/aclgroup--4c7248ae.md).

- *ban*: a [player ban](mta://reference/misc/ban.md).

- *text-item*: a [text display item](mta://reference/misc/textitem.md).

- *text-display*: a [text display item](mta://reference/misc/textdisplay.md).

### Returns

Returns a [string](mta://reference/misc/string.md) containing the specified userdata's type, or *false* plus an error message if the given value is not userdata.

## Example

This example shows a function that can be used to work around the impossibility to transfer vectors as arguments when using [triggerClientEvent](mta://scripting/server/functions/triggerclientevent.md) and [triggerServerEvent](mta://scripting/client/functions/triggerserverevent.md), by converting them into a table which can be used safely.

```
function safeArgsForTransfer(...)
    local args = { ... }
    for index, arg in ipairs(args) do
        if type(arg) == "userdata" and getUserdataType(arg):match("vector") then
            -- Transform every kind of vector userdata to a table which can be transfered safely
            args[index] =
            {
                arg:getX(),
                arg:getY(),
                arg.getZ and arg:getZ() or nil,
                arg.getW and arg:getW() or nil,
                -- Extra field to distinguish from normal tables
                ["isVectorWorkaround"] = true
            }
        end
    end
    return unpack(args)
end
```

## See Also

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

- getUserdataType

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
