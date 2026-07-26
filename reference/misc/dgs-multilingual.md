---
doc_id: "mta-wiki:12605"
title: "DGS Multilingual"
source_title: "DGS Multilingual"
source_url: "https://wiki.multitheftauto.com/wiki/DGS_Multilingual"
revision_id: 76065
language: "en"
categories: []
generated_at: "2026-07-26T16:11:19.366591+00:00"
---

# DGS Multilingual

Description

- 1. DGS has a built-in multilingual (multi-language) system.

- 2. multilingual allows dynamic language changing and prevents non-essential GUI recreating or text reset by code.

- 3. DGS multilingual system will specify the structure of **Translation Table** (Dictionary).

## Usage 1 (Basic usage)

- 0. Don't forget to **import DGS Head** or use "**export.dgs:**".

- 1. A **Translation Table** (Dictionary) should be specified:

```
Dict = {
	TestText1="Welcome To DGS",
}
```

- 2. And, send the dictionary into DGS:

```
dgsSetTranslationTable("testDict",Dict) --Name,Dictionary.
```

- 3. Now, DGS knows that dictionary, we need to tell DGS we want to use it:

```
dgsSetAttachTranslation("testDict") --This is global setting to one resource
```

- 3. Create a label:

```
label = dgsCreateLabel (0.51, 0.54, 0.16, 0.14, {"TestText"}, true )
```

## Usage 2 (Basic usage)

- 0. Don't forget to **import DGS Head** or use "**export.dgs:**".

- 1. A **Translation Table** (Dictionary) should be specified:

```
Dict = {
	TestText1="Welcome To DGS",
}
```

- 2. And, send the dictionary into DGS:

```
dgsSetTranslationTable("testDict",Dict) --Name,Dictionary.
```

- 3. Now, DGS knows that dictionary, we can create a label and attach its text to the dictionary:

```
label = dgsCreateLabel (0.51, 0.54, 0.16, 0.14, {"TestText"}, true )
dgsAttachToTranslation(label,"testDict") --Only attach one element to the dictionary.
```

Or you can also do:

```
label = dgsCreateLabel (0.51, 0.54, 0.16, 0.14, "", true )
dgsAttachToTranslation(label,"testDict") --Only attach one element to the dictionary.
dgsSetText(label,{"TestText"})
```

## Usage 3 (With parameters)

- 0. Don't forget to **import DGS Head** or use "**export.dgs:**".

- 1. A **Translation Table** (Dictionary) should be specified. And here we have an extra **%rep%** that takes the place of **parameter**:

```
Dict = {
	TestText1="Welcome To %rep%",
	TestText2="Welcome To %rep% %rep%",
}
```

- 2. And, send the dictionary into DGS:

```
dgsSetTranslationTable("testDict",Dict) --Name,Dictionary.
```

- 3. Now, DGS knows that dictionary, tell DGS we want to use it:

```
dgsSetAttachTranslation("testDict")
```

- 4. Create a label, pass **"DGS"** as the argument

```
label1 = dgsCreateLabel (0.51, 0.54, 0.16, 0.14, {"TestText1","DGS"}, true )
label2 = dgsCreateLabel (0.51, 0.64, 0.16, 0.14, {"TestText2","DGS",":D"}, true )  -- 2 parameters.
label3 = dgsCreateLabel (0.51, 0.74, 0.16, 0.14, {"TestText2","DGS"}, true )  -- the rest unused '''%rep%''' will be deleted.
```

## Usage 4 (High Level Translation)

- 0. Don't forget to **import DGS Head** or use "**export.dgs:**".

- 1. A **Translation Table** (Dictionary) should be specified. And DGS parameter support 2nd level translation:

```
Dict = {
	TestText="Welcome To %rep%. Have a good time %rep%",
	Smile=":)",
}
```

- 2. And, send the dictionary into DGS:

```
dgsSetTranslationTable("testDict",Dict) --Name,Dictionary.
```

- 3. Now, DGS knows that dictionary, tell DGS we want to use it:

```
dgsSetAttachTranslation("testDict")
```

- 4. Create a label, and use 2nd level translation:

```
label = dgsCreateLabel (0.51, 0.54, 0.16, 0.14, {"TestText","DGS", {"Smile"}}, true )
```

or more

```
label = dgsCreateLabel (0.51, 0.54, 0.16, 0.14, {"TestText","DGS", {"TestText",{"TestText","Smile","Smile"},"Smile"}}, true )
```

## Usage 5 (Conditional Translation)

- 0. Don't forget to **import DGS Head** or use "**export.dgs:**".

- 1. A **Translation Table** (Dictionary) should be specified. And the translation item should be a table includes *condition*s and *result*s.

```
testDict = {
	exampleTranslation = {
		"health == 'Superman'",     "You are a superman",
		"find({0}, health)",               "Your health is 0",
		"health <= 40",                   "Your health is low",
		"health <= 60",                   "Your health is medium",
		"health <= 80",                   "Your health is high",
		"Your health is $health",
	}
}
```

- 2. The table seems to be hard to understand. But actually, you can understand it like this:

```
if health == 'Superman' then          --condition 1
	return "You are a superman"       --result 1
elseif find({0}, health) then              --condition 2
	return "Your health is 0"              --result 2
elseif health <= 40 then                  --condition 3
	return "Your health is low"          --result 3
elseif health <= 60 then                  --condition 4
	return "Your health is medium"   --result 4
elseif health <= 80 then                  --condition 5
	return "Your health is high"         --result 5
else
	return "Your health is "..health     --result if not matched (this must exist)
end
```

- 3. In the condition, we provides [string](mta://reference/misc/string.md), [table](mta://reference/misc/table.md) and following functions:

```
bool find( table matchTable, mixed anythingToMatch )
```

- 4. Then send the dictionary into DGS:

```
dgsSetTranslationTable("testDict",testDict) --Name,Dictionary.
```

- 5. Now, DGS knows that dictionary, tell DGS we want to use it:

```
dgsSetAttachTranslation("testDict")
```

- 6. Create a label, and use conditional translation:

```
label = dgsCreateLabel (0.51, 0.54, 0.16, 0.14, { "TestText", health=40 }, true )
```

With DGS translation property listener, you can also do this:

```
label = dgsCreateLabel (0.51, 0.54, 0.16, 0.14, {"TestText", health=20 }, true )
dgsTranslationAddPropertyListener(label,"health")		--Properties have higher priority than the items in text table
dgsSetProperty(label,"health","Superman")
setTimer(function()
	dgsSetProperty(label,"health",60)
end,1000,1)
```

## Usage 6 (Language Change)

- 0. Don't forget to **import DGS Head** or use "**export.dgs:**".

- 1. A **Translation Table** (Dictionary) should be specified:

```
Dict1 = {
	TestText="Welcome To DGS",
}
Dict2 = {
	TestText="SGD oT emocleW",
}
```

- 2. And, send the dictionary into DGS:

```
dgsSetTranslationTable("testDict",Dict1) --Name,Dictionary.
```

- 3. Now, DGS knows that dictionary, tell DGS we want to use it:

```
dgsSetAttachTranslation("testDict")
```

- 4. Create a label:

```
label = dgsCreateLabel (0.51, 0.54, 0.16, 0.14, {"TestText"}, true )
```

- 4. Replace the dictionary (language changed), and you will see the text changed automatically:

```
dgsSetTranslationTable("testDict",Dict2)
```
