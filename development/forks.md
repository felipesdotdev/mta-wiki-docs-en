---
doc_id: "mta-wiki:11909"
title: "Forks"
source_title: "Forks"
source_url: "https://wiki.multitheftauto.com/wiki/Forks"
revision_id: 79870
language: "en"
categories: ["Development"]
generated_at: "2026-07-26T16:15:02.075748+00:00"
---

# Forks

| [[{{{image}}}\|link=\|]] | Note: Information on this page does not apply to the official builds of MTA. |
| --- | --- |
|  |  |

Multi Theft Auto is open-source software, freely available on [GitHub multitheftauto/mtasa-blue](https://github.com/multitheftauto/mtasa-blue).
Anyone is free to fork the project as long as they abide by the terms of our license, The GNU General Public License v3.

You can find explanations of the GNU GPL v3 here: [choosealicense.com](https://choosealicense.com/licenses/gpl-3.0/) and [tldrlegal.com](https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)). Our [license](https://github.com/multitheftauto/mtasa-blue/blob/master/LICENSE) takes precedence, but this generally means that you must:

- state significant changes made to the software

- disclose the source code

- share your code under the same license

- include the original copyright notice

If you are working on a fork, we ask that you include a link to your homepage and where we can find the source code. This allows us to keep up to date on projects and even introduce improvements to the vast majority of MTA players. Adding your Discord name is not compulsory, but if you ask for development help on our GitHub, forum or Discord, it helps us know what project you are from and that you are abiding by the license.

## Forks and anti-cheat

(from [https://wiki.multitheftauto.com/wiki/Anti-cheat_support_for_custom_builds](https://wiki.multitheftauto.com/wiki/Anti-cheat_support_for_custom_builds))

### **// UPDATE (December 2022)**

You can now leverage "full Anticheat for forks" as well. For more information, visit this article: **[Forks Full AC](mta://development/forks-full-ac.md)**

.. But otherwise

Custom MTA builds and forked projects will face some challenges relating to anti-cheat (AC). Due to the fact that many forks and custom builds perform in ways that the anti-cheat module does not expect, we were forced to remove plenty of advanced detections and protections from the anti-cheat, in order to create and provide a separate module (the one from [https://mirror.mtasa.com/bdata/netc.dll](https://mirror.mtasa.com/bdata/netc.dll)) that, simply put, is a much weaker anti-cheat than the 'real' MTA has. So, unless you take measures of your own, your forked project can (and will) easily become infested with cheaters. This can be sidestepped with [Forks Full AC](mta://development/forks-full-ac.md) (click for article). But in the standard scenario, reading the below information helps.

The anti-cheat and netcode components (netc.dll, net.dll, FairplayKD.sys) are, unlike MTA itself, closed-source, and therefore without informing yourself it would be hard to overcome the challenges.

AC is generally unsupported for forked projects and may be dropped entirely in the future. This means that you generally *cannot* rely on the MTA anti-cheat for your fork. **We strongly advise that you write and implement your own AC.**

If you cannot write your own AC, here are steps you can follow to get the most out of our (unsupported) AC:

- Always use the version of our net modules (e.g [netc.dll](https://mirror.mtasa.com/bdata/netc.dll) and [net.dll](https://mirror.mtasa.com/bdata/net.dll)) that matches our commit on master that your fork is based on

- To be specific, you can use the latest module that is bitstream version compatible

- You can fetch these modules by running [https://github.com/multitheftauto/mtasa-blue/blob/master/win-build.bat](https://github.com/multitheftauto/mtasa-blue/blob/master/win-build.bat)

- Never block any MTA traffic (client and server communicates with official MTAHQ servers) in your project

*** Make sure to use 'unstable' build type and not 'custom', or else the 15% AC features for "bdata forks netc" goes down to 1%. See build type documentation at [mtasa-blue/Shared/sdk/version.h](https://github.com/multitheftauto/mtasa-blue/blob/master/Shared/sdk/version.h) for details and proper configuration**

### AC features missing in custom builds

- No detection of changes to gta_sa code section

- No detection of changes to certain gta_sa variables

- No detection against memory modification

- No detection against various Lua injection methods

- SetElementData not protected against external changes by hacks

- Much fewer AC heuristics and protection of internals

- Continuous updates for all patched methods and vulnerabilities to write cheats based on aren't guaranteed (occasionally, they are cherry-picked; one of the reasons why updating netc.dll to the latest offered version is beneficial). This is the biggest (and most important) part of the original anti-cheat.

- MTA modules aren't checked for modifications or remote hooking/manipulation

- and much more

Generally, most of what will work are some signature-based detections. No heuristics, patched methods, and patched vulnerabilities. Signature-based detections are the weakest kind, and the mainstream anti-cheat tackles the actual problem rather than being signature-based. Note that certain forks (e.g the russian "MTA Province") have even less MTA anti-cheat support, so not even the minimal amount that most other forks enjoy. This is due to fork developers having the ability to completely block or break client > MTAHQ communication traffic (something we heavily rely on to help forks counteract cheating, as most regular AC features and protections aren't available), or do and change other things that from a technical perspective will cause AC features not to work as intended or fail immediately. If you don't want your fork to even become cheater-infested as much as "MTA Province" and how they call it, "their clones" (of Province).. in addition to having set buildtype to "custom" whereas it should be "unstable". Then now you hopefully know what to watch out for as fork developer. Also, it would be nice if this message reaches the developers of cheater-heavy forks like Province.

Additionally, MTA anti-cheat team does some additional, manual work to break up cheating on forks, e.g by causing occasional banwaves of known forks cheats using way too simple detection methods, on a best effort basis (without any guarantees). It is only meant as a courtesy from MTA, done when we feel like it, or maybe when you reach out to us.. and you cannot rely on it.
  

The aforementioned banwaves are known to result in bans with reasons that look similar to, and are known by cheaters as, "BAN: RPBOX / NEXTRP / PROVINCE CHEAT" (depending on the names of forks affected by a certain cheat) so please do not refer these users to MTA for ban appeals either.
