---
doc_id: "mta-wiki:13510"
title: "Modules/FileSystem/translator/relPath"
source_title: "Modules/FileSystem/translator/relPath"
source_url: "https://wiki.multitheftauto.com/wiki/Modules/FileSystem/translator/relPath"
revision_id: 73770
language: "en"
categories: []
generated_at: "2026-07-26T16:16:12.582507+00:00"
---

# Modules/FileSystem/translator/relPath

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

## [FileSystem](mta://reference/misc/modules-filesystem.md) Translator Functions

- [open](mta://reference/misc/modules-filesystem-translator-open.md)

- [exists](mta://reference/misc/modules-filesystem-translator-exists.md)

- [createDir](mta://reference/misc/modules-filesystem-translator-createdir.md)

- [chdir](mta://reference/misc/modules-filesystem-translator-chdir.md)

- [delete](mta://reference/misc/modules-filesystem-translator-delete.md)

- [copy](mta://reference/misc/modules-filesystem-translator-copy.md)

- [rename](mta://reference/misc/modules-filesystem-translator-rename.md)

- [size](mta://reference/misc/modules-filesystem-translator-size.md)

- [stat](mta://reference/misc/modules-filesystem-translator-stat.md)

- relPath

- [relPathRoot](mta://reference/misc/modules-filesystem-translator-relpathroot.md)

- [absPath](mta://reference/misc/modules-filesystem-translator-abspath.md)

- [absPathRoot](mta://reference/misc/modules-filesystem-translator-abspathroot.md)

- [scanDir](mta://reference/misc/modules-filesystem-translator-scandir.md)

- [scanDirEx](mta://reference/misc/modules-filesystem-translator-scandirex.md)

- [getDirs](mta://reference/misc/modules-filesystem-translator-getdirs.md)

- [getFiles](mta://reference/misc/modules-filesystem-translator-getfiles.md)

- [setOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-setoutbreakenabled.md)

- [getOutbreakEnabled](mta://reference/misc/modules-filesystem-translator-getoutbreakenabled.md)

- [setPathProcessingMode](mta://reference/misc/modules-filesystem-translator-setpathprocessingmode.md)

- [getPathProcessingMode](mta://reference/misc/modules-filesystem-translator-getpathprocessingmode.md)
