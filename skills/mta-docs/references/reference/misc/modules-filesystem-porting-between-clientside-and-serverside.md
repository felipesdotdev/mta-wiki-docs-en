---
doc_id: "mta-wiki:7550"
title: "Modules/FileSystem/Porting Between Clientside and Serverside"
source_title: "Modules/FileSystem/Porting Between Clientside and Serverside"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/Porting_Between_Clientside_and_Serverside"
revision_id: 38800
language: "en"
categories: []
---

# Modules/FileSystem/Porting Between Clientside and Serverside

There are common issues when wanting to port [FileSystem](mta://reference/misc/modules-filesystem.md) code between clientside and serverside environments. This article should help you avoid pitfalls and getting stuck. Since the issues are mostly about lower-level functionality - with a good abstraction layer - you will not have to rewrite much logic.

## There is No 'This Resource' Directory serverside

While the [MTA:Eir](mta://reference/misc/mta-eir.md) client exposes a secure API that bases translator creation around resource folders, the FileSystem module **cannot do that**. The reason is very technical. Hence if you want to get the resource directory you are *operating* in, you need to **hardcode** it.

```
-- Create a translator in our resource directory.
local resRoot = fsys.createTranslator( "mods/deathmatch/resources/thisResource/" ); -- thisResource shall be the name of the running resource.
```

## Serverside Translator Abstraction API

Once the location of the resource is known and a translator is established, then the creation of translators can be abstracted to the resource directory in a similar way as on the MTA:Eir client. This allows creation of translators that are relative to the resources in a secure way.

```
function fileCreateTranslator( path )
    -- Get an absolute path relative to the resource instance directory.
    local absTransPath = resRoot.absPathRoot( path );

    -- It fails if it tries to up-root.
    if not ( absTransPath ) then
        return false;
    end

    -- Create a new translator and return it.
    return fsys.createTranslator( absTransPath );
end
```
