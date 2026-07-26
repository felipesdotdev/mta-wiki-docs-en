---
doc_id: "mta-wiki:2719"
title: "Perl SDK"
source_title: "Perl SDK"
source_url: "https://wiki.multitheftauto.com/wiki/Perl_SDK"
revision_id: 79885
language: "en"
categories: ["SDK", "Tutorials"]
generated_at: "2026-07-26T16:16:28.220820+00:00"
---

# Perl SDK

Currently there is not a Perl SDK as such, but you can use the following code to call a function on an MTA server, assuming you have access:

```
using JSON;

sub callFunction {
	my ($server, $resourcename, $functionname) = @_;
	my $content = objToJson([@_[3..$#_]]);
	$ua = LWP::UserAgent->new;
	$ua->parse_head(0);
	$ua->agent("");
	my $url = "http://" . $server . "/" . $resourcename . "/call/" . $functionname;
	$req = HTTP::Request->new(POST => $url);
	$req->content_type('application/x-www-form-urlencoded');
        $req->content($content);
	$req->header('Accept' => 'text/html');
	$res = $ua->request($req);
	my $ret = "";
	eval {
		$ret = jsonToObj($res->content);
	};
	return $ret;
}
```

This requires that you install the JSON package. You can do this easily by navigating to your perl 'bin' directory and executing "cpan", then typing "install JSON".

Syntax:

```
my $ret = callFunction("hostname:httpPort", "resourceName", "functionName" [, args ...]);
```

The function returns an array of the values returned by the function.
