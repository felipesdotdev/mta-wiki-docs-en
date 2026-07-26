---
doc_id: "mta-wiki:5790"
title: "GetNetworkStats"
source_title: "GetNetworkStats"
source_url: "https://wiki.multitheftauto.com/wiki/GetNetworkStats"
revision_id: 29950
language: "en"
categories: ["Server_functions", "Client_functions"]
generated_at: "2026-07-26T16:15:16.150748+00:00"
---

# GetNetworkStats

This function returns network status information.

## Syntax

Click to collapse [-]
Client

```
table getNetworkStats ( )
```

Click to collapse [-]
Server

```
table getNetworkStats ( [ element thePlayer = nil ] )
```

### Optional Arguments

- **thePlayer:** The player you want to retrieve network stats from.

### Returns

Returns a table, the indexes in the table are the following:

- **bytesReceived** - Total number of bytes received since the connection was started

- **bytesSent** - Total number of bytes sent since the connection was started

- **packetsReceived** - Total number of packets received since the connection was started

- **packetsSent** - Total number of packets sent since the connection was started

- **packetlossTotal** - (0-100) Total packet loss percentage of sent data, since the connection was started

- **packetlossLastSecond** - (0-100) Packet loss percentage of sent data, during the previous second

- **messagesInSendBuffer**

- **messagesInResendBuffer** - Number of packets queued to be resent (due to packet loss)

- **isLimitedByCongestionControl**

- **isLimitedByOutgoingBandwidthLimit**

- **encryptionStatus**

## Example

Click to collapse [-]
Client

This example outputs the local players network status information to their console when using the /netstatus command

```
function netStatus()
	for index, value in pairs(getNetworkStats()) do
		outputConsole(index..": "..value)
	end
	outputChatBox("Network status output to console", 0, 255, 0)
end
addCommandHandler("netstatus", netStatus)
```

This example outputs a warning to local player if packet loss occured in the last second

```
function packetLossCheck()
	local loss = getNetworkStats()["packetlossLastSecond"]
	if (loss > 0) then
		outputChatBox("Packet loss detected when communicating with server, gameplay may be affected", 255, 0, 0)
	end
end
setTimer(packetLossCheck, 1000, 0)
```

This example tracks the average and peak packetloss over the last 60 seconds **PLEASE NOTE:** this example is untested.

```
PACKETLOSS_HISTORY_LENGTH = 60	-- Sample period in seconds
packetlossHistory = {}
packetlossAvg = 0		-- (Output) Average packet loss over last 60 seconds
packetlossPeak = 0		-- (Output) Peak packet loss over last 60 seconds

function samplePacketLoss()
	table.insert( packetlossHistory, getNetworkStats().packetlossLastSecond )
	while( #packetlossHistory > PACKETLOSS_HISTORY_LENGTH ) do
		table.remove( packetlossHistory, 1 )
	end
	packetlossAvg = 0
	packetlossPeak = 0
	for _,value in ipairs(packetlossHistory) do
		packetlossAvg = packetlossAvg + value
		packetlossPeak = math.max( packetlossPeak, value )
	end
	packetlossAvg = packetlossAvg / #packetlossHistory
end

setTimer(samplePacketLoss,1000,0)
```

## See Also

- [createTrayNotification](mta://scripting/client/functions/createtraynotification.md)

- [downloadFile](mta://scripting/client/functions/downloadfile.md)

- [getKeyboardLayout](mta://scripting/client/functions/getkeyboardlayout.md)

- [getLocalization](mta://scripting/client/functions/getlocalization.md)

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

- getNetworkStats

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
