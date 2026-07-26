---
doc_id: "mta-wiki:3128"
title: "Timer"
source_title: "Timer"
source_url: "https://wiki.multitheftauto.com/wiki/Timer"
revision_id: 76899
language: "en"
categories: []
generated_at: "2026-07-26T16:16:58.210146+00:00"
---

# Timer

A timer object refers to a timer set to execute a function a certain number of times with a specified delay.

Note that after a timer has completed all its iterations, it is destroyed and any stored pointers to it become invalid. Also timers are not under the *resource* hierarchy, because they are not elements, for instance, if you create a timer, it will not be destroyed when the resource in which it was created is stopped, so in this case you should kill the timer manually.

## Related scripting functions

- [getTimers](mta://scripting/shared/functions/gettimers.md)

- [killTimer](mta://scripting/shared/functions/killtimer.md)

- [setTimer](mta://scripting/shared/functions/settimer.md)

- [isTimer](mta://scripting/shared/functions/istimer.md)

- [getTimerDetails](mta://scripting/shared/functions/gettimerdetails.md)
