---
doc_id: "mta-wiki:9055"
title: "MacOS"
source_title: "MacOS"
source_url: "https://wiki.multitheftauto.com/wiki/MacOS"
revision_id: 82850
language: "en"
categories: ["Development"]
---

# MacOS

| [[\|link=\|]] | Warning: This page is intended for developers. If you are here looking for instructions to install the client on macOS, please read this page! |
| --- | --- |
|  |  |

 

This page is incomplete, and is still being updated by developers. If you are here to learn how to run MTA on OS X, you only need to read the first section "[Making Your Own Wrapper](#Making_Your_Own_Wrapper)".

Contact [User:qaisjp](https://wiki.multitheftauto.com/wiki/User:Qaisjp) if you need any help with anything on this page.

### User Experience

This section outlines what our automated version will do.

A *.dmg* file will be distributed. EULAs can be embedded within *.dmg* files.

This file will contain a link to the Applications folder and the Multi Theft Auto application. The user is expected to transfer the application to the applications directory before running.

**The application will**:

- confirm we are not running from an img file

- check if there is currently a valid GTA:SA directory

- if not, prompt for a directory.

- Wineskin does not support symbolic links. Once the directory has been chosen, we copy the gta_sa.exe file over and directory junction the rest of the files.

- start Multi Theft Auto for us automatically

## Making Your Own Wrapper

This section is written like a tutorial for public consumption, but is intended to serve as working documentation to aid the automated version in development. It is recommended that you read through this entire section (including the "Tips" section at the bottom) before following the tutorial, if you wish to build your own Wineskin wrapper. You do not need to read any other sections.

### Grabbing the Winery

- Grab the [Wineskin Winery](https://sourceforge.net/projects/wineskin/files/Wineskin%20Winery.app%20Version%201.7.zip/download). At the time of writing, v1.7. This allows you to create your own wrapper.

- Open *Wineskin Winery.app*, and [click "Update" underneath "No Wrapper Installed" to download the master wrapper.](https://wiki.multitheftauto.com/images/c/c3/MacOS_wineskin_tut1.png).

- Now click the + plus button. This will bring up a new window titled "Add Engine".

- Select the latest engine (at the time of writing, WS9Wine1.9.15) and [click the blue "Download and Install" button](https://wiki.multitheftauto.com/images/7/7a/MacOS_wineskin_tut2.png).

- Now you can [click "Create New Blank Wrapper" button at the bottom of the "Wineskin Winery" window](https://wiki.multitheftauto.com/images/b/b4/MacOS_wineskin_tut3.png).

- Call the application whatever you like, "Multi Theft Auto" is a good name to use.

- [You may receive a firewall dialog.](https://wiki.multitheftauto.com/images/4/4c/MacOS_wineskin_tut4.png) Press "Yes".

- Allow the wrapper to be created. This will take some time.

- A new wrapper will be generated in the Applications folder **in your home folder**. It will not appear in your main Applications folder (which resides in the root of your drive, for all the users).

Now we have generated an empty wrapper, we need to add GTA, install MTA, and configure some other settings.

### Running San Andreas

Firstly, we will test out Grand Theft Auto: San Andreas. For the sake of this tutorial we will assume that you already have a folder containing your GTA:SA files (copied over from a Windows installation). You *may* need a no-cd version of the exe.

- Right click your main wrapper app (in my case, "MTASA.app") and press "Show package contents"

- [There should be three items inside here.](https://wiki.multitheftauto.com/images/f/f5/MacOS_wineskin_tut5.png) Open the *drive_c* shortcut, open *Program Files*, and create a folder called *Rockstar Games*.

- Copy (or move) your *GTA San Andreas* folder here.

- [Your drive_c folder should now look a bit like this.](https://wiki.multitheftauto.com/images/c/c6/MacOS_wineskin_tut6.png)

- Now select *Wineskin.app* (which inside our main app). [This application allows us to configure our wrapper.](https://wiki.multitheftauto.com/images/7/79/MacOS_wineskin_tut7.png)

- Select "Advanced" to bring up a window titled "Wineskin Advanced".

- Click the "Browse" button next to the "Windows EXE" field and navigate to *gta_sa.exe*. [The window should now look like this.](https://wiki.multitheftauto.com/images/8/87/MacOS_wineskin_tut8.png)

- Press "Set Screen Options" at the bottom of the window, and make sure you deselect "Decorate windows", and select "Use Direct3D boost". [It should be configured like this.](https://wiki.multitheftauto.com/images/0/02/MacOS_wineskin_tut9.png) **[High Sierra (and above) users must read these instructions.](http://wineskin.urgesoftware.com/tiki-view_blog_post.php?postId=87)**

- Click Done. On the "Wineskin Advanced" window, press "Test Run" and San Andreas will begin to run. Note that it will take some time for it to run.

- After the two GTASA startup logos display, press any key to skip the splash screen.

- After you've tried the game a little, quit. You may close (press Cancel) the dialog box that asks you whether you want to view logs.

### Running Multi Theft Auto

Now we need to install Multi Theft Auto.

- Some font files are required for MTA to run. Copy the font files (*.ttf*) from [here](https://drive.google.com/open?id=0B4SUSkTXjliXZnBXV2pEWkdTTms) and extract them to `drive_c/windows/fonts` (inside our wrapper). You may have to create the fonts folder yourself if it does not exist.

- Download the installer from [the homepage](https://multitheftauto.com).

- Open Wineskin.app (inside our wrapper) and select "Install Software", and then select "Choose Setup Executable".

- Navigate to the *.exe* installer (that should be inside your Downloads folder) and allow Wineskin to load it.

- Proceed with the installer as usual. **Do not change the Destination Folder for where MTA will be installed.**

- The installer may encounter errors *Unable to install Microsoft Visual Studio 20xx redistributable*. It is okay to ignore these.

- Deselect *Run MTA* when you have finished installing.

- Press "Advanced" on the Wineskin window, and now browse to the *Multi Theft Auto.exe* file.

- Perform a Test Run, and hopefully Multi Theft Auto should run!

### Tips

- You can use the keybind Cmd+Opt+A at any time to switch between windowed & fullscreen. You may need to use this if you cmd+tab out of the app, and the app ends up moving to windowed mode.

- If you are asked at any time to install Gecko or Mono, simply press yes.

- If you receive the message "Warning: Could not detect anti-virus product" when starting MTA, simply check the box saying "I will not install an anti-virus", and press OK. This message occurs because MTA cannot detect OS X antiviruses.
