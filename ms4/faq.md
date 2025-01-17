# LEGO Mindstorms Robot Inventor "Mindstorms 4" 51515 FAQ

This FAQ has been written from the perspective of using a _Windows PC_ as host, not e.g. a tablet.

The FAQ is currently split in three sections: 
[general](#general-questions), 
[Word Blocks specific](#word-blocks-specific-questions) and 
[Python specific](#python-specific-questions) questions.



![next chapter](images/chapter-next.png)
# General Questions


## How to switch off the brick?
I opened the box, and one of the first things I did was to power on the brick.
However, I could not figure out how to switch it off.

You have to first download the LEGO app (next question) on your PC and then upgrade the Hub OS. 
Only then I was able to switch the hub off.
Upgrading OS only works from PC (probably MAC also works, but phone and iPad probably don't) .

How to switch off? Keep the big button pressed, it gives three beeps, and then you can release.
In some cases (Python program running instead of a Word Block) I do not hear the three beeps.

Here is a demo on [YouTube](https://youtu.be/CQVBp5e3tng)


## Where is the LEGO app?
The booklet in the mindstorms box tells you to visit [https://www.lego.com/devicecheck](https://www.lego.com/devicecheck).
I skipped that, because I have a brand new PC and a brand new Android device, so no need to check... But then I wondered where should I _download_ the Mindstorms app?

Well, go to [devicecheck](https://www.lego.com/devicecheck), select mindstorms,
and click on one of the "stores" to download the app.

![Available stores](images/stores.png)

Instead of the Mindstorms app, you might like to try the [Spike prime software](https://education.lego.com/en-us/downloads/spike-prime/software).
It seems identical, and it has support for the force sensor, which is missing in the Mindstorms app. Did not try.

This "app" is what is normally known as an IDE (integrated development environment).
It is an editor, compiler, uploader, debugger and help system in one.
But LEGO calls  "the app".

I have the feeling that the app updates itself, because sometimes the version number in the titlebar changes.
However, you not always have the latest-greatest, the update is "slow".
To force an update goto the Windows Store, search for the LEGO Mindstorms app, and press update.


## How to make a shortcut to the LEGO app on my Windows Desktop?
I don't like "apps" from the Windows store. They are special in all kind of ways.
For example how do you create a shortcut on your desktop?

Go to Start > Run (e.g. Windows-R) and enter `shell:AppsFolder`.
This pops up a folder with apps, and you can drag a shortcut to e.g. your Desktop.

![Shortcuts](images/shortcut.png)

Found [here](https://winaero.com/desktop-shortcut-store-app-windows-10/).


## Can I redo the getting started?

In the LEGO app, goto to Help > Settings > General and click the "Welcome Robot Inventors!".


## What are the technical specs?
LEGO has leaflets on [Spike prime](https://education.lego.com/en-gb/product-resources/spike-prime/downloads/technical-specifications), which
is largely the same as Mindstorms Robot Inventor.

- **hub**: 5x5 LEDs, 6 ports, Gyro, 3 buttons, one with RGB LED, beeper, Bluetooth, USB, MicroPython  
  **cpu:** 100MHz M4, 320 kB RAM, 1M FLASH; 32MB RAM extern  
  **battery**:  2100 mAh @ 7.3 V  >500 cycles
- **color sensor**: 100 Hz sample rate,  color sensing (RGB/HSV), reflectivity sensing, ambient sensing, white led emission
- **distance sensor**: 100 Hz sample rate, range 50..2000 mm, resolution 1 mm, 4 LEDs for decoration
- **motor**: torque 0..18 Ncm, speed 0..185 RPM, current 110..800 mA;  
  **rotation sensor**: 360 ticks per revolution, 3 degrees accuracy, 100 Hz sampling


## Is there help from LEGO?

Yes, LEGO is publishing instruction videos on YouTube. Unfortunately not on a separate channel or in a playlist (grr).
These I found (top-most is oldest):

 - [Robot Inventor Explained!](https://www.youtube.com/watch?v=ntBkg2x3EJ0)
 - [Connect Your Hub](https://www.youtube.com/watch?v=MEj1_pS3esw)
 - [Your First Program](https://www.youtube.com/watch?v=sIfAlu29YyA)
 - [Navigate Your Hub](https://www.youtube.com/watch?v=dWR8ucYlzjQ)
 - [Turn your Devices Into a Remote Control](https://www.youtube.com/watch?v=qJ3cr-LKnEM)
 - [Create Animations](https://www.youtube.com/watch?v=_lQs_HE9Soc)
 - [Edit Your Programs](https://www.youtube.com/watch?v=WeECsUD6TQs)
 - [Connect a Game Controller](https://www.youtube.com/watch?v=g9M9WgwFbZE)
 - [Make Your Models Come Alive](https://www.youtube.com/watch?v=OLMGm7gV370)
 - [Program Your Sensors](https://www.youtube.com/watch?v=avhgnYp5CzQ)


## Are there other good resources?

 - [python readthedocs](https://hubmodule.readthedocs.io/en/latest/) from Nard Strijbosch
 - [python API](https://lego.github.io/MINDSTORMS-Robot-Inventor-hub-API/) from LEGO
 

## Which projects can I build?
Of course, there are the five robots that come with the box.
Building instructions are digital only, you can find them in the app via Help > Settings > Building instructions.
Or you can click the robot in the home screen, and go from there in smaller steps.
Alternatively you can download them as [pdf](https://www.lego.com/en-us/service/buildinginstructions/51515).

Do note that the robots come with add-ons, which are really great,
for example [Charly drum master](https://youtu.be/EAHvnpIGu1U)
or [Tricky chain reaction](https://youtu.be/szFxBSRUh7c?t=167)

If you like more, or simpler builds, you could have a look at 
[Spike prime instructions](https://education.lego.com/en-us/support/spike-prime/building-instructions)
or [alternative link](https://education.lego.com/en-us/product-resources/spike-prime/downloads/building-instructions).

There are several nice community builds:
 - [Hotrod](https://sites.google.com/view/devbots/free-ebooks/hot-rod)
 - [Ox](https://youtu.be/ZYQG9EfIw28)
 - [Bike](https://youtu.be/MCVW2Uqanlw)
 - [Rock paper scissors](https://youtu.be/MwoE_gScDd8)
 - [Robot arm](https://youtu.be/uxm7qhLNYyw)  
   [Instructions](https://m.facebook.com/download/865529984270200/arm.pdf)
   [Version 2](https://m.facebook.com/groups/mindstormsrobotinventor/permalink/478705086475784/)
 - [Canadarm](https://youtu.be/3sKHHaLFzY8)
   [gripper hint](https://education.lego.com/en-us/lessons/prime-invention-squad/super-cleanup)
 - [Candy sorter](https://m.facebook.com/groups/mindstormsrobotinventor/permalink/478354733177486/)
 - [F1 race car](https://rebrickable.com/mocs/MOC-62452/ninoguba/premier-f1-race-car-robot-inventor)
 - [Tic tac too](https://youtu.be/9Qm_rJGbT8U)
 - [Clock](https://youtu.be/XmRcth8nZUA)
 - [Steam lococomotive](https://youtu.be/D6fnY4Q5w9c)
 - [Airplane](https://youtu.be/yfcK1Wd1Xm8)
 - [Scooter](https://youtu.be/oLr_ScaK5Nk)
 - [Balancing Robot](https://youtu.be/XXEp5R3kDNg)
 - [Balancing Trike](https://legostudiovives.be/balancing_lego_robots/)
 - [Cube solver](https://youtu.be/e2EDLIPwlSM)
 - [Cube solver from MindCuber](http://mindcuber.com/mindcuberri/mindcuberri.html)
 - [Writing machine](https://rebrickable.com/mocs/MOC-61225/Bundy/inventor-writer-based-on-one-set-51515-mindstorms-inventor)
 - [R5D1 robot](https://m.facebook.com/download/338474627340404/R5D1%20Instructions.pdf)
 - [HugBot](https://youtu.be/j0IdLnO3k3M)
 - [AI brick sorter](https://robotics.benedettelli.com/lego-mindstorms-learning-brick-sorter-bird/)
 - [4 legged walker](https://youtu.be/pM3Hx4ajv4c)

## Where are my recent projects?
When you start the LEGO Mindstorms Robot inventor app, you get a screen with pictures (links) to the 5 robots.
At first this is nice, but after a while you want to continue with your own projects.

![Projects](images/projects.png)

You have to click PROJECTS at the bottom of the app's home screen.
Unfortunately, the list of projects starts with the standard LEGO ones, and not with e.g. the most recent ones.
You have to scroll all the way down. This is much improved since version 10.2.0!

The mouse scroll wheel does work, but the scroll bar itself is too thin to easily grab with the mouse. Grr.

The LEGO app is very limited in using _keys_. 
The DownArrow (or UpArrow) don't work. 
Fortunately PageDown and PageUp do work, best is probably End (or Home).
Unfortunately, you first have to click the project list (to give it focus) and make the keys work. Grr.

## How should I name my projects?
Most projects end up with a name like `Project 17`, because the LEGO app does not ask for a name.
By default it just numbers them, using the lowest free number.

You have to explicitly remember to press File > Save As (preferably right after you create a new project). Grr.


## How do I start a new project?
Want to start a new project? Press CODE at the bottom of the home screen. You get an empty new Word Block program. 
Rather have a Python program? In the Word Block editor (top) create a new tab.
Or, in the home screen click File > New Project.

Now you are _asked_ for the type of project (Word Block or Python).

After creating the project I suggest to immediately rename with File > Save As.


## How to save my project?
There is no Save button.

It seems the project is saved constantly when you interact with it (clicking the tab is enough).
I see the time stamp change in the file explorer.

The only condition is that the project is non-empty, or that you did a Save As.
So, only an empty project that is not yet renamed does not get saved, which makes sense.


## Where are my projects saved?
The LEGO app made a directory `C:\Users\maarten\Documents\LEGO MINDSTORMS` for my (Maarten's) projects.
If you Save As `xxx`, the file ends up there, as `xxx 1.lms`.

The extension lms probably refers to LEGO MindStorms. The "space-one" suffix is automatically appended.
The next time you Save As a project and _type_ `xxx` it gets the name `xxx 2.lms` (note the `2`).
Non-standard windows behavior. Grr.

You can however Save As and _select_ the existing `xxx 1.lms`.
That pops up an "are you sure you want to overwrite" dialogue.

It also means you can't call your program `beep3`, because the LEGO app gets confused by the 3, 
strips it and appends a space and another number. grr.


## What is an lms file?
The LEGO app saves Mindstorms projects as files with the extension `.lms` (LEGO MindStorms presumably).
This is a binary file format, which is a pity for Python programs.

However, an lms file turns out to be an archive. If you have, e.g. [7zip](https://www.7-zip.org/) you can unzip lms files.

![Inside the lms file](images/lms.png)

This `icon.svg` is the icon displayed on the projects page. For a Python program it is a fixed one, for a Word Blocks program it is a "picture" of the program.

The `manifest.json` contains unknown details. I have freely formatted it for readability (e.g. removed all details of the `frames` field for the Word Blocks, added whitespace).

```text
{                                                                {
  "type":"word-blocks",                                            "type":"python",
  "autoDelete":false,                                              "autoDelete":false,
  "created":"2020-10-26T11:40:45.552Z",                            "created":"2020-10-27T09:01:52.735Z",
  "id":"TWLdDSlhsQyc",                                             "id":"oU3m7qCYhOst",
  "lastsaved":"2020-10-27T19:07:51.938Z",                          "lastsaved":"2020-10-27T09:47:52.208Z",
  "size":19529,                                                    "size":1148,
  "name":"test 2",                                                 "name":"version 1",
  "slotIndex":0,                                                   "slotIndex":0,
  "workspaceX":119.99999999999989,                                 "workspaceX":120,
  "workspaceY":119.99999999999955,                                 "workspaceY":120,
  "zoomLevel":0.675,                                               "zoomLevel":0.5,
  "showAllBlocks":false,                                           "hardware":{
  "version":6,                                                       "python":{
  "hardware":{                                                         "name":"LEGO Hub A8:E2:CC:BB:EE:DD",
    ":V-eSnh?r]sx%eM7=Sn|":{                                           "connection":"bluetooth-classic",
      "id":"COM4",                                                     "lastConnectedHubId":"a8:e2:cc:bb:ee:dd",
      "description":"",                                                "id":"a8:e2:cc:bb:ee:dd",
      "connection":"usb",                                              "type":"flipper"
      "name":"LEGO Hub",                                             }
      "type":"flipper",                                            },
      "hubState":{"programRunning":false},                         "state":{}
      "lastConnectedHubId":"COM4"                                }
    }
  },
  "extensions":["flipperevents","flippersensors"],
  "state":{
    "playMode":"play",
    "canvasDrawerTab":"monitorTab",
    "canvasDrawerOpen":true
  },
  "animations":{
    "Q62qCPATcnucgz9Ldm_T":{
      "params":{
        "transition":2,
        "frames":[{"pixels":[...]}...],
        "loop":false,
        "fps":8,
        "animationName":"Play"
      },
      "lastSave":1603712445547,
      "id":"Q62qCPATcnucgz9Ldm_T"
    }
  }
}
```

The third file is the actual program. For Word Blocks, some format, unknown to me.
For Python, it is the Python text wrapped in json, below freely formatted by me for readability.

```json
{"program":"
   import sys\n
   \n
   # print( dir(sys) )\n
   # for n in dir(sys): print( \"sys.\"+n+\" = \", eval(\"sys.\"+n) )\n
   \n
   print( \"byteorder=\", sys.byteorder )\n
   print( \"implementation=\", sys.implementation )\n
   print( \"maxsize=\", sys.maxsize )\n
   print( \"path=\", sys.path )\n
   print( \"platform=\", sys.platform )\n
   print( \"version=\", sys.version )\n
   \n
"}
```


## What is an llsp file?

An `llsp` file is presumably the same as an `lms` file.
The only difference seems to be that an `lms` is for Robot Inventors app and the `llsp` is for the Lego Spike Prime app.

Like the `lms` file, it is an archive with an icon, manifest and code file.


## How to update the hub firmware?
I see people talk about hub firmware updates, but the Mindstorms app does not have a feature for that - at least I couldn't find it. Maybe the Spike prime app allows explicit firmware updates (downgrades, alternatives...).

However, when LEGO releases a new version, you will get a message in the app. If you accept it the hub will be updated.
This updates the hub’s OS, not the user data (saved projects).

By the way, if you open a serial port to the Python REPL (see other question), and press ^C you stop the run-time (?).
If you then close REPL and start the LEGO mindstorms app, it believes the hub firmware is broken and suggest to flash it again.
You could do that. You could also just powercycle the hub (or press ^D for soft reset while still in REPL).


## What software version is current?
The app version is in the title bar.
The Hub has an OS, its version is shown in the Hub Connection window.
For Python we use a script 

```python
import sys
print(sys.implementation)
print(sys.version)
```

### Per 2021 December 26

- The app version is 10.3.0
  - Getting started on home page  
    ![app 10.3.0 home](images/version10.3.0-home.png)
  - Bluetooth auto connect  
    ![app 10.3.0 auto BT](images/version10.3.0-autobt.png)
- The Hub OS version is 3.1.43 (no fourth number)
- The `sys.implementation` micropython 1.14.0, mpy 517
- The `sys.version` 3.4.0

![App and OS version](images/version10.3.0.png)


### Per 2021 August 26

- The app version 10.2.0  
   - It now asks for age and consent to collect data.
   - Help Center is updated
   - My projects is now easier to work with
   - It seems there is hub-to-hub communication (see Tips & Tricks in the Help Center)
- The Hub OS version is 3.1.29 (no fourth number)
- The `sys.implementation` micropython 1.14.0, mpy 517
- The `sys.version` 3.4.0

![App and OS version](images/version10.2.0.png)

### Per 2021 June 6

All version numbers are the same as per May 16, but there are now eight community fan inventions: 
Exploration Rover, Sea Turtle, Melody Maker, 
**Melody Maker**, **Salamoot**, **Print and Scan**, **Wrecking Bot**, Pet Gelo and Tricky Flippin'.

![Community](images/community8.jpg)


### Per 2021 May 16

- The app version 10.1.0  
  In main menu, SETTING is replaced by COMMUNITY, which lists five robots: 
  **Exploration Rover**, **Sea Turtle**, **Melody Maker**, 
  and two that were previously extensions: Pet Gelo and Tricky Flippin'.
  Some [users](https://www.facebook.com/legomindstorms/posts/3704825206290085) 
  report three more: Salamoot, Wreckin' Bot, Print and Scan.
- The Hub OS version is 3.1.7.2
- The `sys.implementation` micropython 1.12.0, mpy 517
- The `sys.version` 3.4.0

![App and OS version](images/version10.1.0.png)


### Per 2020 nov 30

- The app version 10.0.3  
  Now has a "Getting started".  
  Now has motor calibration (that O is 0 degrees).  
  Now has robot (extensions) from the community.
- The Hub OS version is 2.1.4.13
- The `sys.implementation` micropython 1.11.0
- The `sys.version` 3.4.0

![App and OS version](images/version10.0.3.png)


### Per 2020 nov 29

- The app version 10.0.2
- The Hub OS version is 2.1.4.10
- The `sys.implementation` micropython 1.11.0
- The `sys.version` 3.4.0

![App and OS version](images/version10.0.2.png)


### Per 2020 oct 27
- The app version is 4.0.4-dev.99999
- The Hub OS version is 2.1.4.10
- The `sys.implementation` micropython 1.11.0
- The `sys.version` 3.4.0

![App and OS Version](images/version.png)

![Python Version](images/pythonversion.png)



## Are there any quality issues?
I have picked up two from social media, and later found I suffer from both.

The first is the worst: some color sensors are broken.
I found it [here](https://www.facebook.com/groups/mindstormsrobotinventor/permalink/405690047110622/) and 
later [here](https://www.facebook.com/groups/mindstormsrobotinventor/permalink/404200153926278/).
The one that came with the 51515 box is fine. 
But I ordered a second [one](https://www.bricklink.com/v2/catalog/catalogitem.page?S=45605).
If I plug it in the hub, it is sometimes recognized, and sometimes not.
Recognized means that it lights up, appears in the  "triangle" test app, and is listed in the LEGO app under the port.
For my second sensor none of these happen (in "half" the time).
I contacted LEGO support and they claim that with the latest firmware this is resolved.

The second issue is less of a problem: the O positions of the motors have a deviation.
I found it [here](https://www.facebook.com/groups/mindstormsrobotinventor/permalink/399918451021115/?comment_id=399946571018303).
If you handposition the motor to O, its position is not returned as 0 (but ~5).
If you tell the motor to go to position 0, it is not at O, but some degrees off.
Most motors have a deviation within ±5°, but one of mine has an offset of nearly 15°.
The good news is that it is structural, so you can compensate in software.

**Update:** the LEGO app version 10.0.3 has a calibration procedure that presumably programs the O correction in the motors.

To force a motor update, goto the Hub connection, and find the "Update motors" in the overflow menu. You need the LEGO app version 10.0.3 or higher.

![Motor update](images/updatemotors.png)


## Are there special startup features?


1) Turn off the hub and unplug the USB cable.
   Press and hold the Bluetooth button on the hub while reconnecting the USB cable. 
   Release the Bluetooth button when it starts to flashing colors (purple, red, blue). 
2) Connect the hub to a computer via USB, turn off the hub.
   Press and hold the left button and press the center button. This turns on the hub; release both buttons when completely on. 
   When you press connect in the LEGO app, the hub OS is updated.


## Are there any hotkeys?
I think LEGO did a bad job here. Many functions are not operatable by key.
Probably LEGO aims at touch screens.

Note #=shift, ^=ctrl, @=alt

Word blocks is horrible, there are basically no hotkeys.
  - ^Z for undo is working, but ^Y for redo isn't (it is available in bottom menu or right click menu)
  - @F4 stops application.
  - @F or @H (for file or help menu) is _not_ working.
  - Cut and paste (^C, ^V) is _not_ working. You can right-click and Duplicate, but this duplicates the whole stack.  
    **Update** in 10.3.0 (but maybe earlier), copy and paste seems to work, even across projects! 
  - I found no hotkey for Run or Download.
  - Cursor keys (panning) do nothing.

Python is a better. But not due to LEGO, but because they took a standard control for the editor.
It behaves much like [Microsoft Studio Code](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
  - ^C, ^V, ^X for copy, paste, cut.
  - ^Z, ^Y for undo, redo.
  - Cursor movement with arrow or page keys, optionally in combination with ^.
  - Select by pressing # while moving cursor.
  - ^F, ^H for find and replace (grr: the hub bar overlaps with the find bar, bigger grr: paste does not work in the search bar).
  - **^#P issues a play**.
  - ^#D issues a download.
  - **There is no way to clear the console other than to restart the whole mindstorms app - grr**.
  - **You can only walk up (arrow-up, page-up, home) in the console, not down (arrow-down, page-down and end all jump to end), and the scroll bar sucks - grr**.
  - Fancy line commenting: ^K ^C add line comment, ^K ^U delete line comment, ^/ toggle line comment.
  - #@A to toggle block comment.
  - Very fancy multi cursor (bit over the top) with @click, or ^#@ with cursor movement.
  - **There is no rich languages editing, ^SPC appears to work but it doesn't know the object, it just shows all occuring strings.**








![next chapter](images/chapter-next.png)
# Word Blocks specific questions


## How can I debug my Word Block program?
A bit hidden feature in the Word Block editor are the two icons on the right hand side.

The bottom one (Show/Hide Monitor) allows you to show (hide) a pane with a live view of the variables.

Great feature! Not present in Python, but Python has a better feature: the console!
A downside is that the monitor updates periodically (timed), so you do not see all changes.

The monitor feature does work in "download mode", you  do not have to use "streaming mode". I did not expect that...

![Monitor](images/monitor.png)


## How to send my project to the Hub?
There are actually three ways to do that.

- The most straighforward way is to press the Play button.
  Your program is compiled, uploaded and run. If a program was running on the hub, it is stopped.
  Note that the Hub has 20 slots (0..19), the app calls them "storage positions".
  By default your program goes to slot 0, but if you click one of the two "slot select buttons" (the arrows), you can specify another slot.

  If you open the Hub connection on the PC, and then select tab Programs,
  you see the slots with the names of the project they currently store. Plus the option to delete or reorder slots.

- Another way it to only download, not _run_: press the Download button in the slot selection pane.

- A special way to run is _streaming_ mode.
  It does not save the project in a slot. So code is lost on the hub after stopping the program.
  Python does not support streaming.

![Play](images/play.png)


## What is streaming?
I'm not entirely sure of all the details of [streaming mode](https://www.lego.com/en-us/service/help/products/themes-sets/lego-mindstorms-robot-inventor/coding-with-the-lego-mindstorms-robot-inventor-app-408100000020946).

- The program you’re creating is not stored in a slot on the hub as it is with download mode.
- Instead, the PC maintains a connection with the hub, and the instructions will stream to the hub as they are executed.
- Remote control (pane in Mindstorms app, or Game controller) requires streaming mode.
- You can make "live" changes in your program (see figure).  
  ![Streaming](images/streaming.png)
- You can single click any block (even in the left-hand side toolbar) to execute it immediately. It highlights yellow.  
  ![Execute single statement](images/execsingle.png)
- You can even click a variable in the toolbar to see its value. It highlights yellow and shows speech bubble with current value.  
  ![Execute variable](images/execvar.png)

However,
- Somehow, showing the monitor does not require streaming mode.
- Also, sound via PC does not require streaming mode.
- The "weather" extension does not need streaming either (but the project must be open in the LEGO app).


## Isn't streaming mode slow?
In streaming mode, the code is streamed from the PC to the hub, while the program is executed.
This sounds a bit like an interpreter, and thus it sounds slow.

It isn't always. In fact, it is sometimes the other way around: streaming is nearly 1000x faster in the below program.
Disclaimer: my test program does not execute a balanced set of blocks, and that is an understatement.

I guess the reason for this is that in streaming mode, all the code is run on the PC, and only _actuator commands_ and _sensor reads_ are streamed to the hub.
So if you do not do "integer increments on the PC" but need "sensor or actuator actions on the hub" it is likely slower.

![Speed comparison](images/speed.png)


## Is there help (API documentation) for Word Blocks?
Yes, sort off. If you press Settings in the home screen, or Help > Setting, you can pick _Help and Support_ and then
_Word Blocks description_. This has a two or three lines of help per block.

It has a very bad document structure (hard to see sections), does not support copy and paste, and worst of all,
can not be opened while programming. Grr.

![Word Blocks help](images/wordblockhelp.png)


## How to stop my Word Blocks program?
Good question: if you 
n't stop, the hub will not power down, so stopping is important.

In Word Blocks, there is an explicit stop block.

![Stopping in Word Blocks](images/wordblockstop.png)

In Python, I haven't found a good one yet. 


## Can I show two digits on the screen

The screen is a bit small, but we can make a 2x5 font for digits that is sort-of readable 
(especially the 0 and 8 are a bit hard to read).

![Show99](images/show99.png)

I was inspired by [Anton's mindstorms hacks](https://antonsmindstorms.com/2021/02/08/how-to-display-two-digit-numbers-on-a-5x5-led-matrix-with-lego-spike-prime-or-robot-inventor/)
but made it a bit simpler. See the Word Blocks [Example](blocks/Show99.lms).

The python version is even simpler, see question below.


## What is degrees, position and relative position?

The motors in Mindstorms 4 are a bit different from the earlier ones (NXT and EV3).
The motors in the last 3 generations of Mindstorms all have a position sensor, but the one in Mindstorms 4 is _absolute_.
So, for example, it not only knows that it _moved_ 45 degrees, it also knows it is _at_ 60 degrees (assuming the motor started at 15).
The "0 degrees" is arbitrary, but it is marked on the motorhub.

![Position](images/position.jpg)

So, a motor moves _degrees_ (or _rotations_), the "delta", thereby moving from one absolution _position_ to another absolute _position_.
A _position_ is always a number from (including) 0 to (excluding) 360 (in Python it seems to be -180..+180).
The _degrees_ to move can be any number, even fractional (not very exciting) or negative (turn the other way around).

The absolute sensor is nice for "non drive motors". When motors are used for driving, they turn and turn, and there is no need for a "zero" position.
But when motors are used for a door, a windshield wiper, a swinging radar, a clock, the robot needs to know where the "zero" position is.
In the past you needed a touch sensor for that (or drive the motor to a mechanical stop). But no longer in Mindstorms 4.

There is one small problem though: when a motor rotates, the _position_ sensor wraps around: it goes from 357, 358, 359, 0, 1, 2.
To solve this, there is a second "sensor" _relative position_. This one keeps on counting.
In the screenshot below, the motor moved (by hand actually) nearly 1.3 rotation. The _relative position_ recorded this as 460 degrees, but the _position_ of the hub is 100 degrees.

![Position versus relative position](images/position-vs-rel.png)

For me the term _relative position_ is a bit confusing, I expected something like "cumulative degrees".
But it is clear the _position_ is actually "absolute position" (LEGO just dropped the "absolute"), so the other one is "relative" :-)

The _position_ sensor is located in the "Motors" section of the Word blocks palette,
but for the _relative position_ sensor you need to enable the extension "More Motors".

One last word, some of my motors were ~10 degrees off with respect to their "zero mark".
It is structural, so that was easy to fix by adding a correction of 10.
However in later releases of the LEGO app, the motors were calibrated solving this problem.


## What is the mapping from integer to colors?

There are several places where colors play a role.

The most obvious is the color sensor. It returns the detected color.
Secondly, the center button can emit a chosen color.
Also the 3x3 LED matrix from Spike Essential uses color.

The Word Block has a color picker, but sometimes, you might want to store or manipulate the numerical color value.

![Color chart](images/color-chart.png)

The "turquoise" color is the color of Robot Inventor (e.g. the hub bottom).


## What are all those (blue) Motor blocks?

At first, the amount of motor block is overwhelming. Let's look at the blue blocks first: "Motors".

The logo and name is a first important hint: the blue blocks ("Motors" and "More Motors") operate on a _single_ motor.
The pink blocks ("Movement" and "More Movement") operate on _two_ motors, the left and right one for driving (movement).

Actually, that is a lie (but a simplification that helps understanding).
The pink Movement blocks control _two_ motors and _keeps them in sync_. If one stops (break it with your hand), the other stops as well.
Think of a bulldozer with a left and a right track, they need to move at the same speed for the bulldozer to go straight.
The blue motor blocks on the other hand, control one motor. So there is no syncing.
And yes, you can use a blue block to control two motors in one go, but they are _not_ synced.

Back to the blue blocks.

![Motors](images/motors1.png)

The first block tells the _selected motor_ to move, either in _rotations_, _degrees_, or _seconds_.
You can specify the _amount_ and the _direction_ (clockwise or counter clockwise).
Note that if the amount is negative, the motor reverse the direction.

The only thing that is missing in this command is _speed_. LEGO decided to exclude speed from the motor blocks.
Instead they have a separate set-speed block (5th in the figure above); it sets the default speed for that motor.
We will see that some blocks do have a speed parameter, this takes precedence over the default speed.
If there is no set-speed block, the defaults is 75%.

The second motor block is similar, but instead of setting an amount, we set a target _position_.
Note that we can force the direction (clockwise or counter clockwise), or let the motor take the shortest path.

The first two blocks have a target (in rotations, degrees, seconds, or position).
These blocks switch on the motor(s), waits till the target is reached, and switch off the motor.
Only then the block finishes and the next block will be executed.

Block 3 and 4 split this start-wait-stop; they are needed when the target is not know when starting the motor.
There is no amount, just direction (also here the speed comes from the set-speed block).
Block 3 start-motor starts a motor, there is no wait the next block is executed immediately - but the motor keeps on rotating.
At some moment - e.g. a sensor sees that the robot gets close to a wall - block 4 stop-motor is executed.
By the way, note the subtle spacing in the figure above: block 3 and 4 belong together, the spacing is narrow.

Block 5 sets the default speed as discussed above.

Block 6 and 7 have a different shape.
The first 5 blocks are known as _Stack Blocks_ in [scratch](https://en.scratch-wiki.info/wiki/Blocks), I would call them _statements_.
Block 6 and 7 are known as _Reporter Blocks_, I would call them (integer or string) _expressions_.
In this case they are special form of an expression: they are a function call to a sensor.
The _position_ gives the (absolute) position of the motor (0..359), and _speed_ the actual speed.
Note that speed is _not_ the speed set with the set-speed block, but the actual speed of the (running) motor.

There are more blue block: there is an extension with the obvious name More Motors.
Roughly they add a speed parameter to the stack blocks.

![More Motors](images/motors2.png)

The first "more motors block" is similar to the first "motors block".
It tells the _selected motor(s)_ to move, either in _rotations_, _degrees_, or _seconds_.
You can specify the _amount_ but not explicitly the _direction_ (you can do that by negating the amount).
What is extra is that we can override the default _speed_.
Note that if the speed is negative, it also reverse the direction.

The second "more motors block" is similar to the third "motors block".
It switches the motor on. No direction, but there is _speed_.
Also here, if the speed is negative, direction is reversed.

The third one is similar to the second "motors block": it goes to a position.
But in this case a _relative position_ so there is no need for a path (clockwise or counter clockwise).

Note that _relative position_ is like a software variable.
It tracks changes in _position_, but it does not reset when _position_ transitions from 359 to 0.
With block 4 set-relative-position we can write that variable (usually reset it to 0), and with block 5 we can read it (find how much degrees the motor rotated since reset).

The next two blocks (6 and 7) are about _power_. I guess they measure current through the motors as opposed to RPM.
Have not used this, but did test this in Python (see other question).

The stop and stall blocks (8, 9 , 10) are not working for me - do not understand them.

Have not used the acceleration.

Note that set-motor-stop, set-stall-detection, and set-acceleration, are settings, like set-speed.


## What are all those (pink) Movement blocks?
Why are there pink Movement blocks next to the blue Motor blocks?

The pink Movement blocks control _two_ motors and _keeps them in sync_. If one stops (break it with your hand), the other stops as well.
Think of a bulldozer with a left and a right track, they need to move at the same speed for the bulldozer to go straight.
The blue motor blocks on the other hand, control one motor. So there is no syncing.

The crux is the motors are kept in sync. You will mostly use them for driving, but you could also control two windshield wipers.
Because they are often used for driving, we see one more unit for _amount_: centimeters (ok two: also inches).
For this to work, we need to set the circumference of the wheel.

![Wheel circumference](images/wheel.png)

As we see, the standard wheel has a circumference of 175.9 mm, and indeed that is the default setting as we can see in the 7th pink block.
The 6th block is probably even more important: it identifies which two ports are used for the movement motors.
Please note that A+B is different then B+A: the direction reverses.
The 5th block is the default speed setting for the movement motors.
This completes the explanation of the last three block (5, 6, and 7), the settings blocks.

![Movement](images/movement.png)

The blocks that are left (1-4) are familiar.
We have two target blocks (1 and 2), where we can set the target (in cm, inch, rotations, degrees, seconds).
We have the no-target blocks (block 3 and 4) that start and stop.
All block have in common that we need to set the "synchronisation" between the motors.

The first block allows forward and backward (both motors same speed), or left and right (one motor still, the other rotating).

The second and third block allow to fine-tune the speed ratio between the wheels.
This is a bit funny: up to 95% both motors go in the same direction, but one slower and slower (at 95% it is nearly stopped).
However, at 100% the "slow" motor suddenly runs at full speed in reverse. See question below on movement graph (Python).

We can also add an extension, properly named More Movement.

![More Movement](images/movement2.png)

As with the blue blocks, now the speed is part of the blocks, overriding the default.
The difference with blue is that we need to set the speed for both motors.
So either there are two speed parameters, or one "steer" and one "speed".
Also here we have blocks that use power (motor current?) instead of speed (motor RPM).

And I have the not yet understood stop, stall or acceleration blocks.


## How do I add an extension?

The Word Blocks has a full palet of blocks to chose from.
But you can add even more blocks, from so-called extensions.
Example are

- Extra motor and movement block
- Sound via host
- Blocks that are specific for the models that come with the box
- Game controller integration

![Extensions](images/extensions.png)


## Can I "remote control" my robot?
A bit hidden feature in the Word Block editor are the two icons on the right hand side.

The top one (Remote Control) allows you to create a "Remote Control" pane in the environment, with _widgets_.
The widgets on the PC pane communicate via Bluetooth (and presumably also USB) to the Hub.
On the hub they trigger events that can be used in your program.

Great feature! Missing are widgets that _output_ content; most _input_ events in you program.
For example a virtual LED would be nice, or a string box, or a string list (dare I say "console").

There is one serious drawback: the program [needs](https://www.lego.com/en-us/service/help/products/themes-sets/lego-mindstorms-robot-inventor/coding-with-the-lego-mindstorms-robot-inventor-app-408100000020946#:~:text=Because%20Streaming,running) to execute in _streaming_ mode (i.e. live connection to the PC). 

The remote control is not present in Python - probably because it has no streaming mode.

![Remote Control](images/remotecontrol.png)


## Can I remote control my robot with a game controller?
At this moment in beta, there is the option to add support for game controllers (Sony, Microsoft).

Click the Block Extension button and then either enable the Playstation DualShock or XBox One controller.
New blocks will pop-up in your palette (left).

There is one serious drawback: the program [needs](https://www.lego.com/en-us/service/help/products/themes-sets/lego-mindstorms-robot-inventor/coding-with-the-lego-mindstorms-robot-inventor-app-408100000020946#:~:text=Because%20Streaming,running) to execute in streaming mode (ie live connection to the PC). Another drawback is the latency, lingo for "slow": the button press goes from controller, via Bluetooth link, to the PC; the PC streams actions to the hub. 

The game control is not present in Python - probably because it has no streaming mode.
It is pity that Python does not have a Bluetooth package so that we can directly hookup Bluetooth devices.

![game controller](images/btcontroller.png)


## How to get my game controller to work?
I ordered a [replica DualShock4](https://www.aliexpress.com/item/1005001493670700.html) of which the rumors tell it is working.
In the mean time, I can confirm it works with LEGO Mindstorms.

It took me some time to get it connected to the (Windows) PC. This is what I did.
 - Your PC must have Bluetooth. Laptops typically have that, desktops typically must use a Bluetooth dongle 
   (e.g. something like [this](https://nl.aliexpress.com/item/4000558398862.html) - note did not test this one myself!)
 - You must have enabled Bluetooth in Windows.
   Open the "action center" (the speech bubble right to the clock in the system tray) and make sure Bluetooth is "blue".  
   ![Enable Bluetooth](images/bluetooth1.png)
 - Only the first time, _right-click_ on the blue Bluetooth button and select "Goto Settings".
 - In "Bluetooth & other devices" settings, press "Add Bluetooth or other device".  
   ![Add Bluetooth device](images/bluetooth2.png)
 - In the window that pops up, click "Bluetooth" (top) - I did not use "Everything else" (bottom) although it is mentioning Xbox controllers.  
   ![Add Bluetooth device](images/bluetooth3.png)
 - Now, bring the game controller in pairing mode. 
   To do that, press the SHARE button, and while that is kept pressed, also press center POWER button.  
   ![Pairing mode](images/dualshock.png)  
   Keep them both pressed for around 5 seconds, until pairing mode is entered.
   When pairing mode is entered, the colored light on the game controller starts flashing blue (two flashes then a wait).
 - The game controller should appear in the "Add a device" list.
   Click it. "Connecting" appears, and after a while you can click "Done".  
   ![Add Bluetooth device](images/bluetooth4.png)  
   Once connected, the colored light on the game controller is permanently on (blue).
 - The LEGO app should now also show that a controller is connected.  
   ![Bluetooth controller connected](images/bluetooth5.png)  


## How can I test my game controller?
I wrote a [test](blocks/DualShockTest.lms), which test all buttons, except SHARE, OPTIONS, or POWER.

![DualShockTest](images/DualShockTest.png)


## How can I switch off my game controller?
Good question. Don't know myself.

I think that on Playstation 4 devices, you can click OPTIONS, then you get a menu and chose "power off" of the Playstation 4.
Or you press the power button on the Playstation 4 - this likely also switches off it "keyboard" - the game controller.

But we don't have a Playstation 4 to switch off.
What I do is to power cycle (switch off and on) Bluetooth in "action center".


## Can I have a peek under the hood (Debug mode)?
Yes we can. The LEGO app can be switched to Debug mode, and this gives us several peeks.
You must have some software background to do this.

The process to switch the LEGO app to Debug mode is described by 
[attilafarago](https://digitalbrick.home.blog/2021/09/20/experiments-with-the-spike-advanced-mode-debug-mode/).
In a nutshell, take these steps:
 - Exit the LEGO app.
 - Navigate in your file explorer to 
   `C:\Users\<user>\AppData\Local\Packages\TheLEGOGroup.LEGOMINDSTORMSInventor_m36angppq0g76\LocalCache\Roaming\MINDSTORMS_ROBOTINVENTOR\`.
 - Open `settings.json` (suggest to back-up that file first).
 - Add the line `"ui.debug": true,` (at the top) assuming it is not there yet, otherwise change `false` to `true`.
 - Restart LEGO app, it has a warning at the bottom `Debug Mode (Click to expand)`.

Read the post of attilafarago for details, but for me the most important aspects of the Debug mode are these:
 - When we click the `Debug Mode (Click to expand)` we get an extra side panel with debug options.
   Will not discuss that in this FAQ.
 - The menu bar at the top has an extra "Debug" entry.
   With this we can see how the Word Blocks are compiled to Python code just before they are send to the hub.
   See question below.
 - We get an extra extension: Word Block for advanced usage.
   For an example see the question on the 3x3 LED matrix.


## Is Word Block compiled to Python?
Yes it seems so.
 - Enable Debug mode (see other question).
 - Create a Word Block program.
 - Press the new menu entry `Toggle Developer Tools`, this pops up an extra window.
 - Select the `console` tab.
 - Compile/upload the program to the hub (as you normally would, e.g. press the play button).
 - On the console you see the generated Python code.

![Generated python](images/WordBlock2Python.png)

```python
import hub
from runtime import VirtualMachine

# When program starts
async def stack_1(vm, stack):
    # Control forever
    while True:
        # Beep for time
        await vm.system.sound.beep_async(60, 200)
        # Control wait until
        while True:
            if hub.button.right.is_pressed():
                break
            yield 0
        # Beep for time
        await vm.system.sound.beep_async(72, 200)
        # Control wait until
        while True:
            if hub.button.left.is_pressed():
                break
            yield 0
        yield

def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "DoQxmpFih88L1GjKB3fI")

    vm.register_on_start("EnSC-Bz3km2eRaiY5isv", stack_1)

    return vm
```


## Can I use the large angular motor with Robot Inventor?

![Large angular motor](images/large-angular-motor-88017.png)

Yes, I have the angular motor, and it is automatically recognized as a motor.
The LEGO app does not make a difference with the standard motors.


## Can I use the touch/force sensor with Robot Inventor?

![Force sensor](images/Education-SPIKE-Prime-Force-Sensor-45678.png)

The LEGO Robot Inventor does not ship with a "touch" sensor.
Spike prime does, and you can order it separately. I did.

After adding the standard extension "More Sensors" we get Word Blocks for the force sensor.

![More sensors](images/more-sensor.png)


## Can I use the 3x3 LED color matrix with Robot Inventor?

![Color matrix](images/Technic-3x3-Color-Light-Matrix-45608.png)

When you use the Robot Inventor in the "test mode" 
(pressing the middle button when the screen shows the "play" slot)
we can press the left or right button to change the speed of a connected motor.
When we hook up the color matrix the test mode sort of works as for a motor: 
when we change the "speed" with the left and right button, the matrix changes color (all 9 LEDs in one go).

I did not yet succeed in controlling it from _plain_ Word Blocks.
I do have a Python solution (see other question and answer below).
And there is a Word Blocks solution if you are willing to use the Debug blocks you get in the Debug mode (see other question).


## Can I use the 3x3 LED color matrix with Robot Inventor Debug mode?

After a study in Python (see question below), I learned how to control the matrix.

Mode 0 uses the matrix as a "battery level indicator", will not use that here.
Mode 1 switches the whole matrix to one uniform color at one high brightness level.
Mode 2 allows individual LEDs in the matrix to be controlled qua color and brightness. That does sort-of work.
Mode 3 configures transitions between matrix mode switches.

The LED matrix does (not yet) have a Word Block, but the Debug mode 
offers Word Blocks that we can use.

 - Enable the Debug mode (see a question above).
 - Start a new Word Blocks project
 - Press the "Show block extensions" on the left bottom.
 - At the bottom of the extensions press the "debug" button. 
   This adds a dark blue group of debug extensions.
 - Now enter below program.
    
![Debug mode](images/Matrix-Debug-WordBlocks.png)

As we can see in the [YouTube video](https://www.youtube.com/watch?v=tcQDFgmpieU), 
mode 1 and 3 work, but 2 doesn't.

That is bad, because **mode 2 is the most important mode of the matrix**.

It turned out that the error is the string we send; we should not pass a string of nine bytes, we should pass a list of nine numbers separated by spaces.
See below for details - and a bug in the Debug blocks.


## Bug in Robot Inventor Debug blocks?

For mode 2, we need to send 9 bytes to the matrix. 
In Python we can just send a string of 9 characters and that is what I tried in our 
first experiment: send a string of 9 characters, just like in Python. 

Didn't work. I decided to send a list of 9 integers (`lst` filled with nine integers via `col`).

![mode 2](images/Matrix-Debug-WordBlocks-Mode2.png)

And the good news is: that works ... except for bright colors.

Later I found out that the list variable (`lst`) is not needed, we can simply enter a list of numbers in the Word Block,
we just need to separate the numbers with spaces.

![mode 2](images/Matrix-Debug-WordBlocks-Mode2-Simple.png)

Both the above Word Block programs work exactly the same.
They make 4 times a pattern (the Dutch National Flag), and this is how they look (no video this time :-).
Note that the last one is wrong - see below why.

![mode 2 result](images/Matrix-Debug-WordBlocks-Mode2-result.png)

Below each pattern (flag) we find the 9 (decimal) values that are in `lst` and are send to the
matrix. Below that, we see the same numbers in hexadecimal. This makes it easier to interpret
because the first nibble encodes the brightness, and the second nibble encodes the color 
(an enumeration: red=9, white=10, blue=3, see another question).

Behind the scenes, the Word Block is translated to Python, and it converts the
the series of 9 numbers to a byte array. That array is depicted on the third row.

However, there is a bug in the Word Block compiler; it uses UTF-8 to form the byte array,
and that makes LED values above 127 (above 0x7F) to be encoded in _two_ bytes.
The byte that is prepended is the first UTF "escape" character 0xC2.

On the last line we see what that means for the brightest pattern, instead of 9 bytes
we send 18 bytes to the matrix (which only looks at the first 9). Every odd byte is C2 
which renders as purple, as we can see in the fourth flag above.

I had a peek at the generated code, and I believe it really is a compiler bug.

This is the offending line, here in action using LED values below 128.
We see that it produces a byte array of nine bytes, with the bytes we expect (e.g. ASCII value of `Y` is 89, `Z` is 90 and `S` 83).

```python
>>> bytes("".join([chr(math.floor(clamp(to_number(p_1), 0, 255) + 0.5)) for p_1 in " 89  89  89   90  90  90   83  83  83".split()]),"utf-8")
b'YYYZZZSSS'
```

When using LED values above 128, we get a wrong result: an byte array of 18 bytes.
The even bytes are all wrong (0xC2), the odd bytes are correct.

```python
>>> bytes("".join([chr(math.floor(clamp(to_number(p_1), 0, 255) + 0.5)) for p_1 in "153 153 153  154 154 154  147 147 147".split()]), "utf-8")
b'\xc2\x99\xc2\x99\xc2\x99\xc2\x9a\xc2\x9a\xc2\x9a\xc2\x93\xc2\x93\xc2\x93'
```

The fix is simple, the code should not go from int-array _via char-array_ to byte-array. 
It should directly go from int-array to byte-array.

If we try this new code, with the values below 128 we get the same result as before.

```python
>>> bytes([math.floor(clamp(to_number(p_1), 0, 255) + 0.5) for p_1 in " 89  89  89   90  90  90   83  83  83".split()])
b'YYYZZZSSS'
```

When we try the new code with the high values it now also produces the correct result.

```python
>>> bytes([math.floor(clamp(to_number(p_1), 0, 255) + 0.5) for p_1 in "153 153 153  154 154 154  147 147 147".split()])
b'\x99\x99\x99\x9a\x9a\x9a\x93\x93\x93'
```

Would be nice if LEGO would fix this.
Would also be nice of the Debug Word Blocks would be a normal extension, and that you don't need to switch the app to Debug mode.
Finally, it would be nice if the `to_number()` would also accept numbers of the form 0x9A, that would make the LED settings easier to read (for the nerds).




















![next chapter](images/chapter-next.png)
# Python specific questions


## How can I debug my Python program?
Python lacks the monitor feature. Bummer!
But it does have something better: a console.

You can just `print()` in the hub code, and the print result is send to the PC console.

![Console](images/console.png)

I have not yet found a way to `input()` - that is a pity.

I also have not found a way to clear the console.

Finally, I have not found keys to scroll down the console.


## Is there help (API documentation) for Python?
The help for Python is found on the right had side in the Python editor.

It is better than the help for Word Blocks. Document structure is better but not good.
Does support copy and paste (although not for every piece of text).
Can be open during programming (pfeew).

![Python help](images/pythonhelp.png)


## How to stop my Python program?
Good question: if your program doesn't stop, the hub will not power down, so stopping is important.

In Word Blocks, there is an explicit stop block. 
In Python, I haven't found a good method yet. I did find `sys.exit(0)` (don't forget the `import sys`).
It does stop the program, but with a sort-of error.
You can see this in the console (red message), but also the center LED on the hub flashes red 3 times.

![Stopping in Python](images/pythonstop.png)

Instead of using `sys.exit()`, we can also use `raise SystemExit`, which is more or less the
[same](https://docs.python.org/3/library/exceptions.html#:~:text=exception%20SystemExit,function.).
It also suffers from the same problem: red message in console and red flashes on hub.


## How can I set the 5x5 matrix in Python?
There is no easy way in Python to put an image in the 5x5 matrix, other then the list of standard ones.
There is the `hub.light_matrix.set_pixel(x,y,bright)` API, setting one pixel at a time.
I made my own helper.

```python
from mindstorms import MSHub
hub = MSHub()

# Lights up 5x5 matrix.
# Parameter `bits` is a 25 bits vector: a 1 switches on that led.
# Bit 24 is upper left, bit 0 is lower right.
def set_image(bits):
    hub.light_matrix.off()
    cur=1<<24
    for y in range(5):
        for x in range(5):
            if bits & cur : hub.light_matrix.set_pixel(x,y,100)
            cur >>= 1

spiral= 0b_01111_10000_10110_10001_01110

set_image( spiral )
```

with this as result

![Spiral on hub matrix](images/spiral.jpg)

A downside of the helper is that it sets all pixels either to 0 or to 100 percent brightness.

As it turns [out](https://m.facebook.com/groups/SPIKEcommunity/permalink/1113849935659904), there is a low-level way.
This means, not using `minstorms.MSHub`, but rather `hub`. Secondly, it is not obvious that `hub.display.show()` is overloaded:
it not only accepts _strings_ (`hub.display.show("Hello")`), but also _images_.
I hear you ask what images are. Well, images are objects created from the class `Image`.

```python
>>> import hub
>>> img=hub.Image('97531:86420:00900:02468:13579')
>>> hub.display.show(img)
```

![low level display control](images/display.jpg)


## Can I show (hex) digits on the screen

The screen is a bit small, but we can make a 2x5 font for digits that is sort-of readable 
(especially the 0 and 8 are a bit hard to read).

![Show99](images/show99.png)

This version uses the high level `MSHub` module.
The function `decdigits(num)` shows a number between 0 and 99 on the screen.

```python
font = [ "99999:99999", "90090:99999", "99909:90999", "90909:99999", "00990:99999", "90999:99909", "99999:99909", "99909:00099", "99099:99099", "90999:99999" ]
def decdigits(num) :
    hub.light_matrix.show( font[num//10] + ":00000:" + font[num%10] )

hub = MSHub()
hub.speaker.beep()
for ix in range(100) :
    decdigits(ix)
    wait_for_seconds(0.2)
```

This version uses the low level `hub` module.
The function `hexdigits(num)` shows a hexadecimal number between 0 and ff on the screen.


```python
import hub,time
font = [ "99999:99999", "90090:99999", "99909:90999", "90909:99999", "00990:99999", "90999:99909", "99999:99909", "99909:00099", "99099:99099", "90999:99999" 
       , "99909:99999", "99999:99900", "99999:90009", "99900:99999", "99999:90909", "99999:00909" ]
def hexdigits(num) :
    img = hub.Image( font[num//16] + ":00000:" + font[num%16] )
    hub.display.show(img)
hub.display.align(5)
hexdigits(0xAf)
```


## Can I use the 3x3 LED color matrix with Robot Inventor?

![Color matrix](images/Technic-3x3-Color-Light-Matrix-45608.png)

I did not yet succeed in controlling it from Word Blocks, but I do have a Python solution:
 
```python
import hub,  time

matrix = hub.port.A.device
matrix.mode(2)

while True:
    matrix.mode(2,b"III@@@@@@")
    time.sleep(4)
    matrix.mode(2,b"@@@@@@FFF")
    time.sleep(2)
    matrix.mode(2,b"@@@HHH@@@")
    time.sleep(1)
```

Notes
 - We use the `device` of a `port`.
 - We must first select `mode(2)`.
 - Next we must send exactly 9 bytes to configure the LED matrix - note that we use a byte string `b'...'`. 
 - The byte at position `i` in the string controls LED `i`.
 - The value `v` of each byte shall be `v=b*16+c`, where `b` is the brightness, and `c` the color.
 - Legal values for `b` are 1..10, and legal values for `c` are 0..10.
 - b=1 is most dim, b=10 is most bright.
 - c is the standard LEGO color scheme.

   |  0  |   1   |   2  | 3  |    4    |  5 |  6  |   7  |   8  | 9 |  10 |
   |-----|-------|------|----|---------|----|-----|------|------|---|-----|
   | off |magenta|violet|blue|turquoise|mint|green|yellow|orange|red|white|
   
 - If we write `v` in hex it looks like `bc`: e.g. most dim blue is \x13 and the most bright red is \xA9.
 - Note that the brightness level 3 colors are in the range `\x30`, .. `\x39`, `\x3A`,  
   which happens to match the characters `'0'`, .. `'9'`, `':'`
 - Similarly, brightness level 4 colors are in the range `\x40`, `\x41`, .. `\x4A`, 
   which happens to match the characters `'@'`, `'A'`, .. `'J'`,
   (brightness 5 would be `'P'`, .. `Z`).
 - Next, brightness level 6 colors are in the range `\x50`, `\x51`, .. `\x5A`, 
   which happens to match the characters ``'`'``, `'a'`, .. `'j'`,
   (brightness 7 would be `'p'`, .. `z`).

This leads to the following "shortcut" table.

![color codes](color-table/table.png)

I learned that each device has a "mode".
A mode is sort of a register that determines the state of the device.
The LED matrix has four modes, see
[readthedocs](https://buildhat.readthedocs.io/en/latest/buildhat/matrix.html) or
[pdf](https://datasheets.raspberrypi.com/build-hat/build-hat-serial-protocol.pdf) about
the Raspberry pi Hat.

 - **mode 0 = M0 = "LEV O" = level output**  
   Mode 0 has an argument 0..9 that enables green bands showing a sort of battery level form 0=empty to 9=full

 - **mode 1 = M1 = "COL O" = color output**  
   Mode 1 has an argument from 0 to 10, and all LEDs will light up brightly in that color (see table above).
   
 - **mode 2 = M2 = "PIX O" = pixel output**  
   Mode 2 has nine arguments: b*16+c, where b is brightness (0..9) and c is color (0..10) 
 
 - **mode 3 = M3 = "TRANS" = transitions**  
   Mode 3 has one argument the transition effect: 0 is none (default), 1 is row-by-row, and 2 fade-down-fade-up.

The below script tests all modes.
 
```python
# Testing the LEGO Spike Prime Essentials 3x3 LED matrix
# see eg https://buildhat.readthedocs.io/en/latest/buildhat/matrix.html
# see eg https://datasheets.raspberrypi.com/build-hat/build-hat-serial-protocol.pdf

import hub,time
matrix = hub.port.F.device

# mode 0 = M0 = "LEV O" = level output
# select 0 ; write1 c0 p -- where p is a number from 0 to 9, will light the matrix in bar-graph style according to the value of p.
# Maarten:  rows of green in increasing brightness: 0=000, 1=001, 2=002, 3=003, 4=013, 5=023, 6=033, 7=133, 8=233, 9=333 useful as battery level
matrix.mode(0)
matrix.mode(0,b"\x07") # do not yet understand coding
time.sleep(1)

# mode 1 = M1 = "COL O" = color output
# select 1 ; write1 c1 p -- where p is a hexadecimal number from 0 to 0x0a will light the matrix in a solid colour according to the value of p.
# Maarten: all nine leds bright in color p 
matrix.mode(1)
matrix.mode(1,b"\x08") # 8 is orange
time.sleep(1)

# mode 2 = M2 = "PIX O" = pixel output
# write1 c2 67 72 78 82 89 92 9a a4 aa -- The first hex digit (from 0 to a) specifies the brightness and the second hex digit (from 0 to a) the basic colour.
# Maarten: nine leds set, each to \xbc: brightness b and color c
matrix.mode(2)
matrix.mode(2,b"\x67\x72\x78\x82\x89\x92\x9a\xa4\xaa")
time.sleep(1)
matrix.mode(2,"cccfffggg") # normal strings (not explicitly byte strings) work
time.sleep(1)
matrix.mode(2,"ddd") # Too short does not work
time.sleep(1)
matrix.mode(2,"iiiiiiiijjjjjjjjjjjjjjjjjjjjjjjjjjj") # Too long works
time.sleep(1)

# mode 3 = M3 = "TRANS" = transitions
# write1 c3 1 -- enables row-by-row animated transitions
matrix.mode(3) # late insight: this line is not needed for mode 3 (it is not a mode but a parameter)
matrix.mode(3,b"\x01")

matrix.mode(2)
matrix.mode(2,b"\x67\x72\x78\x82\x89\x92\x9a\xa4\xaa")
time.sleep(5)
matrix.mode(2,b"\x99\x99\x99\x9A\x9A\x9A\x93\x93\x93")
time.sleep(5)
matrix.mode(2,b"\x91\x97\x93\x94\x95\x99\x9A\x92\x96")
time.sleep(5)

# write1 c3 2 -- enables a fade to black and fade back up.
matrix.mode(3) # late insight: this line is not needed
matrix.mode(3,b"\x02")

matrix.mode(2)
matrix.mode(2,b"\x67\x72\x78\x82\x89\x92\x9a\xa4\xaa")
time.sleep(5)
matrix.mode(2,b"\x99\x99\x99\x9A\x9A\x9A\x93\x93\x93")
time.sleep(5)
matrix.mode(2,b"\x91\x97\x93\x94\x95\x99\x9A\x92\x96")
time.sleep(5)

# Mode 0: No transition, immediate pixel drawing
matrix.mode(3) # late insight: this line is not needed
matrix.mode(3,b"\x00")
```

There is a [video](https://www.youtube.com/watch?v=krTXmznwOUY) on the result.

See also the question on "port info" below.



## Can I connect to REPL - interactive Python?
Yes you can ([instructable](https://www.instructables.com/MicroPython-on-SPIKE-Prime/)).
The Python interpreter in the Hub has an interactive command shell that executes a so-called read-eval-print loop (REPL).
The Hub has two serial links, one over Bluetooth and one over USB. Both are enabled for REPL.

Connect the Hub to your PC either via Bluetooth, or, easier, a USB cable.
Right click on the Windows start button and select Device Manager, and fold open the _Ports (COM & LPT)_ section. It requires some experimentation (e.g unplug USB to see which port disappears) to determine which port(s) connect to the Hub. In my case it is COM4 (serial over the USB link) and COM5 (serial over Bluetooth).

![COM ports](images/COM.png)

Next, we need a terminal program to send an receive commands over serial. I happen to use an oldy [realterm](https://realterm.sourceforge.io/), but [putty](https://www.putty.org/) is a good and popular alternative.

Configure the COM port (115200/8/N/1), and connect.
The hub is running a program (I think `runtime.start()`) that spits out data, and this now floods the terminal. Stop that program by sending a CTRL-C.
We get a prompt from `MicroPython v1.11-1139-gf7407e5a0 on 2020-06-19; LEGO Technic Large Hub with STM32F413xx`

![Connect](images/connect.png)


## What can I do in REPL - interactive Python?

A good start is the trusted `dir()` command.

```python
>>> dir()
['hub_runtime', 'gc', '__name__', 'micropython']
```

The `gc` object [controls the garbage collector](https://docs.micropython.org/en/latest/library/gc.html),
variable `__name__` holds the value `'__main__'`, and
object `micropython` helps in [access and control of the internals](https://docs.micropython.org/en/latest/library/micropython.html).
Our best candidate is `hub_runtime`.

If you want to know what such an object offers, use `dir` again (`dir(hub_runtime)`).
Even better, this REPL offers command completion with the TAB key.
For example, after type `hu`TAB, we get `hub_runtime`, if we then type `.`TAB we get

```python
>>> hub_runtime.
__class__       __name__        start           __file__
BT_VCP          Timer           USB_VCP         hub
init            LightMethods    LinegraphMonitorMethods
MotorMethods    MoveMethods     SoundMethods    WaitMethods
ProgramMethods  HubMethods      get_event_loop  register_ports
TIMER_PACE_HIGH                 error_handler   pop_force_reset
RTTimer         notify_gesture_event            RPCProtocol
system          ProgramRunner   HubUI           runtime
scratch         sensors         __connection_changed
>>> hub_runtime.
```

After some searching, we can get the current yaw via a call to the `position`.
We called twice, rotating the hub in between.
First number looks like the yaw.

```python
>>> hub_runtime.hub.motion.position()
(25, -1, 0)
>>> hub_runtime.hub.motion.position()
(44, -1, 0)
>>>
```

The `help()` command, as suggested when we pressed ^C, is _not_ very useful.

```python
>>> help()
Welcome to MicroPython!

For online help please visit http://micropython.org/help/.

Quick overview of commands for the board:
  hub.info()    -- print some general information
  hub.status()  -- print sensor data

Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode
  CTRL-F        -- on a blank line, enter filetransfer mode

For further help on a specific object, type help(obj)
For a list of available modules, type help('modules')
>
```

The `hub.info()` does not work: `name 'hub' isn't defined` (we already knew that, `hub` was not listed by `dir`).
The "Control commands" seem a bit advanced now - see [here](https://docs.micropython.org/en/latest/reference/repl.html) for some help.
There is one good hint though: `help("modules")`.

```python
>>> help("modules")
__main__          math              uerrno            urandom
_onewire          micropython       uhashlib          ure
builtins          sys               uheapq            uselect
cmath             uarray            uio               ustruct
firmware          ubinascii         ujson             utime
gc                ucollections      umachine          utimeq
hub               uctypes           uos               uzlib
Plus any modules on the filesystem
```

This lists the module `hub`! Let's try to import it, and give the status command.

```python
>>> import hub
>>> hub.status()
{'gyroscope': (2, 8, 3), 'position': (51, 0, 0), 'accelerometer': (15, -8, 1026)
, 'port': {'C': [0, -2, 12, 0], 'D': [], 'B': [0, 2, 70, 0], 'E': [], 'A': [0, -
1, 168, 0], 'F': [14]}, 'display': '09000:09900:09990:09900:09000'}
>>> hub.sound.beep()
>>>
```

We see that we moved the robot a bit (yaw is now 51).
The `.`TAB trick made us find the beep command, which works!


## Which modules are available in Python?

The REPL help suggests to use the `hub` module.
However, the LEGO app suggest to use `mindstorms.MSHub`.
And a `dir` of both shows they are different.
This is very confusing.

With the `help("modules")` we found the `hub` module.
But it also gave the hint `Plus any modules on the filesystem`.
And we see there is a module `uos` for [basic "operating system" services](https://docs.micropython.org/en/latest/library/uos.html).
This micro-OS includes a filesystem!

```python
>>> import uos
>>> uos.listdir('/')
['projects', 'runtime', 'system', '_api', 'commands', 'event_loop', 'mindstorms'
, 'programrunner', 'protocol', 'sounds', 'spike', 'ui', 'util', 'boot.py', 'hub_
runtime.mpy', 'main.py', 'version.py', '.runtime_hash', 'extra_files', '.extra_f
iles_hash', 'bt-lk1.dat', 'bt-lk2.dat', 'runtime.log']
>>> uos.listdir('/mindstorms')
['__init__.mpy', 'control.mpy', 'operator.mpy', 'util.mpy']
>>> print( open('/mindstorms/__init__.mpy','r').read() )
M uP
,mindstorms/__init__.py€apii€"large_technic_hub*T2
MSHubLargeTechnicHub4QcT
        Qc
>>>
```

Reading the file `__init__.mpy` is not very succseful.
An `mpy` file is "a binary container file format that holds precompiled code, and which can be imported like a normal .py module",
see [doucmentation](https://docs.micropython.org/en/latest/reference/mpyfiles.html#:~:text=a%20binary,module).

But its presence is important: we have a directory `mindstorms` with a file `__init__.[m]py`, and this means we have a package:
"The `__init__.py` files are required to make Python treat directories containing the file as packages.", see [documentation](https://docs.python.org/3/tutorial/modules.html#:~:text=The%20__init__.py,packages.).

We even see the string `MSHub` in the `__init__.mpy`. Let's try to import and get the yaw.

```python
>>> from mindstorms import MSHub
>>> h=MSHub()
>>> h.motion_sensor.get_yaw_angle()
50
>>> h.motion_sensor.get_yaw_angle()
62
>>>
```

Success.

We can now do in REPL what we do in the LEGO app.

Still confused about the difference between `import hub` and `from mindstorms import MSHub`.
See the question "Why are there so many ways to do ... in Python?"


## Which files are in the Python filesystem?

Since there is a micro OS (uos module) which supports a file system, we can list all files.
I wrote this Python script

```python
import os

def ls(dir='/',indent='') :
  if dir and dir[-1]!='/' : dir+='/'
  for entry in os.listdir(dir):
    stat=os.stat(dir+entry)
    if stat[0]==16384 :
      print(indent+entry+'/')
      ls(dir+entry+'/',indent+'  ')
    if stat[0]==32768 :
      print(indent+entry, stat[6])

def cat(filename):
  with open(filename,'r') as file :
    return file.read()
```

How do I get that on the hub?

- Connect via UART as above. 
- Don't forget to press ^C to get the REPL prompt.
- Copy the above Python script with the extra whiteline at the end (as in get it in the clipboard - ^C).
- In REPL goto paste mode by pressing ^E (see `help()`).
- Paste the Python script (as in paste the clipboard).
- Finish paste mode ^D (see help line at start of paste mode).
- After that, we test with `dir()` that `ls` and `cat` are present.
- Then we execte both.

The whole session looks like this, but I have removed large chunks to keep the overview

```python
MicroPython v1.11-1139-gf7407e5a0 on 2020-06-19; LEGO Technic Large Hub with STM32F413xx
Type "help()" for more information.
>>>  
# Pressed ^E here to enter paste mode
paste mode; Ctrl-C to cancel, Ctrl-D to finish
=== 
# Pasted the two function defs
===
# pressed ^D here to finish paste mode
>>> dir()
['os', '__name__', 'ls', 'hub_runtime', 'gc', 'micropython', 'cat']
>>> ls()
projects/
  22622.py 4742
  27602.py 228
runtime/
  extensions/
    __init__.mpy 197
    music.mpy 322
    sound.mpy 372
    weather.mpy 1220
  __init__.mpy 130
  multimotor.mpy 302
  stack.mpy 901
  timer.mpy 141
mindstorms/
  __init__.mpy 135
  control.mpy 58
  operator.mpy 60
  util.mpy 52
sounds/
  menu_click 13632
  menu_fastback 17584
  menu_program_start 15832
  menu_program_stop 34000
  menu_shutdown 65706
  startup 39682
spike/
  __init__.mpy 133
  control.mpy 53
  operator.mpy 55
  util.mpy 47
boot.py 0
hub_runtime.mpy 2015
main.py 118
version.py 54
extra_files/
  Affirmative 49108
  Damage 30370
  Error 11470
  Ping 32052
  Strike 25182
runtime.log 232
>>> cat('main.py')
'import gc\nimport micropython\n\nimport hub_runtime\n\nmicropython.alloc_emergency_exception_buf(256)\n\nhub_runtime.start()\n'
>>>
```

I have logged the [output of ls](files.txt).
Every directory that has an `__init__.mpy` is very likely a Python package.
This holds for every (?) directory except `extra_files` which seems to host the sounds.

The `boot.py` is run by micro python each time the hub boots.
After that, it runs `main.py`. The former file is empty (note the 0 size after the name).
The `hub_runtime.start()` is the program that spits out the data when we log in (which we stopped with ^C).


## When using a motor pair (pink block) what does the steering do (show me the graph)?

The behavior of the steer command in the (pink) motor pair blocks is not very intuitive.
When going `straight`, both motors have the same power. When going more and more to the right,
the left motor keeps its speed and right goes slower. 
So far so good. But at 100, suddenly the right motor reverses.
Can we graph this?

Unfortunately, there is no console in Word Blocks, so I wrote a script in Python.
My assumption is that `MotorPair.move()` in Python maps to the pink blocks in Word Blocks.

The script loops over all steering values, lets the motors run for 1 second, and then checks how far they got (in degrees).
Here is the code.

```python
from mindstorms import Motor, MotorPair

motorA = Motor('A')
motorB = Motor('B')
motorAB = MotorPair('A', 'B')

measurements = []
for steering in range(-110,111):
    motorA.set_degrees_counted(0)
    motorB.set_degrees_counted(0)
    motorAB.move(1, unit='seconds', steering=steering, speed=100)
    measurement= ( steering, -motorA.get_degrees_counted(), motorB.get_degrees_counted() )
    print(measurement)
    measurements.append( measurement )
```

If you run this is in REPL, you can copy the output - I don't know how to copy console output in the LEGO app :-(.
The first few lines look like this (steering, left motor degrees, right motor degrees):

```text
(-110, -819, 813)
(-109, -807, 809)
(-108, -808, 807)
(-107, -805, 808)
(-106, -807, 810)
(-105, -811, 812)
(-104, -809, 810)
(-103, -808, 812)
(-102, -808, 812)
(-101, -815, 814)
(-100, -806, 809)
(-99, -4, 417)
(-98, 0, 416)
(-97, 13, 438)
(-96, 26, 453)
(-95, 28, 586)
(-94, 33, 609)
(-93, 45, 670)
(-92, 57, 718)
(-91, 66, 747)
(-90, 75, 764)
(-89, 88, 806)
(-88, 99, 816)
(-87, 107, 819)
(-86, 116, 821)
(-85, 124, 816)
```

I have saved the complete output as [excel](MotorPairSync.xlsx), and plotted this in a graph.
 
![MotorPair Sync](images/motorpairsync.png)
 
Looking at this graph I have the following obeservations
- It is symmetrical (positive versus negative steering) - that's good.
- Let's only look at positive steering 0..100 (steer to the right).
- The left wheel has constant speed (800) over nearly the full range (0 to ~90) - make sense.
- From ~90 to 99 there is a funny dip in the left motor speed - why?
- The right wheel has a linearly decreasing speed (800 to 0) over nearly the full range (0 to 99) - sounds good. 
- The only exception is steering at 100, where the motor speed suddenly is -800 - rotate on the spot exception.
- The range above 100 is equal to the case at 100 - clipping, makes sense.


## How do callbacks work in Python?

Simple example of a callback with a button in REPL:

```python
import hub
hub.button.center.on_change(lambda ms:print("pressed",ms))
```

This "installs" a callback.
You get the REPL prompt back, and nothing seems to have changed.
But when you now press the center button for about 1 sec, out of the blue there is this message.

```text
pressed 0
pressed 1030
```

With `hub.button.center.on_change(None)` you remove the callback.

Note that the callback is like an interrupt service routine!

```python
import hub
import time

count = 0

def reset_count(ms):
  global count
  count = 0
  
hub.button.center.on_change(reset_count)

def do_count():
  global count
  while True:
    print(count)
    count = count + 1
    time.sleep(1)
```

This is a demo run.

```python
>>> do_count()
0
1
2
3
4
5   # Pressed the center button of hub here
0
1
2
3
4   
5
6
7   # Pressed ^C in REPL here
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 17, in do_count
KeyboardInterrupt:
>>>
```


## What is motor.get()?

The Python API has a `motor.get()`. It returns 4 numbers what are those?

The first number is the speed, and the last (forth) number is power.
You can check that by executing `hub_runtime.hub.port.B.motor.run_at_speed(30)`, and the do a `get()`.
The first number returned is 30. 
If you slow the motor with your hand, you see the first number stay at 30, but the last number goes up: you need more power to keep speed.

```python
>>> hub_runtime.hub.port.B.motor.run_at_speed(30)
>>> hub_runtime.hub.port.B.motor.get()
[30, 7673, 133, 32]
>>> hub_runtime.hub.port.B.motor.get()
[30, 12439, -141, 42]
>>> hub_runtime.hub.port.B.motor.run_at_speed(0)
```

If on the other hand, you issue `hub_runtime.hub.port.B.motor.pwm(40)` and then do `get()`s, 
this changes (note that PWM is a frm of power control).
The first number returned is ~40. 
If you slow the motor with your hand, you see the first number drop, but the last number stays at 40: with constant power, the speed reduces with friction.

```python
>>> hub_runtime.hub.port.B.motor.pwm(40)
>>> hub_runtime.hub.port.B.motor.get()
[41, 22643, -16, 40]
>>> hub_runtime.hub.port.B.motor.get()
[30, 24829, 10, 40]
>>> hub_runtime.hub.port.B.motor.pwm(0)
```

The middle two numbers are the relative and absolute position.

In the image below, I first aligned the motor on the O (actually just over it) - and then I powered it (plugged it in).
Notice that the absolute position is indeed a bit positive (18). The relative position is a software position, initialized to 0 on power up.
So, first photo shows 0, 18 

The I (manually) turned the motor clockwise by 61 degrees.
Second photo confirms that the relative position is now 61 and the absolute 79.

I hand rotated about 80 more clockwise, with 139, 158 as result. Still makes sense.

![Motor position](images/rotate-A.jpg)

A small surprise comes after rotating another 50 degrees clockwise.
The relative position 139 increases to 193, which makes sense.
The absolute position changes from 158 to -149. 
So here we see that absolute positions are in the range -180..+180.

Turning some more clockwise goes to 308, -33, so relative still grows and absolute gets closer to 0.

Turning even more clockwise, the relative keeps on counting even beyond 360 (377), and absolute starts increasing from 0 again.


## My motor O position is not 0?

When I handposition my 4 motors to O, then connect them to the hub, and then check their position, I get this result

```pyton
>>> hub_runtime.hub.port.A.motor.get()
[0, 0, 15, 0]
>>> hub_runtime.hub.port.B.motor.get()
[0, 0, 5, 0]
>>> hub_runtime.hub.port.C.motor.get()
[0, 0, 0, 0]
>>> hub_runtime.hub.port.D.motor.get()
[0, 0, 3, 0]
```

I did the handpositioning 5 times (with a reset of the hub) and tabulated that.

| motor | test 1 | test 2 | test 3 | test 4 | test 5 | average |
|:-----:|:------:|:------:|:------:|:------:|:------:|:-------:|
|   A   |   15   |   12   |   12   |   17   |   12   |   13.6  |
|   B   |    5   |    6   |    4   |    4   |    6   |    5.0  |
|   C   |    0   |    5   |    5   |    5   |    4   |    3.8  |
|   D   |    3   |    6   |    4   |    7   |    9   |    5.8  |

My conclusion is that the sensor offset is structural (as in "LEGO mounted the sensor a couple of degrees rotated").
Especially the motor connected to port A has a large deviation.

We can also test it the other way around: tell the motors to go to position 0 and look at it.

```python
>>> from mindstorms import Motor
>>> Motor('A').run_to_position(0)
>>> Motor('B').run_to_position(0)
>>> Motor('C').run_to_position(0)
>>> Motor('D').run_to_position(0)
```

As we see in the photo, none of the motors is at position O.

![Motor errors](images/motor-error.jpg)

**NOTE** In the mean time, the LEGO app has a feature to calibrate the zero position of the motors, fixing this issue.


## Why are there so many ways to do ... in Python?
The LEGO app wants us to use 

```python
>>> from mindstorms import MSHub
>>> h=MSHub()
>>> h.status_light.on()
```

Note that we create an `h` object from the `MSHub` class in the `mindstorms` package.
On that object, we call the `on()` method on a `status_light` property (?).

The above does work in Python's REPL. But the REPL way suggests an alternative:
we can use the `hub` package, and call the `led` function.

```python
>>> import hub
>>> hub.led(0,99,0)
```

What is going on here - why are there two methods?
As [Erik Mejer explains](https://www.facebook.com/groups/SPIKEcommunity/permalink/1113849935659904/?comment_id=1113856928992538&reply_comment_id=1113946612316903),
there are two layers.

![Layers](images/layers.png)

The upper layer is the easy to get started with one.
It's promoted and documented in the app; it’s what gets imported by default.

The lower layer gives access to more functionality but at the risk 
that it may not play well with the rest of the systems running on the hub. 


## What is port info telling me about modes?

I used this script when a peripheral is connected to port A.

```python
import hub,time
def infoA():
	for key,val in hub.port.A.info().items():
		if key=='modes':
			for i, v in enumerate( val ):
				print(key+"["+str(i)+"]=",v)
				time.sleep(0.1)
		else :
			print(key+"=",val)
```

When I connect the light sensor, this is the output of `infoA()`

```python
fw_version= 268435456
modes[0]= {'symbol': 'IDX', 'format': {'datasets': 1, 'type': 0, 'figures': 2, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':  0, 'name': 'COLOR', 'pct': (0.0, 100.0), 'map_in': 228, 'si': (0.0,    10.0), 'raw': (0.0, 10.0)}
modes[1]= {'symbol': 'PCT', 'format': {'datasets': 1, 'type': 0, 'figures': 3, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':  0, 'name': 'REFLT', 'pct': (0.0, 100.0), 'map_in':  48, 'si': (0.0,   100.0), 'raw': (0.0, 100.0)}
modes[2]= {'symbol': 'PCT', 'format': {'datasets': 1, 'type': 0, 'figures': 3, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':  0, 'name': 'AMBI' , 'pct': (0.0, 100.0), 'map_in':  48, 'si': (0.0,   100.0), 'raw': (0.0, 100.0)}
modes[3]= {'symbol': 'PCT', 'format': {'datasets': 3, 'type': 0, 'figures': 3, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x05\x04', 'map_out': 16, 'name': 'LIGHT', 'pct': (0.0, 100.0), 'map_in':   0, 'si': (0.0,   100.0), 'raw': (0.0, 100.0)}
modes[4]= {'symbol': 'RAW', 'format': {'datasets': 2, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':  0, 'name': 'RREFL', 'pct': (0.0, 100.0), 'map_in':  16, 'si': (0.0,  1024.0), 'raw': (0.0, 1024.0)}
modes[5]= {'symbol': 'RAW', 'format': {'datasets': 4, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':  0, 'name': 'RGB I', 'pct': (0.0, 100.0), 'map_in':  16, 'si': (0.0,  1024.0), 'raw': (0.0, 1024.0)}
modes[6]= {'symbol': 'RAW', 'format': {'datasets': 3, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':  0, 'name': 'HSV'  , 'pct': (0.0, 100.0), 'map_in':  16, 'si': (0.0,   360.0), 'raw': (0.0, 360.0)}
modes[7]= {'symbol': 'RAW', 'format': {'datasets': 4, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':  0, 'name': 'SHSV' , 'pct': (0.0, 100.0), 'map_in':  16, 'si': (0.0,   360.0), 'raw': (0.0, 360.0)}
modes[8]= {'symbol': 'RAW', 'format': {'datasets': 4, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':  0, 'name': 'DEBUG', 'pct': (0.0, 100.0), 'map_in':  16, 'si': (0.0, 65535.0), 'raw': (0.0, 65535.0)}
modes[9]= {'symbol': ''   , 'format': {'datasets': 7, 'type': 1, 'figures': 5, 'decimals': 0}, 'capability': b'@@\x00\x00\x04\x84'   , 'map_out':  0, 'name': 'CALIB', 'pct': (0.0, 100.0), 'map_in':   0, 'si': (0.0, 65535.0), 'raw': (0.0, 65535.0)}
speed= 115200
hw_version= 268435456
combi_modes= (99,)
type= 61
```

When I connect the distance sensor, this is the output

```python
fw_version= 268435456
modes[0]= {'symbol': 'CM' , 'format': {'datasets': 1, 'type': 1, 'figures': 5, 'decimals': 1}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':   0, 'name': 'DISTL', 'pct': (0.0, 100.0), 'map_in': 145, 'si': (0.0,   250.0), 'raw': (0.0, 2500.0)}
modes[1]= {'symbol': 'CM' , 'format': {'datasets': 1, 'type': 1, 'figures': 4, 'decimals': 1}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':   0, 'name': 'DISTS', 'pct': (0.0, 100.0), 'map_in': 241, 'si': (0.0,    32.0), 'raw': (0.0, 320.0)}
modes[2]= {'symbol': 'CM' , 'format': {'datasets': 1, 'type': 1, 'figures': 5, 'decimals': 1}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':   0, 'name': 'SINGL', 'pct': (0.0, 100.0), 'map_in': 144, 'si': (0.0,   250.0), 'raw': (0.0, 2500.0)}
modes[3]= {'symbol': 'ST' , 'format': {'datasets': 1, 'type': 0, 'figures': 1, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':   0, 'name': 'LISTN', 'pct': (0.0, 100.0), 'map_in':  16, 'si': (0.0,     1.0), 'raw': (0.0, 1.0)}
modes[4]= {'symbol': 'uS' , 'format': {'datasets': 1, 'type': 2, 'figures': 5, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':   0, 'name': 'TRAW' , 'pct': (0.0, 100.0), 'map_in': 144, 'si': (0.0, 14577.0), 'raw': (0.0, 14577.0)}
modes[5]= {'symbol': 'PCT', 'format': {'datasets': 4, 'type': 0, 'figures': 3, 'decimals': 0}, 'capability': b'@ \x00\x00\x04\x84'   , 'map_out':  16, 'name': 'LIGHT', 'pct': (0.0, 100.0), 'map_in':   0, 'si': (0.0,   100.0), 'raw': (0.0, 100.0)}
modes[6]= {'symbol': 'PCT', 'format': {'datasets': 1, 'type': 0, 'figures': 1, 'decimals': 0}, 'capability': b'@\x80\x00\x00\x04\x84', 'map_out': 144, 'name': 'PING' , 'pct': (0.0, 100.0), 'map_in':   0, 'si': (0.0,     1.0), 'raw': (0.0, 1.0)}
modes[7]= {'symbol': 'PCT', 'format': {'datasets': 1, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'@\x00\x00\x00\x04\x84', 'map_out':   0, 'name': 'ADRAW', 'pct': (0.0, 100.0), 'map_in': 144, 'si': (0.0,  1024.0), 'raw': (0.0, 1024.0)}
modes[8]= {'symbol': 'PCT', 'format': {'datasets': 7, 'type': 0, 'figures': 3, 'decimals': 0}, 'capability': b'@@\x00\x00\x04\x84'   , 'map_out':   0, 'name': 'CALIB', 'pct': (0.0, 100.0), 'map_in':   0, 'si': (0.0,   255.0), 'raw': (0.0, 255.0)}
speed= 115200
hw_version= 268435456
combi_modes= ()
type= 62
```


When I connect the touch (force) sensor, this is the output

```python
fw_version= 268435456
modes[0]= {'symbol': 'N'  , 'format': {'datasets': 1, 'type': 0, 'figures': 4, 'decimals': 1}, 'capability': b'\x00\x00\x00\x00\x04\x84', 'map_out': 0, 'name': 'FORCE', 'pct': (0.0, 100.0), 'map_in': 112, 'si': (0.0,   10.0), 'raw': (0.0, 100.0)}
modes[1]= {'symbol': 'ST' , 'format': {'datasets': 1, 'type': 0, 'figures': 1, 'decimals': 0}, 'capability': b'\x00\x00\x00\x00\x04\x84', 'map_out': 0, 'name': 'TOUCH', 'pct': (0.0, 100.0), 'map_in':   4, 'si': (0.0,    1.0), 'raw': (0.0, 1.0)}
modes[2]= {'symbol': 'TEV', 'format': {'datasets': 1, 'type': 0, 'figures': 1, 'decimals': 0}, 'capability': b'\x00\x80\x00\x00\x04\x84', 'map_out': 0, 'name': 'TAP'  , 'pct': (0.0, 100.0), 'map_in':   4, 'si': (0.0,    3.0), 'raw': (0.0, 3.0)}
modes[3]= {'symbol': 'N'  , 'format': {'datasets': 1, 'type': 0, 'figures': 4, 'decimals': 1}, 'capability': b'\x00\x00\x00\x00\x04\x84', 'map_out': 0, 'name': 'FPEAK', 'pct': (0.0, 100.0), 'map_in':  16, 'si': (0.0,   10.0), 'raw': (0.0, 100.0)}
modes[4]= {'symbol': 'RAW', 'format': {'datasets': 1, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'\x00\x00\x00\x00\x04\x84', 'map_out': 0, 'name': 'FRAW' , 'pct': (0.0, 100.0), 'map_in':  16, 'si': (0.0, 1023.0), 'raw': (0.0, 1023.0)}
modes[5]= {'symbol': 'RAW', 'format': {'datasets': 1, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'\x00\x00\x00\x00\x04\x84', 'map_out': 0, 'name': 'FPRAW', 'pct': (0.0, 100.0), 'map_in':  16, 'si': (0.0, 1023.0), 'raw': (0.0, 1023.0)}
modes[6]= {'symbol': ''   , 'format': {'datasets': 8, 'type': 1, 'figures': 4, 'decimals': 0}, 'capability': b'\x00@\x00\x00\x04\x84'   , 'map_out': 0, 'name': 'CALIB', 'pct': (0.0, 100.0), 'map_in':   0, 'si': (0.0, 1023.0), 'raw': (0.0, 1023.0)}
speed= 115200
hw_version= 268435456
combi_modes= (63,)
type= 63
```

When I connect the 3x3 LED matrix (bought separately), this is the output

```python
combi_modes= ()
fw_version= 285212672
speed= 115200
modes[0]= {'symbol': 'PCT', 'format': {'datasets': 1, 'type': 0, 'figures': 1, 'decimals': 0}, 'capability': b'\x80\x00\x00\x00\x05\x04', 'map_out': 80, 'name': 'LEV O', 'pct': (-100.0, 100.0), 'map_in': 0, 'si': (-9.0, 9.0), 'raw': (-9.0, 9.0)}
modes[1]= {'symbol': 'PCT', 'format': {'datasets': 1, 'type': 0, 'figures': 2, 'decimals': 0}, 'capability': b'\x80\x00\x00\x00\x05\x04', 'map_out': 68, 'name': 'COL O', 'pct': (0.0, 100.0), 'map_in': 0, 'si': (0.0, 10.0), 'raw': (0.0, 10.0)}
modes[2]= {'symbol': '   ', 'format': {'datasets': 9, 'type': 0, 'figures': 3, 'decimals': 0}, 'capability': b'\x80\x00\x00\x00\x05\x04', 'map_out': 16, 'name': 'PIX O', 'pct': (0.0, 100.0), 'map_in': 0, 'si': (0.0, 170.0), 'raw': (0.0, 170.0)}
modes[3]= {'symbol': '   ', 'format': {'datasets': 1, 'type': 0, 'figures': 1, 'decimals': 0}, 'capability': b'\x80\x00\x00\x00\x05\x04', 'map_out': 16, 'name': 'TRANS', 'pct': (0.0, 100.0), 'map_in': 0, 'si': (0.0, 2.0), 'raw': (0.0, 2.0)}
uid= bytearray(b'\x00k\x000\x18G033798\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
type= 64
hw_version= 4
>>>
```

When I connect a (small) motor, this is the output

```python
fw_version= 4096
modes[0]= {'symbol': 'PCT'         , 'format': {'datasets': 1, 'type': 0, 'figures': 1, 'decimals': 0},   'capability': b'\x10\x00\x00\x00\x01\x04', 'map_out': 16, 'name': 'POWER', 'pct': (-100.0, 100.0)       , 'map_in': 0, 'si': (-100.0, 100.0)   , 'raw': (-100.0, 100.0)}
modes[1]= {'symbol': 'PCT'         , 'format': {'datasets': 1, 'type': 0, 'figures': 4, 'decimals': 0},   'capability': b'!\x00\x00\x00\x01\x04'   , 'map_out': 16, 'name': 'SPEED', 'pct': (-100.0, 100.0)       , 'map_in':16, 'si': (-100.0, 100.0)  , 'raw': (-100.0, 100.0)}
modes[2]= {'symbol': 'DEG'         , 'format': {'datasets': 1, 'type': 2, 'figures': 4, 'decimals': 0},   'capability': b'$\x00\x00\x00\x01\x04'   , 'map_out':  8, 'name': 'POS'  , 'pct': (-100.0, 100.0)       , 'map_in': 8, 'si': (-360.0, 360.0)   , 'raw': (-360.0, 360.0)}
modes[3]= {'symbol': 'DEG'         , 'format': {'datasets': 1, 'type': 1, 'figures': 3, 'decimals': 0},   'capability': b'"\x00\x00\x00\x01\x04'   , 'map_out':  8, 'name': 'APOS' , 'pct': (-200.0, 200.0)       , 'map_in': 8, 'si': (-180.0, 179.0)   , 'raw': (-180.0, 179.0)}
modes[4]= {'symbol': 'PCT'         , 'format': {'datasets': 1, 'type': 0, 'figures': 1, 'decimals': 0},   'capability': b' @\x00\x00\x01\x04'      , 'map_out':  8, 'name': 'LOAD' , 'pct': (0.0, 100.0)          , 'map_in': 8, 'si': (0.0, 127.0)      , 'raw': (0.0, 127.0)}
modes[5]= {'symbol': '\x01\x04\x01', 'format': {'datasets': 0, 'type': 0, 'figures': 0, 'decimals': 194}, 'capability': b'\x00\x00\x00\x00\x00\x00', 'map_out':  0, 'name': '1'    , 'pct': (3444.96, 1.12104e-43), 'map_in': 0, 'si': (0.0, 2.24208e-44), 'raw': (5.73972e-42, 5.73972e-42)}
speed= 115200
hw_version= 4096
combi_modes= (14, 15)
type= 75
```

I guess `type=75` denotes a motor. An important aspect of the modes is the `name`: POWER, SPEED, POS, APOS, LOAD, 1.

Here is a small overview.

| sensor   |  type  | names                                                            |
|:--------:|:------:|:-----------------------------------------------------------------|
| light    |    61  | COLOR, REFLT, AMBI, LIGHT, RREFL, RGB I, HSV, SHSV, DEBUG, CALIB |
| distance |    62  | DISTL, DISTS, SINGL, LISTN, TRAW, LIGHT, PING, ADRAW, CALIB      |
| force    |    63  | FORCE, TOUCH, TAP, FPEAK, FRAW, FPRAW, CALIB                     |
| 3x3 LED  |    64  | LEV O, COL O, PIX O, TRANS                                       |
| motor (S)|    75  | POWER, SPEED, POS, APOS, LOAD, 1                                 |

I do not fully understand the modes. Some hints
 - `name` gives the name of the mode such as `TRANS` or `POWER`.
 - `symbol` gives the unit, such as `PCT` (percent), `DEG` (degree), `N` (newton).
 - `format` describes the data associated with the mode
   - `datasets` gives the number of values in the mode (e.g. 1 for `COL O` but 9 for `PIX O`) 
   - `type` gives the datatype of each value (0=char=8bits, 1=short=16bits, 2=int=32bits, 3=float=32bits)
   - `figures` gives the number of characters needed to display the value
   - `decimals` gives the number of decimal places needed to display the value
 - `capability` do not understand
 - `map_out` do not understand
 - `map_in` do not understand
 - `pct`, `si`, `raw` somehow gives the ranges of the values in this mode in various units (percent, signed int (?), raw)



## How can I do data logging?

Since the MicroPython environment has a filesystem, we can log data to a file.
Just standard Python ... you would expect.
I stumbled on one tricky thing, an error "object with buffer protocol required".

I believe the root cause is that MicroPython does not support writing numbers, only strings to files (they have the "characters in a buffer").
The below program takes 10 light measurements (2 seconds appart), converts each measurement to a string, and writes that to a file `data.log`.
Each measurement it gives a beep.

```python
from mindstorms import ColorSensor
from mindstorms import MSHub
from mindstorms.control import wait_for_seconds

print("datalog")
hub = MSHub()
light = ColorSensor('E')

with open('data.log','w') as logfile:
    for num in range(10):
        sample = light.get_ambient_light()
        line = str(num) + ' ' + str(sample)
        print(line)
        logfile.write(line+'\n')
        wait_for_seconds(2)
        hub.speaker.beep()
```

Notes
 - Program suffers from not ending (see question "How to stop my Python program?")
 - I passed just a filename in the example, but you can specify a full path.
 - The file `data.log` has no path, so it is written to the current directory.
   As it turns out, that is the root. 
 - How do I find my file?
   In the question "Which files are in the Python filesystem?" you'll find an `ls()` command, which works in REPL.
   If you run that, we get the following file list (abridged). At the end we find our `data.log`.
   
   ```python
   >>> ls()
   projects/
   ...
   .extra_files_hash 539
   bt-lk1.dat 69
   bt-lk2.dat 69
   runtime.log 240
   data.log 41
   ```

 - How do I "get the contents" of my file?
   In the question "Which files are in the Python filesystem?" you'll find a `cat()` command, which works in REPL.
   If you run that, we get the following content.
   
   ```python
   >>> cat('data.log')
   '0 1\n1 12\n2 7\n3 7\n4 5\n5 4\n6 6\n7 5\n8 4\n9 4\n'
   ```

 - To get them to your PC, you need someting like the [spike tools](https://github.com/nutki/spike-tools).
   To be investigated.
   
 - To delete the log file use e.g. (in REPL)

   ```python
   import os
   os.remove('data.log')
   ```

## Which functions are hidden in Python modules?

Somebody made a [dump](https://github.com/gpdaniels/spike-prime/issues/7).

Similar in [pdf](https://micropython-lego-ri5.readthedocs.io/_/downloads/en/latest/pdf/).

## How can I do parallel tasks in Python?

Use `uasyncio`? or check out my [multitask](multitask) project.

(end)

