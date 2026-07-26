---
doc_id: "mta-wiki:6952"
title: "Handling.cfg"
source_title: "Handling.cfg"
source_url: "https://wiki.multitheftauto.com/wiki/Handling.cfg"
revision_id: 70292
language: "en"
categories: []
---

# Handling.cfg

Making MTA work with handling.cfg

MTA ignores the GTA file data/handling.cfg because of the custom handling functions, and for fair play reasons (so that clients have no power over vehicle handlings, it's default unless the server decides otherwise).

There are two ways to get a custom handling.cfg working in MTA:

## Recommended way

Most servers that want to offer handling customisation power directly to the player (so they have the freedom to load their own handlings and modify it to their likings) would add this resource on their server:

- [Hedit (Handling Editor GUI)](mta://resources/hedit.md) (part of official resources and therefore located in the **\mods\deathmatch\resources\[gameplay]\hedit** folder

If you cannot find it there, you need to update your resources package from [https://mirror.mtasa.com/mtasa/resources/mtasa-resources-latest.zip](https://mirror.mtasa.com/mtasa/resources/mtasa-resources-latest.zip) (it got added in 2021) or only that resource from the official resources [**github page**](https://github.com/multitheftauto/mtasa-resources/tree/master/%5Bgameplay%5D/hedit)

## Another way

To load custom handling.cfg, follow these steps:

- Download the [Handling Loader resource](http://nightly.mtasa.com/files/res/handling_loader.zip)

- Unzip **handling_loader.zip** contents into **server/mods/deathmatch/resources/handling_loader/**

- Start server, or type **refresh** into the server console

- (Optional) Copy the global **handling.cfg** into **server/mods/deathmatch/resources/handling_loader/**

- (Optional) Tell clients to put their personalized **handling.cfg** into **MTA San Andreas 1.6\mods\deathmatch\resources\handling_loader\**

- Start **Handling Loader** with the command **start handling_loader**

The server handling.cfg will apply to everyone on the server. (If installed)  

The customized handling lines of the player installed handling.cfg will only apply to the cars that player drives.
