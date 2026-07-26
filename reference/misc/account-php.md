---
doc_id: "mta-wiki:7330"
title: "Account PHP"
source_title: "Account PHP"
source_url: "https://wiki.multitheftauto.com/wiki/Account_PHP"
revision_id: 49414
language: "en"
categories: []
generated_at: "2026-07-26T16:11:54.368451+00:00"
---

# Account PHP

Check MTA server account

This php function will return true if the password matches the hash from the accounts database

```
function passwordMatch( $plain, $hash )
{
	//-- Empty passwords never match
	if ( $plain == "" || $hash == "" )
		return false;

	if ( strlen($hash) == 64 + 32 + 1 )
	{
		//-- SHA256 + type + salt
		$strSha256 = substr( $hash, 0, 64 );
		$strType = substr( $hash, 64, 1 );
		$strSalt = substr( $hash, 65, 32 );

		//-- Password hash was generated from MD5, so do the same thing for the test
		if ( $strType == "1" )
			$plain = strtoupper(md5($plain));

		$strPasswordHashed = strtoupper(hash( "sha256", $strSalt . $plain ));
		return $strPasswordHashed == $strSha256;
	}
	else
	if ( strlen($hash) == 32 )
	{
		//-- MD5
		return strtoupper(md5($plain)) == $hash;
	}
	return false;
}
```
