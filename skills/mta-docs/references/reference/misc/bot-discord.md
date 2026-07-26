---
doc_id: "mta-wiki:14536"
title: "Bot Discord"
source_title: "Bot Discord"
source_url: "https://wiki.multitheftauto.com/wiki/Bot_Discord"
revision_id: 81840
language: "en"
categories: ["Resources"]
---

# Bot Discord

Discord Bot for MTA:SA

This resource is designed to connect an MTA:SA server with a Discord server.

This page is always updated for the latest bot version!

**Status**: Open Source & Work in Progress

**Github Repository**: [https://github.com/Ahmed-Ly/botdiscord](https://github.com/Ahmed-Ly/botdiscord)

**community**: [https://community.multitheftauto.com/index.php?p=resources&s=details&id=18961](https://community.multitheftauto.com/index.php?p=resources&s=details&id=18961)

**free host for bot**: [https://render.com/](https://render.com/)

**Current Version**: 1.9.0

my account discord is ahmedly.

# Features

Send and receive messages between Discord and MTA:SA

Execute admin commands via Discord

Support for sending server notifications to a Discord channel

# Installation Guide

Download the files from the link above.

Place the discord-bot folder inside the resources folder in MTA:SA.

Update mtaserver.conf to add the resource to the list.

Add the bot token details in config.lua.

if you using render must use environment variables not config for token.

Start the server and use the command /start yourresourcename.

# Usage

**1. Sending Messages from Discord to MTA**

When a message is sent in the designated Discord channel, it will automatically appear in-game.

**2. Executing Admin Commands from Discord**

Admins in Discord can use the following command:

!kick playerName reason

and the player will be kicked from the server.

**3. Sending Notifications from MTA to Discord**

When a new player joins, a notification will be sent to the designated Discord channel:

addEventHandler("onPlayerJoin", root, function()
local playerName = getPlayerName(source)
sendDiscordMessage("" .. playerName .. " has joined the server!")
end)

# Requirements

MTA:SA server running version 1.6.0 or later.

A Discord bot activated with a token.

discord.py library on the server.

Additional dependencies: Install discord.py, Flask, and requests using:

pip install discord.py Flask requests configparser

# Troubleshooting

Ensure the bot token is correct in config.ini.

Verify that the bot has permission to send messages in the required channel.

Use /debugscript 3 to monitor any errors within MTA.

# Notes

Ensure MTA is correctly configured in the script and that you have updated credentials such as username, password, host, and port to match your MTA server settings.
