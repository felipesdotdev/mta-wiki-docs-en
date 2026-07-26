---
doc_id: "mta-wiki:4574"
title: "Using Squid to speed up resource downloads"
source_title: "Using Squid to speed up resource downloads"
source_url: "https://wiki.multitheftauto.com/wiki/Using_Squid_to_speed_up_resource_downloads"
revision_id: 54537
language: "en"
categories: ["Tutorials"]
---

# Using Squid to speed up resource downloads

Squid is a web cache that, in this case, makes it easy to mirror your resource directory. This means you can host your resources on another web server, but you don't have to manually copy the files there. Setting this up takes about 15 minutes or so - if everything goes well.

## Getting Squid

You can either download a pre-made (binary) build of Squid or make your own.

If the server for Squid is running Windows, you probably want to download a premade build.

Binaries: [[1]](http://www.squid-cache.org/Download/binaries.dyn)
Source: [[2]](http://www.squid-cache.org/Versions/v3/3.0/)

I've tested this with version squid-3.0.STABLE15.

If you've downloaded the source, extract the .tar.gz file and follow the instructions in the INSTALL file.

When configuring the cache, open the squid.conf file and use the following settings (*replace* the entire existing config with this):

```
http_port <THE PORT YOU WANT SQUID TO RUN ON> accel defaultsite=<YOUR SERVER IP HERE>

cache_peer <YOUR SERVER IP HERE> parent <YOUR SERVER HTTP PORT HERE> 0 no-query originserver name=myAccel

acl our_sites dstdomain <YOUR SERVER IP HERE>
http_access allow our_sites
cache_peer_access myAccel allow our_sites
cache_peer_access myAccel deny all
```

Replace each of the bits in angled brackets with the relevant details. Don't leave the angled brackets in!

## Setting up the MTA server

Shut down your server.

Edit your server config file - server/mods/deathmatch/mtaserver.conf.

Change the *httpdownloadurl* tag to point to your squid server, e.g. [http://127.0.0.1:3128](http://127.0.0.1:3128).

Save the file and relaunch your server.

Test that you can connect to it and download resources!
