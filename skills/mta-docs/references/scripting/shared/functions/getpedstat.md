---
doc_id: "mta-wiki:3980"
title: "GetPedStat"
source_title: "GetPedStat"
source_url: "https://wiki.multitheftauto.com/wiki/GetPedStat"
revision_id: 48767
language: "en"
categories: ["Server_functions", "Client_functions"]
---

# GetPedStat

This function returns the value of the specified statistic of a specific [ped](https://wiki.multitheftauto.com/index.php?search=ped).

## Syntax

```
float getPedStat ( ped thePed, int stat )
```

**OOP Syntax** [Help! I don't understand this!](mta://tutorials/oop-introduction.md)

**Method**: *[ped](https://wiki.multitheftauto.com/index.php?search=ped):getStat(...)*

### Required Arguments

- **thePed**: The [ped](https://wiki.multitheftauto.com/index.php?search=ped) whose stat you want to retrieve.

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

### Returns

Returns the value of the requested statistic.

## Example

Click to collapse [-]
Server

This example announces whether a player is fat upon spawn

```
function checkWeightOnSpawn ( )
    local stat = getPedStat ( source, 21 )
    -- Check that getPedStat returned a value
    if ( stat > 500 ) then
        -- Output the stat in the chat box
        outputChatBox ( getPlayerName ( source ) .. " needs to lose a bit of weight!" )
    end
end
addEventHandler ( "onPlayerSpawn", getRootElement(), checkWeightOnSpawn )
```

## See Also

- [addPedClothes](mta://scripting/shared/functions/addpedclothes.md)

- [getPedClothes](mta://scripting/shared/functions/getpedclothes.md)

- [removePedClothes](mta://scripting/shared/functions/removepedclothes.md)

- [createPed](mta://scripting/shared/functions/createped.md)

- [getPedAmmoInClip](mta://scripting/shared/functions/getpedammoinclip.md)

- [getPedArmor](mta://scripting/shared/functions/getpedarmor.md)

- [getPedFightingStyle](mta://scripting/shared/functions/getpedfightingstyle.md)

- [getPedOccupiedVehicle](mta://scripting/shared/functions/getpedoccupiedvehicle.md)

- [getPedOccupiedVehicleSeat](mta://scripting/shared/functions/getpedoccupiedvehicleseat.md)

- getPedStat

- [getPedTarget](mta://scripting/shared/functions/getpedtarget.md)

- [getPedTotalAmmo](mta://scripting/shared/functions/getpedtotalammo.md)

- [getPedWalkingStyle](mta://scripting/shared/functions/getpedwalkingstyle.md)

- [getPedWeapon](mta://scripting/shared/functions/getpedweapon.md)

- [getPedWeaponSlot](mta://scripting/shared/functions/getpedweaponslot.md)

- [getPedContactElement](mta://scripting/shared/functions/getpedcontactelement.md)

- [getValidPedModels](mta://scripting/shared/functions/getvalidpedmodels.md)

- [isPedChoking](mta://scripting/shared/functions/ispedchoking.md)

- [isPedDead](mta://scripting/shared/functions/ispeddead.md)

- [isPedDoingGangDriveby](mta://scripting/shared/functions/ispeddoinggangdriveby.md)

- [isPedDucked](mta://scripting/shared/functions/ispedducked.md)

- [isPedHeadless](mta://scripting/shared/functions/ispedheadless.md)

- [isPedInVehicle](mta://scripting/shared/functions/ispedinvehicle.md)

- [isPedOnGround](mta://scripting/shared/functions/ispedonground.md)

- [isPedReloadingWeapon](mta://scripting/shared/functions/ispedreloadingweapon.md)

- [isPedWearingJetpack](mta://scripting/shared/functions/ispedwearingjetpack.md)

- [killPed](mta://scripting/shared/functions/killped.md)

- [removePedFromVehicle](mta://scripting/shared/functions/removepedfromvehicle.md)

- [setPedAnimation](mta://scripting/shared/functions/setpedanimation.md)

- [setPedAnimationProgress](mta://scripting/shared/functions/setpedanimationprogress.md)

- [setPedAnimationSpeed](mta://scripting/shared/functions/setpedanimationspeed.md)

- [setPedArmor](mta://scripting/shared/functions/setpedarmor.md)

- [setPedDoingGangDriveby](mta://scripting/shared/functions/setpeddoinggangdriveby.md)

- [setPedFightingStyle](mta://scripting/shared/functions/setpedfightingstyle.md)

- [setPedHeadless](mta://scripting/shared/functions/setpedheadless.md)

- [setPedStat](mta://scripting/shared/functions/setpedstat.md)

- [setPedWalkingStyle](mta://scripting/shared/functions/setpedwalkingstyle.md)

- [setPedWeaponSlot](mta://scripting/shared/functions/setpedweaponslot.md)

- [warpPedIntoVehicle](mta://scripting/shared/functions/warppedintovehicle.md)
