---
doc_id: "mta-wiki:8301"
title: "OnClientBrowserLoadingFailed"
source_title: "OnClientBrowserLoadingFailed"
source_url: "https://wiki.multitheftauto.com/wiki/OnClientBrowserLoadingFailed"
revision_id: 82085
language: "en"
categories: ["Client_events", "Changes_in_1.5"]
---

# OnClientBrowserLoadingFailed

The event is triggered when the browser can not load the page.

| [[{{{image}}}\|link=\|]] | Note: Error Codes: ERR_NONE 0 ERR_FAILED -2 ERR_ABORTED -3 ERR_INVALID_ARGUMENT -4 ERR_INVALID_HANDLE -5 ERR_FILE_NOT_FOUND -6 ERR_TIMED_OUT -7 ERR_FILE_TOO_BIG -8 ERR_UNEXPECTED -9 ERR_ACCESS_DENIED -10 ERR_NOT_IMPLEMENTED -11 ERR_CONNECTION_CLOSED -100 ERR_CONNECTION_RESET -101 ERR_CONNECTION_REFUSED -102 ERR_CONNECTION_ABORTED -103 ERR_CONNECTION_FAILED -104 ERR_NAME_NOT_RESOLVED -105 ERR_INTERNET_DISCONNECTED -106 ERR_SSL_PROTOCOL_ERROR -107 ERR_ADDRESS_INVALID -108 ERR_ADDRESS_UNREACHABLE -109 ERR_SSL_CLIENT_AUTH_CERT_NEEDED -110 ERR_TUNNEL_CONNECTION_FAILED -111 ERR_NO_SSL_VERSIONS_ENABLED -112 ERR_SSL_VERSION_OR_CIPHER_MISMATCH -113 ERR_SSL_RENEGOTIATION_REQUESTED -114 ERR_CERT_COMMON_NAME_INVALID -200 ERR_CERT_DATE_INVALID -201 ERR_CERT_AUTHORITY_INVALID -202 ERR_CERT_CONTAINS_ERRORS -203 ERR_CERT_NO_REVOCATION_MECHANISM -204 ERR_CERT_UNABLE_TO_CHECK_REVOCATION -205 ERR_CERT_REVOKED -206 ERR_CERT_INVALID -207 ERR_CERT_END -208 ERR_INVALID_URL -300 ERR_DISALLOWED_URL_SCHEME -301 ERR_UNKNOWN_URL_SCHEME -302 ERR_TOO_MANY_REDIRECTS -310 ERR_UNSAFE_REDIRECT -311 ERR_UNSAFE_PORT -312 ERR_INVALID_RESPONSE -320 ERR_INVALID_CHUNKED_ENCODING -321 ERR_METHOD_NOT_SUPPORTED -322 ERR_UNEXPECTED_PROXY_AUTH -323 ERR_EMPTY_RESPONSE -324 ERR_RESPONSE_HEADERS_TOO_BIG -325 ERR_CACHE_MISS -400 ERR_INSECURE_RESPONSE -501 |
| --- | --- |
|  |  |

## Parameters

```
string url, int errorCode, string errorDescription
```

- **url:** the requested URL.

- **errorCode:** the error code.

- **errorDescription:** a short description.

## Source

The [browser](mta://reference/misc/element-browser.md) element.

## Example

```
addEventHandler("onClientBrowserLoadingFailed", root,
	function(url, errorCode, errorDescription)
		outputChatBox("This webpage is not available" .. url .. "Unknown" .. errorCode .. "Unknown" .. errorDescription)
	end
)
```

## See Also

- [onClientBrowserCreated](mta://scripting/client/events/onclientbrowsercreated.md)

- [onClientBrowserCursorChange](mta://scripting/client/events/onclientbrowsercursorchange.md)

- [onClientBrowserDocumentReady](mta://scripting/client/events/onclientbrowserdocumentready.md)

- [onClientBrowserInputFocusChanged](mta://scripting/client/events/onclientbrowserinputfocuschanged.md)

- onClientBrowserLoadingFailed

- [onClientBrowserLoadingStart](mta://scripting/client/events/onclientbrowserloadingstart.md)

- [onClientBrowserNavigate](mta://scripting/client/events/onclientbrowsernavigate.md)

- [onClientBrowserPopup](mta://scripting/client/events/onclientbrowserpopup.md)

- [onClientBrowserResourceBlocked](mta://scripting/client/events/onclientbrowserresourceblocked.md)

- [onClientBrowserTooltip](mta://scripting/client/events/onclientbrowsertooltip.md)

- [onClientBrowserWhitelistChange](mta://scripting/client/events/onclientbrowserwhitelistchange.md)
