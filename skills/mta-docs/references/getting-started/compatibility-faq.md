---
doc_id: "mta-wiki:9276"
title: "Compatibility FAQ"
source_title: "Compatibility FAQ"
source_url: "https://wiki.multitheftauto.com/wiki/Compatibility_FAQ"
revision_id: 81941
language: "en"
categories: []
---

# Compatibility FAQ

Compatibility Comparison

|  | Warning: Using the legacy build is not without risk, there are known security issues in the Chrome Embedded Framework (CEF) that MTA:SA 1.5.7 uses for Windows XP and Vista. It is recommended that you upgrade from XP or Vista to a supported Windows version. (Windows XP and Vista are no longer supported by MTA after September 2019.) |
| --- | --- |
|  |  |

| Operating System | Service Pack/Version | Release Date | Supported by Microsoft [1] | Does MTA:SA 1.6.0 work? | Chrome Embedded Framework Updates | Future MTA:SA releases/updates |
| --- | --- | --- | --- | --- | --- | --- |
| Windows XP | Service Pack 3 | August 2001 | No | No | No | 1.5.7 was the last version |
| Windows Vista | Service Pack 2 | November 2006 | No | No | No | 1.5.7 was the last version |
| Windows 7 | Service Pack 1 | July 2009 | No | Yes | Yes | Yes |
| Windows 8.0 | n/a | August 2012 | No | n/a | n/a | n/a |
| Windows 8.1 | n/a | August 2013 | No | Yes | Yes | Yes |
| Windows 10 [2] | 1507 | July 2015 | No | n/a | n/a | n/a |
| 1511 | November 2015 | No | n/a | n/a | n/a |  |
| 1607 | August 2016 | No | n/a | n/a | n/a |  |
| 1703 | April 2017 | No | n/a | n/a | n/a |  |
| 1709 | October 2017 | No | n/a | n/a | n/a |  |
| 1803 | April 2018 | No | n/a | n/a | n/a |  |
| 1809 | September 2018 | No | n/a | n/a | n/a |  |
| 1903 | May 2019 | No | n/a | n/a | n/a |  |
| 1909 | November 2019 | No | n/a | n/a | n/a |  |
| 2004 | May 2020 | No | Yes | Yes | Yes |  |
| 20H2 | October 2020 | No | Yes | Yes | Yes |  |
| 21H1 | May 2021 | No | Yes | Yes | Yes |  |
| 21H2 | Nov 2021 | Yes | Yes | Yes | Yes |  |
| Windows 11 [3] | 21H2 | October 2021 | Yes | Yes | Yes | Yes |
| 22H2 | September 2022 | Yes | Yes | Yes | Yes |  |
| 23H2 | October 2023 | Yes | Yes | Yes | Yes |  |

- Please use a supported version of Windows 10 to run MTA.

- There are no guarantees that MTA will work on older not by Microsoft supported Windows 8 and 10 versions.

## FAQ - Frequently Asked Questions

### Google is dropping XP/Vista support for Chrome browser? What does this even have to do with MTA:SA?

As you may know from our previous [news posts](https://forum.mtasa.com/topic/75559-mtasa-15-release-candidate-is-ready-for-testing/), MTA:SA uses CEF (Chrome Embedded Framework) components for providing some functionality for the mod since version 1.5. Being Chromium-based, CEF components are also being phased out for users of older Operating Systems and will simply not work on them.

### Does MTA:SA 1.5.7 work fine on Windows XP and Windows Vista?

Yes, it works fine if you install it through the legacy build. We still can not really recommend using these systems anymore due to the reasons listed below.

CEF compatibility issue aside, these Operating Systems (XP especially) are really old nowadays. You are putting yourself at risk if you use them as they are either no longer supported by Microsoft (XP) or the support will be discontinued soon (April 2017 - Vista).

### What will happen if I try to use the regular build of 1.5.7 on Windows XP/Vista?

MTA:SA installer will display an error and will not let you install the mod on such systems. You will be asked to download the legacy build from our website.

### And what will happen if I try to use the legacy build of 1.5.7 on Windows 7 and above?

Similarly, MTA:SA installer will display an error and will not let you install the mod on such systems. You will be asked to download the regular build from our website.

### Why couldn't you just stick to the older version of CEF then so that XP/Vista would be still supported? / What about releasing two versions of the mod? A regular one with newest CEF and a legacy one with the older CEF build that still works on XP/Vista?

Hey, but we actually do provide a legacy build for MTA:SA 1.5.7 for XP/Vista users with an older version of CEF components.

The problem with sticking with either of these options is that we would have to continue providing a version that is vulnerable to any present and future security exploits that exist in Chromium and are already widely used. We do not want to put our users at risk because of that. CEF developers themselves do not want to provide long-term security support for such a build either.

### I am playing the mod on Windows 7/Windows 8/Windows 8.1/Windows 10 or newer. Am I affected by this?

No, you will not be affected at all. In fact, you will have a better experience with built-in web browser components than before due to security and performance fixes included in the newer CEF versions.

### I am using Windows XP/Vista and I would still like to play future versions of MTA:SA. What can I do about it?

If you are using Windows XP or Windows Vista, you should upgrade your OS to a newer one. You will likely be required to do a clean install for that, so back up your stuff first. You should use these tools first to see if your PC is capable of upgrading to newer OS:

```
Windows 7: Windows 7 Upgrade Advisor
   Windows 8/10: Windows 8 Upgrade Assistant
```

Is your PC toaster-tier which does not support Windows 8 or even 7? That means it is probably the right time to buy something more modern.

But fear not, if you are already using Windows 7 or newer, just install the newest build of MTA:SA 1.5.7 and you are set! And if you don't want to upgrade your OS or PC, well, we will keep offering the legacy build that works on XP/Vista for a while...

## Notes

- [↑](#cite_ref-1) [https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet](https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet)

- [↑](#cite_ref-2) ([[1]](https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet))

- [↑](#cite_ref-3) ([[2]](https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet))

- [↑](#cite_ref-4) [https://bitbucket.org/chromiumembedded/cef](https://bitbucket.org/chromiumembedded/cef)

- [↑](#cite_ref-5) [http://www.magpcss.org/ceforum/viewtopic.php?f=6&t=14187](http://www.magpcss.org/ceforum/viewtopic.php?f=6&t=14187)

## See also

- [Topic about the compatibility changes](https://forum.mtasa.com/topic/89685-mtasa-windows-xpvista-cef-components-and-you/)
