---
doc_id: "mta-wiki:5514"
title: "Translating"
source_title: "Translating"
source_url: "https://wiki.multitheftauto.com/wiki/Translating"
revision_id: 75527
language: "en"
categories: ["Outdated_Pages", "Development"]
generated_at: "2026-07-26T16:17:00.907219+00:00"
---

# Translating

|  | This article is (partially) outdated and the information may no longer apply. |
| --- | --- |
| Reason: "See https://multitheftauto.crowdin.com/multitheftauto " |  |

It's proposed that we have a way of translating MTA into different languages, and allowing our community to contribute their translations.

## Why?

We've seen a couple of people try to fork MTA to make arabic and polish translations. We want to discourage forking for such trivial reasons if we can. Also, we'd encourage more players to play MTA if they can understand it.

## How

The library *gettext* seems to be the standard way of doing this, at least in the Linux world.

Writing our own seems to be a bad idea - we don't know enough about languages to do this.

We should be able to use utf8 to encode the strings, meaning very little of our code should need to change. Most of our current support for unicode is done with utf8 so this seems easy. It remains to be seen how much needs to be changed to support this.

## The code

Gettext works by wrapping strings in calls to the *gettext* function.
So:

```
[c++]
Print ( "Press Q to shut down the server!\n" );
```

Becomes:

```
[c++]
Print ( gettext("Press Q to shut down the server!\n") );
```

Though, we probably don't want to include new line characters, so it becomes:

```
[c++]
Print ( "%s\n", gettext("Press Q to shut down the server!"));
```

Plus, it can be convenient to have a shorthand, and it seems that defining _ as gettext is conventional, so you end up with:

```
[c++]
Print ( "%s\n", _("Press Q to shut down the server!"));
```

Maybe we should make a short hand version of Print that always does a new line?

## Generating the translation template

From the code you can generate the template that lists the strings that need to be generated. gettext comes with a tool for this, and I've wrapped it up in a script that makes it more convenient. It's currently utils/build_gettext_catalog.py (though not yet committed).

This scans all the cpp and h files in the MTA10 and MTA10_SERVER directories and passes them into the xgettext executable which generates a *pot* file, which looks something like the following:

```
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2010-12-20 19:27+0000\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=CHARSET\n"
"Content-Transfer-Encoding: 8bit\n"

#. Couldn't load our mod
msgid "Press Q to shut down the server!"
msgstr ""
```

Notice that comments from the code are extracted and placed above the strings, so we can provide guidance for what each string's purpose is.

## Editing

The template itself isn't edited, I think. You can create a copy of it and generate a new translation by filling in the msgstr strings. There are editors, such as the cross platform poedit that deals with these files and handles various useful things such as validating them and merging them when new strings are added to the template. This seems pretty easy to use. It notices things such as missing formatting specifiers (%s etc) in strings.

Once you've edited the file, you can save it as a .po file. This is basically identical to the .pot file, just has translations in it.

These files are turned into .mo files which are compiled versions. Poedit does this for you, but I've made a script that does it in the utils directory.

## Where?

I've placed the translations in a root *Translations* directory (alongside MTA10 and MTA10_SERVER). The translations are shared between client and server, I'm not sure if this is a good or bad thing, but it could be changed. It might save work and disk space somewhat, though we probably want the translations to be placed in the server and client directories anyway.

## Making it work

To make it work, you link against libintl.lib (in vendor/gettext/libs) and have the dll libintl3.dll along side the executables.

Currently I've only tested this in the CServerImpl.cpp file, adding this at the top:

```
[c++]
#include <libintl.h>
#define _ gettext
```

Then this in the constructor:

```
[c++]
char* s = setlocale(LC_ALL, "");
bindtextdomain("messages", "translations/"); // specifies the directory to look in
textdomain( "messages");
```

## Files

We would ship the .mo files. Each language would have a directory in the Translations directory, e.g. en_US, fr_FR etc, inside which is a directory LC_MESSAGES, inside which is a messages.mo file. We can't really change anything except where this directory is and what the .mo file is called, the locale and the LC_MESSAGES directories have to be there. It seems.

## What?

We ideally allow every part of MTA client and server to be translated. The server is less important, but we ought to do it if we can.

## User Interface

We'd need to provide a user interface for changing language. We can use the system settings (somehow - gettext may do this for us?) to work out the right language. But often, users may be more comfortable with another language (or their translation might be awful).

This would make most sense to be in the 'Interface' tab of the client settings. Server-side, we'd provide a config setting.

## The hard work

Once the system is set up, some people need to go through and mark up each string that we want to be translatable. This could be anyone really as coding isn't really required (except with some odd strings perhaps).

## The really hard work

Getting people to translate it is obviously hard work. But I imagine we have a lot of keen community members who will do this, if we release the relevant files and isnstruct them on how to do it. As the tools we're using are fairly standard, we may find that people already know how to use them if they've translated other projects.

## What else?

Perhaps we want to add a 'server language' setting that gets shown in the server browser. I'm not sure if we want to encourage such ghettoization, but it might be of benefit to our users.

## Notes

Do we need strlen to not work on utf8 strings in 1.1? Could we just make it the same as utf8len (or whatever it's called)?
