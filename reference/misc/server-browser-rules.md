---
doc_id: "mta-wiki:14516"
title: "Server Browser Rules"
source_title: "Server Browser Rules"
source_url: "https://wiki.multitheftauto.com/wiki/Server_Browser_Rules"
revision_id: 81682
language: "en"
categories: []
generated_at: "2026-07-26T16:16:36.675121+00:00"
---

# Server Browser Rules

|  | Warning: The system described in this article is still work-in-progress! |
| --- | --- |
|  |  |

| [[{{{image}}}\|link=\|]] | Note: Developers are working on creating a new Server Browser Interface. Check these issues on GitHub: Add banner, server description and tags #2104 Revamp server browser #998 Language filter/search #759 |
| --- | --- |
|  |  |

## Information

"**Server Browser Rules**" are *key-value* string pairs defined server-side.

These values are automatically transmitted/announced/broadcasted by your MTA Server using the ASE (All-Seeing Eye) protocol, when queried on the ASE UDP Port (server port + 123), which is 22126 by default.

These **rules** are included in your server's ASE response in addition to the server name, port, game type, map name, MTA version, password-protected, player count, max players and list of online players.

This data is to be received and parsed by MTA Clients (in the Server Browser) to display the list of online MTA servers with custom information for each server.

## Setting & Getting

These *rules* can be set in your MTA Server's configuration file ([Server_mtaserver.conf](mta://reference/misc/server-mtaserver-conf.md)) using the following XML format:

```
<rule name="NAME_HERE" value="VALUE_HERE"/>
```

They can also be defined and obtained using these two server-side functions:

- [setRuleValue](mta://scripting/server/functions/setrulevalue.md)

- [getRuleValue](mta://scripting/server/functions/getrulevalue.md)

## Expected Values

The maximum amount of characters allowed in a rule value is **200**.

The Server Browser looks for the following information (optional) provided by servers:

| Key | Explanation | Accepted values | Example |
| --- | --- | --- | --- |
| description | Human-readable brief description of your server | Text | Custom cars and maps! Join various minigames from racing to drifting |
| languages | Comma separated list of languages that your server supports | See Allowed Languages | en_US |
| tags | Comma separated list of tags that describe your server | See Allowed Tags | freeroam, minigames, pvp, drifting |
| website_url | Website URL of your server | Valid URL starting with https:// | https://example-website.com |
| social_url_1 | Social media URL #1 | Valid URL starting with https:// | https://discord.com/invite/example |
| social_url_2 | Social media URL #2 | Valid URL starting with https:// | https://youtube.com/@exampleChannel |
| social_url_3 | Social media URL #3 | Valid URL starting with https:// | https://facebook.com/examplePage |

## Full Example

Below is an example configuration that you can include in **mtaserver.conf**:

```
<rule name="description" value="Custom cars and maps! Join various minigames from racing to drifting" />
<rule name="languages" value="en_US" />
<rule name="tags" value="freeroam, minigames, pvp, drifting" />
<rule name="website_url" value="https://example-website.com" />
<rule name="social_url_1" value="https://discord.com/invite/example" />
<rule name="social_url_2" value="https://youtube.com/@exampleChannel" />
<rule name="social_url_3" value="https://facebook.com/examplePage" />
```

## Allowed Tags

Allowed tags: TO BE DECIDED

Maximum tags: 4

## Allowed Languages

Allowed language codes are the ones listed as **locales** in the MTA Client's [MTA/locale folder](https://github.com/multitheftauto/mtasa-blue/tree/master/Shared/data/MTA%20San%20Andreas/MTA/locale).

e.g. **en_US**

Maximum languages: 5 (?)

## Useful Information

- [github.com/multitheftauto/mtasa-blue: PR #3761](https://github.com/multitheftauto/mtasa-blue/pull/3761)

- [wikipedia.org: The All-Seeing Eye](https://en.wikipedia.org/wiki/The_All-Seeing_Eye)

- [int64.org: All-Seeing Eye Protocol](https://int64.org/docs/gamestat-protocols/ase.html)
