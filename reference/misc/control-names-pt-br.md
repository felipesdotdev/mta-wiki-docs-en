---
doc_id: "mta-wiki:12807"
title: "PT-BR/Control names"
source_title: "Control names/PT-BR"
source_url: "https://wiki.multitheftauto.com/wiki/Control_names/PT-BR"
revision_id: 69297
language: "en"
categories: ["Translated/Scripting_Concepts"]
generated_at: "2026-07-26T16:07:49.331934+00:00"
---

# PT-BR/Control names

Esta página lista todos os nomes de controles. Eles podem ser usados como argumentos principais pelos comandos do console *bind* e *unbind* e também em funções como [bindKey](mta://scripting/shared/functions/bindkey.md), [unbindKey](mta://scripting/shared/functions/unbindkey.md), [toggleControl](mta://scripting/shared/functions/togglecontrol.md) etc.

Tabela Lua listando todos os nomes de controle disponíveis e que estão nesta página:

```
controles = { "fire", "aim_weapon", "next_weapon", "previous_weapon", "forwards", "backwards", "left", "right", "zoom_in", "zoom_out",
 "change_camera", "jump", "sprint", "look_behind", "crouch", "action", "walk", "conversation_yes", "conversation_no",
 "group_control_forwards", "group_control_back", "enter_exit", "vehicle_fire", "vehicle_secondary_fire", "vehicle_left", "vehicle_right",
 "steer_forward", "steer_back", "accelerate", "brake_reverse", "radio_next", "radio_previous", "radio_user_track_skip", "horn", "sub_mission",
 "handbrake", "vehicle_look_left", "vehicle_look_right", "vehicle_look_behind", "vehicle_mouse_look", "special_control_left", "special_control_right",
 "special_control_down", "special_control_up" }
```

## Lista de controles do GTA

A PÉ

- **fire** - Dispara a arma de um jogador (**Nota**: Se você quer desabilitar o disparo de armas, lembre-se também de desabilitar os controles **action** e  **fire**.)

- **aim_weapon** - Aponta a arma atual do jogador (se possível) (isto também afeta *right-click* + *F*)

- **next_weapon** - Troca para a próxima arma

- **previous_weapon** - Troca para a arma anterior

- **forwards** - Move para frente

- **backwards** - Move para trás

- **left** - Move para esquerda

- **right** - Move para direita

- **zoom_in** - Amplica o zoom de uma arma (sniper/rocket launcher/camera etc)

- **zoom_out** - Diminui o zoom da arma

- **change_camera** - Altera o tipo de câmera

- **jump** - Faz jogador pular

- **sprint** - Faz o jogador dar uma arrancada (começar a correr)

- **look_behind** - Faz o jogador olhar para trás (e permite que o jogador olhe para atrás dele)

- **crouch** - Faz o jogador se agachar

- **action** - Mostra o menu de status (acionado ao pressionar TAB)

- **walk** - Faz o jogador se mexer/andar devagar

- **conversation_yes** - Responde sim para alguma questão

- **conversation_no** - Responde não para alguma questão

- **group_control_forwards** - Faz com que o grupo que você está controlando, mova-se para frente

- **group_control_back** - Faz com que o grupo que você está controlando, mova-se para trás

- **enter_exit** - Faz o jogador entrar no veículo. Também usado para estilos de luta alternativos.

NO VEÍCULO

- **vehicle_fire** - Dispara a arma primária do veículo do jogador (tipo o míssel do Hunter) ou dispara com o driveby

- **vehicle_secondary_fire** - Dispara a arma secundária do veículo do jogador (tipo a minigun do Hunter)

- **vehicle_left** - Faz o veículo do jogador virar a direita

- **vehicle_right** - Faz o veículo do jogador virar a esquerda

- **steer_forward** - Faz o veículo do jogador "virar" para frente/baixo.  (inclina para frente/baixo com helicópteros/aviões)

- **steer_back** - Faz o veículo do jogador "virar" para trás/cima. (inclina para trás/cima com helicópteros/aviões)

- **accelerate** - Faz o veículo do jogador acelerar

- **brake_reverse** - Faz o veículo do jogador freiar, se já estiver parado, então dá a ré

- **radio_next** - Troca para a próxima estação de rádio (Não funciona - use [setRadioChannel](mta://scripting/client/functions/setradiochannel.md) e [onClientPlayerRadioSwitch](mta://scripting/client/events/onclientplayerradioswitch.md).)

- **radio_previous** - Troca para a estação de rádio anterior (Não funciona - use [setRadioChannel](mta://scripting/client/functions/setradiochannel.md) e [onClientPlayerRadioSwitch](mta://scripting/client/events/onclientplayerradioswitch.md).)

- **radio_user_track_skip** - Pula a faixa atual que está sendo reproduzida na estação de rádio personalizada

- **horn** - Toqua a buzina do veículo do jogador (se o veículo tiver uma buzina) e pode acionar a sirene em veículos de emergência

- **sub_mission** - Inicia uma sub-missão se estiver disponível (tipo as missões de taxi)

- **handbrake** - Aplica o freio de mão no veículo do jogador

- **vehicle_look_left** - Olha para a esquerda

- **vehicle_look_right** - Olha para a direita

- **vehicle_look_behind** - Olha para trás

- **vehicle_mouse_look**

- **special_control_left** - Move algum componente especial do veículo para a esquerda (Tipo o canhão do tanque de guerra Rhino)

- **special_control_right** - Move algum componente especial do veículo para a direita (Tipo o canhão do tanque de guerra Rhino)

- **special_control_down** - Move algum componente especial do veículo para baixo (Tipo o canhão do tanque de guerra Rhino)

- **special_control_up** - Move algum componente especial do veículo para cima (Tipo o canhão do tanque de guerra Rhino)

- **enter_exit** - Faz o jogador sair do veículo

## Comandos hard-coded do MTA

Na lista a seguir há nomes de comandos hard-coded do MTA que não usam bindKey, mas podem atuar como bindKey usando em [addCommandHandler](https://wiki.multitheftauto.com/index.php?title=PT-BR/addCommandHandler&action=edit&redlink=1). Fora isso, esta lista de controles vai funcionar **somente** com as funções [toggleControl](mta://scripting/shared/functions/togglecontrol.md) e [toggleAllControls](mta://scripting/shared/functions/toggleallcontrols.md). Por favor note que [toggleControl](mta://scripting/shared/functions/togglecontrol.md) não pode desabilitar screenshot.

COMANDOS DO MTA

- **enter_passenger** - Entra no veículo mais perto como passageiro

- **screenshot** - Tira uma print(screenshot)

- **chatbox** - Habilita o input do chatbox

- **radar** - Altera a visibilidade do mapa-radar

- **radar_zoom_in** - Amplia o zoom do mapa-radar

- **radar_zoom_out** - Reduz o zoom do mapa-radar

- **radar_move_north** - Move para o norte no mapa-radar

- **radar_move_south** - Move para o sul no mapa-radar

- **radar_move_east** - Move para o leste no mapa-radar

- **radar_move_west** - Move para o oeste no mapa-radar

- **radar_attach** - Anexa a visualização para o jogador local no mapa-radar
