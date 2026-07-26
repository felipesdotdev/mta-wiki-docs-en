---
doc_id: "mta-wiki:2711"
title: "Resource : FPSRTS/Brief"
source_title: "Resource:FPSRTS/Brief"
source_url: "https://wiki.multitheftauto.com/wiki/Resource%3AFPSRTS/Brief"
revision_id: 8725
language: "en"
categories: []
generated_at: "2026-07-26T16:17:01.279722+00:00"
---

# Resource : FPSRTS/Brief

**If you have read this page and are interested in helping us out with suggestions/code, please join #project-theta on IRC. Thanks!**

This gamemode is a fairly straightforward FPS/RTS game. This has been done before in games like Natural Selection (NS) - the most popular half-life 1 'unofficial' mod - and Battlefield 2.

## Why do this?

- It offers a lot of variety

- Its more complex than most game modes, so it shows off what MTA can do

- It should be fun to play!

## What is the aim?

The aim of the game is for one team to destroy the other's command center. Obviously this divides the efforts of the team somewhat between defence and offence. A key aspect is the collection of money, this can be done by building structures (such as oil rigs) at particular points on the map. The structure then provides the team with a steady flow of money until it is destroyed by the opposing team.

## How it works

One player on each team gets to be the commander. In NS this is pretty much the first person who gets the the "command station" (not that everyone wants to). In BF2, I think players can nominate themselves and then get voted in. Either way works. In both cases players can vote against the commander and once a certain percentage have, he gets kicked out of the command station and banned from it for the rest of the game.

The commander is able to see the map in an RTS fashion - like **Command & Conquer**. They have a kind of 45 degree view of the map from above. The commander has their cursor visible all the time, and can click on a number of buttons on their GUI that do a variety of things:

- Spawn a vehicle at the point a player clicks

- Spawn a weapon at a point

- Drop health and ammo for players

- Create buildings for the players to "build"

- Upgrade through the "tech tree"

- Give a player a waypoint

- Scan an area to see the enemy

Each of these actions costs some money.

## Buildings

Buildings can act as a requirement for certain actions, for example you might have to own a garage to be able to get vehicles, or an ammunation to get weapons. This may not be feasable in practice, so the alternative is that the commander can place these structures (or something representing them) that enables them. Buildings can also enable tech tree upgrades, such as an upgrade at ammunation might allow you to upgrade it so you can get better weapons. Also, teams should have different (balanced) capabilities to keep the game interesting: an example would be that a garage of team A would spawn different vehicles than a garage of team B.

## Tech tree

Tech trees are part of almost all RTS games - from Age of Empires to the Command & Conquer games and many more. The game starts with the tech tree at its most basic. The commander then has the option to upgrade as they play, each upgrade costing a value in money and taking a certain amount of time. Upgrades are dependent on other upgrades, and potentially mutually exclusive.

Example upgrades:

- Heavy weapons

- Fast cars

- Ability to give cars NOS

- Ability to drop tanks

- Ability to modify weather ;)

- Changing gravity

## Waypoints

The commander can give players waypoints - places to go. These can then be rendered on the player's screen and on their radar map. The player isn't required to follow them (and probably won't in many games), but they can!

## Commander summary

Essentially the commander is in control - the rest of the players depend on the commander for support. The commander can only see the map in the area around the players. This means they can't see the players on the opposite team.

## Other players

The non-commander players play as normal. They can request things from the commander using some hotkeys (like health, ammo, an order). They get given waypoints which they can ignore if they want, but these encourage team-play. Players have to build buildings for the commander, and prevent the other team from destroying their buildings and ultimately their command center.

## General ideas

As its hard to provide static defence (guns that shoot at players automatically), mines might be a better suggestion. These could be almost or entirely invisible and just blow up when the opposite team goes over them. To make it more interesting, they could blow up when either team went over them, but the team that placed them can see them on the radar or similar...

## Whats the next step?

We need to discuss this, expand this brief, then work on drawing up a solid specification. The overall aim while developing this should be to create a game mode that can be expanded later with a more complicated tech tree.

Much of the code required can be borrowed from the editor. A camera has already been coded for the commander view. Some models could be made for things like oilrigs and "oil location markers" and other buildings that can be built.
