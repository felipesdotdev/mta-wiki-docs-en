---
doc_id: "mta-wiki:1720"
title: "Control names"
source_title: "Control names"
source_url: "https://wiki.multitheftauto.com/wiki/Control_names"
revision_id: 82021
language: "en"
categories: ["Scripting_Concepts"]
generated_at: "2026-07-26T16:10:35.211606+00:00"
---

# Control names

This page lists all the control names. These can be used as key arguments by the console commands *bind* and *unbind* as well as scripting functions such as [bindKey](mta://scripting/shared/functions/bindkey.md), [unbindKey](mta://scripting/shared/functions/unbindkey.md), [toggleControl](mta://scripting/shared/functions/togglecontrol.md) etc.

Lua table of all the valid control names listed on this page:

```
controlTable = { "fire", "aim_weapon", "next_weapon", "previous_weapon", "forwards", "backwards", "left", "right", "zoom_in", "zoom_out",
 "change_camera", "jump", "sprint", "look_behind", "crouch", "action", "walk", "conversation_yes", "conversation_no",
 "group_control_forwards", "group_control_back", "enter_exit", "vehicle_fire", "vehicle_secondary_fire", "vehicle_left", "vehicle_right",
 "steer_forward", "steer_back", "accelerate", "brake_reverse", "radio_next", "radio_previous", "radio_user_track_skip", "horn", "sub_mission",
 "handbrake", "vehicle_look_left", "vehicle_look_right", "vehicle_look_behind", "vehicle_mouse_look", "special_control_left", "special_control_right",
 "special_control_down", "special_control_up" }
```

```
analogControlTable = { "left", "right", "forwards", "backwards", "vehicle_left", "vehicle_right", "steer_forward", "steer_back", "accelerate",
 "brake_reverse", "special_control_left", "special_control_right", "special_control_up", "special_control_down" }
```

## GTA control list

ON FOOT

- **fire** Fire a player's weapon. (**Note**: If you want to disable weapons fire, remember to also disable the control **action** in addition to the control **fire**.)

- **aim_weapon** Aim the player's current weapon. (if possible) (this also affects right-click + F punching)

- **next_weapon** Switch to the next weapon.

- **previous_weapon** Switch to the previous weapon.

- **forwards** Move forwards.

- **backwards** Move backwards.

- **left** Move left.

- **right** Move right.

- **zoom_in** Zoom targeted weapon in. (sniper/rocket launcher/camera etc)

- **zoom_out** Zoom targeted weapon out.

- **change_camera** Change camera mode.

- **jump** Make the player jump.

- **sprint** Make the player sprint.

- **look_behind** Make the player look behind. (and allow the player to see behind them)

- **crouch** Make the player crouch/duck.

- **action** Show the stats menu - Fire with tab key.

- **walk** Make the player move slowly/quietly.

- **conversation_yes** Answer yes to a question.

- **conversation_no** Answer no to a question.

- **group_control_forwards** Make the group you are controlling move forwards.

- **group_control_back** Make the group you are controlling move backwards.

- **enter_exit** Make the player enter a vehicle. Also used for alternative fighting styles.

IN VEHICLE

- **vehicle_fire** Fire the player's vehicle's primary weapon (e.g. hunter's missiles) or shoot with driveby.

- **vehicle_secondary_fire** Fire the player's vehicle's secondary weapon. (e.g. hunter's minigun)

- **vehicle_left** Make the player's vehicle turn left.

- **vehicle_right** Make the player's vehicle turn right.

- **steer_forward** Make the player's vehicle turn down. (lean forwards for helicopters/planes)

- **steer_back** Make the player's vehicle turn up. (lean backwards for helicopters/planes)

- **accelerate** Make the player's vehicle accelerate.

- **brake_reverse** Make the player's vehicle brake (slow down) and if stationary reverse.

- **radio_next** Change to the next radio station. (Doesn't work - use [setRadioChannel](mta://scripting/client/functions/setradiochannel.md) and [onClientPlayerRadioSwitch](mta://scripting/client/events/onclientplayerradioswitch.md) instead.)

- **radio_previous** Change to the previous radio station. (Doesn't work - use [setRadioChannel](mta://scripting/client/functions/setradiochannel.md) and [onClientPlayerRadioSwitch](mta://scripting/client/events/onclientplayerradioswitch.md) instead.)

- **radio_user_track_skip** Skip the current track being played on the custom radio station.

- **horn** Play the horn of the player's vehicle (if the vehicle has a horn) and can trigger the siren on emergency vehicles.

- **sub_mission** Start a submission if one is avaliable. (e.g. taxi missions)

- **handbrake** Apply the handbrake on the player's vehicle.

- **vehicle_look_left** Look to the left.

- **vehicle_look_right** Look to the right.

- **vehicle_look_behind** Look behind.

- **vehicle_mouse_look**

- **special_control_left** Move the some special vehicle component left. (e.g. tank's turret)

- **special_control_right** Move the some special vehicle component right. (e.g. tank's turret)

- **special_control_down** Move the some special vehicle component down. (e.g. tank's turret)

- **special_control_up** Move the some special vehicle component up. (e.g. tank's turret)

- **enter_exit** Make the player exit a vehicle.

## MTA hard-coded commands

The following are names of hard-coded MTA commands which do not use bindKey, but can act as bindKey by using them in an [addCommandHandler](mta://scripting/shared/functions/addcommandhandler.md). Other than that, this control list will **only** work with the functions [toggleControl](mta://scripting/shared/functions/togglecontrol.md) and [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md). Please note that [toggleControl](mta://scripting/shared/functions/togglecontrol.md) can't disable screenshot.

MTA COMMANDS

- **enter_passenger** Enters the closest vehicle as passenger

- **screenshot** Takes a screenshot

- **chatbox** Opens the chatbox for input

- **radar** Toggles the full SA player-map showing (default **F11**) - previously called radar-map (not to be confused with the HUD mini-map)

- **radar_zoom_in** Zooms in on the player-map

- **radar_zoom_out** Zooms out on the player-map

- **radar_move_north** Moves north on the player-map

- **radar_move_south** Moves south on the player-map

- **radar_move_east** Moves east on the player-map

- **radar_move_west** Moves west on the player-map

- **radar_attach** Attaches the view to following the local-player on the player-map
