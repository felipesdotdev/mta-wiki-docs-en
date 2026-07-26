---
doc_id: "mta-wiki:2718"
title: "PHP SDK"
source_title: "PHP SDK"
source_url: "https://wiki.multitheftauto.com/wiki/PHP_SDK"
revision_id: 79883
language: "en"
categories: ["Tutorials", "SDK"]
generated_at: "2026-07-26T16:16:27.480469+00:00"
---

# PHP SDK

You can access the MTA Web Interface from almost any programming language that can request web pages. PHP can do this very easily.

This SDK provides one function call that will allow you to call any exported script functions on any server that you have access to.

## Installation

### Prerequisites

This SDK requires PHP 7.1 or greater.

### HTTPlug client abstraction

As this SDK uses HTTPlug, you will have to require some libraries for get it working. See [“HTTPlug for library users”](http://docs.php-http.org/en/latest/httplug/users.html) for more info.

warning: **Note**: If you don’t follow this requirement before require the SDK, composer will throw you an error.

### Setup

The only supported installation method is via [Composer](https://getcomposer.org). Run the following command to require this SDK in your project:

```
composer require multitheftauto/mtasa-php-sdk
```

## A simple example

There are three ways to call an MTA server’s exported functions, as shown in the following example:

```
<?php

require_once('vendor/autoload.php');

use MultiTheftAuto\Sdk\Mta;
use MultiTheftAuto\Sdk\Model\Server;
use MultiTheftAuto\Sdk\Model\Authentication;

$server = new Server('127.0.0.1', 22005);
$auth = new Authentication('myUser', 'myPassword');
$mta = new Mta($server, $auth);

$response = $mta->getResource('someResource')->call('callableFunction', $arg1, $arg2, $arg3, ...);
// or
$response = $mta->getResource('someResource')->call->callableFunction($arg1, $arg2, $arg3, ...);

var_dump($response);
```

## A page that can be called by [callRemote](mta://scripting/server/functions/callremote.md)

This example just adds two numbers passed to it by a Lua script.

**PHP:** (for the page that Lua expects to be at *http://www.example.com/page.php*)

```
<?php 

require_once('vendor/autoload.php');

use MultiTheftAuto\Sdk\Mta;

$input = Mta::getInput();
Mta::doReturn($input[0] + $input[1]);
```

**Lua:**

```
-- result is called when the function returns
function result(sum)
    outputChatBox(sum)
end
function addNumbers(number1, number2)
    callRemote ( "http://www.example.com/page.php", result, number1, number2 )
end 
addNumbers ( 123, 456 ) -- call the function
```

## Releases

Visit [the releases page on GitHub](https://github.com/multitheftauto/mtasa-php-sdk/releases) to download the SDK.

### Note for Python

There is a community made Python SDK with the same semantics on [the OwlGaming Gitlab](https://gitlab.com/OwlGamingCommunity/mta-python-sdk) for use on Python projects.

## Version History

You can see in the [repository changelog file](https://github.com/multitheftauto/mtasa-php-sdk/blob/master/CHANGELOG.md) the changes applied.
