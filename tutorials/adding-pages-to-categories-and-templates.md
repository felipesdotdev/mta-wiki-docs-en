---
doc_id: "mta-wiki:7155"
title: "Help : Adding Pages to Categories and Templates"
source_title: "Adding Pages to Categories and Templates"
source_url: "https://wiki.multitheftauto.com/wiki/Adding_Pages_to_Categories_and_Templates"
revision_id: 77685
language: "en"
categories: ["Adding_Pages_to_Categories_and_Templates", "MTA_Wiki:Editing", "Tutorial"]
generated_at: "2026-07-26T16:11:50.623551+00:00"
---

# Help : Adding Pages to Categories and Templates

Introduction

Did you create a new page, such as a function, and it isn't showing up in a list? Did you try and edit it in only to see {{weird_tags_like_this}} instead of text relating to the page you viewed? Welcome to the world of templates. We have noticed in [RecentChanges](https://wiki.multitheftauto.com/wiki/Special:RecentChanges) that people are making pages and not linking to them properly. **These pages are being lost in the bowels of the Wiki!**

We also use categories in this wiki, but they are not as crucial as templates. Please read on to learn about both and to understand how to contribute to our wiki properly.

# Template

### What is a Template

It is like a big copy paste on a clipboard. You write a template tag on another page and it writes everything that was on the template page.

- **Why Use Templates?**

It allows the same information to be represented in multiple places, without duplicating texts and updating them manually numerous times.

- **Example?**

Look at the page source (edit button) on our functions or event pages. You can see that the functions aren't actually listed there, each function group has its own template. The main use for this is to fill out the "See Also" section of individual functions with their related functions.

### How Do You Make/Edit/Use a Template?

The best way to teach is by example. I will need a template to direct people to this guide from multiple pages in the wiki. Let's just create this template together! FUN!

#### 1. Choosing a Template Name

The best template name explains what it is. Typically the best thing is to make the template URL identical to the actual page. Therefore I am going to use:

```
http://wiki.multitheftauto.com/index.php?title=Template:Adding_Pages_to_Categories_and_Templates
```

**IMPORTANT:** Remember that all wiki pages are case sensitive. The same page can exist in uppercase and lowercase! Capitalize appropriately.

If I tried to link to a template that doesn't exist this happens:
Template: link to nonexistant template click here to create

So as you can see, it is better we create the template before attempting to link to it!

#### 2. Filling out the Template

At the template page, hit create page, and you'll see the edit field box. Type in whatever you need to be said in other pages and save the page. It could be simple text, links to a set of functions, or even as advanced as a bit of code that determines something, such as our future functions template. If you were trying to add to our functions/events then you would just edit a link to your function into the template. Don't screw it up or I will be disappointed in you!

From this point, you use the template page name as a tag inside the pages where you want to use it. My template tag is:

```
{{Adding_Pages_to_Categories_and_Templates}}
```

#### 3. Demonstration

So here I will actually link to the template. If you check the template page source, you will see exactly what is printed below:

*Contributors:* Did you create a page but it's not on this list? Confused? **Read: [Adding Pages to Categories and Templates](mta://tutorials/adding-pages-to-categories-and-templates.md)**

**Note:** The easiest way to reach a template that was used on a page is to edit the page and scroll to the bottom. A list of all templates used will appear with links to the template pages. For something like the main function pages you have to edit the ENTIRE page to see templates used at the bottom, they do not appear if you only edit a section.

# Category

### What is a Category

Categories group pages together. The categories have their own special page where all the grouped pages are alphabetized. Think of them like sorting the Wiki into folders for common pages. For example here is a link to the server functions category page: [Category:Server_functions](https://wiki.multitheftauto.com/wiki/Category:Server_functions)

### How do I Make/Edit/Use Categories

A page is put into a category by editing the following syntax into a page:

```
[[:Category:pagename]]
```

You do need to create the category page just as you would a template. Again, you simply go to the URL of the category page you want to make. The format is:

```
http://wiki.multitheftauto.com/index.php?title=Category:Page_Name_Here
```

For the category page itself, you simply write a small explanation what the category (folder) is about.

If you look at the source of the pages listed in [Category:Server_functions](https://wiki.multitheftauto.com/wiki/Category:Server_functions), you may notice that the category tag is not in them! It actually is there, but it is being applied through the clever combination of a template with the category embedded.

Those nice colored stripes you see at the tops of pages are all templates that have a category tag embedded. This was designed to make it hard for people to mess-up categories. For example, look at the page source for the blue stripe that says "Client and Server Function" [http://wiki.multitheftauto.com/index.php?title=Template:Server_client_function&action=edit](http://wiki.multitheftauto.com/index.php?title=Template:Server_client_function&action=edit)

### Demonstration

I have put a category tag in this page. This is reflected at the very bottom of the page you are reading right now. The category page just happens to be the exact same name. Unlike templates, it is not typical to name the category after a page. They are more like folder names. This is just for demonstration however.

The category page is here: [Category:Adding_Pages_to_Categories_and_Templates](https://wiki.multitheftauto.com/wiki/Category:Adding_Pages_to_Categories_and_Templates)

# More Info

### Lists of Templates and Categories

Looking for template and category listings? This is one thing [SpecialPages](https://wiki.multitheftauto.com/wiki/Special:SpecialPages) is for.

**Templates:**

- [Special:UncategorizedTemplates](https://wiki.multitheftauto.com/wiki/Special:UncategorizedTemplates)

Templates not organized into templates (ie think of categories as folders).

- [Special:UnusedTemplates](https://wiki.multitheftauto.com/wiki/Special:UnusedTemplates)

Unused templates

- [Special:WantedTemplates](https://wiki.multitheftauto.com/wiki/Special:WantedTemplates)

Tags are linked to this template, but the page itself doesn't exist. It still works de facto. You need to hit create on the template page.

- [Special:MostLinkedTemplates](https://wiki.multitheftauto.com/wiki/Special:MostTranscludedPages)

Templates that were tagged in the most pages

**Categories:**

- [Special:Categories](https://wiki.multitheftauto.com/wiki/Special:Categories)

All categories overview.

- [Special:UncategorizedCategories](https://wiki.multitheftauto.com/wiki/Special:UncategorizedCategories)

Categories not within another category (ie not used as subfolders of folders).

- [Special:UnusedCategories](https://wiki.multitheftauto.com/wiki/Special:UnusedCategories)

Unused categories

- [Special:WantedCategories](https://wiki.multitheftauto.com/wiki/Special:WantedCategories)

Tags are linked to this category, but the page itself doesn't exist. It still works de facto. You need to hit create on the category page.

- [Special:MostLinkedCategories](https://wiki.multitheftauto.com/wiki/Special:MostLinkedCategories)

Categories that were tagegd in the most places

### Further Reference

[http://en.wikipedia.org/wiki/Help:Template](http://en.wikipedia.org/wiki/Help:Template)  

[http://en.wikipedia.org/wiki/Help:Category](http://en.wikipedia.org/wiki/Help:Category)

### See Also

[MTA_Wiki:Editing_Guidelines](mta://scripting/concepts/mta-wiki-editing-guidelines.md) - This is a complete overview of how we use Wiki for MTA, this was only part of it. Please read this!

### Questions?

Best way to discuss wiki is live on IRC. See the community box on the [Main Page](mta://reference/misc/main-page.md) for more info.
