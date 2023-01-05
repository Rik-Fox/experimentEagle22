#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on October 31, 2022, at 12:38
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import (
    sound,
    gui,
    visual,
    core,
    data,
    event,
    logging,
    clock,
    colors,
    layout,
)
from psychopy.constants import (
    NOT_STARTED,
    STARTED,
    PLAYING,
    PAUSED,
    STOPPED,
    FINISHED,
    PRESSED,
    RELEASED,
    FOREVER,
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (
    sin,
    cos,
    tan,
    log,
    log10,
    pi,
    average,
    sqrt,
    std,
    deg2rad,
    rad2deg,
    linspace,
    asarray,
)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = "2022.2.4"
expName = "experimentEagle22"  # from the Builder filename that created this script
expInfo = {
    "participant": f"{randint(0, 999999):06.0f}",
    "session": "001",
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo["date"] = data.getDateStr()  # add a simple timestamp
expInfo["expName"] = expName
expInfo["psychopyVersion"] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = (
    _thisDir
    + os.sep
    + "data/%s_%s_%s" % (expInfo["participant"], expName, expInfo["date"])
)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(
    name=expName,
    version="",
    extraInfo=expInfo,
    runtimeInfo=None,
    originPath="C:\\Users\\rfox\\PhD\\Term1_experiments_22\\experimentEagle22\\experimentEagle22.py",
    savePickle=True,
    saveWideText=True,
    dataFileName=filename,
)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + ".log", level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768),
    fullscr=True,
    screen=0,
    winType="pyglet",
    allowStencil=False,
    monitor="testMonitor",
    color=[0, 0, 0],
    colorSpace="rgb",
    blendMode="avg",
    useFBO=True,
    units="height",
)
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo["frameRate"] = win.getActualFrameRate()
if expInfo["frameRate"] != None:
    frameDur = 1.0 / round(expInfo["frameRate"])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig["Keyboard"] = dict(use_keymap="psychopy")

ioSession = "1"
if "session" in expInfo:
    ioSession = str(expInfo["session"])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend="iohub")

# --- Initialize components for Routine "Intro_Page" ---
Title = visual.TextStim(
    win=win,
    name="Title",
    text="Intro page",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=0.0,
)
SubTitle = visual.TextStim(
    win=win,
    name="SubTitle",
    text="Controls and example pic",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=-1.0,
)
arrows = visual.ImageStim(
    win=win,
    name="arrows",
    image="/home/rfox/PhD/Term1_22-23_Experiements/experimentEagle22/images/SeekPng.com_arrow-keys-png_3271603.png",
    mask=None,
    anchor="center",
    ori=0.0,
    pos=(0, 0),
    size=(0.5, 0.5),
    color=[1, 1, 1],
    colorSpace="rgb",
    opacity=None,
    flipHoriz=False,
    flipVert=False,
    texRes=128.0,
    interpolate=True,
    depth=-2.0,
)
wasd = visual.ImageStim(
    win=win,
    name="wasd",
    image="/home/rfox/PhD/Term1_22-23_Experiements/experimentEagle22/images/SeekPng.com_wasd-png_1791627.png",
    mask=None,
    anchor="center",
    ori=0.0,
    pos=(0, 0),
    size=(0.5, 0.5),
    color=[1, 1, 1],
    colorSpace="rgb",
    opacity=None,
    flipHoriz=False,
    flipVert=False,
    texRes=128.0,
    interpolate=True,
    depth=-3.0,
)
Sim = visual.ImageStim(
    win=win,
    name="Sim",
    image="/home/rfox/PhD/Term1_22-23_Experiements/experimentEagle22/images/Simulator.png",
    mask=None,
    anchor="center",
    ori=0.0,
    pos=(0, 0),
    size=(0.5, 0.5),
    color=[1, 1, 1],
    colorSpace="rgb",
    opacity=None,
    flipHoriz=False,
    flipVert=False,
    texRes=128.0,
    interpolate=True,
    depth=-4.0,
)
button = visual.ButtonStim(
    win,
    text="Click here or press spacebar to continue",
    font="Arvo",
    pos=(0, 0),
    letterHeight=0.05,
    size=None,
    borderWidth=0.0,
    fillColor="darkgrey",
    borderColor=None,
    color="white",
    colorSpace="rgb",
    opacity=None,
    bold=True,
    italic=False,
    padding=None,
    anchor="center",
    name="button",
)
button.buttonClock = core.Clock()
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Start_Page" ---
Start_Info = visual.TextStim(
    win=win,
    name="Start_Info",
    text="Any text\n\nincluding line breaks",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=0.0,
)
button_2 = visual.ButtonStim(
    win,
    text="Click here or hit Space bar",
    font="Arvo",
    pos=(0, 0),
    letterHeight=0.05,
    size=None,
    borderWidth=0.0,
    fillColor="darkgrey",
    borderColor=None,
    color="white",
    colorSpace="rgb",
    opacity=None,
    bold=True,
    italic=False,
    padding=None,
    anchor="center",
    name="button_2",
)
button_2.buttonClock = core.Clock()
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Simulation" ---

# --- Initialize components for Routine "Safety_Judgements" ---
Question = visual.TextStim(
    win=win,
    name="Question",
    text="Any text\n\nincluding line breaks",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=0.0,
)
Vehicle_image = visual.ImageStim(
    win=win,
    name="Vehicle_image",
    image=None,
    mask=None,
    anchor="center",
    ori=0.0,
    pos=(0, 0),
    size=(0.5, 0.5),
    color=[1, 1, 1],
    colorSpace="rgb",
    opacity=None,
    flipHoriz=False,
    flipVert=False,
    texRes=128.0,
    interpolate=True,
    depth=-1.0,
)
Sub_Question = visual.TextStim(
    win=win,
    name="Sub_Question",
    text="Any text\n\nincluding line breaks",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=-2.0,
)
slider = visual.Slider(
    win=win,
    name="slider",
    startValue=None,
    size=(1.0, 0.1),
    pos=(0, -0.4),
    units=None,
    labels=None,
    ticks=(1, 2, 3, 4, 5),
    granularity=0.0,
    style="rating",
    styleTweaks=(),
    opacity=None,
    labelColor="LightGray",
    markerColor="Red",
    lineColor="White",
    colorSpace="rgb",
    font="Open Sans",
    labelHeight=0.05,
    flip=False,
    ori=0.0,
    depth=-3,
    readOnly=False,
)
Sub_Question_2 = visual.TextStim(
    win=win,
    name="Sub_Question_2",
    text="Any text\n\nincluding line breaks",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=-4.0,
)
slider_2 = visual.Slider(
    win=win,
    name="slider_2",
    startValue=None,
    size=(1.0, 0.1),
    pos=(0, -0.4),
    units=None,
    labels=None,
    ticks=(1, 2, 3, 4, 5),
    granularity=0.0,
    style="rating",
    styleTweaks=(),
    opacity=None,
    labelColor="LightGray",
    markerColor="Red",
    lineColor="White",
    colorSpace="rgb",
    font="Open Sans",
    labelHeight=0.05,
    flip=False,
    ori=0.0,
    depth=-5,
    readOnly=False,
)
Sub_Question_3 = visual.TextStim(
    win=win,
    name="Sub_Question_3",
    text="Any text\n\nincluding line breaks",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=-6.0,
)
slider_3 = visual.Slider(
    win=win,
    name="slider_3",
    startValue=None,
    size=(1.0, 0.1),
    pos=(0, -0.4),
    units=None,
    labels=None,
    ticks=(1, 2, 3, 4, 5),
    granularity=0.0,
    style="rating",
    styleTweaks=(),
    opacity=None,
    labelColor="LightGray",
    markerColor="Red",
    lineColor="White",
    colorSpace="rgb",
    font="Open Sans",
    labelHeight=0.05,
    flip=False,
    ori=0.0,
    depth=-7,
    readOnly=False,
)

# --- Initialize components for Routine "AV_Judgements" ---
AV_Question = visual.TextStim(
    win=win,
    name="AV_Question",
    text="Any text\n\nincluding line breaks",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=0.0,
)
car_image = visual.ImageStim(
    win=win,
    name="car_image",
    image="/home/rfox/PhD/Term1_22-23_Experiements/pygame_ped_env/pygame_ped_env/images/Topdown_vehicle_sprites_pack/car.png",
    mask=None,
    anchor="center",
    ori=0.0,
    pos=(0, 0),
    size=(0.5, 0.5),
    color=[1, 1, 1],
    colorSpace="rgb",
    opacity=None,
    flipHoriz=False,
    flipVert=False,
    texRes=128.0,
    interpolate=True,
    depth=-1.0,
)
slider_4 = visual.Slider(
    win=win,
    name="slider_4",
    startValue=None,
    size=(1.0, 0.1),
    pos=(0, -0.4),
    units=None,
    labels=None,
    ticks=(1, 2, 3, 4, 5),
    granularity=0.0,
    style="rating",
    styleTweaks=(),
    opacity=None,
    labelColor="LightGray",
    markerColor="Red",
    lineColor="White",
    colorSpace="rgb",
    font="Open Sans",
    labelHeight=0.05,
    flip=False,
    ori=0.0,
    depth=-2,
    readOnly=False,
)
car_image_2 = visual.ImageStim(
    win=win,
    name="car_image_2",
    image="/home/rfox/PhD/Term1_22-23_Experiements/pygame_ped_env/pygame_ped_env/images/Topdown_vehicle_sprites_pack/car.png",
    mask=None,
    anchor="center",
    ori=0.0,
    pos=(0, 0),
    size=(0.5, 0.5),
    color=[1, 1, 1],
    colorSpace="rgb",
    opacity=None,
    flipHoriz=False,
    flipVert=False,
    texRes=128.0,
    interpolate=True,
    depth=-3.0,
)
slider_5 = visual.Slider(
    win=win,
    name="slider_5",
    startValue=None,
    size=(1.0, 0.1),
    pos=(0, -0.4),
    units=None,
    labels=None,
    ticks=(1, 2, 3, 4, 5),
    granularity=0.0,
    style="rating",
    styleTweaks=(),
    opacity=None,
    labelColor="LightGray",
    markerColor="Red",
    lineColor="White",
    colorSpace="rgb",
    font="Open Sans",
    labelHeight=0.05,
    flip=False,
    ori=0.0,
    depth=-4,
    readOnly=False,
)

# --- Initialize components for Routine "Thanks" ---
Thank_You = visual.TextStim(
    win=win,
    name="Thank_You",
    text="Any text\n\nincluding line breaks",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=0.0,
)
Consent_remind = visual.TextStim(
    win=win,
    name="Consent_remind",
    text="Any text\n\nincluding line breaks",
    font="Open Sans",
    pos=(0, 0),
    height=0.05,
    wrapWidth=None,
    ori=0.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    languageStyle="LTR",
    depth=-1.0,
)
button_3 = visual.ButtonStim(
    win,
    text="Click here to Finish Experiment",
    font="Arvo",
    pos=(0, 0),
    letterHeight=0.05,
    size=None,
    borderWidth=0.0,
    fillColor="darkgrey",
    borderColor=None,
    color="white",
    colorSpace="rgb",
    opacity=None,
    bold=True,
    italic=False,
    padding=None,
    anchor="center",
    name="button_3",
)
button_3.buttonClock = core.Clock()
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = (
    core.Clock()
)  # to track time remaining of each (possibly non-slip) routine

# --- Prepare to start Routine "Intro_Page" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Intro_PageComponents = [Title, SubTitle, arrows, wasd, Sim, button, key_resp]
for thisComponent in Intro_PageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, "status"):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Intro_Page" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Title* updates
    if Title.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        Title.frameNStart = frameN  # exact frame index
        Title.tStart = t  # local t and not account for scr refresh
        Title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Title, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "Title.started")
        Title.setAutoDraw(True)

    # *SubTitle* updates
    if SubTitle.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        SubTitle.frameNStart = frameN  # exact frame index
        SubTitle.tStart = t  # local t and not account for scr refresh
        SubTitle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SubTitle, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "SubTitle.started")
        SubTitle.setAutoDraw(True)

    # *arrows* updates
    if arrows.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        arrows.frameNStart = frameN  # exact frame index
        arrows.tStart = t  # local t and not account for scr refresh
        arrows.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arrows, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "arrows.started")
        arrows.setAutoDraw(True)
    if arrows.status == STARTED:
        if bool(1.0):
            # keep track of stop time/frame for later
            arrows.tStop = t  # not accounting for scr refresh
            arrows.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "arrows.stopped")
            arrows.setAutoDraw(False)

    # *wasd* updates
    if wasd.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        wasd.frameNStart = frameN  # exact frame index
        wasd.tStart = t  # local t and not account for scr refresh
        wasd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wasd, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "wasd.started")
        wasd.setAutoDraw(True)
    if wasd.status == STARTED:
        if bool(1.0):
            # keep track of stop time/frame for later
            wasd.tStop = t  # not accounting for scr refresh
            wasd.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "wasd.stopped")
            wasd.setAutoDraw(False)

    # *Sim* updates
    if Sim.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        Sim.frameNStart = frameN  # exact frame index
        Sim.tStart = t  # local t and not account for scr refresh
        Sim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Sim, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "Sim.started")
        Sim.setAutoDraw(True)
    if Sim.status == STARTED:
        if bool(1.0):
            # keep track of stop time/frame for later
            Sim.tStop = t  # not accounting for scr refresh
            Sim.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "Sim.stopped")
            Sim.setAutoDraw(False)

    # *button* updates
    if button.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "button.started")
        button.setAutoDraw(True)
    if button.status == STARTED:
        if bool(1.0):
            # keep track of stop time/frame for later
            button.tStop = t  # not accounting for scr refresh
            button.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "button.stopped")
            button.setAutoDraw(False)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(
                    button.buttonClock.getTime()
                )  # store time of first click
                button.timesOff.append(
                    button.buttonClock.getTime()
                )  # store time clicked until
            else:
                button.timesOff[
                    -1
                ] = button.buttonClock.getTime()  # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = (
                True  # if button is still clicked next frame, it is not a new click
            )
        else:
            button.wasClicked = (
                False  # if button is clicked next frame, it is a new click
            )
    else:
        button.wasClicked = False  # if button is clicked next frame, it is a new click

    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "key_resp.started")
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(
            key_resp.clearEvents, eventType="keyboard"
        )  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=["space"], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = (
        False  # will revert to True if at least one component still running
    )
    for thisComponent in Intro_PageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if (
        continueRoutine
    ):  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Intro_Page" ---
for thisComponent in Intro_PageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("button.numClicks", button.numClicks)
if button.numClicks:
    thisExp.addData("button.timesOn", button.timesOn)
    thisExp.addData("button.timesOff", button.timesOff)
else:
    thisExp.addData("button.timesOn", "")
    thisExp.addData("button.timesOff", "")
# check responses
if key_resp.keys in ["", [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData("key_resp.keys", key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData("key_resp.rt", key_resp.rt)
thisExp.nextEntry()
# the Routine "Intro_Page" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Trials = data.TrialHandler(
    nReps=5.0,
    method="random",
    extraInfo=expInfo,
    originPath=-1,
    trialList=[None],
    seed=None,
    name="Trials",
)
thisExp.addLoop(Trials)  # add the loop to the experiment
thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec("{} = thisTrial[paramName]".format(paramName))

for thisTrial in Trials:
    currentLoop = Trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec("{} = thisTrial[paramName]".format(paramName))

    # --- Prepare to start Routine "Start_Page" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    Start_PageComponents = [Start_Info, button_2, key_resp_2]
    for thisComponent in Start_PageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, "status"):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "Start_Page" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Start_Info* updates
        if Start_Info.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            Start_Info.frameNStart = frameN  # exact frame index
            Start_Info.tStart = t  # local t and not account for scr refresh
            Start_Info.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Start_Info, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "Start_Info.started")
            Start_Info.setAutoDraw(True)
        if Start_Info.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                Start_Info.tStop = t  # not accounting for scr refresh
                Start_Info.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "Start_Info.stopped")
                Start_Info.setAutoDraw(False)

        # *button_2* updates
        if button_2.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
            # keep track of start time/frame for later
            button_2.frameNStart = frameN  # exact frame index
            button_2.tStart = t  # local t and not account for scr refresh
            button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_2, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "button_2.started")
            button_2.setAutoDraw(True)
        if button_2.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                button_2.tStop = t  # not accounting for scr refresh
                button_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "button_2.stopped")
                button_2.setAutoDraw(False)
        if button_2.status == STARTED:
            # check whether button_2 has been pressed
            if button_2.isClicked:
                if not button_2.wasClicked:
                    button_2.timesOn.append(
                        button_2.buttonClock.getTime()
                    )  # store time of first click
                    button_2.timesOff.append(
                        button_2.buttonClock.getTime()
                    )  # store time clicked until
                else:
                    button_2.timesOff[
                        -1
                    ] = button_2.buttonClock.getTime()  # update time clicked until
                if not button_2.wasClicked:
                    continueRoutine = False  # end routine when button_2 is clicked
                    None
                button_2.wasClicked = True  # if button_2 is still clicked next frame, it is not a new click
            else:
                button_2.wasClicked = (
                    False  # if button_2 is clicked next frame, it is a new click
                )
        else:
            button_2.wasClicked = (
                False  # if button_2 is clicked next frame, it is a new click
            )

        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "key_resp_2.started")
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(
                key_resp_2.clearEvents, eventType="keyboard"
            )  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=["space"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[
                    -1
                ].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = (
            False  # will revert to True if at least one component still running
        )
        for thisComponent in Start_PageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if (
            continueRoutine
        ):  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "Start_Page" ---
    for thisComponent in Start_PageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData("button_2.numClicks", button_2.numClicks)
    if button_2.numClicks:
        Trials.addData("button_2.timesOn", button_2.timesOn)
        Trials.addData("button_2.timesOff", button_2.timesOff)
    else:
        Trials.addData("button_2.timesOn", "")
        Trials.addData("button_2.timesOff", "")
    # check responses
    if key_resp_2.keys in ["", [], None]:  # No response was made
        key_resp_2.keys = None
    Trials.addData("key_resp_2.keys", key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        Trials.addData("key_resp_2.rt", key_resp_2.rt)
    # the Routine "Start_Page" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "Simulation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Simulator
    print("Hello world")

    # keep track of which components have finished
    SimulationComponents = []
    for thisComponent in SimulationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, "status"):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "Simulation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = (
            False  # will revert to True if at least one component still running
        )
        for thisComponent in SimulationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if (
            continueRoutine
        ):  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "Simulation" ---
    for thisComponent in SimulationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Simulation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "Safety_Judgements" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider.reset()
    slider_2.reset()
    slider_3.reset()
    # keep track of which components have finished
    Safety_JudgementsComponents = [
        Question,
        Vehicle_image,
        Sub_Question,
        slider,
        Sub_Question_2,
        slider_2,
        Sub_Question_3,
        slider_3,
    ]
    for thisComponent in Safety_JudgementsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, "status"):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "Safety_Judgements" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *Question* updates
        if Question.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            Question.frameNStart = frameN  # exact frame index
            Question.tStart = t  # local t and not account for scr refresh
            Question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "Question.started")
            Question.setAutoDraw(True)
        if Question.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                Question.tStop = t  # not accounting for scr refresh
                Question.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "Question.stopped")
                Question.setAutoDraw(False)

        # *Vehicle_image* updates
        if Vehicle_image.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            Vehicle_image.frameNStart = frameN  # exact frame index
            Vehicle_image.tStart = t  # local t and not account for scr refresh
            Vehicle_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Vehicle_image, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "Vehicle_image.started")
            Vehicle_image.setAutoDraw(True)
        if Vehicle_image.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                Vehicle_image.tStop = t  # not accounting for scr refresh
                Vehicle_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "Vehicle_image.stopped")
                Vehicle_image.setAutoDraw(False)

        # *Sub_Question* updates
        if Sub_Question.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            Sub_Question.frameNStart = frameN  # exact frame index
            Sub_Question.tStart = t  # local t and not account for scr refresh
            Sub_Question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Sub_Question, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "Sub_Question.started")
            Sub_Question.setAutoDraw(True)
        if Sub_Question.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                Sub_Question.tStop = t  # not accounting for scr refresh
                Sub_Question.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "Sub_Question.stopped")
                Sub_Question.setAutoDraw(False)

        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "slider.started")
            slider.setAutoDraw(True)

        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False

        # *Sub_Question_2* updates
        if Sub_Question_2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            Sub_Question_2.frameNStart = frameN  # exact frame index
            Sub_Question_2.tStart = t  # local t and not account for scr refresh
            Sub_Question_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Sub_Question_2, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "Sub_Question_2.started")
            Sub_Question_2.setAutoDraw(True)
        if Sub_Question_2.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                Sub_Question_2.tStop = t  # not accounting for scr refresh
                Sub_Question_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "Sub_Question_2.stopped")
                Sub_Question_2.setAutoDraw(False)

        # *slider_2* updates
        if slider_2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            slider_2.frameNStart = frameN  # exact frame index
            slider_2.tStart = t  # local t and not account for scr refresh
            slider_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_2, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "slider_2.started")
            slider_2.setAutoDraw(True)

        # Check slider_2 for response to end routine
        if slider_2.getRating() is not None and slider_2.status == STARTED:
            continueRoutine = False

        # *Sub_Question_3* updates
        if Sub_Question_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            Sub_Question_3.frameNStart = frameN  # exact frame index
            Sub_Question_3.tStart = t  # local t and not account for scr refresh
            Sub_Question_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Sub_Question_3, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "Sub_Question_3.started")
            Sub_Question_3.setAutoDraw(True)
        if Sub_Question_3.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                Sub_Question_3.tStop = t  # not accounting for scr refresh
                Sub_Question_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "Sub_Question_3.stopped")
                Sub_Question_3.setAutoDraw(False)

        # *slider_3* updates
        if slider_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            slider_3.frameNStart = frameN  # exact frame index
            slider_3.tStart = t  # local t and not account for scr refresh
            slider_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_3, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "slider_3.started")
            slider_3.setAutoDraw(True)

        # Check slider_3 for response to end routine
        if slider_3.getRating() is not None and slider_3.status == STARTED:
            continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = (
            False  # will revert to True if at least one component still running
        )
        for thisComponent in Safety_JudgementsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if (
            continueRoutine
        ):  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "Safety_Judgements" ---
    for thisComponent in Safety_JudgementsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData("slider.response", slider.getRating())
    Trials.addData("slider.rt", slider.getRT())
    Trials.addData("slider_2.response", slider_2.getRating())
    Trials.addData("slider_2.rt", slider_2.getRT())
    Trials.addData("slider_3.response", slider_3.getRating())
    Trials.addData("slider_3.rt", slider_3.getRT())
    # the Routine "Safety_Judgements" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "AV_Judgements" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider_4.reset()
    slider_5.reset()
    # keep track of which components have finished
    AV_JudgementsComponents = [AV_Question, car_image, slider_4, car_image_2, slider_5]
    for thisComponent in AV_JudgementsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, "status"):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "AV_Judgements" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *AV_Question* updates
        if AV_Question.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            AV_Question.frameNStart = frameN  # exact frame index
            AV_Question.tStart = t  # local t and not account for scr refresh
            AV_Question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AV_Question, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "AV_Question.started")
            AV_Question.setAutoDraw(True)
        if AV_Question.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                AV_Question.tStop = t  # not accounting for scr refresh
                AV_Question.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "AV_Question.stopped")
                AV_Question.setAutoDraw(False)

        # *car_image* updates
        if car_image.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            car_image.frameNStart = frameN  # exact frame index
            car_image.tStart = t  # local t and not account for scr refresh
            car_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(car_image, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "car_image.started")
            car_image.setAutoDraw(True)
        if car_image.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                car_image.tStop = t  # not accounting for scr refresh
                car_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "car_image.stopped")
                car_image.setAutoDraw(False)

        # *slider_4* updates
        if slider_4.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            slider_4.frameNStart = frameN  # exact frame index
            slider_4.tStart = t  # local t and not account for scr refresh
            slider_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_4, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "slider_4.started")
            slider_4.setAutoDraw(True)

        # Check slider_4 for response to end routine
        if slider_4.getRating() is not None and slider_4.status == STARTED:
            continueRoutine = False

        # *car_image_2* updates
        if car_image_2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            car_image_2.frameNStart = frameN  # exact frame index
            car_image_2.tStart = t  # local t and not account for scr refresh
            car_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(car_image_2, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "car_image_2.started")
            car_image_2.setAutoDraw(True)
        if car_image_2.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                car_image_2.tStop = t  # not accounting for scr refresh
                car_image_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, "car_image_2.stopped")
                car_image_2.setAutoDraw(False)

        # *slider_5* updates
        if slider_5.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            slider_5.frameNStart = frameN  # exact frame index
            slider_5.tStart = t  # local t and not account for scr refresh
            slider_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_5, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "slider_5.started")
            slider_5.setAutoDraw(True)

        # Check slider_5 for response to end routine
        if slider_5.getRating() is not None and slider_5.status == STARTED:
            continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = (
            False  # will revert to True if at least one component still running
        )
        for thisComponent in AV_JudgementsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if (
            continueRoutine
        ):  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "AV_Judgements" ---
    for thisComponent in AV_JudgementsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData("slider_4.response", slider_4.getRating())
    Trials.addData("slider_4.rt", slider_4.getRT())
    Trials.addData("slider_5.response", slider_5.getRating())
    Trials.addData("slider_5.rt", slider_5.getRT())
    # the Routine "AV_Judgements" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 5.0 repeats of 'Trials'


# --- Prepare to start Routine "Thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
ThanksComponents = [Thank_You, Consent_remind, button_3, key_resp_3]
for thisComponent in ThanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, "status"):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Thanks" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Thank_You* updates
    if Thank_You.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        Thank_You.frameNStart = frameN  # exact frame index
        Thank_You.tStart = t  # local t and not account for scr refresh
        Thank_You.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thank_You, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "Thank_You.started")
        Thank_You.setAutoDraw(True)
    if Thank_You.status == STARTED:
        if bool(1.0):
            # keep track of stop time/frame for later
            Thank_You.tStop = t  # not accounting for scr refresh
            Thank_You.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "Thank_You.stopped")
            Thank_You.setAutoDraw(False)

    # *Consent_remind* updates
    if Consent_remind.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        Consent_remind.frameNStart = frameN  # exact frame index
        Consent_remind.tStart = t  # local t and not account for scr refresh
        Consent_remind.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Consent_remind, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "Consent_remind.started")
        Consent_remind.setAutoDraw(True)
    if Consent_remind.status == STARTED:
        if bool(1.0):
            # keep track of stop time/frame for later
            Consent_remind.tStop = t  # not accounting for scr refresh
            Consent_remind.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "Consent_remind.stopped")
            Consent_remind.setAutoDraw(False)

    # *button_3* updates
    if button_3.status == NOT_STARTED and tThisFlip >= 0 - frameTolerance:
        # keep track of start time/frame for later
        button_3.frameNStart = frameN  # exact frame index
        button_3.tStart = t  # local t and not account for scr refresh
        button_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_3, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "button_3.started")
        button_3.setAutoDraw(True)
    if button_3.status == STARTED:
        if bool(1.0):
            # keep track of stop time/frame for later
            button_3.tStop = t  # not accounting for scr refresh
            button_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "button_3.stopped")
            button_3.setAutoDraw(False)
    if button_3.status == STARTED:
        # check whether button_3 has been pressed
        if button_3.isClicked:
            if not button_3.wasClicked:
                button_3.timesOn.append(
                    button_3.buttonClock.getTime()
                )  # store time of first click
                button_3.timesOff.append(
                    button_3.buttonClock.getTime()
                )  # store time clicked until
            else:
                button_3.timesOff[
                    -1
                ] = button_3.buttonClock.getTime()  # update time clicked until
            if not button_3.wasClicked:
                continueRoutine = False  # end routine when button_3 is clicked
                None
            button_3.wasClicked = (
                True  # if button_3 is still clicked next frame, it is not a new click
            )
        else:
            button_3.wasClicked = (
                False  # if button_3 is clicked next frame, it is a new click
            )
    else:
        button_3.wasClicked = (
            False  # if button_3 is clicked next frame, it is a new click
        )

    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, "key_resp_3.started")
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(
            key_resp_3.clearEvents, eventType="keyboard"
        )  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=["space"], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = (
        False  # will revert to True if at least one component still running
    )
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if (
        continueRoutine
    ):  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Thanks" ---
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData("button_3.numClicks", button_3.numClicks)
if button_3.numClicks:
    thisExp.addData("button_3.timesOn", button_3.timesOn)
    thisExp.addData("button_3.timesOff", button_3.timesOff)
else:
    thisExp.addData("button_3.timesOn", "")
    thisExp.addData("button_3.timesOff", "")
# check responses
if key_resp_3.keys in ["", [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData("key_resp_3.keys", key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData("key_resp_3.rt", key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + ".csv", delim="auto")
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
