---
doc_id: "mta-wiki:12388"
title: "GetSkinNameFromID"
source_title: "GetSkinNameFromID"
source_url: "https://wiki.multitheftauto.com/wiki/GetSkinNameFromID"
revision_id: 66841
language: "en"
categories: ["Useful_Functions"]
generated_at: "2026-07-26T16:15:25.172545+00:00"
---

# GetSkinNameFromID

Gets the name of the skin from the given skin id.

## Syntax

```
string getSkinNameFromID ( int id )
```

### Required Arguments

- **id:** the skin model ID. For players/peds: A GTASA player model (skin) ID. See [Character Skins](mta://reference/misc/character-skins.md) to see what values will return names.

### Return

Returns the name of the Skin if the model ID was valid

## Code

Click to collapse [-]
Clientside Script

```
local skinsTable = {
[0] = "CJ", [1] = "Truth", [2] = "Maccer", [7] = "Casual JeanJacket", [9] = "Business Lady",
[10] = "Old Fat Lady", [11] = "Card Dealer 1", [12] = "Classy Gold Hooker", [13] = "Homegirl", [14] = "Floral Shirt",
[15] = "Plaid Baldy", [16] = "Earmuff Worker", [17] = "Black suit", [18] = "Black Beachguy", [19] = "Beach Gangsta",
[20] = "Fresh Prince", [21] = "Striped Gangsta", [22] = "Orange Sportsman", [23] = "Skater Kid", [24] = "LS Coach",
[25] = "Varsity jacket", [26] = "Hiker", [27] = "Construction 1", [28] = "Black Dealer", [29] = "White Dealer",
[30] = "Religious Essey", [31] = "Fat Cowgirl", [32] = "Eyepatch", [33] = "Bounty Hunter", [34] = "Marlboro Man",
[35] = "Fisherman", [36] = "Mailman", [37] = "Baseball Dad", [38] = "Old Golf Lady", [39] = "Old Maid",
[40] = "Classy Dark Hooker", [41] = "Tracksuit Girl", [43] = "Porn Producer", [44] = "Tatooed Plaid", [45] = "Beach Mustache",
[46] = "Dark Romeo", [47] = "Top Button Essey", [49] = "Ninja Sensei", [50] = "Mechanic", [51] = "Black Bicyclist",
[52] = "White Bicyclist", [53] = "Golf Lady", [54] = "Hispanic Woman", [55] = "Rich Bitch", [56] = "Legwarmers 1",
[57] = "Chinese Businessman", [58] = "Chinese Plaid", [59] = "Chinese Romeo", [60] = "Chinese Casual", [61] = "Pilot",
[62] = "Pajama Man 1", [63] = "Trashy Hooker", [64] = "Transvestite", [66] = "Varsity Bandits", [67] = "Red Bandana",
[68] = "Preist", [69] = "Denim Girl", [70] = "Scientist", [71] = "Security Guard", [72] = "Bearded Hippie",
[73] = "Flag Bandana", [75] = "Skanky Hooker", [76] = "Businesswoman 1", [77] = "Bag Lady", [78] = "Homeless Scarf",
[79] = "Fat Homeless", [80] = "Red Boxer", [81] = "Blue Boxer", [82] = "Fatty Elvis", [83] = "Whitesuit Elvis",
[84] = "Bluesuit Elvis", [85] = "Furrcoat Hooker", [87] = "Firecrotch", [88] = "Casual Old Lady", [89] = "Cleaning Lady",
[90] = "Barely Covered", [91] = "Sharon Stone", [92] = "Rollergirl", [93] = "Hoop Earrings 1", [94] = "Andy Capp",
[95] = "Poor Old Man", [96] = "Soccer Player", [97] = "Baywatch Dude", [99] = "Rollerguy", [100] = "Biker Blackshirt",
[101] = "Jacker Hippie", [102] = "Baller Shirt", [103] = "Baller Jacket", [104] = "Baller Sweater", [105] = "Grove Sweater",
[106] = "Grove Tropbutton", [107] = "Grove Jersey", [108] = "Vagos Topless", [109] = "Vagos Pants", [110] = "Vagos Shorts",
[111] = "Russian Muscle", [112] = "Russian Hitman", [113] = "Russian Boss", [114] = "Aztecas Stripes", [115] = "Aztecas Jacket",
[116] = "Aztecas Shorts", [117] = "Triad 1", [118] = "Triad 2", [119] = "Triad 3", [120] = "Sinacco Suit",
[121] = "Da Nang Army", [122] = "Da Nang Bandana", [123] = "Da Nang Shades", [124] = "Sinacco Muscle", [125] = "Mafia Enforcer",
[126] = "Mafia Wiseguy", [127] = "Mafia Hitman", [128] = "Native Rancher", [129] = "Native Librarian", [130] = "Native Ugly",
[131] = "Native Sexy", [132] = "Native Geezer", [133] = "Furys Trucker", [134] = "Homeless Smoker", [135] = "Skullcap Hobo",
[136] = "Old Rasta", [137] = "Boxhead", [138] = "Bikini Tattoo", [139] = "Yellow Bikini", [140] = "Buxom Bikini",
[141] = "Cute Librarian", [142] = "African 1", [143] = "Sam Jackson", [144] = "Drug Worker 1", [145] = "Drug Worker 2",
[146] = "Drug Worker 3", [147] = "Sigmund Freud", [148] = "Businesswoman 2", [149] = "Businesswoman 2 b", [150] = "Businesswoman 3",
[151] = "Melanie", [152] = "Schoolgirl 1", [153] = "Foreman", [154] = "Beach Blonde", [155] = "Pizza Guy",
[156] = "Old Reece", [157] = "Farmer Girl", [158] = "Farmer", [159] = "Farmer Redneck", [160] = "Bald Redneck",
[161] = "Smoking Cowboy", [162] = "Inbred", [163] = "Casino Bouncer 1", [164] = "Casino Bouncer 2", [165] = "Agent Kay",
[166] = "Agent Jay", [167] = "Chicken", [168] = "Hotdog Vender", [169] = "Asian Escort", [170] = "PubeStache Tshirt",
[171] = "Card Dealer 2", [172] = "Card Dealer 3", [173] = "Rifa Hat", [174] = "Rifa Vest", [175] = "Rifa Suspenders",
[176] = "Style Barber", [177] = "Vanilla Ice Barber", [178] = "Masked Stripper", [179] = "War Vet", [180] = "Bball Player",
[181] = "Punk", [182] = "Pajama Man 2", [183] = "Klingon", [184] = "Neckbeard", [185] = "Nervous Guy",
[186] = "Teacher", [187] = "Japanese Businessman 1", [188] = "Green Shirt", [189] = "Valet", [190] = "Barbara Schternvart",
[191] = "Helena Wankstein", [192] = "Michelle Cannes", [193] = "Katie Zhan", [194] = "Millie Perkins", [195] = "Denise Robinson",
[196] = "Aunt May", [197] = "Smoking Maid", [198] = "Ranch Cowgirl", [199] = "Heidi", [200] = "Hairy Redneck",
[201] = "Trucker Girl", [202] = "Beer Trucker", [203] = "Ninja 1", [204] = "Ninja 2", [205] = "Burger Girl",
[206] = "Money Trucker", [207] = "Grove Booty", [209] = "Noodle Vender", [210] = "Sloppy Tourist", [211] = "Staff Girl",
[212] = "Tin Foil Hat", [213] = "Hobo Elvis", [214] = "Caligula Waitress", [215] = "Explorer", [216] = "Turtleneck",
[217] = "Staff Guy", [218] = "Old Woman", [219] = "Lady In Red", [220] = "African 2", [221] = "Beardo Casual",
[222] = "Beardo Clubbing", [223] = "Greasy Nightclubber", [224] = "Elderly Asian 1", [225] = "Elderly Asian 2", [226] = "Legwarmers 2",
[227] = "Japanese Businessman 2", [228] = "Japanese Businessman 3", [229] = "Asian Tourist", [230] = "Hooded Hobo", [231] = "Grannie",
[232] = "Grouchy lady", [233] = "Hoop Earrings 2", [234] = "Buzzcut", [235] = "Retired Tourist", [236] = "Happy Old Man",
[237] = "Leopard Hooker", [238] = "Amazon", [240] = "Hugh Grant", [241] = "Afro Brother", [242] = "Dreadlock Brother",
[243] = "Ghetto Booty", [244] = "Lace Stripper", [245] = "Ghetto Ho", [246] = "Cop Stripper", [247] = "Biker Vest",
[248] = "Biker Headband", [249] = "Pimp", [250] = "Green Tshirt", [251] = "Lifeguard", [252] = "Naked Freak",
[253] = "Bus Driver", [254] = "Biker Vest b", [255] = "Limo Driver", [256] = "Shoolgirl 2", [257] = "Bondage Girl",
[258] = "Joe Pesci", [259] = "Chris Penn", [260] = "Construction 2", [261] = "Southerner", [262] = "Pajama Man 2 b",
[263] = "Asian Hostess", [264] = "Whoopee the Clown", [265] = "Tenpenny", [266] = "Pulaski", [267] = "Hern",
[268] = "Dwayne", [269] = "Big Smoke", [270] = "Sweet", [271] = "Ryder", [272] = "Forelli Guy",
[274] = "Medic 1", [275] = "Medic 2", [276] = "Medic 3", [277] = "Fireman LS", [278] = "Fireman LV",
[279] = "Fireman SF", [280] = "Cop 1", [281] = "Cop 2", [282] = "Cop 3", [283] = "Cop 4",
[284] = "Cop 5", [285] = "SWAT", [286] = "FBI", [287] = "Army", [288] = "Cop 6",
[290] = "Rose", [291] = "Kent Paul", [292] = "Cesar", [293] = "OG Loc", [294] = "Wuzi Mu",
[295] = "Mike Toreno", [296] = "Jizzy", [297] = "Madd Dogg", [298] = "Catalina", [299] = "Claude from GTA 3",
[300] = "Ryder", [301] = "Ryder Robber", [302] = "Emmet", [303] = "Andre", [304] = "Kendl",
[305] = "Jethro", [306] = "Zero", [307] = "T-bone Mendez", [308] = "Sindaco Guy", [309] = "Janitor",
[310] = "Big Bear", [311] = "Big Smoke with Vest", [312] = "Physco", 
}
function getSkinNameFromID(i)
    local id = tonumber (i)
        assert(id, "Bad argument 1 @ getSkinFromID [Number expected, got " .. type(i) .. "]")
    local name = skinsTable[id]
        assert(name,"Bad argument 1 @ getSkinFromID [Invaild skin ID]")
    return name 
end
```

## Example

**Example 1:** This example shows you a command to get the skin name with [getElementModel](mta://scripting/shared/functions/getelementmodel.md) :

Click to collapse [-]
Example1

```
addCommandHandler('skin',
function()
local name = getSkinNameFromID(getElementModel(localPlayer))
if name then
outputChatBox('SkinName : ('..name..') of ID ('..getElementModel(localPlayer)..')',255,255,0)
else
outputChatBox('Failed to get the SkinName : Wrong ID or not Found in the Table',255,255,0)
end
end)
```

**Example 2:** This example check if the skin name is CJ when press on gui button:

Click to expand [+]
Example2

```
wnd = guiCreateWindow(524, 259, 310, 223, "skin name", false)
btn = guiCreateButton(52, 76, 190, 31, "Iam CJ ?", false, wnd)

function checkCJ( )
local skinname = getSkinNameFromID(getElementModel(localPlayer))
if skinname == 'CJ' then
outputChatBox('you have CJ skin',0,255,0)
else
outputChatBox('you havenot CJ',255,0,0)
end
end
addEventHandler('onClientGUIClick',btn,checkCJ)
```

**Example 3:** This example check the skin name by command and id:

Click to expand [+]
Example2

```
function skinNameID ( commandName,id )
if (id) and tonumber(id) then
local skinname = getSkinNameFromID(id)
if skinname then
outputChatBox('SkinName : ('..name..') of ID : ('..id..')',255,0,0)
else
outputChatBox('Failed to get the SkinName : Wrong ID or not Found in the Table',255,255,255)
end
end
end
addCommandHandler ( "name", skinNameID )
```

Author: MrKAREEM , Edited By Live

## See Also

### Table functions

- [addTableChangeHandler](mta://scripting/shared/functions/addtablechangehandler.md) » This function monitors the changes of a table.

- [pairsByKeys](mta://scripting/shared/functions/pairsbykeys.md) » This function sort pairs table.

- [rangeToTable](mta://scripting/shared/functions/rangetotable.md) » This function converts a string range to a table containing number values.

- [setTableProtected](mta://scripting/shared/functions/settableprotected.md) » This function protects a table and makes it read-only.

- [setTableToSql](mta://scripting/shared/functions/settabletosql.md) » This function is used to save the table in the database (sql).

- [Sort_Functions](mta://scripting/shared/functions/sort-functions.md) » These functions are able to sort your tables by a key.

- [getKeyFromValueInTable](mta://scripting/shared/functions/getkeyfromvalueintable.md) » This function returns the key of the specified value in a table.

- [getTableFromSql](mta://scripting/shared/functions/gettablefromsql.md) » This functionality is used to obtain saved tables using the function ([SetTableToSql](https://wiki.multitheftauto.com/wiki/SetTableToSql)).

- [isValueInTable](mta://scripting/shared/functions/isvalueintable.md) » This function returns true if the value exists in the table, false if the value does not exist in the table.

- [table.compare](mta://scripting/shared/functions/table-compare.md) » This function checks whether two given tables are equal.

- [table.copy](mta://scripting/shared/functions/table-copy.md) » This function copies a whole table and all the tables in that table.

- [table.deepmerge](mta://scripting/shared/functions/table-deepmerge.md) » This function deep merges two tables. Every nested table will be correspondingly merged.

- [table.element](mta://scripting/shared/functions/table-element.md) » This function returns a new table with only userdata content.

- [table.flip](mta://scripting/shared/functions/table-flip.md) » This function returns the table from the last value to the first value, such as reflection.

- [table.getRandomRows](mta://scripting/shared/functions/table-getrandomrows.md) » This function returns random rows from table.

- [table.map](mta://scripting/shared/functions/table-map.md) » This function goes through a table and replaces every field with the return of the passed function, where the field's value is passed as first argument and optionally more arguments.

- [table.merge](mta://scripting/shared/functions/table-merge.md) » This function merges two or more tables together.

- [table.random](mta://scripting/shared/functions/table-random.md) » This function retrieves a random value from a table.

- [table.removeValue](mta://scripting/shared/functions/table-removevalue.md) » This function removes a specified value from a table.

- [table.size](mta://scripting/shared/functions/table-size.md) » This function returns the absolute size of a table.

- [table.flatten](mta://scripting/shared/functions/table-flatten.md) » This function converts a nested table into a flattened table with concatenated keys.

### ACL functions

- [aclGroupClone](mta://scripting/shared/functions/aclgroupclone.md) » This function clone a group to another group with/without ACLs and/or objects.

- [renameAclGroup](mta://scripting/shared/functions/renameaclgroup.md) » This function gives an existing ACL group a new name.

- [getPlayersInACLGroup](mta://scripting/shared/functions/getplayersinaclgroup.md) » This function returns all players in an ACL group.

- [isPlayerInACL](mta://scripting/shared/functions/isplayerinacl.md) » This function checks if a player element is in an ACL group.

### Account functions

- [getPlayerFromAccountName](mta://scripting/shared/functions/getplayerfromaccountname.md) » This function is used to obtain a player by the name of his account.

- [isPlayerAccount](mta://scripting/shared/functions/isplayeraccount.md) » This function checks if the account is a valid player account (account exists and is not a guest account)

### Camera functions

- [smoothMoveCamera](mta://scripting/shared/functions/smoothmovecamera.md) » This function allows you to create a cinematic camera flight.

- [sCamera](mta://scripting/shared/functions/scamera.md) » The function creates a speed camera in-game, fines speeding vehicles, and notifies the driver and take money from player based on vehicle speed.

### Colshape functions

- [createGarageColShape](mta://scripting/shared/functions/creategaragecolshape.md) » This function creates a collision shape from the specified garage.

### Cursor functions

- [getCursorMovedOn](mta://scripting/shared/functions/getcursormovedon.md) » This function checks in which way the cursor is currently moving.

- [setCursorCenteredOnRectangle](mta://scripting/shared/functions/setcursorcenteredonrectangle.md) » This functions will center the cursor inside a rectangle.

### Drawing functions

- [dxDrawAnimWindow](mta://scripting/shared/functions/dxdrawanimwindow.md) » This function draws an animated 2D window on the screen.

- [dxDrawBorderedRectangle](mta://scripting/shared/functions/dxdrawborderedrectangle.md) » This is a function that will create a bordered rectangle.

- [dxDrawBorderedText](mta://scripting/shared/functions/dxdrawborderedtext.md) » This is a function that will create a bordered text.

- [dxDrawDashedLine](mta://scripting/shared/functions/dxdrawdashedline.md) » This function draws a line with dashes.

- [dxDrawEditbox](mta://scripting/shared/functions/dxdraweditbox.md) » This function draws a edit box across the screen - rendered for one frame. This should be used in conjunction with **onClientRender** in order to display continuously.

- [dxDrawGifImage](mta://scripting/shared/functions/dxdrawgifimage.md) » This function simulates the effect of a GIF image by using image sprites in 2D.

- [dxDrawImage3D](mta://scripting/shared/functions/dxdrawimage3d.md) » This function draws a 3D image in GTA world.

- [dxDrawImageOnElement](mta://scripting/shared/functions/dxdrawimageonelement.md) » This function draws an image on any element.

- [dxDrawLinedRectangle](mta://scripting/shared/functions/dxdrawlinedrectangle.md) » This is a function that will create a rectangle outline with dx lines.

- [dxDrawLoading](mta://scripting/shared/functions/dxdrawloading.md) » This function draws a loading bar on the screen.

- [dxDrawOctagon3D](mta://scripting/shared/functions/dxdrawoctagon3d.md) » This function creates a 3D Octagon

- [dxDrawPolygon](mta://scripting/shared/functions/dxdrawpolygon.md) » This function draws a custom polygon on the screen.

- [dxDrawProgressBar](mta://scripting/shared/functions/dxdrawprogressbar.md) » This function simulates a progress bar drawed using DirectDraw.

- [dxDrawRectangle3D](mta://scripting/shared/functions/dxdrawrectangle3d.md) » This function draws a 3D rectangle in GTA world.

- [dxDrawRectangleOnPlayer](mta://scripting/shared/functions/dxdrawrectangleonplayer.md) » This function draws a 3D rectangle above the player.

- [dxDrawRing](mta://scripting/shared/functions/dxdrawring.md) » This function draws a ring with dx lines.

- [dxDrawRombo](mta://scripting/shared/functions/dxdrawrombo.md) » This function creates a Rhombus.

- [dxDrawSprite](mta://scripting/shared/functions/dxdrawsprite.md) » This function draw a sprite in the 3D world.

- [dxDrawTextOnElement](mta://scripting/shared/functions/dxdrawtextonelement.md) » This function draws a text on any element.

- [dxDrawTextOnRectangle](mta://scripting/shared/functions/dxdrawtextonrectangle.md) » Esta funcion crea un rectangle con un texto dentro.

- [dxDrawTriangle](mta://scripting/shared/functions/dxdrawtriangle.md) » This is a function that will create a triangle with dx lines.

- [dxDrawBordered3DLine](mta://scripting/shared/functions/dxdrawbordered3dline.md) »This function creates a bordered area with 3D dx lines.

- [dxFade](mta://scripting/shared/functions/dxfade.md) » This function fade-in or fade-out any dxDraw by gradually changing its alpha value.

- [dxGetFontSizeFromHeight](mta://scripting/shared/functions/dxgetfontsizefromheight.md) » This function calculates the font size from given height.

- [dxGetRealFontHeight](mta://scripting/shared/functions/dxgetrealfontheight.md) » This function calculates the height of a font.

- [wordWrap](mta://scripting/shared/functions/wordwrap.md) » This function breaks a long string into a table of separate lines limited to a specific length in pixels, for drawing separately.

- [CreateRectangle3D](mta://scripting/shared/functions/createrectangle3d.md) » This is a function that will create a 3d rectangle on the player screen.

- [getScreenStartPositionFromBox](mta://scripting/shared/functions/getscreenstartpositionfrombox.md) » This function helps with getting the correct position for your dx-effects.

### Effects functions

- [attachEffect](mta://scripting/shared/functions/attacheffect.md) » This function allows you attach an effect to an element.

- [setScreenFlash](mta://scripting/shared/functions/setscreenflash.md) » This function will make the screen flash(like a screenshot).

### Element functions

- [autoAttach](mta://scripting/shared/functions/autoattach.md) » This function attaches one element into another at the same position and rotation they are.

- [attachElementToBone](mta://scripting/shared/functions/attachelementtobone.md) » This function allows you to attach an element to ped bone accurately using new bone functions.

- [getElementDirectionCardialPoint](mta://scripting/shared/functions/getelementdirectioncardialpoint.md) » This function returns the direction of the element according to the *wind rose*.

- [getElementSpeed](mta://scripting/shared/functions/getelementspeed.md) » This function returns the specified element's speed in m/s, km/h or mph.

- [getElementUsingData](mta://scripting/shared/functions/getelementusingdata.md) » This function returns table elements that contains the elements data with the given key and value.

- [getElementZoneFullName](mta://scripting/shared/functions/getelementzonefullname.md) » This function allows you to retrieve the zone full name of a element.

- [getElementsInDimension](mta://scripting/shared/functions/getelementsindimension.md) » This function returns a table of elements that are in the specified dimension.

- [getElementsWithinMarker](mta://scripting/shared/functions/getelementswithinmarker.md) » This function returns a table of elements that are within a marker's collision shape.

- [getNearestElement](mta://scripting/shared/functions/getnearestelement.md) » This function returns the nearest element (of a specific type) to a player.

- [getPositionInFrontOfElement](mta://scripting/shared/functions/getpositioninfrontofelement.md) » This function returns position in provided distance away from element, including element's rotation.

- [isElementInAir](mta://scripting/shared/functions/iselementinair.md) » This function checks if an element is in air or not.

- [isElementInPhotograph](mta://scripting/shared/functions/iselementinphotograph.md) » This function checks if an element is in the player's camera picture area.

- [isElementInRange](mta://scripting/shared/functions/iselementinrange.md) » This function allows you to check if an element's range to a main point is within the maximum range.

- [isElementMoving](mta://scripting/shared/functions/iselementmoving.md) » This function checks if an element is moving.

- [isElementPlayer](mta://scripting/shared/functions/iselementplayer.md) » This function checks whether the element is a player or not.

- [isElementWithinAColShape](mta://scripting/shared/functions/iselementwithinacolshape.md) » This function checks if an element is within a collision shape element.

- [multi_check](mta://scripting/shared/functions/multi-check.md) » This function checks one element to many, handy and clean.

- [setElementSpeed](mta://scripting/shared/functions/setelementspeed.md) » This function allows you to set the speed of an element in kph or mph units.

- [getElementResourceName](mta://scripting/shared/functions/getelementresourcename.md) » This function returns the name of the resource that created an element.

### Events

- [onClientPlayerTimeChange](mta://scripting/client/functions/onclientplayertimechange.md) » This code implements an event that is triggered when the player's real time change.

- [onPlayerZoneChange](mta://scripting/shared/functions/onplayerzonechange.md) » This code implements an event that is triggered when the player enters a new area on the map.

- [onVehicleWeaponFire](mta://scripting/shared/functions/onvehicleweaponfire.md) » This code implements an event that is triggered when a player in a vehicle fires a vehicle's weapon.

### Input functions

- [bindControlKeys](mta://scripting/shared/functions/bindcontrolkeys.md) » This function allows you to bind each key bound to a control individually. Doing this bypasses a little MTA restriction.

- [unbindControlKeys](mta://scripting/shared/functions/unbindcontrolkeys.md) » This function allows you to unbind each key bound to a control individually. Use this function with [bindControlKeys](mta://scripting/shared/functions/bindcontrolkeys.md).

- [getBoundControls](mta://scripting/shared/functions/getboundcontrols.md) » This function returns a table of control names that are bound to the specified key.

- [isCommandHandlerAdded](mta://scripting/shared/functions/iscommandhandleradded.md) » This function allows you to check if a command is added or not in the respective resource.

### Data functions

- [levenshtein](mta://scripting/shared/functions/levenshtein.md) » This function can be used to calculate the Levenshtein distance between two strings.

- [gregorianToJalali](mta://scripting/shared/functions/gregoriantojalali.md) » This function converts gregorian date to jalali/shamsi date.

- [byte2human](mta://scripting/shared/functions/byte2human.md) » This function converts an integer (number of bytes) into a human-readable unit.

- [capitalize](mta://scripting/shared/functions/capitalize.md) » This function capitalizes a given string.

- [convertDate](mta://scripting/shared/functions/convertdate.md) » This function converts date to another look.

- [convertServerTickToTimeStamp](mta://scripting/shared/functions/convertserverticktotimestamp.md) » This function converts server ticks to a unix timestamp.

- [convertTextToSpeech](mta://scripting/shared/functions/converttexttospeech.md) » This function converts the provided text to a speech in the provided language which players can hear.

- [findRotation3D](mta://scripting/shared/functions/findrotation3d.md) » This function takes two sets of XYZ coordinates. It returns the 3D direction from point A to point B.

- [findRotation](mta://scripting/shared/functions/findrotation.md) » This function takes two points and returns the direction from point A to point B.

- [formatDate](mta://scripting/shared/functions/formatdate.md) » This function formats a date on the basis of a format string and returns it.

- [formatNumber](mta://scripting/shared/functions/formatnumber.md) » This function formats large numbers by adding commas.

- [generateRandomASCIIString](mta://scripting/shared/functions/generaterandomasciistring.md) » This function returns a random string which uses ASCII characters.

- [generateString](mta://scripting/shared/functions/generatestring.md) » This function generates a random string with any characters.

- [getAge](mta://scripting/shared/functions/getage.md) » This function calculates the age of a given birthday.

- [getDistanceBetweenElements](mta://scripting/shared/functions/getdistancebetweenelements.md) » Returns the distance between two elements.

- [getDistanceBetweenPointAndSegment2D](mta://scripting/shared/functions/getdistancebetweenpointandsegment2d.md) » This function takes point coordinates and line (a segment) starting and ending coordinates. It returns the shortest distance between the point and the line.

- [getEasterDate](mta://scripting/shared/functions/geteasterdate.md) » This function returns easter date monthday and month for a given year.

- [getElementRelatedAngle](mta://scripting/shared/functions/getelementrelatedangle.md) » This function returns the related angle between one element to another. This is useful to check which side an element is to another.

- [getFreeDimension](mta://scripting/shared/functions/getfreedimension.md) » This function get free dimension.

- [getOffsetFromXYZ](mta://scripting/shared/functions/getoffsetfromxyz.md) » This function allows you to take an entity and a position and calculate the relative offset between them accounting for rotations.

- [getPointFromDistanceRotation](mta://scripting/shared/functions/getpointfromdistancerotation.md) » This function finds a point based on a starting point, direction and distance.

- [getRealMonth](mta://scripting/shared/functions/getrealmonth.md) » This function returns the current month name

- [getRGColorFromPercentage](mta://scripting/shared/functions/getrgcolorfrompercentage.md) »This function returns two integers representing red and green colors according to the specified percentage.

- [getScreenRotationFromWorldPosition](mta://scripting/shared/functions/getscreenrotationfromworldposition.md) » This function returns a screen relative rotation to a world position.

- [getTimestamp](mta://scripting/shared/functions/gettimestamp.md) » This function returns the UNIX timestamp of a specified date and time.

- [getServerAveragePing](mta://scripting/shared/functions/getserveraverageping.md) » This function gets average players ping.

- [gradientString](mta://scripting/shared/functions/gradientstring.md) » This function transforms a string in a new coloured gradient string.

- [hex2rgb](mta://scripting/shared/functions/hex2rgb.md) » This function convert hex to rgb.

- [hexColorToRGB](mta://scripting/shared/functions/hexcolortorgb.md) » This function convert hex string/number to RGBA values.

- [isLeapYear](mta://scripting/shared/functions/isleapyear.md) » This function returns a boolean representing if a given year is a leap year.

- [isValidMail](mta://scripting/shared/functions/isvalidmail.md) » This function checks whether a provided e-mail string is valid.

- [removeHex](mta://scripting/shared/functions/removehex.md) » This function is used to remove hexadecimal numbers (colors, for example) from strings.

- [RGBToHex](mta://scripting/shared/functions/rgbtohex.md) » This function returns a string representing the color in hexadecimal.

- [RGBToHSV](mta://scripting/shared/functions/rgbtohsv.md) » This function convert RGB to HSV color space.

- [RGBToDecimal](mta://scripting/shared/functions/rgbtodecimal.md) » This function convert RGB to Decimal color.

- [secondsToTimeDesc](mta://scripting/shared/functions/secondstotimedesc.md) » This function converts a plain seconds-integer into a user-friendly time description.

- [string.count](mta://scripting/shared/functions/string-count.md) » This function counts the amount of occurences of a string in a string.

- [string.explode](mta://scripting/shared/functions/string-explode.md) » This function splits a string at a given separator pattern and returns a table with the pieces.

- [string.insert](mta://scripting/shared/functions/string-insert.md) » This function inserts a string within another string at a given position.

- [splitMultiple](mta://scripting/shared/functions/splitmultiple.md) » This function improves the split function so that multiple characters can be used as the split at character.

- [switch](mta://scripting/shared/functions/switch.md) » This function allows the value of a variable or expression to control the flow of program execution via a multiway branch.

- [tocolor2rgba](mta://scripting/shared/functions/tocolor2rgba.md) » This function convert tocolor to rgba.

- [toHex](mta://scripting/shared/functions/tohex.md) » This function converts a decimal number to a hexadecimal number, as a fix to be used client-side.

- [var dump](mta://scripting/shared/functions/var-dump.md) » This function outputs information about one or more variables using outputConsole.

- [wavelengthToRGBA](mta://scripting/shared/functions/wavelengthtorgba.md) » This function converts a physical wavelength of light to a RGBA color.

- [fixPersianString](mta://scripting/shared/functions/fixpersianstring.md) » This function returns a fixed sorted bilingual RTL for strings consisting of Farsi/Arabic and English.

- [getColorName](mta://scripting/shared/functions/getcolorname.md) » This function retrieves the nearest color name for a given RGB value using an online API.

### GUI functions

- [centerWindow](mta://scripting/shared/functions/centerwindow.md) » This function centers a CEGUI window element responsively in any resolution.

- [isMouseOnGUICloseButton](mta://scripting/shared/functions/ismouseonguiclosebutton.md) » This function allows you to check whether the mouse cursor/pointer is within a gui-window's native close button.

- [isMouseOnGuiElement](mta://scripting/shared/functions/ismouseonguielement.md) » This function allows you to check whether or not your mouse is over a specific gui element, this is especially useful if the gui element has a parent.

- [guiMoveElement](mta://scripting/shared/functions/guimoveelement.md) » This function moves guiElement by/like using moveObject.

- [guiSetStaticImageMovable](mta://scripting/shared/functions/guisetstaticimagemovable.md) » This function allows you to move a static image like a gui window.

##### Comboboxes

- [guiComboBoxAdjustHeight](mta://scripting/shared/functions/guicomboboxadjustheight.md) » This function adjusts a CEGUI combobox element to have the correct height.

##### Gridlists

- [convertGridListToText](mta://scripting/shared/functions/convertgridlisttotext.md) » This function converts grid list contents to text.

- [getGridListRowIndexFromText](mta://scripting/shared/functions/getgridlistrowindexfromtext.md) » This function returns the GridList row index from the specified text.

- [guiGridListAddPlayers](mta://scripting/shared/functions/guigridlistaddplayers.md) » This function add all online players to a grid list.

- [isTextInGridList](mta://scripting/shared/functions/istextingridlist.md) » This function checks if some text exist or not in the GridList.

- [guiGridListGetColumnIDFromTitle](mta://scripting/shared/functions/guigridlistgetcolumnidfromtitle.md) » This function gets a gridlist's column ID from the column title.

- [guiGridListGetSelectedText](mta://scripting/shared/functions/guigridlistgetselectedtext.md) » This function returns a string containing the inner text of a selected gridlist item.

- [guiGridListSetColumnNonSortable](mta://scripting/shared/functions/guigridlistsetcolumnnonsortable.md) » This function makes a gridlist column become non-sortable.

##### Labels

- [guiLabelAddEffect](mta://scripting/shared/functions/guilabeladdeffect.md) » This function add an effects to the gui-label like (shadow, outline).

### Marker functions

- [createMarkerAttachedTo](mta://scripting/shared/functions/createmarkerattachedto.md) » This function creates a marker that is attached to an element.

### Math functions

- [reMap](mta://scripting/shared/functions/remap.md) » Re-maps a number from one range to another.

- [math.clamp](mta://scripting/shared/functions/math-clamp.md) » This function returns the number between range of numbers or it's minimum or maximum.

- [math.getBezierPoint](mta://scripting/shared/functions/math-getbezierpoint.md) » Get N-th order bezier point.

- [math.hypot](mta://scripting/shared/functions/math-hypot.md) » This function returns the Hypotenuse of the triangle given by sides x and y.

- [math.isPointInPolygon](mta://scripting/shared/functions/math-ispointinpolygon.md) » Check if point is inside polygon or not.

- [math.lerp](mta://scripting/shared/functions/math-lerp.md) » Get val between two integer.

- [math.percent](mta://scripting/shared/functions/math-percent.md) » This function returns a percentage from two number values.

- [math.polygonArea](mta://scripting/shared/functions/math-polygonarea.md) » Compute area of any polygon.

- [math.randomDiff](mta://scripting/shared/functions/math-randomdiff.md) » Generates a pseudo-random integer that's always different from the last random number generated.

- [math.rotVecToEulerAngle](mta://scripting/shared/functions/math-rotvectoeulerangle.md) » Rotation Vector To Euler Angle

- [math.round](mta://scripting/shared/functions/math-round.md) » Rounds a number whereas the number of decimals to keep and the method may be set.

- [mathNumber](mta://scripting/shared/functions/mathnumber.md) » This function is a workaround for the client-side floating-point precision of 24-bits.

- [math.percentProgress](mta://scripting/shared/functions/math-percentprogress.md) » Returns a percentage progress from two specific values.

- [math.average](mta://scripting/shared/functions/math-average.md) » This function returns the simple arithmetic mean of multiple numbers.

- [math.absin](mta://scripting/shared/functions/math-absin.md) » This function returns a formula representing the just positive half of a sine wave.

### Map functions

- [assignLod](mta://scripting/shared/functions/assignlod.md) » This function lets you conveniently generate and apply a LOD model to a mapping object.

- [getWorldPositionFromMapPosition](mta://scripting/shared/functions/getworldpositionfrommapposition.md) » This function converts an F11 map position to world position.

- [getClosestPoint](mta://scripting/shared/functions/getclosestpoint.md) » This function finds the closest point from a given element to a list of points in 2D space.

### Ped functions

- [getAlivePlayersInTeam](mta://scripting/shared/functions/getaliveplayersinteam.md) » This function returns a table of the alive players in a team.

- [getGuestPlayers](mta://scripting/shared/functions/getguestplayers.md) » This function gets a players not login or players Guest .

- [getOnlineAdmins](mta://scripting/shared/functions/getonlineadmins.md) » This function returns a table of all logged-in administrators.

- [getPedEyesPosition](mta://scripting/shared/functions/getpedeyesposition.md) » This function allows you to get peds eyes position.

- [getPedGender](mta://scripting/shared/functions/getpedgender.md) » This function allows you to get peds their gender.

- [getPedMaxHealth](mta://scripting/shared/functions/getpedmaxhealth.md) » This function returns a pedestrians's maximum health by converting it from their maximum health stat.

- [getPedMaxOxygenLevel](mta://scripting/shared/functions/getpedmaxoxygenlevel.md) » This function returns a ped's maximum oxygen level by converting it from their maximum underwater stamina stat.

- [getPedWeaponSkill](mta://scripting/shared/functions/getpedweaponskill.md) » This function returns a ped's corresponding weapon skill level name.

- [getPedHitBone](mta://scripting/shared/functions/getpedhitbone.md) » This function gets the approximate number of the bone where the ped is hit.

- [getPlayerFromNamePart](mta://scripting/shared/functions/getplayerfromnamepart.md) » This function returns a player from partial name.

- [getPlayerFromSerial](mta://scripting/shared/functions/getplayerfromserial.md) » This function returns a player from their serial.

- [getPlayersByData](mta://scripting/shared/functions/getplayersbydata.md) » This function returns a table of players that have the specified data name.

- [getPlayersInPhotograph](mta://scripting/shared/functions/getplayersinphotograph.md) » This function returns a table of all players in photograph.

- [getPlayersInVehicles](mta://scripting/shared/functions/getplayersinvehicles.md) » This function returns a table of the players insides vehicles from a specified dimension.

- [getPlayerNameFromID](mta://scripting/shared/functions/getplayernamefromid.md) » This function will get the player name from the ID element data.

- [isPedAiming](mta://scripting/shared/functions/ispedaiming.md)» This function checks if a pedestrian is aiming their weapon.

- [isPedAimingNearPed](mta://scripting/shared/functions/ispedaimingnearped.md) » This is similar to isPedAiming but uses a colshape to be more precise.

- [isPedDiving](mta://scripting/shared/functions/ispeddiving.md) » This feature checks that pedestrian is diving in the water.

- [isPedDrivingVehicle](mta://scripting/shared/functions/ispeddrivingvehicle.md) » This function checks if a specified pedestrian is driving a vehicle.

- [isPedNearbyWall](mta://scripting/shared/functions/ispednearbywall.md) » This function checks if player/ped is nearby a objects like buildings or walls.

- [isPlayerInTeam](mta://scripting/shared/functions/isplayerinteam.md) » This function checks if a player is in a specified team.

- [setPedAttack](mta://scripting/shared/functions/setpedattack.md) » This function will make a ped attack a specified target.

- [setPedFollow](mta://scripting/shared/functions/setpedfollow.md) » This function will make a ped follow a specified target.

- [isPedFalling](mta://scripting/shared/functions/ispedfalling.md) » This function checks if the player/ped is falling from a high place.

### Player functions

- [countPlayersInRange](mta://scripting/shared/functions/countplayersinrange.md) » This function returns the number of players that are within a certain range of the specified coordinates.

- [getPlayerPreviousAndNextWeapon](mta://scripting/shared/functions/getplayerpreviousandnextweapon.md) » This function returns the player previous and next weapon.

- [getPlayersInRange](mta://scripting/shared/functions/getplayersinrange.md) » This function make a table of players within certain range.

- [isPlayerActuallyInVehicle](mta://scripting/shared/functions/isplayeractuallyinvehicle.md) » This function checks if a player is actually in a vehicle instead of just in the process of entering.

- [isPlayerHitByVehicle](mta://reference/misc/isplayerhitbyvehicle.md) » This function cancels event when a element is hit by a vehicle.

- [toggleAllVehicleControls](mta://reference/misc/toggleallvehiclecontrols.md) » This function toggles all vehicle controls for a player on or off based on the provided boolean value.

- [isPlayerNameRandomized](mta://scripting/shared/functions/isplayernamerandomized.md) » This function Checks whether the given player name looks like an automatically-generated random nickname.

### Resource functions

- [getResourceScripts](mta://scripting/shared/functions/getresourcescripts.md) » This function returns a table of the resource scripts.

- [getResourceSettings](mta://scripting/shared/functions/getresourcesettings.md) » This function returns a table of the resource settings.

- [getResourceSize](mta://scripting/shared/functions/getresourcesize.md) » This function returns the size of a specified resource in kB(kilobyte)

- [refreshResource](mta://scripting/shared/functions/refreshresource.md) » This function refreshes your resource if you changed any of the files

- [setResourcePriority](mta://scripting/shared/functions/setresourcepriority.md) » This function set resource download priority group.

### Sound functions

- [isSoundFinished](mta://scripting/shared/functions/issoundfinished.md) » This function checks if a sound element has finished.

- [stopSoundSlowly](mta://scripting/shared/functions/stopsoundslowly.md) » This function stop your sound element slowly.

### Browser functions

- [playVideo](mta://scripting/shared/functions/playvideo.md) » This function plays a video on the screen.

### Team functions

- [getTeamFromColor](mta://scripting/shared/functions/getteamfromcolor.md) » This function returns a team element by the specified color.

- [getTeamWithFewestPlayers](mta://scripting/shared/functions/getteamwithfewestplayers.md) » This function returns a team element with least players of all the specified teams.

### Vehicle functions

- [findEmptyCarSeat](mta://scripting/shared/functions/findemptycarseat.md) » This function finds you the first empty seat in a vehicle.

- [getNearestVehicle](mta://scripting/shared/functions/getnearestvehicle.md) » This function gets the nearest vehicle to the specified player in a specified distance.

- [getRandomVehicle](mta://scripting/shared/functions/getrandomvehicle.md) » This function gets a random vehicle.

- [getValidVehicleModels](mta://scripting/shared/functions/getvalidvehiclemodels.md) » This function returns a table of all valid vehicle models.

- [getVehiclesCountByType](mta://scripting/shared/functions/getvehiclescountbytype.md) » This function returns the amount of vehicles by the given type as an integer value.

- [getVehicleTurnVelocityCenterOfMass](mta://scripting/shared/functions/getvehicleturnvelocitycenterofmass.md)» This function gets a vehicle's turn velocity relative to the vehicle's center or mass.

- [isVehicleDoubleExhaust](mta://scripting/shared/functions/isvehicledoubleexhaust.md) » This function checks is exhaust vehicle double.

- [isVehicleEmpty](mta://scripting/shared/functions/isvehicleempty.md) » This function checks whether a vehicle is empty.

- [isVehicleOccupied](mta://scripting/shared/functions/isvehicleoccupied.md) » This function checks if a specified vehicle is occupied.

- [isVehicleOnRoof](mta://scripting/shared/functions/isvehicleonroof.md) » This function checks whether vehicle is on roof.

- [isVehicleOnFire](mta://scripting/shared/functions/isvehicleonfire.md) » This function checks if the vehicle is on fire or not.

- [isVehicleReversing](mta://scripting/shared/functions/isvehiclereversing.md) » This function checks if a specified vehicle is moving backwards.

- [isVehicleUpgraded](mta://scripting/shared/functions/isvehicleupgraded.md) » This function checks is vehicle upgraded by upgrade ID.

- [setVehicleGravityPoint](mta://scripting/shared/functions/setvehiclegravitypoint.md) » This function sets a vehicle's gravity in the direction of a 3 dimensional coordinate with the strength specified.

- [setVehicleTurnVelocityCenterOfMass](mta://scripting/shared/functions/setvehicleturnvelocitycenterofmass.md) » This function sets a vehicle's turn velocity relative to the vehicle's center or mass.

- [setVehicleHandlingFromText](mta://scripting/shared/functions/setvehiclehandlingfromtext.md) » This function sets a vehicle's handling from text.

- [setVehicleWheelModel](mta://scripting/shared/functions/setvehiclewheelmodel.md) » This function changes the wheel model of the informed vehicle.

- [setVehicleDirtEnabled](mta://scripting/shared/functions/setvehicledirtenabled.md) » This function toggles a dirt removal shader effect on the specified vehicle.

### Weapon functions

- [getJetpackWeaponsEnabled](mta://scripting/shared/functions/getjetpackweaponsenabled.md) » This function returns a table of enabled weapons usable on a jetpack.

### Object functions

- [getDynamicDoorObjectOpenRatio](mta://scripting/shared/functions/getdynamicdoorobjectopenratio.md) » This function tells you how open a dynamic door is in a range from 0 to 1.

- [isElementObject](mta://scripting/shared/functions/iselementobject.md) » This function tells you if an element is an object or no.

### XML functions

- [getXMLNodes](mta://scripting/shared/functions/getxmlnodes.md) » This function returns all children of a XML node.

### Engine functions

- [engineGetCOLsFromLibrary](mta://scripting/shared/functions/enginegetcolsfromlibrary.md) » This function gets the collision data from the col library.

- [engineLoadIMGContainer](mta://scripting/shared/functions/engineloadimgcontainer.md) » This function loads the IMG container.

### Utility

- [animate](mta://scripting/shared/functions/animate.md) » This function allows you to use interpolateBetween without render event and easily used.

- [callClientFunction](mta://scripting/shared/functions/callclientfunction.md) » This function allows you to call any client-side function from the server's side.

- [callServerFunction](mta://scripting/shared/functions/callserverfunction.md) » This function allows you to call any server-side function from the client's side.

- [check](mta://scripting/shared/functions/check.md) » This function checks if its arguments are of the right type and calls the error-function if one is not.

- [checkPassiveTimer](mta://scripting/shared/functions/checkpassivetimer.md) » This function allows you to use passive timers in your conditions. For example you want to prevent players repeatedly using a command.

- [coroutine.resume](mta://scripting/shared/functions/coroutine-resume.md) » This function applies a fix for hidden coroutine error messages.

- [compact](mta://scripting/shared/functions/compact.md) » This function create table containing variables and their values.

- [createDirectory](mta://scripting/shared/functions/createdirectory.md) » This function creates a directory in the resource's file system.

- [getBanBySerial](mta://scripting/shared/functions/getbanbyserial.md) » This function returns the ban if the serial is banned.

- [getBanFromName](mta://scripting/shared/functions/getbanfromname.md) » This functions returns the ban of the given playername.

- [getCurrentFPS](mta://scripting/shared/functions/getcurrentfps.md) » This function returns the frames per second at which GTA: SA is running.

- getSkinNameFromID » This function returns the name of the skin from the given id.

- [IfElse](mta://scripting/shared/functions/ifelse.md) » This function returns one of two values based on a boolean expression.

- [isLastExecuteInTimer](mta://scripting/shared/functions/islastexecuteintimer.md) » This function check if the execute is the last execute in the timer.

- [isMouseInCircle](mta://scripting/shared/functions/ismouseincircle.md) » This function checks if a cursor position is in circular area or not.

- [isMouseInPosition](mta://scripting/shared/functions/ismouseinposition.md) » This function allows you to check whether the mouse cursor/pointer is within a rectangular position.

- [iterElements](mta://scripting/shared/functions/iterelements.md) » This function returns *a time-saving* iterator for your for-loops.

- [PlotTrajectoryAtTime](mta://scripting/shared/functions/plottrajectoryattime.md) » Calculate projectile/water trajectory.

- [preprocessor](mta://scripting/shared/functions/preprocessor.md) » This function allow you to use gcc macros.

- [vector3:compare](mta://scripting/shared/functions/vector3-compare.md) » This method checks whether two vectors match, with optional precision.

- [svgCreateRoundedRectangle](mta://scripting/shared/functions/svgcreateroundedrectangle.md) » This function creates a rectangle with rounded edges.

- [debounce](mta://scripting/shared/functions/debounce.md) » This function is removing unwanted input noise.

- [listAllFiles](mta://scripting/shared/functions/listallfiles.md) » This function lists all files and subdirectories within a given directory and its subdirectories.

- [dumpdelete](mta://scripting/shared/functions/dumpdelete.md) » This function recursively deletes elements inside a table, destroying elements like vehicles, peds, or killing timers.

- [isEventHandlerAdded](mta://scripting/shared/functions/iseventhandleradded.md) » This function checks whether a specific event handler has already been added to an element.

- [wait](mta://scripting/shared/functions/wait.md) » This function pauses the execution of a function for a specific amount of time. It allows you to write sequential, readable code instead of using complex callback structures or multiple timers.

### String functions

- [string.endsWith](mta://scripting/shared/functions/string-endswith.md) » This function checks if a string ends with other string.

- [string.startsWith](mta://scripting/shared/functions/string-startswith.md) » This function checks if a string starts with other string.

- [string.repetition](mta://scripting/shared/functions/string-repetition.md) » This function repeats a substring n times.
