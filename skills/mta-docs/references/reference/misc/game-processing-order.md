---
doc_id: "mta-wiki:6162"
title: "Game Processing Order"
source_title: "Game Processing Order"
source_url: "https://wiki.multitheftauto.com/wiki/Game_Processing_Order"
revision_id: 67823
language: "en"
categories: []
---

# Game Processing Order

Game processing order

Here is an overview to show the order in which things get done during an average frame of playing MTA.

The [onClientPreRender](mta://scripting/client/events/onclientprerender.md) event is triggered after GTA updates the world, and is the ideal place to do dxDraws that are in some way attached to world elements.

The [onClientHUDRender](mta://scripting/client/events/onclienthudrender.md) event is triggered before GTA renders the in-game HUD, so it the best place to apply any full screen effects that you want 'behind' the HUD.

The [onClientPedsProcessed](mta://scripting/client/events/onclientpedsprocessed.md) event is triggered after GTA updates bone transformations for all peds. This event can be used for updating bones.
