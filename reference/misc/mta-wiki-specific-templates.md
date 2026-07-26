---
doc_id: "mta-wiki:7154"
title: "Help : MTA Wiki Specific Templates"
source_title: "MTA Wiki:Specific Templates"
source_url: "https://wiki.multitheftauto.com/wiki/MTA_Wiki%3ASpecific_Templates"
revision_id: 81042
language: "en"
categories: ["Changes_in_2.9", "Changes_in_3.0", "MTA_Wiki:Editing"]
generated_at: "2026-07-26T16:16:07.357117+00:00"
---

# Help : MTA Wiki Specific Templates

Information about the specific MTA wiki page templates for this wiki. (They do probably not exists on other Mediawiki wiki's)

| [[{{{image}}}\|link=\|]] | Tip: If you want to avoid spacing between the page title and the template itself, you should include the template before __NOTOC__ other templates and/or magic words . |
| --- | --- |
|  |  |

## Funtion / event templates

### Deprecated function/event

Use this template to indicate functions or events that are being deleted from MTA because there is a more generic way to perform what they do (and they are necessary no longer). The last two arguments of this template aren't mandatory, and can be ignored if there isn't an alternative function or aditional text.

**Format:** {{Deprecated|alternativeFunction|more text}}

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions, but there should be a more generic way to perform what it does. |
| --- | --- |
|  |  |

|  | This function is deprecated. This means that its use is discouraged and that it might not exist in future versions. |
| --- | --- |
| Please use alternativeFunction instead. more text |  |

Wiki pages containing this template will be added to the [Category:Deprecated](https://wiki.multitheftauto.com/wiki/Category:Deprecated) for reference.

### Function/event needs example

Use this template to indicate when a function or event needs a scripting example.

**Format:** {{Needs Example}}

|  | Script Example Missing Function Help:MTA Wiki Specific Templates needs a script example, help out by writing one. |
| --- | --- |
| Before submitting check out Editing Guidelines Script Examples . |  |

Wiki pages containing this template will be added to the [Category:Needs Example](https://wiki.multitheftauto.com/wiki/Category:Needs_Example) for reference.

### Disabled function/event

Use this template to indicate when a function or event has been disabled in the MTA: SA source code. Normally there's an important reason for this. The last two parameters aren't mandatory and can be ignored.

**Format:** {{Disabled|reason|bugTrackerIssueNumber}}

|  | Function has been disabled. |
| --- | --- |
|  |  |

|  | Function has been disabled. |
| --- | --- |
| Reason/Note: reason - Bugtracker Issue: #bugTrackerIssueNumber |  |

Wiki pages containing this template will be added to the [Category:Needs Checking](https://wiki.multitheftauto.com/wiki/Category:Needs_Checking) and [Category:Disabled Functions and Events](https://wiki.multitheftauto.com/wiki/Category:Disabled_Functions_and_Events) for reference.

### Module only function/event

Use this template to indicate a module only function/event template. That will inform readers that this function is module specific and not build-in to MTA itself.
Note: You only have to add the module name not the 'Modules/' prefix.

**Format:** {{ModuleFunction|Module Name}}

|  | This function is provided by the external module ModuleName . You must install this module to use this function. |
| --- | --- |
|  |  |

### New function/event/change

Use this template to indicate a function, event or change that will be applied in a future version of MTA. This template is best used when it contains the function/event/change description, because it removes itself when MTA gets updated (MTA version is greater than the *targetVersion* specified in this template parameters). All arguments of this template are mandatory.
Notes: *targetVersion* parameter must be a number in the format 3.0XXX, where XXX is the version when the function/event/change will be applied. For example, if a function will be added in MTA version *2.0.1*, put 3.0*201* in *targetVersion*. *showVersion* parameter is only visual and specifies the text contained in "From version ... onwards".

**Format:** {{New feature/item|targetVersion|showVersion|Revision}}

ADDED/UPDATED IN VERSION 2.9 [r19999](https://buildinfo.mtasa.com/?Author=&Branch=&Revision=19999):

This template has *3.0157* and *2.9* and *19999* as parameters, so it'll be removed and only this text will be shown when MTA version is 3.1.2 or higher.

If you want to display a change from a previous version in the format of "Before version x.x", use the following code:

**Format:** {{Deprecated feature|untilVersion|showVersion}}

BEFORE VERSION 3.0

This template has *3.0300* and *3.0* versions as parameters, so this box will only be displayed until MTA's version is 3.0 or higher.  After that, it'll disappear completely.

## Article/Page/Category Maintenance

### Article Needs Checking

These are functions that need to be checked to ensure they do work as specified. If there are any problems with a function, example or the wiki page itself, attach a note to the top of the page and describe the problems.

**Format:** {{Needs Checking|STATE_PROBLEM_HERE}}

|  | This article needs checking. |
| --- | --- |
| Reason: STATE_PROBLEM_HERE |  |

Wiki pages attached to this template will be added to the [Category:Needs_Checking](https://wiki.multitheftauto.com/wiki/Category:Needs_Checking)

### Article Outdated

If the information in the article no longer applies and/or an alternative article exists you can use this template and link to the alternative article. If it is still useful and/or (partially) valid and needs to be updated or no alternative article exists use the 'Article Needs Checking' template.

**Format without reason:** {{Outdated}}

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
|  |  |

**Format with reason:** {{Outdated|The Reason HERE}}

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
| Reason: The Reason HERE |  |

Wiki pages attached to this template will be added to the [Category:Outdated Pages](https://wiki.multitheftauto.com/wiki/Category:Outdated_Pages)

### Article translation Outdated

If the article translation is outdated use this template.

**Format without subtext:** {{Outdatedtr}}

|  | This translated article is (partially) outdated and the information may no longer apply. |
| --- | --- |
|  |  |

**Format with subtext:** {{Outdatedtr|The subtext here}}

|  | This translated article is (partially) outdated and the information may no longer apply. |
| --- | --- |
| The subtext here |  |

Wiki pages attached to this template will be added to the Category:Outdated Pages

## General Templates

### Warning

Warning template for in-line warnings.

**Format:** {{Warning|Warning info here}}

| [[{{{image}}}\|link=\|]] | Warning: Warning info here |
| --- | --- |
|  |  |

Warning template for article warnings.

**Format:** {{Warning|Warning info here|true}}

|  | Warning: Warning info here |
| --- | --- |
|  |  |

### Note

**Note:** Note info here

The note box floats always right in the page/article.

**Format:** {{Note box|Note info here}}

Template for in-line note:

**Format:** {{Note|Note info here}}

| [[{{{image}}}\|link=\|]] | Note: Note info here |
| --- | --- |
|  |  |

Alternative in-line note:

**Format:** {{Important Note|Note info here}}

| [[{{{image}}}\|link=\|]] | Important Note: Note info here |
| --- | --- |
|  |  |

### Tip

**Format:** {{Tip|Text here}}

| [[{{{image}}}\|link=\|]] | Tip: Text here |
| --- | --- |
|  |  |

## Localization

### Localized article

Adds a link to a localized article in this wiki, with a flag which represents the language the article is written in.

**Format:** {{Localized article|Main Page|Wiki's main page|us|en}}

[Wiki's main page](mta://reference/misc/main-page.md) 
For more information about the use of the template, please refer to [its page](https://wiki.multitheftauto.com/wiki/Template:Localized_article).

## Special

### Delete

Mark a page for deletion, so administrators can decide if they remove the page.

**Format:** {{Delete|Reason here}}

|  | This page is marked for deletion. |
| --- | --- |
| Reason: Reason Here Actions: Delete (Administrators) - Discuss - What links here - Category |  |

Wiki pages attached to this template will be added to the [Category:MTA Wiki:Delete](https://wiki.multitheftauto.com/wiki/Category:MTA_Wiki:Delete)
