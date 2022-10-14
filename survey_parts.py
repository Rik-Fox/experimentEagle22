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


def updateComponent(component, frame, tStart, tGlobal):
    if component.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        component.frameNStart = frame  # exact frame index
        component.tStart = tStart  # local t and not account for scr refresh
        component.tStartRefresh = tGlobal  # on global time
        win.timeOnFlip(component, "tStartRefresh")  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, f"{component.name}.started")
        component.setAutoDraw(True)


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
    fullscr=False,
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

trialComponents = []
slider = visual.Slider(
    win=win,
    name="slider",
    startValue=None,
    size=(1.0, 0.05),
    pos=(0, 0.05),
    units=None,
    labels=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    granularity=0.0,
    style="rating",
    styleTweaks=(),
    opacity=None,
    labelColor="LightGray",
    markerColor="Red",
    lineColor="White",
    colorSpace="rgb",
    font="Open Sans",
    labelHeight=0.025,
    flip=False,
    ori=0.0,
    depth=0,
    readOnly=False,
)
# trialComponents.append(slider)

slider_2 = visual.Slider(
    win=win,
    name="slider_2",
    startValue=None,
    size=(1.0, 0.05),
    pos=(0, -0.15),
    units=None,
    labels=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    granularity=0.0,
    style="rating",
    styleTweaks=(),
    opacity=None,
    labelColor="LightGray",
    markerColor="Red",
    lineColor="White",
    colorSpace="rgb",
    font="Open Sans",
    labelHeight=0.025,
    flip=False,
    ori=0.0,
    depth=-1,
    readOnly=False,
)
# trialComponents.append(slider_2)

slider_3 = visual.Slider(
    win=win,
    name="slider_2",
    startValue=None,
    size=(1.0, 0.05),
    pos=(0, -0.35),
    units=None,
    labels=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    granularity=0.0,
    style="rating",
    styleTweaks=(),
    opacity=None,
    labelColor="LightGray",
    markerColor="Red",
    lineColor="White",
    colorSpace="rgb",
    font="Open Sans",
    labelHeight=0.025,
    flip=False,
    ori=0.0,
    depth=-1,
    readOnly=False,
)
# trialComponents.append(slider_3)

init_textbox = visual.TextBox2(
    win,
    text="Please read the information sheet and hand your consent form back to the Experiment Leader\nIf you have not already done so",
    font="Open Sans",
    pos=(0, 0.4),
    letterHeight=0.04,
    size=(1, 0.2),
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
# trialComponents.append(init_textbox)

init_textbox_2 = visual.TextBox2(
    win,
    text="Once you comence each trial you will be asked to click to continue after which you will see the simulator below to control the pedestrian (circled) please use the arrow keys, or W,A,S and D keys if you prefer",
    font="Open Sans",
    pos=(0, 0.2),
    letterHeight=0.03,
    size=(1, 0.2),
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
# trialComponents.append(init_textbox_2)

init_textbox_3 = visual.TextBox2(
    win,
    text="Press Space to continue",
    font="Open Sans",
    pos=(0, -0.45),
    letterHeight=0.03,
    size=(1, 0.2),
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
# trialComponents.append(init_textbox_3)

textbox = visual.TextBox2(
    win,
    text="Thank you For Particpating!\nPlease click below to end the experiment and remember to collect your Debrief before leaving.",
    font="Open Sans",
    pos=(0, 0.2),
    letterHeight=0.05,
    size=(1, 0.2),
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
trialComponents.append(textbox)

textbox2 = visual.TextBox2(
    win,
    text="N.B. by clicking you are confirming your consent for your data to be used and it will no longer be able to be withdrawn",
    font="Open Sans",
    pos=(0, -0.1),
    letterHeight=0.03,
    size=(1, 0.2),
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
trialComponents.append(textbox2)

Q1 = visual.TextBox2(
    win,
    text="Speed",
    font="Open Sans",
    pos=(0, 0.125),
    letterHeight=0.03,
    size=(1, 0.2),
    borderWidth=2.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    bold=False,
    italic=False,
    lineSpacing=1.0,
    padding=0.0,
    alignment="left",
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
# trialComponents.append(Q1)

Q2 = visual.TextBox2(
    win,
    text="Positioning",
    font="Open Sans",
    pos=(0, -0.075),
    letterHeight=0.03,
    size=(1, 0.2),
    borderWidth=2.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    bold=False,
    italic=False,
    lineSpacing=1.0,
    padding=0.0,
    alignment="left",
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
# trialComponents.append(Q2)

Q3 = visual.TextBox2(
    win,
    text="Steering",
    font="Open Sans",
    pos=(0, -0.275),
    letterHeight=0.03,
    size=(1, 0.2),
    borderWidth=2.0,
    color="white",
    colorSpace="rgb",
    opacity=None,
    bold=False,
    italic=False,
    lineSpacing=1.0,
    padding=0.0,
    alignment="left",
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
# trialComponents.append(Q3)

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
# trialComponents.append(text)

car_img = visual.ImageStim(
    win=win,
    image="/home/rfox/PhD/Term1_22-23_Experiements/pygame_ped_env/pygame_ped_env/images/Topdown_vehicle_sprites_pack/car.png",
    mask=None,
    units="",
    pos=(-0.175, 0.4),
    size=None,  # (0.2, 0.1),  # value is % of screen size
    anchor="topleft",
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
    name="car",
    autoLog=None,
    maskParams=None,
)
# trialComponents.append(car_img)

car_img_2 = visual.ImageStim(
    win=win,
    image="/home/rfox/PhD/Term1_22-23_Experiements/pygame_ped_env/pygame_ped_env/images/Topdown_vehicle_sprites_pack/car2.png",
    mask=None,
    units="",
    pos=(-0.175, -0.05),
    size=None,  # (0.2, 0.1),  # value is % of screen size
    anchor="topleft",
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
    name="car",
    autoLog=None,
    maskParams=None,
)
# trialComponents.append(car_img_2)

wasd_img = visual.ImageStim(
    win=win,
    image="/home/rfox/PhD/Term1_22-23_Experiements/experimentEagle22/images/SeekPng.com_wasd-png_1791627.png",
    mask=None,
    units="",
    pos=(0.3, -0.2),
    size=(0.225, 0.15),  # value is % of screen size
    anchor="topleft",
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
    name="car",
    autoLog=None,
    maskParams=None,
)
# trialComponents.append(wasd_img)

arrow_img = visual.ImageStim(
    win=win,
    image="/home/rfox/PhD/Term1_22-23_Experiements/experimentEagle22/images/SeekPng.com_arrow-keys-png_3271603.png",
    mask=None,
    units="",
    pos=(-0.5, -0.2),
    size=(0.225, 0.15),  # value is % of screen size
    anchor="topleft",
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
    name="car",
    autoLog=None,
    maskParams=None,
)
# trialComponents.append(arrow_img)

sim_img = visual.ImageStim(
    win=win,
    image="/home/rfox/PhD/Term1_22-23_Experiements/experimentEagle22/images/Simulator.png",
    mask=None,
    units="",
    pos=(-0.25, 0.1),
    size=(0.5, 0.5),  # value is % of screen size
    anchor="topleft",
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
    name="car",
    autoLog=None,
    maskParams=None,
)
# trialComponents.append(sim_img)

button = visual.ButtonStim(
    win,
    "Click Here to Finish Experiment",
    font="Arvo",
    pos=(0, -0.3),
    size=(0.4, 0.2),
    padding=None,
    anchor="center",
    units=None,
    color="white",
    fillColor="darkgrey",
    borderColor=None,
    borderWidth=0,
    colorSpace="rgb",
    opacity=None,
    letterHeight=None,
    bold=True,
    italic=False,
    name="",
    autoLog=None,
)
trialComponents.append(button)

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

    for thisComponent in trialComponents:
        if hasattr(thisComponent, "reset"):
            thisComponent.reset()
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

        # for thisComponent in instanceStartComponents:
        #     updateComponent(thisComponent, frameN, t, tThisFlipGlobal)
        # waitKeys(self, maxWait=float('inf'), keyList=None, waitRelease=True,
        #          clear=True)

        for thisComponent in trialComponents:
            updateComponent(thisComponent, frameN, t, tThisFlipGlobal)

        if button.isClicked and button.status == STARTED:
            continueRoutine = False
        elif defaultKeyboard.getKeys(keyList=["space"]):
            continueRoutine = False

        # Check slider for response to end routine
        if slider.getRating() is not None and slider.status == STARTED:
            continueRoutine = False

        # Check slider_2 for response to end routine
        if slider_2.getRating() is not None and slider_2.status == STARTED:
            continueRoutine = False

        # if textbox.status == STARTED:
        #     # is it time to stop? (based on global clock, using actual start)
        #     if tThisFlipGlobal > textbox.tStartRefresh + 1.0-frameTolerance:
        #         # keep track of stop time/frame for later
        #         textbox.tStop = t  # not accounting for scr refresh
        #         textbox.frameNStop = frameN  # exact frame index
        #         # add timestamp to datafile
        #         thisExp.timestampOnFlip(win, 'textbox.stopped')
        #         textbox.setAutoDraw(False)

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
