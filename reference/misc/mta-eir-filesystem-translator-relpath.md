---
doc_id: "mta-wiki:7506"
title: "MTA:Eir/FileSystem/translator/relPath"
source_title: "MTA:Eir/FileSystem/translator/relPath"
source_url: "https://wiki.multitheftauto.com/wiki/MTA%3AEir/FileSystem/translator/relPath"
revision_id: 73542
language: "en"
categories: []
generated_at: "2026-07-26T16:16:06.192738+00:00"
---

# MTA:Eir/FileSystem/translator/relPath

This function transform a path that is passed to it into a path that is relative to the translators current directory. The path must be accessible from the translator. The path can either be absolute or relative.

## Syntax

```
string translator:relPath ( string path )
```

## Arguments

- **path:** the path that should be transformed into a relative path; can be nil if the current directory should be returned

## Returns

This function returns the relative version of the path that is passed to it, **false** if the specified path is not accessible by the translator.

## Example

Click to collapse [-]
Client

This snippet converts the path relative from one translator to a relative path from another translator.

```
local function getPathTranslatorRelative( srcTranslator, dstTranslator, srcPath )
    -- Get the absolute path from the srcTranslator perspective.
    local absPath = srcTranslator:absPath( srcPath );

    -- Return the relative path from the dstTranslator. Will return false if conversion cannot happen.
    return dstTranslator:relPath( absPath );
end
```

## [FileSystem](mta://reference/misc/mta-eir-filesystem.md) Translator Functions

- [open](mta://reference/misc/mta-eir-filesystem-translator-open.md)

- [exists](mta://reference/misc/mta-eir-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/mta-eir-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/mta-eir-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/mta-eir-filesystem-translator-delete.md)

- [copy](mta://reference/misc/mta-eir-filesystem-translator-copy.md)

- [rename](mta://reference/misc/mta-eir-filesystem-translator-rename.md)

- [size](mta://reference/misc/mta-eir-filesystem-translator-size.md)

- [stat](mta://reference/misc/mta-eir-filesystem-translator-stat.md)

- relPath

- [relPathRoot](mta://reference/misc/mta-eir-filesystem-translator-relpathroot.md)

- [absPath](mta://reference/misc/mta-eir-filesystem-translator-abspath.md)

- [absPathRoot](mta://reference/misc/mta-eir-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/mta-eir-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/mta-eir-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/mta-eir-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/mta-eir-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/mta-eir-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/mta-eir-filesystem-translator-getpathprocessingmode.md)
