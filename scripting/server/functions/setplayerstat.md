---
doc_id: "mta-wiki:1643"
title: "SetPlayerStat"
source_title: "SetPlayerStat"
source_url: "https://wiki.multitheftauto.com/wiki/SetPlayerStat"
revision_id: 44562
language: "en"
categories: ["Server_functions", "Deprecated"]
generated_at: "2026-07-26T16:16:44.066489+00:00"
---

# SetPlayerStat

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use setPedStat instead. |  |

This function allows you to set the float value of a specific statistic for a [player](mta://reference/misc/player.md). **Visual stats (FAT and BODY_MUSCLE) can only be used on the CJ skin.** A large number of the stats will have no effect.

## Syntax

```
bool setPlayerStat ( player thePlayer, int stat, float value )
```

### Required Arguments

- **thePlayer**: the [player](mta://reference/misc/player.md) whose statistic you want to modify.

- **stat**: A whole number determining the stat ID.

Floating Point

- **0:** PROGRESS_MADE

- **1:** TOTAL_PROGRESS

- **2:** LONGEST_BASKETBALL

**Distances:**

- **3:** DIST_FOOT

- **4:** DIST_CAR

- **5:** DIST_BIKE

- **6:** DIST_BOAT

- **7:** DIST_GOLF_CART

- **8:** DIST_HELICOPTER

- **9:** DIST_PLANE

- **10:** LONGEST_WHEELIE_DIST

- **11:** LONGEST_STOPPIE_DIST

- **12:** LONGEST_2WHEEL_DIST

**Cash:**

- **13:** WEAPON_BUDGET

- **14:** FASHION_BUDGET

- **15:** PROPERTY_BUDGET

- **16:** SPRAYING_BUDGET

**Times:**

- **17:** LONGEST_WHEELIE_TIME

- **18:** LONGEST_STOPPIE_TIME

- **19:** LONGEST_2WHEEL_TIME

- **20:** FOOD_BUDGET

**Body:**

- **21:** FAT

- **22:** STAMINA

- **23:** BODY_MUSCLE

- **24:** MAX_HEALTH

- **25:** SEX_APPEAL

- **26:** DIST_SWIMMING

- **27:** DIST_CYCLE

- **28:** DIST_TREADMILL

- **29:** DIST_EXCERSISE_BIKE

- **30:** TATTOO_BUDGET

- **31:** HAIRDRESSING_BUDGET

- **33:** PROSTITUTE_BUDGET

**Gambling:**

- **35:** MONEY_SPENT_GAMBLING

- **36:** MONEY_MADE_PIMPING

- **37:** MONEY_WON_GAMBLING

- **38:** BIGGEST_GAMBLING_WIN

- **39:** BIGGEST_GAMBLING_LOSS

- **40:** LARGEST_BURGLARY_SWAG

- **41:** MONEY_MADE_BURGLARY

- **44:** LONGEST_TREADMILL_TIME

- **45:** LONGEST_EXCERSISE_BIKE_TIME

- **46:** HEAVIEST_WEIGHT_BENCH_PRESS

- **47:** HEAVIEST_WEIGHT_DUMBELLS

- **48:** BEST_TIME_HOTRING

- **49:** BEST_TIME_BMX

- **51:** LONGEST_CHASE_TIME

- **52:** LAST_CHASE_TIME

- **53:** WAGE_BILL

- **54:** STRIP_CLUB_BUDGET

- **55:** CAR_MOD_BUDGET

- **56:** TIME_SPENT_SHOPPING

- **62:** TOTAL_SHOPPING_BUDGET

- **63:** TIME_SPENT_UNDERWATER

**Respect:**

- **64:** RESPECT_TOTAL

- **65:** RESPECT_GIRLFRIEND

- **66:** RESPECT_CLOTHES

- **67:** RESPECT_FITNESS

- **68:** RESPECT

**Weapon skills:**  

*Note: see [Weapon skill levels](mta://reference/misc/weapon-skill-levels.md) for the values that advance weapon skills.*

- **69:** WEAPONTYPE_PISTOL_SKILL

- **70:** WEAPONTYPE_PISTOL_SILENCED_SKILL

- **71:** WEAPONTYPE_DESERT_EAGLE_SKILL

- **72:** WEAPONTYPE_SHOTGUN_SKILL

- **73:** WEAPONTYPE_SAWNOFF_SHOTGUN_SKILL

- **74:** WEAPONTYPE_SPAS12_SHOTGUN_SKILL

- **75:** WEAPONTYPE_MICRO_UZI_SKILL

- **76:** WEAPONTYPE_MP5_SKILL

- **77:** WEAPONTYPE_AK47_SKILL

- **78:** WEAPONTYPE_M4_SKILL

- **79:** WEAPONTYPE_SNIPERRIFLE_SKILL

- **80:** SEX_APPEAL_CLOTHES

- **81:** GAMBLING

Integer

- **120:** PEOPLE_KILLED_BY_OTHERS

- **121:** PEOPLE_KILLED_BY_PLAYER

- **122:** CARS_DESTROYED

- **123:** BOATS_DESTROYED

- **124:** HELICOPTORS_DESTROYED

- **125:** PROPERTY_DESTROYED

- **126:** ROUNDS_FIRED

- **127:** EXPLOSIVES_USED

- **128:** BULLETS_HIT

- **129:** TYRES_POPPED

- **130:** HEADS_POPPED

- **131:** WANTED_STARS_ATTAINED

- **132:** WANTED_STARS_EVADED

- **133:** TIMES_ARRESTED

- **134:** DAYS_PASSED

- **135:** TIMES_DIED

- **136:** TIMES_SAVED

- **137:** TIMES_CHEATED

- **138:** SPRAYINGS

- **139:** MAX_JUMP_DISTANCE

- **140:** MAX_JUMP_HEIGHT

- **141:** MAX_JUMP_FLIPS

- **142:** MAX_JUMP_SPINS

- **143:** BEST_STUNT

- **144:** UNIQUE_JUMPS_FOUND

- **145:** UNIQUE_JUMPS_DONE

- **146:** MISSIONS_ATTEMPTED

- **147:** MISSIONS_PASSED

- **148:** TOTAL_MISSIONS

- **149:** TAXI_MONEY_MADE

- **150:** PASSENGERS_DELIVERED_IN_TAXI

- **151:** LIVES_SAVED

- **152:** CRIMINALS_CAUGHT

- **153:** FIRES_EXTINGUISHED

- **154:** PIZZAS_DELIVERED

- **155:** ASSASSINATIONS

- **156:** LATEST_DANCE_SCORE

- **157:** VIGILANTE_LEVEL

- **158:** AMBULANCE_LEVEL

- **159:** FIREFIGHTER_LEVEL

- **160:** DRIVING_SKILL

- **161:** TRUCK_MISSIONS_PASSED

- **162:** TRUCK_MONEY_MADE

- **163:** RECRUITED_GANG_MEMBERS_KILLED

- **164:** ARMOUR

- **165:** ENERGY

- **166:** PHOTOS_TAKEN

- **167:** KILL_FRENZIES_ATTEMPTED

- **168:** KILL_FRENZIES_PASSED

- **169:** FLIGHT_TIME

- **170:** TIMES_DROWNED

- **171:** NUM_GIRLS_PIMPED

- **172:** BEST_POSITION_HOTRING

- **173:** FLIGHT_TIME_JETPACK

- **174:** SHOOTING_RANGE_SCORE

- **175:** VALET_CARS_PARKED

- **176:** KILLS_SINCE_LAST_CHECKPOINT

- **177:** TOTAL_LEGITIMATE_KILLS

- **178:** BLOODRING_KILLS

- **179:** BLOODRING_TIME

- **180:** NO_MORE_HURRICANES

- **181:** CITIES_PASSED

- **182:** POLICE_BRIBES

- **183:** CARS_STOLEN

- **184:** CURRENT_GIRLFRIENDS

- **185:** BAD_DATES

- **186:** GIRLS_DATED

- **187:** TIMES_SCORED_WITH_GIRL

- **188:** DATES

- **189:** GIRLS_DUMPED

- **190:** TIMES_VISITED_PROSTITUTE

- **191:** HOUSES_BURGLED

- **192:** SAFES_CRACKED

- **194:** STOLEN_ITEMS_SOLD

- **195:** EIGHT_BALLS_IN_POOL

- **196:** WINS_IN_POOL

- **197:** LOSSES_IN_POOL

- **198:** VISITS_TO_GYM

- **200:** MEALS_EATEN

- **225:** UNDERWATER_STAMINA

- **229:** BIKE_SKILL

- **230:** CYCLE_SKILL

- **value**: A float number the stat will be set to. (0..999)

### Returns

Returns *true* if the statistic was changed succesfully. Returns *false* if an invalid player is specified, if the stat-id/value is out of acceptable range or if the FAT or BODY_MUSCLE stats are used on non-CJ players.

## Example

This example allows a player to type the command 'beefcake' to change his player's BODY_MUSCLE stat (#23) to the maximum value of 999. This will result in him looking really muscular.

```
function changeBodyStrength ( player, commandName )
    --Output whether the setPlayerStat was successful in changing the BODY_MUSCLE STAT     
    if ( setPlayerStat ( player, 23, 999 ) ) then
    	outputChatBox ( "Your player looks really muscular" )
    else
        outputChatBox ( "Failed to make your player look muscular." )
    end
end
addCommandHandler ( "beefcake", changeBodyStrength )
```

## See Also

- [getPlayerTeam](mta://scripting/shared/functions/getplayerteam.md)

- [getPlayerBlurLevel](mta://scripting/shared/functions/getplayerblurlevel.md)

- [setPlayerBlurLevel](mta://scripting/shared/functions/setplayerblurlevel.md)

- [getPlayerSerial](mta://scripting/shared/functions/getplayerserial.md)

- [forcePlayerMap](mta://scripting/shared/functions/forceplayermap.md)

- [getPlayerScriptDebugLevel](mta://scripting/shared/functions/getplayerscriptdebuglevel.md)

- [getPlayerFromName](mta://scripting/shared/functions/getplayerfromname.md)

- [getPlayerMoney](mta://scripting/shared/functions/getplayermoney.md)

- [getPlayerName](mta://scripting/shared/functions/getplayername.md)

- [getPlayerNametagColor](mta://scripting/shared/functions/getplayernametagcolor.md)

- [getPlayerNametagText](mta://scripting/shared/functions/getplayernametagtext.md)

- [getPlayerPing](mta://scripting/shared/functions/getplayerping.md)

- [getPlayerWantedLevel](mta://scripting/shared/functions/getplayerwantedlevel.md)

- [givePlayerMoney](mta://scripting/shared/functions/giveplayermoney.md)

- [isPlayerMapForced](mta://scripting/shared/functions/isplayermapforced.md)

- [isPlayerNametagShowing](mta://scripting/shared/functions/isplayernametagshowing.md)

- [setPlayerHudComponentVisible](mta://scripting/shared/functions/setplayerhudcomponentvisible.md)

- [setPlayerMoney](mta://scripting/shared/functions/setplayermoney.md)

- [setPlayerNametagColor](mta://scripting/shared/functions/setplayernametagcolor.md)

- [setPlayerNametagShowing](mta://scripting/shared/functions/setplayernametagshowing.md)

- [setPlayerNametagText](mta://scripting/shared/functions/setplayernametagtext.md)

- [takePlayerMoney](mta://scripting/shared/functions/takeplayermoney.md)

- [countPlayersInTeam](mta://scripting/shared/functions/countplayersinteam.md)

- [getPlayersInTeam](mta://scripting/shared/functions/getplayersinteam.md)

- [isVoiceEnabled](mta://scripting/shared/functions/isvoiceenabled.md)

- [setControlState](mta://scripting/shared/functions/setcontrolstate.md)

- [getControlState](mta://scripting/shared/functions/getcontrolstate.md)
