#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on October 10, 2022, at 20:11
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
expName = "survey_parts"  # from the Builder filename that created this script
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
    originPath="C:\\Users\\rfox\\Documents\\survey_parts.py",
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

# --- Initialize components for Routine "trial" ---
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
    depth=0,
    readOnly=False,
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
    depth=-1,
    readOnly=False,
)
textbox = visual.TextBox2(
    win,
    text="Any text\n\nincluding line breaks",
    font="Open Sans",
    pos=(0, 0),
    letterHeight=0.05,
    size=(None, None),
    borderWidth=2.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    bold=False,
    italic=False,
    lineSpacing=1.0,
    padding=0.0,
    alignment="center",
    anchor="center",
    fillColor=None,
    borderColor=None,
    flipHoriz=False,
    flipVert=False,
    languageStyle="LTR",
    editable=False,
    name="textbox",
    autoLog=True,
)
text = visual.TextStim(
    win=win,
    name="text",
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
    depth=-3.0,
)
img = visual.ImageStim(
    win=win,
    image="/home/rfox/PhD/Term1_22-23_Experiements/pygame_ped_env/pygame_ped_env/images/right/car.png",
    mask=None,
    units="",
    pos=(0, 0),
    size=None,
    anchor="center_left",
    ori=0,
    color=(1, 1, 1),
    colorSpace="rgb",
    contrast=1,
    opacity=None,
    depth=0,
    interpolate=False,
    flipHoriz=False,
    flipVert=False,
    texRes=128,
    name="",
    autoLog=None,
    maskParams=None,
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = (
    core.Clock()
)  # to track time remaining of each (possibly non-slip) routine

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(
    nReps=2.0,
    method="random",
    extraInfo=expInfo,
    originPath=-1,
    trialList=[None],
    seed=None,
    name="trials",
)
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec("{} = thisTrial[paramName]".format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec("{} = thisTrial[paramName]".format(paramName))

    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    slider.reset()
    slider_2.reset()
    textbox.reset()
    # img.reset()
    # keep track of which components have finished
    trialComponents = [slider, slider_2, textbox, text, img]
    for thisComponent in trialComponents:
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

    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *image* updates
        if img.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            img.frameNStart = frameN  # exact frame index
            img.tStart = t  # local t and not account for scr refresh
            img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "img.started")
            img.setAutoDraw(True)

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

        # *textbox* updates
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, "textbox.started")
            textbox.setAutoDraw(True)
        if textbox.status == STARTED:
            pass
            # # is it time to stop? (based on global clock, using actual start)
            # if tThisFlipGlobal > textbox.tStartRefresh + 1.0-frameTolerance:
            #     # keep track of stop time/frame for later
            #     textbox.tStop = t  # not accounting for scr refresh
            #     textbox.frameNStop = frameN  # exact frame index
            #     # add timestamp to datafile
            #     thisExp.timestampOnFlip(win, 'textbox.stopped')
            #     textbox.setAutoDraw(False)

        # # *text* updates
        # if text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        #     # keep track of start time/frame for later
        #     text.frameNStart = frameN  # exact frame index
        #     text.tStart = t  # local t and not account for scr refresh
        #     text.tStartRefresh = tThisFlipGlobal  # on global time
        #     win.timeOnFlip(text, "tStartRefresh")  # time at next scr refresh
        #     # add timestamp to datafile
        #     thisExp.timestampOnFlip(win, "text.started")
        #     text.setAutoDraw(True)
        # if text.status == STARTED:
        #     # is it time to stop? (based on global clock, using actual start)
        #     if tThisFlipGlobal > text.tStartRefresh + 1.0 - frameTolerance:
        #         pass
        #         # # keep track of stop time/frame for later
        #         # text.tStop = t  # not accounting for scr refresh
        #         # text.frameNStop = frameN  # exact frame index
        #         # # add timestamp to datafile
        #         # thisExp.timestampOnFlip(win, "text.stopped")
        #         # text.setAutoDraw(False)

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
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if (
            continueRoutine
        ):  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData("slider.response", slider.getRating())
    trials.addData("slider.rt", slider.getRT())
    trials.addData("slider_2.response", slider_2.getRating())
    trials.addData("slider_2.rt", slider_2.getRT())
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 2.0 repeats of 'trials'


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
