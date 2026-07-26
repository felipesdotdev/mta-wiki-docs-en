---
doc_id: "mta-wiki:12466"
title: "PT-BR/CreateVehicle"
source_title: "CreateVehicle/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/CreateVehicle/PT-BR"
revision_id: 71402
language: "en"
categories: ["Changes_in_1.2"]
generated_at: "2026-07-26T16:07:35.740792+00:00"
---

# PT-BR/CreateVehicle

|  | Nota: Os veículos (e outros elementos) criados em client-side são vistos somente pelo cliente que os criaram, não são sincronizados e os jogadores não podem entrar neles. Eles são essencialmente apenas para exibição. |
| --- | --- |
|  |  |

Esta função cria um veículo em uma localização especificada.

Vale notar que a posição do veículo é relativa ao ponto central do veículo, não sua base. Sendo assim, você precisa garantir que o valor z (eixo vertical) esteja a alguma altura acima do solo. Você pode achar a altura exata com a seguinte função client-side [getElementDistanceFromCentreOfMassToBaseOfModel](mta://scripting/client/functions/getelementdistancefromcentreofmasstobaseofmodel.md), ou você mesmo pode fazer uma estimativa e gerar o veículo para que ele caia no chão.

## Sintaxe

```
vehicle createVehicle ( int model, float x, float y, float z [, float rx, float ry, float rz, string numberplate, bool bDirection, int variant1, int variant2 ] )
```

**Sintaxe POO(OOP)** [Não entendeu o que significa isso?](mta://tutorials/oop-introduction.md)

**Método**: *[Vehicle](mta://reference/misc/vehicle.md)(...)*

### Argumentos necessários

- **model**: O [ID](mta://reference/misc/ids-de-veiculos.md) do veículo que está sendo criado

- **x**: Um número [float](mta://reference/misc/float.md) representando a coordenada X do mapa

- **y**: Um número [float](mta://reference/misc/float.md) representando a coordenada Y do mapa

- **z**: Um número [float](mta://reference/misc/float.md) representando a coordenada Z do mapa

### Argumentos Opcionais

*NOTA:* Ao usar argumentos opcionais, pode ser necessário fornecer todos os argumentos anteriores ao que você deseja usar. Para obter mais informações sobre argumentos opcionais, consulte [Argumentos Opcionais](https://wiki.multitheftauto.com/wiki/BR/Argumentos_Opcionais).

- **rx**: Um número [float](mta://reference/misc/float.md) representando a rotação em torno do eixo X em graus.

- **ry**: Um número [float](mta://reference/misc/float.md) representando a rotação em torno do eixo Y em graus.

- **rz**: Um número [float](mta://reference/misc/float.md) representando a rotação em torno do eixo Z em graus.

- **numberplate**: Uma string que aparecerá na placa do veículo (máximo de 8 caracteres).

- **bDirection** *(serverside only)*: Placeholder [boolean](mta://reference/misc/boolean.md) que fornece compatibilidade com alguns scripts. Isso nunca teve nenhum efeito, mas é lido pelo código. Recomenda-se ignorar esse argumento, passando o argumento *false* ou *variant1* em seu lugar.

- **variant1**: Um [int](mta://reference/misc/int.md) para o primeiro variante do veículo. Veja [vehicle variants](mta://reference/misc/vehicle-variants.md).

- **variant2**: Um [int](mta://reference/misc/int.md) para o segundo variante do veículo. Veja [vehicle variants](mta://reference/misc/vehicle-variants.md).

### Retorna

Retorna o elemento [Elemento/Vehicle](mta://reference/misc/elemento-vehicle.md) que foi criado. Retorna *false* se os argumentos estão incorretos, ou se o limite de 65535 veículos spawnados no mundo for excedido

## Usando trens

Trens são criados usando a função desta página. Eles são colocados no ponto mais próximo do percurso do trem do GTA:SA (geralmente são trilhos de trem) a partir do ponto em que ele foi spawnado.

## Exemplo

Click to collapse [-]
Example 1: Server

Este exemplo cria um marker 'vehicle spawner' que dá ao jogador um veículo assim que ele atinge o marker.

```
local vehMark = createMarker(-2426.34106, -639.12714, 132.93631,"cylinder")

function vehicleSpawner(hitElement,matchingDimension)
	if getElementType(hitElement) == "player" then
		if getPedOccupiedVehicle(hitElement) == false then
		local x,y,z = getElementPosition(hitElement)
			local veh = createVehicle(551, x,y,z)
			warpPedIntoVehicle(hitElement,veh)
		end
	end 
end 
addEventHandler("onMarkerHit",vehMark,vehicleSpawner)
```

Click to collapse [-]
Example 2: Server

Este exemplo cria um veículo a 5 unidades de distância do jogador quando ele digita *createvehicle* e seu nome no console:

```
local distance = 5 --units

-- define our handler (we'll take a variable number of parameters where the name goes, because there are vehicle names with more than one word)
function consoleCreateVehicle ( sourcePlayer, commandName, ... )
   -- if a player triggered it, not the admin,
   if ( sourcePlayer ) then
      -- calculate the position of the vehicle based on the player's position and rotation:
      local x, y, z = getElementPosition ( sourcePlayer ) -- get the player's position
      local rotZ = getElementRotation ( sourcePlayer ) -- get the player's rotation around the Z axis in degrees
      x = x + ( ( math.cos ( math.rad ( rotZ ) ) ) * distance ) -- calculate the X position of the vehicle
      y = y + ( ( math.sin ( math.rad ( rotZ ) ) ) * distance ) -- calculate the Y position of the vehicle

      -- get the complete vehicle name by joining all passed parameters using Lua function table.concat
      local vehicleName = table.concat({...}, " ")
      -- get the vehicle's model ID from the name
      local vehicleID = getVehicleModelFromName ( vehicleName )
      -- if vehicle ID is valid,
      if vehicleID then
            -- create the vehicle using the information gathered above:
            local newVehicle = createVehicle ( vehicleID, x, y, z, 0, 0, rotZ )
            -- if vehicle creation failed, give the player a message
            if not newVehicle then
               outputConsole ( "Failed to create vehicle.", sourcePlayer )
            end
      end
   end
end

-- Attach the 'consoleCreateVehicle' function to the "createvehicle" command
addCommandHandler ( "createvehicle", consoleCreateVehicle )
```

Click to expand [+]
Example 3: Server

Esse script gera um Rhino em cima de um indivíduo sortudo.

```
function scriptCreateTank ( player, command )
      local luckyBugger = getRandomPlayer() -- get a random player
      local x, y, z = getElementPosition ( luckyBugger ) -- retrive the player's position
      createVehicle ( 432, x, y, z + 10 ) -- create the tank 10 units above them
      outputChatBox ( "You got Tank'd!", luckyBugger )
end
--Attach the 'scriptCreateTank' function to the "tank" command
addCommandHandler ( "tank", scriptCreateTank )
```

Click to expand [+]
Example 4: Server

Este exemplo adiciona o comando */spveh* para spawnar um modelo de um carro nas coordenadas fornceidas. Se qualquer um dos carros criados por este comando explodir, ele será respawnado no lugar onde foi criado.

```
-- Do not allow the following IDs to be spawned
local forbiddenCars = { [435] = true, [441] = true, [449] = true, [450] = true, [464] = true, [465] = true, [501] = true,
                        [537] = true, [538] = true, [564] = true, [569] = true, [570] = true, [584] = true, [590] = true,
                        [591] = true, [594] = true, [606] = true, [607] = true, [608] = true, [610] = true, [611] = true }

local cmdVehRoot = createElement("commandVehicles") -- Dummy element containing the cars that this command has created
addCommandHandler("spveh",
    function(player, cmd, modelID, x, y, z, platetext)
        -- Check whether arguments are correct
        local modelID, x, y, z = tonumber(modelID), tonumber(x), tonumber(y), tonumber(z)
        if modelID and x and y and z then
            -- Do not continue if we shouldn't
            if forbiddenCars[modelID] then
                outputChatBox("The car model you provided is not allowed.", player, 255, 0, 0)
                return
            end
            local platetext = type(platetext) == "string" and platetext or "PRIVATE"
            -- Create the actual vehicle and set it as a children of our dummy element
            setElementParent(createVehicle(modelID, x, y, z, 0, 0, 0, platetext), cmdVehRoot)
            -- Inform the player about what we did
            outputChatBox("You have created a " .. getVehicleNameFromModel(modelID) .. " (model ID: " .. modelID .. ") at " .. table.concat({ x, y, z }, ", ") .. " with numberplate " .. platetext .. " successfully.", player, 0, 255, 0)
        else
            outputChatBox("Syntax: /" .. cmd .. " (modelID) (x) (y) (z) [numberplate]", player, 255, 255, 255)
        end
    end
)

-- If a vehicle that has been created using the command blows up, respawn it where it was created
addEventHandler("onVehicleExplode", cmdVehRoot,
    function()
        respawnVehicle(source)
    end
)
```

Click to collapse [-]
Example 5: Client

Este script spawna um tanque em cima do jogador local.

```
function scriptCreateTank ( commandName )
      local luckyBugger = getLocalPlayer() -- get the local player
      local x, y, z = getElementPosition ( luckyBugger ) -- retrive the player's position
      createVehicle ( 432, x, y, z + 10 ) -- create the tank 10 units above them
      outputChatBox ( "You got Tank'd!", 255, 0, 0)
end
--Attach the 'scriptCreateTank' function to the "tank" command
addCommandHandler ( "tank", scriptCreateTank )
```

ADDED/UPDATED IN VERSION 1.4 :

Este é um exemplo de como essa função é usada em OOP(POO - Programação Orientada a Objeto)

Click to collapse [-]
OOP server

This script will create an Infernus at the center (0, 0, 3) of San Andreas upon execution.

```
addEventHandler( "onResourceStart", resourceRoot,
    function()
        infernus = Vehicle(411, Vector3(0, 0, 3)); -- Create an Infernus and spawn it at the middle of SA.
        infernus:setColor(0, 0, 0); -- Set its color to black.
        infernus.damageProof = true; -- Make it damage proof
    end
)
	
addCommandHandler( "blowinfernus",
    function(p)
        if not infernus.blown then -- Check if the Infernus is blown up or not.
            infernus:blow();
        else -- Ouch, it's blown up, let's output an error to the player.
            outputChatBox( "The Infernus has already been blown up by you.", p, 255, 0, 0, false );
        end
    end)
```

## Veja também

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
