---
doc_id: "mta-wiki:7021"
title: "Support - MTA Client and Process Monitor"
source_title: "Support - MTA Client and Process Monitor"
source_url: "https://wiki.multitheftauto.com/wiki/Support_-_MTA_Client_and_Process_Monitor"
revision_id: 79852
language: "en"
categories: ["Support"]
generated_at: "2026-07-26T16:16:54.147180+00:00"
---

# Support - MTA Client and Process Monitor

Instructions for generating a process log for MTA:SA Client

### 1. Download Process Monitor from here: [http://technet.microsoft.com/en-us/sysinternals/bb896645](http://technet.microsoft.com/en-us/sysinternals/bb896645)

 

### 2. Unzip ProcessMonitor.zip

### 3. Download [http://nightly.mtasa.com/files/ProcmonMTAConfiguration.pmc](http://nightly.mtasa.com/files/ProcmonMTAConfiguration.pmc) and put it into the Process Monitor directory

 

### 4. Start Procmon.exe (if it starts with a window called 'Process Monitor Filter', press OK to close it).

### Then select the menu item '**File**->**Import Configuration'**

(If you can't select 'Import Configuration', try running Procmon.exe as administrator)

 

### 5. Select the '**ProcmonMTAConfiguration.pmc'** file and press '**Open'**

### 6. Now start MTA and get to the problem

### 7. After problem has occurred, go back to the Process Monitor window and select the menu item '**File**->**Save...'**

 

### 8. Press the '**Ok'** button in the next window

### 9. Find the file '**Logfile.PML'** and upload at [https://upload.mtasa.com/](https://upload.mtasa.com/)

Give the resulting file link to an MTA developer, or post it on the relevant forum topic  

(If Logfile.PML is large, you can optionally .zip or .rar it before uploading)
