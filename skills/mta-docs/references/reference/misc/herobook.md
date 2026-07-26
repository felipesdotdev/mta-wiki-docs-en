---
doc_id: "mta-wiki:6981"
title: "HeroBook"
source_title: "HeroBook"
source_url: "https://wiki.multitheftauto.com/wiki/HeroBook"
revision_id: 34584
language: "en"
categories: []
---

# HeroBook

Description

It's hell of a lot of work to build tons of GUIs for police manuals or other books on servers. HeroBook is a system that allows ANY user to create a book or a novel rather. The server controls who is able to write a book through exported functions, and the server controls who is able to read what book. Check out HeroInventory, you will be able to integrate this book system into HeroInventory for smoother usage.

## Integrate Into HeroInventory

More information on HeroInventory can be found here: [http://wiki.multitheftauto.com/wiki/HeroInventory](http://wiki.multitheftauto.com/wiki/HeroInventory)

- **Download an image that will suit the book you're trying to integrate.**

- **Add this image into meta.xml**

```
<file src="images/items/BookImageName.png" />
```

- **Add a new items into 'g_items.lua'** Below is simply an example.

```
{"images/items/BookImageName.png", "LSPD Book", "Books"} -- ITEM ID: 2
```

It should look somewhat like this:

```
itemArchive = -- {picture, name, group_name}
{
	{"images/items/Hat.png", "Hat", "Clothes"}, -- ITEM ID: 1 - This is an example.
	{"images/items/BookImageName.png", "LSPD Book", "Books"} -- ITEM ID: 2
}
```

- **In server/s_item_use.lua, you can now create a reaction to clicking on the book.**

```
if itemID == 2 then
   exports["hero-book"]:showClientBook( source, 1 )
end
```

The code above simply shows a created book (Book ID #1). In this example, book ID #1 is a LSPD Book. The client should now be reading the LSPD book.

## Functions

### deleteBook

```
nil deleteAllBooks(  )
```

```
@title
		deleteAllBooks
	@author
		Malicious Hero.
	@parameters

	@description
		This will delete all books.
```

### deleteBook

```
nil deleteBook( int book_id )
```

```
@title
		deleteBook
	@author
		Malicious Hero.
	@parameters
		book_id - The book's ID.
	@description
		This will delete a book.
```

### addBook

```
nil addBook( string title, element authorElement, table content )
```

```
@title
		addBook
	@author
		Malicious Hero.
	@parameters
		title - The title of the book.
		authorElement - Not the author's name. The actual element of the player.
		content - The content of the book; Which is stored in a table for page reasons.
	@description
		This will add a book to the SQL database.
```

### updateBook

```
nil updateBook( int book_id, table tableData)
```

```
@title
		updateBook
	@author
		Malicious Hero.
	@parameters
		book_id - The book's ID.
		tableData - The data of the book. View getBookData for more information.
	@description
		This will save book data into the SQL database.
```

### getBookData

```
table getBookData( int book_id, string highlight )
```

```
@title
		getBookData
	@author
		Malicious Hero.
	@parameters
		book_id - The book's ID.
		highlight - Searches only one specific piece of the book data.
	@description
		This will fetch data for a book into table data. Use the SQL
		field names as reference for variables.
```

## Player Usage Functions

### showClientBook

```
nil showClientBook( element playerElement, int book_id )
```

```
@title
		showClientBook
	@author
		Malicious Hero.
	@parameters
		playerElement - The element you want to edit the book.
		book_id - The book's ID.
	@description
		This will make a client read a book.
```

### clientEditBook

```
nil clientEditBook( element playerElement, int book_id )
```

```
@title
		clientEditBook
	@author
		Malicious Hero.
	@parameters
		playerElement - The element you want to edit the book.
		book_id - The book's ID.
	@description
		This will make a client edit a book.
```
