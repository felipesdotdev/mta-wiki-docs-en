---
doc_id: "mta-wiki:9159"
title: "Authorized Serial Account Protection"
source_title: "Authorized Serial Account Protection"
source_url: "https://wiki.multitheftauto.com/wiki/Authorized_Serial_Account_Protection"
revision_id: 80568
language: "en"
categories: ["Scripting_Concepts"]
---

# Authorized Serial Account Protection

FAQ

## Help, I can't login (game)

To allow the last attempted serial, use the **authserial** command in the server console.  

For example, to allow the last attempted serial for account *MrBob*, enter the following command in the server console:

```
authserial MrBob
```

## Help, I can't login (HTTP)

To login to the HTTP web interface, there are two options:

#### Authorize an IP address:

- Join the MTA server

- Login to the account

- Disconnect from MTA server (optional)

- Login via HTTP

or

#### Set a special password:

- Use the command  **authserial <account_name> httppass** in the server console

- Note the supplied 7 digit code

- Login via HTTP and append the supplied 7 digit code to your password

# Main documentation

## Introduction

New from 1.5.3, Authorized Serial Account Protection provides a way to prevent password reuse causing damage to your server.

## How to enable

Open **mtaserver.conf** and find *<auth_serial_groups>* and change to below.
(If *<auth_serial_groups>* does not exist, then add it)

```
<auth_serial_groups>Admin</auth_serial_groups>
```

If you wish to protect other ACL groups, then add them separated by commas, e.g.:

```
<auth_serial_groups>Admin,SuperModerator</auth_serial_groups>
```

## How to disable

Open **mtaserver.conf** and find *<auth_serial_groups>* and change to below

```
<auth_serial_groups></auth_serial_groups>
```

| [[{{{image}}}\|link=\|]] | Note: Authorized Serial Account Protection helps prevent your server from getting hacked. If there is a chance any of your admins are using the same password on other servers, then do not disable this feature. |
| --- | --- |
|  |  |

## How to use

To allow the last attempted serial for an account, enter the following command in the server console:

```
authserial <account_name>
```

To view authorized serials for an account:

```
authserial <account_name> list
```

To remove the newest authorized serial for an account:

```
authserial <account_name> remove
```

To enable HTTP login from an unauthorized IP, use the following command to get a 7 digit code which should be appended to the HTTP login password *(Requires server version 1.5.4-9.11302)*

```
authserial <account_name> httppass
```
