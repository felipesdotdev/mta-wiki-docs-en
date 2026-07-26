---
doc_id: "mta-wiki:12160"
title: "IDs de veiculos"
source_title: "IDs de veiculos"
source_url: "https://wiki.multitheftauto.com/wiki/IDs_de_veiculos"
revision_id: 65672
language: "en"
categories: ["ID_Lists"]
generated_at: "2026-07-26T16:07:14.166590+00:00"
---

# IDs de veiculos

Introdução

Esta é uma lista de ID's de veículos do GTA:SA, conforme listado no arquivo vehicles.ide. Esses números de identificação do veículo são usados para várias funções de script do veículo.

#### Tabela Lua de todos os IDs de veículo válidos listados nesta página

```
vehicleIds = {400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415,
	416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433,
	434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451,
	452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469,
	470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487,
	488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505,
	506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523,
	524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541,
	542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559,
	560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577,
	578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595,
	596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611
}
```

#### Tabela Lua de todos os nomes de veículos

```
-- (when indexing just do a <vehicle model id you want the name of> - 399 to get the name)
vehicleNames = {"Landstalker", "Bravura", "Buffalo", "Linerunner", "Perennial", "Sentinel", "Dumper", "Fire Truck", "Trashmaster", "Stretch", "Manana", 
                       "Infernus", "Voodoo", "Pony", "Mule", "Cheetah", "Ambulance", "Leviathan", "Moonbeam", "Esperanto", "Taxi", "Washington", "Bobcat", 
                       "Mr. Whoopee", "BF Injection", "Hunter", "Premier", "Enforcer", "Securicar", "Banshee", "Predator", "Bus", "Rhino", "Barracks", "Hotknife", 
                       "Trailer 1", "Previon", "Coach", "Cabbie", "Stallion", "Rumpo", "RC Bandit", "Romero", "Packer", "Monster", "Admiral", "Squalo", 
                       "Seasparrow", "Pizzaboy", "Tram", "Trailer 2", "Turismo", "Speeder", "Reefer", "Tropic", "Flatbed", "Yankee", "Caddy", "Solair", 
                       "Berkley's RC Van", "Skimmer", "PCJ-600", "Faggio", "Freeway", "RC Baron", "RC Raider", "Glendale", "Oceanic", "Sanchez", "Sparrow", "Patriot", 
                       "Quadbike", "Coastguard", "Dinghy", "Hermes", "Sabre", "Rustler", "ZR-350", "Walton", "Regina", "Comet", "BMX", "Burrito", "Camper", "Marquis", 
                       "Baggage", "Dozer", "Maverick", "News Chopper", "Rancher", "FBI Rancher", "Virgo", "Greenwood", "Jetmax", "Hotring Racer", "Sandking", 
                       "Blista Compact", "Police Maverick", "Boxville", "Benson", "Mesa", "RC Goblin", "Hotring Racer 3", "Hotring Racer 2", "Bloodring Banger", 
                       "Rancher Lure", "Super GT", "Elegant", "Journey", "Bike", "Mountain Bike", "Beagle", "Cropduster", "Stuntplane", "Tanker", "Roadtrain", "Nebula", 
                       "Majestic", "Buccaneer", "Shamal", "Hydra", "FCR-900", "NRG-500", "HPV1000", "Cement Truck", "Towtruck", "Fortune", "Cadrona", "FBI Truck", 
                       "Willard", "Forklift", "Tractor", "Combine Harvester", "Feltzer", "Remington", "Slamvan", "Blade", "Freight", "Streak", "Vortex", "Vincent", 
                       "Bullet", "Clover", "Sadler", "Fire Truck Ladder", "Hustler", "Intruder", "Primo", "Cargobob", "Tampa", "Sunrise", "Merit", "Utility Van", 
                       "Nevada", "Yosemite", "Windsor", "Monster 2", "Monster 3", "Uranus", "Jester", "Sultan", "Stratum", "Elegy", "Raindance", "RC Tiger", "Flash", 
                       "Tahoma", "Savanna", "Bandito", "Freight Train Flatbed", "Streak Train Trailer", "Kart", "Mower", "Dune", "Sweeper", "Broadway", "Tornado", 
                       "AT-400", "DFT-30", "Huntley", "Stafford", "BF-400", "Newsvan", "Tug", "Trailer (Tanker Commando)", "Emperor", "Wayfarer", "Euros", "Hotdog", 
                       "Club", "Box Freight", "Trailer 3", "Andromada", "Dodo", "RC Cam", "Launch", "Police LS", "Police", "Police SF", "Police LV", "Police Ranger", 
                       "Ranger", "Picador", "S.W.A.T.", "Alpha", "Phoenix", "Glendale Damaged", "Sadler", "Sadler Damaged", "Baggage Trailer (covered)", 
                       "Baggage Trailer (Uncovered)", "Trailer (Stairs)", "Boxville Mission", "Farm Trailer", "Street Clean Trailer"
}
```

#### Tabela Lua de veículos que não podem ser trancados

```
nonLockableVehicles = {
    594, 606, 607, 611, 584, 608, 435, 450, 591, 539, 441, 464, 501, 465, 564, 472, 473, 493, 595, 484, 430, 453, 452, 446, 454, 581, 509, 481,
    462, 521, 463, 510, 522, 461, 448, 468, 586, 425, 520
}
```

#### Tabela Lua de veículos sem placas

```
noNumberPlates = {
    592, 553, 577, 488, 511, 497, 548, 563, 512, 476, 593, 447, 425, 519, 520, 460, 417, 469, 487, 513, 509, 481, 510, 472, 473, 493, 595, 484,
    430, 453, 452, 446, 454
}
```

#### Tabela Lua de veículos que suportam até três cores diferentes

```
maxColorVehicles = {
    483, 524, 446
}
```

## Aeronaves

| Aviões Name ID Image Andromada 592 AT-400 577 Beagle 511 Cropduster 512 Dodo 593 Hydra 520 Nevada 553 Rustler 476 Shamal 519 Skimmer 460 Stuntplane 513 | Helicópteros Name ID Image Cargobob 548 Hunter 425 Leviathan 417 Maverick 487 News Chopper 488 Police Maverick 497 Raindance 563 Seasparrow 447 Sparrow 469 |  |
| --- | --- | --- |
| Name | ID | Image |
| Andromada | 592 |  |
| AT-400 | 577 |  |
| Beagle | 511 |  |
| Cropduster | 512 |  |
| Dodo | 593 |  |
| Hydra | 520 |  |
| Nevada | 553 |  |
| Rustler | 476 |  |
| Shamal | 519 |  |
| Skimmer | 460 |  |
| Stuntplane | 513 |  |
| Name | ID | Image |
| Cargobob | 548 |  |
| Hunter | 425 |  |
| Leviathan | 417 |  |
| Maverick | 487 |  |
| News Chopper | 488 |  |
| Police Maverick | 497 |  |
| Raindance | 563 |  |
| Seasparrow | 447 |  |
| Sparrow | 469 |  |

## Barcos

| Name | ID | Image |
| --- | --- | --- |
| Coastguard | 472 |  |
| Dinghy | 473 |  |
| Jetmax | 493 |  |
| Launch | 595 |  |
| Marquis | 484 |  |
| Predator | 430 |  |
| Reefer | 453 |  |
| Speeder | 452 |  |
| Squalo | 446 |  |
| Tropic | 454 |  |

## Veículos terrestres

| Bicicletas Name ID Image BF-400 581 Bike 509 BMX 481 Faggio 462 FCR-900 521 Freeway 463 Mountain Bike 510 NRG-500 522 PCJ-600 461 Pizzaboy 448 Sanchez 468 Wayfarer 586 | Carros de 2 portas e compactados Name ID Image Alpha 602 Blista Compact 496 Bravura 401 Buccaneer 518 Cadrona 527 Club 589 Esperanto 419 Euros 587 Feltzer 533 Fortune 526 Hermes 474 Hustler 545 Majestic 517 Manana 410 Picador 600 Previon 436 Stallion 439 Tampa 549 Virgo 491 | Carros de 4 portas e luxuosos Name ID Image Admiral 445 Damaged Glendale 604 Elegant 507 Emperor 585 Glendale 466 Greenwood 492 Intruder 546 Merit 551 Nebula 516 Oceanic 467 Premier 426 Primo 547 Sentinel 405 Stafford 580 Stretch 409 Sunrise 550 Tahoma 566 Vincent 540 Washington 421 Willard 529 |
| --- | --- | --- |
| Name | ID | Image |
| BF-400 | 581 |  |
| Bike | 509 |  |
| BMX | 481 |  |
| Faggio | 462 |  |
| FCR-900 | 521 |  |
| Freeway | 463 |  |
| Mountain Bike | 510 |  |
| NRG-500 | 522 |  |
| PCJ-600 | 461 |  |
| Pizzaboy | 448 |  |
| Sanchez | 468 |  |
| Wayfarer | 586 |  |
| Name | ID | Image |
| Alpha | 602 |  |
| Blista Compact | 496 |  |
| Bravura | 401 |  |
| Buccaneer | 518 |  |
| Cadrona | 527 |  |
| Club | 589 |  |
| Esperanto | 419 |  |
| Euros | 587 |  |
| Feltzer | 533 |  |
| Fortune | 526 |  |
| Hermes | 474 |  |
| Hustler | 545 |  |
| Majestic | 517 |  |
| Manana | 410 |  |
| Picador | 600 |  |
| Previon | 436 |  |
| Stallion | 439 |  |
| Tampa | 549 |  |
| Virgo | 491 |  |
| Name | ID | Image |
| Admiral | 445 |  |
| Damaged Glendale | 604 |  |
| Elegant | 507 |  |
| Emperor | 585 |  |
| Glendale | 466 |  |
| Greenwood | 492 |  |
| Intruder | 546 |  |
| Merit | 551 |  |
| Nebula | 516 |  |
| Oceanic | 467 |  |
| Premier | 426 |  |
| Primo | 547 |  |
| Sentinel | 405 |  |
| Stafford | 580 |  |
| Stretch | 409 |  |
| Sunrise | 550 |  |
| Tahoma | 566 |  |
| Vincent | 540 |  |
| Washington | 421 |  |
| Willard | 529 |  |

| Serviço civil Name ID Image Baggage 485 Bus 431 Cabbie 438 Coach 437 Sweeper 574 Taxi 420 Towtruck 525 Trashmaster 408 Utility Van 552 | Veículos governamentais Name ID Image Ambulance 416 Barracks 433 Enforcer 427 FBI Rancher 490 FBI Truck 528 Fire Truck 407 Fire Truck 544 HPV1000 523 Patriot 470 Police LS 596 Police LV 598 Police Ranger 599 Police SF 597 Rhino 432 S.W.A.T. 601 Securicar 428 | Caminhões pesados e utilitários Name ID Image Benson 499 Boxville Mission 609 Boxville 498 Cement Truck 524 Combine Harvester 532 DFT-30 578 Dozer 486 Dumper 406 Dune 573 Flatbed 455 Hotdog 588 Linerunner 403 Mr. Whoopee 423 Mule 414 Packer 443 Roadtrain 515 Tanker 514 Tractor 531 Yankee 456 | Caminhões leves e vans Name ID Image Berkley's RC Van 459 Bobcat 422 Burrito 482 Damaged Sadler 605 Forklift 530 Moonbeam 418 Mower 572 News Van 582 Pony 413 Rumpo 440 Sadler 543 Tug 583 Walton 478 Yosemite 554 | SUVs e Vagões Name ID Image Huntley 579 Landstalker 400 Perennial 404 Rancher 489 Rancher 505 Regina 479 Romero 442 Solair 458 |
| --- | --- | --- | --- | --- |
| Name | ID | Image |  |  |
| Baggage | 485 |  |  |  |
| Bus | 431 |  |  |  |
| Cabbie | 438 |  |  |  |
| Coach | 437 |  |  |  |
| Sweeper | 574 |  |  |  |
| Taxi | 420 |  |  |  |
| Towtruck | 525 |  |  |  |
| Trashmaster | 408 |  |  |  |
| Utility Van | 552 |  |  |  |
| Name | ID | Image |  |  |
| Ambulance | 416 |  |  |  |
| Barracks | 433 |  |  |  |
| Enforcer | 427 |  |  |  |
| FBI Rancher | 490 |  |  |  |
| FBI Truck | 528 |  |  |  |
| Fire Truck | 407 |  |  |  |
| Fire Truck | 544 |  |  |  |
| HPV1000 | 523 |  |  |  |
| Patriot | 470 |  |  |  |
| Police LS | 596 |  |  |  |
| Police LV | 598 |  |  |  |
| Police Ranger | 599 |  |  |  |
| Police SF | 597 |  |  |  |
| Rhino | 432 |  |  |  |
| S.W.A.T. | 601 |  |  |  |
| Securicar | 428 |  |  |  |
| Name | ID | Image |  |  |
| Benson | 499 |  |  |  |
| Boxville Mission | 609 |  |  |  |
| Boxville | 498 |  |  |  |
| Cement Truck | 524 |  |  |  |
| Combine Harvester | 532 |  |  |  |
| DFT-30 | 578 |  |  |  |
| Dozer | 486 |  |  |  |
| Dumper | 406 |  |  |  |
| Dune | 573 |  |  |  |
| Flatbed | 455 |  |  |  |
| Hotdog | 588 |  |  |  |
| Linerunner | 403 |  |  |  |
| Mr. Whoopee | 423 |  |  |  |
| Mule | 414 |  |  |  |
| Packer | 443 |  |  |  |
| Roadtrain | 515 |  |  |  |
| Tanker | 514 |  |  |  |
| Tractor | 531 |  |  |  |
| Yankee | 456 |  |  |  |
| Name | ID | Image |  |  |
| Berkley's RC Van | 459 |  |  |  |
| Bobcat | 422 |  |  |  |
| Burrito | 482 |  |  |  |
| Damaged Sadler | 605 |  |  |  |
| Forklift | 530 |  |  |  |
| Moonbeam | 418 |  |  |  |
| Mower | 572 |  |  |  |
| News Van | 582 |  |  |  |
| Pony | 413 |  |  |  |
| Rumpo | 440 |  |  |  |
| Sadler | 543 |  |  |  |
| Tug | 583 |  |  |  |
| Walton | 478 |  |  |  |
| Yosemite | 554 |  |  |  |
| Name | ID | Image |  |  |
| Huntley | 579 |  |  |  |
| Landstalker | 400 |  |  |  |
| Perennial | 404 |  |  |  |
| Rancher | 489 |  |  |  |
| Rancher | 505 |  |  |  |
| Regina | 479 |  |  |  |
| Romero | 442 |  |  |  |
| Solair | 458 |  |  |  |

| Lowriders Name ID Image Blade 536 Broadway 575 Remington 534 Savanna 567 Slamvan 535 Tornado 576 Voodoo 412 | Muscle cars Name ID Image Buffalo 402 Clover 542 Phoenix 603 Sabre 475 | Street racers Name ID Image Banshee 429 Bullet 541 Cheetah 415 Comet 480 Elegy 562 Flash 565 Hotknife 434 Hotring Racer 494 Hotring Racer 2 502 Hotring Racer 3 503 Infernus 411 Jester 559 Stratum 561 Sultan 560 Super GT 506 Turismo 451 Uranus 558 Windsor 555 ZR-350 477 |
| --- | --- | --- |
| Name | ID | Image |
| Blade | 536 |  |
| Broadway | 575 |  |
| Remington | 534 |  |
| Savanna | 567 |  |
| Slamvan | 535 |  |
| Tornado | 576 |  |
| Voodoo | 412 |  |
| Name | ID | Image |
| Buffalo | 402 |  |
| Clover | 542 |  |
| Phoenix | 603 |  |
| Sabre | 475 |  |
| Name | ID | Image |
| Banshee | 429 |  |
| Bullet | 541 |  |
| Cheetah | 415 |  |
| Comet | 480 |  |
| Elegy | 562 |  |
| Flash | 565 |  |
| Hotknife | 434 |  |
| Hotring Racer | 494 |  |
| Hotring Racer 2 | 502 |  |
| Hotring Racer 3 | 503 |  |
| Infernus | 411 |  |
| Jester | 559 |  |
| Stratum | 561 |  |
| Sultan | 560 |  |
| Super GT | 506 |  |
| Turismo | 451 |  |
| Uranus | 558 |  |
| Windsor | 555 |  |
| ZR-350 | 477 |  |

| RC Vehicles Name ID Image RC Bandit 441 RC Baron 464 RC Cam 594 RC Goblin 501 RC Raider 465 RC Tiger 564 | Trailers Name ID Image Baggage Trailer 606 Baggage Trailer 607 Farm Trailer 610 Petrol trailer 584 Trailer 611 Trailer 608 Trailer 1 435 Trailer 2 450 Trailer 3 591 | Trens e vagões Name ID Image Box Freight 590 Brown Streak 538 Brown Streak Carriage 570 Flat Freight 569 Freight 537 Tram 449 |
| --- | --- | --- |
| Name | ID | Image |
| RC Bandit | 441 |  |
| RC Baron | 464 |  |
| RC Cam | 594 |  |
| RC Goblin | 501 |  |
| RC Raider | 465 |  |
| RC Tiger | 564 |  |
| Name | ID | Image |
| Baggage Trailer | 606 |  |
| Baggage Trailer | 607 |  |
| Farm Trailer | 610 |  |
| Petrol trailer | 584 |  |
| Trailer | 611 |  |
| Trailer | 608 |  |
| Trailer 1 | 435 |  |
| Trailer 2 | 450 |  |
| Trailer 3 | 591 |  |
| Name | ID | Image |
| Box Freight | 590 |  |
| Brown Streak | 538 |  |
| Brown Streak Carriage | 570 |  |
| Flat Freight | 569 |  |
| Freight | 537 |  |
| Tram | 449 |  |

## Recreativos

| Name | ID | Image |
| --- | --- | --- |
| Bandito | 568 |  |
| BF Injection | 424 |  |
| Bloodring Banger | 504 |  |
| Caddy | 457 |  |
| Camper | 483 |  |
| Journey | 508 |  |
| Kart | 571 |  |
| Mesa | 500 |  |
| Monster | 444 |  |
| Monster 2 | 556 |  |
| Monster 3 | 557 |  |
| Quadbike | 471 |  |
| Sandking | 495 |  |
| Vortex | 539 |  |

## Funções de veículo

- [addVehicleUpgrade](mta://scripting/shared/functions/addvehicleupgrade.md)

- [addVehicleSirens](mta://scripting/shared/functions/addvehiclesirens.md)

- [attachTrailerToVehicle](mta://scripting/shared/functions/attachtrailertovehicle.md)

- [blowVehicle](mta://scripting/shared/functions/blowvehicle.md)

- [createVehicle](mta://scripting/shared/functions/createvehicle.md)

- [detachTrailerFromVehicle](mta://scripting/shared/functions/detachtrailerfromvehicle.md)

- [fixVehicle](mta://scripting/shared/functions/fixvehicle.md)

- [getOriginalHandling](mta://scripting/shared/functions/getoriginalhandling.md)

- [getTrainDirection](mta://scripting/shared/functions/gettraindirection.md)

- [getTrainPosition](mta://scripting/shared/functions/gettrainposition.md)

- [getTrainSpeed](mta://scripting/shared/functions/gettrainspeed.md)

- [getVehicleColor](mta://scripting/shared/functions/getvehiclecolor.md)

- [getVehicleCompatibleUpgrades](mta://scripting/shared/functions/getvehiclecompatibleupgrades.md)

- [getVehicleController](mta://scripting/shared/functions/getvehiclecontroller.md)

- [getVehicleDoorOpenRatio](mta://scripting/shared/functions/getvehicledooropenratio.md)

- [getVehicleDoorState](mta://scripting/shared/functions/getvehicledoorstate.md)

- [getVehicleEngineState](mta://scripting/shared/functions/getvehicleenginestate.md)

- [getVehicleHandling](mta://scripting/shared/functions/getvehiclehandling.md)

- [getVehicleHeadLightColor](mta://scripting/shared/functions/getvehicleheadlightcolor.md)

- [getVehicleLandingGearDown](mta://scripting/shared/functions/getvehiclelandinggeardown.md)

- [getVehicleLightState](mta://scripting/shared/functions/getvehiclelightstate.md)

- [getVehicleMaxPassengers](mta://scripting/shared/functions/getvehiclemaxpassengers.md)

- [getVehicleModelFromName](mta://scripting/shared/functions/getvehiclemodelfromname.md)

- [getVehicleName](mta://scripting/shared/functions/getvehiclename.md)

- [getVehicleNameFromModel](mta://scripting/shared/functions/getvehiclenamefrommodel.md)

- [setVehicleNitroActivated](mta://scripting/shared/functions/setvehiclenitroactivated.md)

- [getVehicleOccupant](mta://scripting/shared/functions/getvehicleoccupant.md)

- [getVehicleOccupants](mta://scripting/shared/functions/getvehicleoccupants.md)

- [getVehicleOverrideLights](mta://scripting/shared/functions/getvehicleoverridelights.md)

- [getVehiclePaintjob](mta://scripting/shared/functions/getvehiclepaintjob.md)

- [getVehiclePanelState](mta://scripting/shared/functions/getvehiclepanelstate.md)

- [getVehiclePlateText](mta://scripting/shared/functions/getvehicleplatetext.md)

- [getVehicleSirenParams](mta://scripting/shared/functions/getvehiclesirenparams.md)

- [getVehicleSirens](mta://scripting/shared/functions/getvehiclesirens.md)

- [getVehicleSirensOn](mta://scripting/shared/functions/getvehiclesirenson.md)

- [getVehicleTowedByVehicle](mta://scripting/shared/functions/getvehicletowedbyvehicle.md)

- [getVehicleTowingVehicle](mta://scripting/shared/functions/getvehicletowingvehicle.md)

- [getVehicleTurretPosition](mta://scripting/shared/functions/getvehicleturretposition.md)

- [getVehicleType](mta://scripting/shared/functions/getvehicletype.md)

- [getVehicleUpgradeOnSlot](mta://scripting/shared/functions/getvehicleupgradeonslot.md)

- [getVehicleUpgradeSlotName](mta://scripting/shared/functions/getvehicleupgradeslotname.md)

- [getVehicleUpgrades](mta://scripting/shared/functions/getvehicleupgrades.md)

- [getVehicleVariant](mta://scripting/shared/functions/getvehiclevariant.md)

- [getVehicleWheelStates](mta://scripting/shared/functions/getvehiclewheelstates.md)

- [isTrainDerailable](mta://scripting/shared/functions/istrainderailable.md)

- [isTrainDerailed](mta://scripting/shared/functions/istrainderailed.md)

- [isVehicleBlown](mta://scripting/shared/functions/isvehicleblown.md)

- [isVehicleDamageProof](mta://scripting/shared/functions/isvehicledamageproof.md)

- [isVehicleFuelTankExplodable](mta://scripting/shared/functions/isvehiclefueltankexplodable.md)

- [isVehicleLocked](mta://scripting/shared/functions/isvehiclelocked.md)

- [isVehicleOnGround](mta://scripting/shared/functions/isvehicleonground.md)

- [isVehicleTaxiLightOn](mta://scripting/shared/functions/isvehicletaxilighton.md)

- [removeVehicleUpgrade](mta://scripting/shared/functions/removevehicleupgrade.md)

- [removeVehicleSirens](mta://scripting/shared/functions/removevehiclesirens.md)

- [setTrainDerailable](mta://scripting/shared/functions/settrainderailable.md)

- [setTrainDerailed](mta://scripting/shared/functions/settrainderailed.md)

- [setTrainDirection](mta://scripting/shared/functions/settraindirection.md)

- [setTrainPosition](mta://scripting/shared/functions/settrainposition.md)

- [setTrainSpeed](mta://scripting/shared/functions/settrainspeed.md)

- [setVehicleColor](mta://scripting/shared/functions/setvehiclecolor.md)

- [setVehicleDamageProof](mta://scripting/shared/functions/setvehicledamageproof.md)

- [setVehicleDoorOpenRatio](mta://scripting/shared/functions/setvehicledooropenratio.md)

- [setVehicleDoorState](mta://scripting/shared/functions/setvehicledoorstate.md)

- [setVehicleDoorsUndamageable](mta://scripting/shared/functions/setvehicledoorsundamageable.md)

- [setVehicleEngineState](mta://scripting/shared/functions/setvehicleenginestate.md)

- [setVehicleFuelTankExplodable](mta://scripting/shared/functions/setvehiclefueltankexplodable.md)

ADDED/UPDATED IN VERSION 1.6.0 [r22771](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=22771):

- [spawnVehicleFlyingComponent](mta://scripting/shared/functions/spawnvehicleflyingcomponent.md)

- [setVehicleHandling](mta://scripting/shared/functions/setvehiclehandling.md)

- [setVehicleHeadLightColor](mta://scripting/shared/functions/setvehicleheadlightcolor.md)

- [setVehicleLandingGearDown](mta://scripting/shared/functions/setvehiclelandinggeardown.md)

- [setVehicleLightState](mta://scripting/shared/functions/setvehiclelightstate.md)

- [setVehicleLocked](mta://scripting/shared/functions/setvehiclelocked.md)

- [setVehicleOverrideLights](mta://scripting/shared/functions/setvehicleoverridelights.md)

- [setVehiclePaintjob](mta://scripting/shared/functions/setvehiclepaintjob.md)

- [setVehiclePanelState](mta://scripting/shared/functions/setvehiclepanelstate.md)

- [setVehiclePlateText](mta://scripting/shared/functions/setvehicleplatetext.md)

- [setVehicleSirens](mta://scripting/shared/functions/setvehiclesirens.md)

- [setVehicleSirensOn](mta://scripting/shared/functions/setvehiclesirenson.md)

- [setVehicleTaxiLightOn](mta://scripting/shared/functions/setvehicletaxilighton.md)

- [setVehicleTurretPosition](mta://scripting/shared/functions/setvehicleturretposition.md)

- [setVehicleVariant](mta://scripting/shared/functions/setvehiclevariant.md)

- [setVehicleWheelStates](mta://scripting/shared/functions/setvehiclewheelstates.md)
