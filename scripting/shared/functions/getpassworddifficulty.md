---
doc_id: "mta-wiki:12165"
title: "GetPasswordDifficulty"
source_title: "GetPasswordDifficulty"
source_url: "https://wiki.multitheftauto.com/wiki/GetPasswordDifficulty"
revision_id: 65715
language: "en"
categories: ["Useful_Functions"]
generated_at: "2026-07-26T16:15:16.678735+00:00"
---

# GetPasswordDifficulty

This function checks the password difficulty

## Syntax

```
int getPasswordDifficulty ( string password )
```

### Required arguments

- **password**: The password whose difficulty you want to check

### Return

Returns a value from 1

## Code

```
function getPasswordDifficulty(password)
    assert(type(password) == "string", "Bad argument @ getPasswordDifficulty [string expected, got " .. tostring(password) .. "]" )
    local strong = 0
    if string.find(password, "[0-9]") then
        strong = strong + 1
    end
    if string.find(password, "%u") then
        strong = strong + 1
    end
    return strong
end
```

## Example

Click to collapse [-]
Example

After using the command with a password, it returns its difficulty

```
function difficulty(commandName, password)
	if not password then
        return outputChatBox("Type password")
    end
    outputChatBox(getPasswordDifficulty(password))
end    
addCommandHandler("difficulty", difficulty)
```

Author: Liberty
