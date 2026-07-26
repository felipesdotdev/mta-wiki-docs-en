---
doc_id: "mta-wiki:13207"
title: "Lua compilation API"
source_title: "Lua compilation API"
source_url: "https://wiki.multitheftauto.com/wiki/Lua_compilation_API"
revision_id: 82014
language: "en"
categories: []
---

# Lua compilation API

This page is a guide for Lua compilation API.

## Syntax

```
POST "https://luac.mtasa.com/index.php"
```

## Parameters

- **luasource:** type **file** the file content

- **compile:** type **value** set to 1 to enable compilation

- **debug:** type **value** set to 1 to enable debug information

- **obfuscate:** type **value**

- Set to 1 to enable some obfuscation

- Set to 2 to enable more obfuscation (From 1.5.2-9.07903)

- Set to 3 to enable even more obfuscation (From 1.5.6-9.18728)

## Examples

### Linux example using curl

```
FROM="example.lua"
TO="compiled.lua"
curl -s -X POST -F compile=1 -F debug=0 -F obfuscate=3 -F luasource=@$FROM https://luac.mtasa.com/ > $TO
```

### Linux example using luac replacement

```
luac_mta -e3 -o compiled.lua example.lua
if [ $? -ne 0 ]; then
   echo "Error"
fi
```

Need luac_mta (R13 2019-07-12) for [Linux 32 bit](https://wiki.multitheftauto.com//luac.mtasa.com/files/linux/x86/luac_mta) or [Linux 64 bit](https://wiki.multitheftauto.com//luac.mtasa.com/files/linux/x64/luac_mta)

### Windows batch file example using curl

```
set FROM="example.lua"
set TO="compiled.lua"
curl.exe -s -X POST -F compile=1 -F debug=0 -F obfuscate=3 -F luasource=@%FROM% https://luac.mtasa.com/ > %TO%
```

Get [curl for win64](https://curl.se/windows/latest.cgi?p=win64-mingw.zip)  

(Original from [https://curl.haxx.se/download.html](https://curl.haxx.se/download.html))

### Windows example using luac.exe replacement

```
luac_mta.exe -e3 -o compiled.lua example.lua
IF NOT ERRORLEVEL 1 goto lp1
   echo "Error"
:lp1
```

Get [luac_mta.exe](https://wiki.multitheftauto.com//luac.mtasa.com/files/windows/x86/luac_mta.exe) (R12 2019-07-12) **only x86**

### Lua example

```
-- This example allows you to compile all resource scripts by using /compilelua command.

local compileEnabled = 1
local debugLevel = 0
local obfuscateLevel = 3
local apiCodes = {
	["ERROR Nothing to do - Please select compile and/or obfuscate"] = true,
	["ERROR Could not compile file"] = true,
	["ERROR Could not read file"] = true,
	["ERROR Already compiled"] = true,
	["ERROR Already encrypted"] = true,
}

local function loadScriptsFromMeta()
	local metaFile = xmlLoadFile("meta.xml")

	if not metaFile then
		outputDebugString("[LUAC]: Failed to load scripts from meta.", 4, 255, 127, 0)

		return false
	end

	local metaChildren = xmlNodeGetChildren(metaFile)
	local scriptsTable = {}

	for nodeID = 1, #metaChildren do
		local metaNode = metaChildren[nodeID]
		local fileSrc = xmlNodeGetAttribute(metaNode, "src")

		if fileSrc then
			local luaScript = string.find(fileSrc, ".lua")

			if luaScript then
				scriptsTable[#scriptsTable + 1] = fileSrc
			end
		end
	end

	xmlUnloadFile(metaFile)

	return scriptsTable
end

local function loadResourceScript(pPath)
	local scriptExists = fileExists(pPath)

	if not scriptExists then
		outputDebugString("[LUAC]: '"..pPath.."' doesn't exists.", 4, 255, 127, 0)

		return false
	end

	local scriptHandler = fileOpen(pPath)

	if not scriptHandler then
		outputDebugString("[LUAC]: '"..pPath.."' failed to open.", 4, 255, 127, 0)

		return false
	end

	local scriptSize = fileGetSize(scriptHandler)
	local scriptRaw = fileRead(scriptHandler, scriptSize)

	fileClose(scriptHandler)

	return scriptRaw
end

local function onScriptCompile(pCompiledLUA, pErrors, pScript)
	local compileSuccess = pErrors == 0

	if not compileSuccess then
		outputDebugString("[LUAC]: '"..pScript.."' failed to compile.", 4, 255, 127, 0)

		return false
	end

	local compileError = apiCodes[pCompiledLUA]

	if compileError then
		outputDebugString("[LUAC]: '"..pScript.."' failed to compile - "..pCompiledLUA, 4, 255, 127, 0)

		return false
	end

	local compiledScript = fileCreate("luac/"..pScript)

	if not compiledScript then
		outputDebugString("[LUAC]: '"..pScript.."' failed to create.", 4, 255, 127, 0)

		return false
	end

	fileWrite(compiledScript, pCompiledLUA)
	fileClose(compiledScript)

	outputDebugString("[LUAC]: '"..pScript.."' compiled successfully.", 4, 255, 127, 0)

	return true
end

function compileLuaScripts(pPlayer)
	local fetchURL = string.format("https://luac.mtasa.com/?compile=%i&debug=%i&obfuscate=%i", compileEnabled, debugLevel, obfuscateLevel)
	local resourceScripts = loadScriptsFromMeta()
	local postData = true

	for scriptID = 1, #resourceScripts do
		local scriptPath = resourceScripts[scriptID]
		local scriptRaw = loadResourceScript(scriptPath)

		fetchRemote(fetchURL, onScriptCompile, scriptRaw, postData, scriptPath)
	end
end
addCommandHandler("compilelua", compileLuaScripts)
```

### Python example

```
import requests

url_raw = 'luac.mtasa.com'
url = f'https://{url_raw}'
url_file = f'{url}/index.php'

newLine = '\r\n'
boundary = '------WebKitFormBoundary'
boundaryLine = f'{boundary}{newLine}'

headers = {
    'Host': url_raw,
    'Origin': url,
    'Referer': url_file,
    'Content-Type': f'multipart/form-data; boundary={boundary[2:]}',
}

fileContent = 'print("Hello, World!")'
fileName = 'main.lua'
docompile = 1
obfuscateLevel = 3
debug = 1

def req() -> requests.Response:
    payload = [
        [
            f'Content-Disposition: form-data; name="luasource"; filename="{fileName}"'.encode('utf-8'),
            b'Content-Type: application/octet-stream',
            f'{newLine}{fileContent}'.encode('utf-8')
        ],
        [
            b'Content-Disposition: form-data; name="compile"',
            f'{newLine}{docompile}'.encode('utf-8')
        ],
        [
            b'Content-Disposition: form-data; name="obfuscate"',
            f'{newLine}{obfuscateLevel}'.encode('utf-8')
        ],
        [
            b'Content-Disposition: form-data; name="debug"',
            f'{newLine}{debug}'.encode('utf-8')
        ],
        [
            b'Content-Disposition: form-data; name="Submit"',
            f'{newLine}Submit'.encode('utf-8')
        ]
    ]

    data = boundaryLine
    for c in payload:
        for cc in c:
            data += cc.decode('utf-8') + '\r\n'
        data += boundaryLine

    return requests.post(url_file, headers=headers, data=data)

if __name__ == '__main__':
    fileName = input('Filename (with extension): ')
    with open(fileName, 'r+') as f:
        fileContent = f.read()
    obfuscateLevel = int(input('Obfuscate level [0-3]: '))
    _docompile = input('Compile [true/false]: ').lower()
    if _docompile == 'true' or _docompile == 't' or _docompile == '1':
        docompile = '1'
    else:
        docompile = '0'
    _debug = input('Debug [true/false]: ').lower()
    if _debug == 'true' or _debug == 't' or _debug == '1':
        debug = '1'
    else:
        debug = '0'

    try:
        content = req().content
        if content == b'ERROR Could not compile file':
            print('Could not compile file!')
            exit(1)

        with open(fileName, 'wb+') as f:
            f.write(content)
        print('Done!')
    except Exception as e:
        print('An error occured:', e)
```

## Changelog

| Version | Description |
| --- | --- |

| 2014-08-10 | encrypt has been renamed to obfuscate . blockdecompile has been removed. |
| --- | --- |
