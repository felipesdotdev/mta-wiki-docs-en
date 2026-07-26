---
doc_id: "mta-wiki:7153"
title: "Help : Editing Guidelines"
source_title: "MTA Wiki:Editing Guidelines"
source_url: "https://wiki.multitheftauto.com/wiki/MTA_Wiki%3AEditing_Guidelines"
revision_id: 78873
language: "en"
categories: ["MTA_Wiki:Editing"]
generated_at: "2026-07-26T16:16:07.245893+00:00"
---

# Help : Editing Guidelines

| [[{{{image}}}\|link=\|]] | Important Note: This wiki is an older version (1.39.3), functionality from the Mediawiki help pages may not always work. |
| --- | --- |
|  |  |

Before you contribute to the Multi Theft Auto Wiki make sure you know/understand the basics of [MediaWiki](http://www.mediawiki.org/wiki/Help:Contents). This article is a guide on how to edit the MTA Wiki properly.

## Editing Pages

*MediaWiki general help page: [Editing Pages](http://www.mediawiki.org/wiki/Help:Editing_pages)*

| [[{{{image}}}\|link=\|]] | Note: Don't duplicate content on the wiki use templates instead if you want to use the same content on multiple pages. |
| --- | --- |
|  |  |

### Minor Edits

From Wikipedia: "A check to the "minor edit" box signifies that only superficial differences exist between the version with your edit and the previous version: typo corrections, formatting and presentational changes, rearranging of text without modifying content, etc. A minor edit is a version that the editor believes requires no review and could never be the subject of a dispute. The "minor edit" option is one of several options available only to registered users."

### Editing Function/Event Pages

 

Layout Function Pages

Specific information for editing the MTA Wiki.

##### Contents of Function/Event Pages

Function and event pages have a layout that is easy to identify and consistent. Before adding function and/or event pages make sure they do exist in the MTA Core!

###### Layout Function Pages

- No Table of Contents: __NOTOC__

- Define if function is server and/or client: {{Server client function}}

- Server only function:  {{Server function}}

- Client only function:  {{Client function}}

- Both client and server: {{Server client function}}

- Explain the function

- Syntax: Use <syntaxhighlight lang="lua"></syntaxhighlight>

- Required Arguments

- Optional Arguments (not always necessary)

- Returns

- Example

- See Also: Add the template to which function group this function belongs

###### Layout Event Pages

- No Table of Contents: __NOTOC__

- Define if event is server or client: {{server event}}

- Server event:  {{Server event}}

- Client event:  {{Client event}}

- Parameters

- Source: The source of the event.

- Example

- See Also

Events can only be server or client side not both.

##### Tips

- When creating a new page for a function or event, you need to edit the template for 'See Also' too. If you don't add it to a function/event group template this page is orphaned.

- When you don't want to add examples, add the {{Needs Example}} template at the top of the page.

- If you added examples to a page make sure to remove template {{Needs Example}} when necessary.

## Script Examples

| [[{{{image}}}\|link=\|]] | Note: When writing a script example always test and verify that your example is working, submitting not working examples is a waste of time for everyone. |
| --- | --- |
|  |  |

- Preferably use four spaces instead of one tabulator.

- Use the syntaxhighlighting codebox provided on this wiki. (<syntaxhighlight lang="lua">(CODE HERE)</syntaxhighlight>)

- If the event/function is both client and server you should use the section template with server and/or client classes.

- For server side examples: <section name="Example 1" **class="server"** show="true"></section>

- For client side examples: <section name="Example 2" **class="client"** show="false"></section>

When an event/function is only client or server side you should only use the code box and not the section tags.

If there are enough scripting examples, remove the template {{Needs Example}} or the [[Category:Needs Example]] when necessary.

## Templates

*MediaWiki general help page: [Templates](http://www.mediawiki.org/wiki/Help:Templates)*

Templates are a consistent set of visual styling and can be used in articles to get the reader's attention or mark a page for example as outdated. Some templates also require arguments, for more information on how to use MTA's specific wiki templates go [here](https://wiki.multitheftauto.com/wiki/Help:MTA_Wiki_Specific_Templates).

| [[{{{image}}}\|link=\|]] | Tip: If you want to avoid spacing between the page title and the template itself, you should include the template before __NOTOC__ other templates and/or magic words . |
| --- | --- |
|  |  |

Using templates is recommended when using the same content over a large number of pages. This will save you time when you want to change something in that content and doesn't require you to edit all the pages but just the template.

- [How to use MTA Wiki's Specific templates](https://wiki.multitheftauto.com/wiki/Help:MTA_Wiki_Specific_Templates)

## Protected Pages

Protected pages cannot be modified by normal users, if you want to change something on a protected page you will have to ask someone who has the right permissions to modify them.

## Orphaned Pages

A page is considered orphaned when no other page(s) link to that page. This means no one will find it unless they use the search function.

- [Orphaned pages](https://wiki.multitheftauto.com/wiki/Special:LonelyPages)

- [Adding Pages to Categories and Templates](mta://tutorials/adding-pages-to-categories-and-templates.md)

## Icons

When you want to use icons, it is recommended to use general icons this improves the consistency of the wiki.

- [Tango Icons](https://commons.wikimedia.org/wiki/Tango_icons)

## Helpful links

- [Wikipedia Cheatsheet](http://en.wikipedia.org/wiki/Wikipedia:Cheatsheet) - Quick overview of general editing tags and functions.

- [MediaWiki Help](http://www.mediawiki.org/wiki/Help:Contents) - General help for the MediaWiki software.

- [Mediawiki Examples](http://meta.wikimedia.org/wiki/Help:Wikitext)

## References

- [↑](#cite_ref-1) [http://en.wikipedia.org/wiki/Help:Minor_edit](http://en.wikipedia.org/wiki/Help:Minor_edit)

- [↑](#cite_ref-2) [http://www.mediawiki.org/wiki/Help:Protected_pages](http://www.mediawiki.org/wiki/Help:Protected_pages)
