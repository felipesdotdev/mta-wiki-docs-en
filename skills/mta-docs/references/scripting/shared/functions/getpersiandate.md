---
doc_id: "mta-wiki:14522"
title: "GetPersianDate"
source_title: "GetPersianDate"
source_url: "https://wiki.multitheftauto.com/wiki/GetPersianDate"
revision_id: 81726
language: "en"
categories: ["Useful_Functions"]
---

# GetPersianDate

getPersianDate

This function calculates and returns the Persian (Jalali) date based on the server's real time.

**Author:** [Aria](https://wiki.multitheftauto.com/wiki/User:Aria)

### Syntax

```
getPersianDate()
```

### Returns

- **year**: The Persian (Jalali) year.

- **month**:  The Persian (Jalali) month.

- **day**:  The Persian (Jalali) day.

### Code

Click to collapse [-]
Server/Client side Script

```
function getPersianDate()
    -- Get the current real time
    local time = getRealTime()
    
    -- Extract Gregorian year, month, and day
    local gy = time.year + 1900 
    local gm = time.month + 1 
    local gd = time.monthday 

    -- Table of cumulative days for each month in a non-leap year
    local g_d_m = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334}
    
    -- Adjust the year if the month is after February (for leap year calculation)
    local gy2 = (gm > 2) and (gy + 1) or gy
    
    -- Calculate the total number of days since a fixed starting point
    local days = 355666 + (365 * gy) + math.floor((gy2 + 3) / 4) - math.floor((gy2 + 99) / 100) + math.floor((gy2 + 399) / 400) + gd + g_d_m[gm]
    
    -- Calculate the Jalali year
    local jy = -1595 + (33 * math.floor(days / 12053))
    days = days % 12053
    jy = jy + (4 * math.floor(days / 1461))
    days = days % 1461
    
    -- Adjust the Jalali year if there are remaining days
    if days > 365 then
        jy = jy + math.floor((days - 1) / 365)
        days = (days - 1) % 365
    end
    
    -- Calculate the Jalali month and day
    local jm = (days < 186) and math.floor((days - 1) / 31) + 1 or math.floor((days - 186) / 30) + 7
    local jd = (days < 186) and ((days - 1) % 31) + 1 or ((days - 186) % 30) + 1

    -- Return the Persian (Jalali) date as a table
    return {year = jy, month = jm, day = jd}
end
```

## Example

Click to collapse [-]
client

```
addCommandHandler("date", function()
    local PersianDate = getPersianDate()
    outputChatBox("Persian Date: " .. PersianDate.year .. "/" .. PersianDate.month .. "/" .. PersianDate.day)
end)
```

Click to collapse [-]
server

```
addCommandHandler("date", function(player)
    local PersianDate = getPersianDate()
    outputChatBox("Persian Date: " .. PersianDate.year .. "/" .. PersianDate.month .. "/" .. PersianDate.day, player)
end)
```

### Notes

- This function works on both the server and client.

- It does not require any external dependencies.
