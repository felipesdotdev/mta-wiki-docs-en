---
doc_id: "mta-wiki:9292"
title: "Command fakelag"
source_title: "Command fakelag"
source_url: "https://wiki.multitheftauto.com/wiki/Command_fakelag"
revision_id: 78942
language: "en"
categories: []
generated_at: "2026-07-26T16:12:15.786451+00:00"
---

# Command fakelag

Debug sync issues caused by network lag and packet loss

Two commands: **fakelag** on the client and **sfakelag** on the server.  

Enable the commands by adding **<fakelag>1</fakelag>** to **mtaserver.conf** and start the MTA server.

| [[{{{image}}}\|link=\|]] | Note: The MTA server will not advertise itself to the master server list while the fakelag command is enabled. |
| --- | --- |
|  |  |

## Command usage

Server:

```
sfakelag <packet loss> <extra ping> <ping variance> [ <KBPS limit> ]
```

Client:

```
fakelag <packet loss> <extra ping> <ping variance> [ <KBPS limit> ]
```

- **packet loss** - is in percent. - e.g. A value of 50 will mean 50% of packets will be lost

- **extra ping** - is the base ping lag to add in milliseconds. - e.g. A value of 100 will add a 100ms delay on all sent packets

- **ping variance** (AKA ping jitter) is the range of ping lag to add in milliseconds. - e.g. A value of 200 will add an extra 0 to 200ms delay on all sent packets

- **KBPS limit** - limits the send throughput to the supplied value

## Example

```
fakelag 50 100 200
```

Means: 50% of sent packets are lost and every packet is delayed from between 100 and 300 ms

## Notes

Commands require at least server and client version **1.5.3-9.11217**  

**fakelag** only affects packets *sent* by the client  

**sfakelag** only affects packets *sent* by the server

To enable the sfakelag command from a client, add the following line to the Admin group in acl.xml:

```
<right name="command.sfakelag" access="true"></right>
```
