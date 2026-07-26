---
doc_id: "mta-wiki:7834"
title: "SendMailTo"
source_title: "SendMailTo"
source_url: "https://wiki.multitheftauto.com/wiki/SendMailTo"
revision_id: 40951
language: "en"
categories: ["Useful_Functions", "Utility_templates"]
generated_at: "2026-07-26T16:16:36.630760+00:00"
---

# SendMailTo

This function allows you to send a mail with a php system
You must include the "MTASDK" in your PHP file. ([https://wiki.multitheftauto.com/wiki/PHP_SDK](https://wiki.multitheftauto.com/wiki/PHP_SDK))

## Syntax

```
string sendMailTo( string mail, string sender, string headertext, string text)
```

## Required Arguments

- **text:** The text of the e-mail is in the.

## Optional Arguments

*NOTE:* When using optional arguments, you might need to supply all arguments before the one you wish to use. For more information on optional arguments, see [optional arguments](mta://reference/misc/optional-arguments--f0d8694a.md).

- **mail:** Here, the recipient is defined.

- **sender:** Here, the sender must be entered that sent the e-mail.

- **headertext:** Here the subject text needs to go, which it is e-mail in the subject line.

## Code

```
function sendMailTo ( mail, sender, headertext, text )

	callRemote ( "http://www.example.com/send.php", EMailAccepted, mail, sender, headertext, text )

end

function EMailAccepted ()

	outputDebugString ( "E-Mail was succesfully sended." )

end
```

**PHP:** You must create a send.php file, then then convert to UTF-8 on your FTP upload.

```
[php]
<?php 
	
	include ( "mta_sdk.php" );
	$input = mta::getInput();
	
	mail($input[0], $input[2], $input[3], "From: ".$input[1]."\n" . "Content-Type: text/html; charset=iso-8859-1\n"); 
?>
```

## Example

Click to collapse [-]
Server

```
function MailText ( player, cmd, headertext, ... )
	local text = table.concat ( {...}, " " )
	if text then
		
		sendMailTo ( "yourmail@example.com", "sendermail@example.com", headertext, text )
		
	end
	
end
addCommandHandler ( "sendmail", MailText )
```

Author: SuperHomie(me)
