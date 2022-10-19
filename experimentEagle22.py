#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Mon 17 Oct 2022 11:47:59 
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


class ExperimentRunner(object):
    def __init__(self) -> None:
        # Ensure that relative paths start from the same directory as this script
        _thisDir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(_thisDir)
        # Store info about the experiment session
        psychopyVersion = "2022.2.4"
        expName = (
            "experimentEagle22"  # from the Builder filename that created this script
        )
        self.expInfo = {
            "participant": f"{randint(0, 999999):06.0f}",
            "session": "001",
        }
        # --- Show participant info dialog --
        dlg = gui.DlgFromDict(dictionary=self.expInfo, sortKeys=False, title=expName)
        if dlg.OK == False:
            core.quit()  # user pressed cancel
        self.expInfo["date"] = data.getDateStr()  # add a simple timestamp
        self.expInfo["expName"] = expName
        self.expInfo["psychopyVersion"] = psychopyVersion

        # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
        filename = (
            _thisDir
            + os.sep
            + "data/%s_%s_%s"
            % (self.expInfo["participant"], expName, self.expInfo["date"])
        )

        # An ExperimentHandler isn't essential but helps with data saving
        self.thisExp = data.ExperimentHandler(
            name=expName,
            version="",
            extraInfo=self.expInfo,
            runtimeInfo=None,
            originPath="/home/rfox/PhD/Term1_22-23_Experiements/experimentEagle22/experimentEagle22.py",
            savePickle=True,
            saveWideText=True,
            dataFileName=filename,
        )
        # save a log file for detail verbose info
        logFile = logging.LogFile(filename + ".log", level=logging.EXP)
        logging.console.setLevel(
            logging.WARNING
        )  # this outputs to the screen, not a file

        self.endExpNow = False  # flag for 'escape' or other condition => quit the exp
        self.frameTolerance = 0.001  # how close to onset before 'same' frame

        # Start Code - component code to be run after the window creation

        # --- Setup the Window ---
        self.win = visual.Window(
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
        self.win.mouseVisible = False
        # store frame rate of monitor if we can measure it
        self.expInfo["frameRate"] = self.win.getActualFrameRate()
        if self.expInfo["frameRate"] != None:
            frameDur = 1.0 / round(self.expInfo["frameRate"])
        else:
            frameDur = 1.0 / 60.0  # could not measure, so guess
        # --- Setup input devices ---
        ioConfig = {}

        # Setup iohub keyboard
        ioConfig["Keyboard"] = dict(use_keymap="psychopy")

        ioSession = "1"
        if "session" in self.expInfo:
            ioSession = str(self.expInfo["session"])
        ioServer = io.launchHubServer(window=self.win, **ioConfig)
        eyetracker = None

        # create a default keyboard (e.g. to check for escape)
        self.defaultKeyboard = keyboard.Keyboard(backend="iohub")

        self.initComponents()

    def initComponents(self):

        # --- Initialize components for Routine "Intro_Page" ---
        Title = visual.TextStim(
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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
        Sim_image = visual.ImageStim(
            win=self.win,
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
            self.win,
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

        self.intro_page = [Title, SubTitle, arrows, wasd, Sim_image, button, key_resp]

        # --- Initialize components for Routine "Start_Page" ---
        Start_Info = visual.TextStim(
            win=self.win,
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
            self.win,
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

        self.start_page = [Start_Info, button_2, key_resp_2]

        # --- Initialize components for Routine "Simulation" ---

        self.Sim = []

        # --- Initialize components for Routine "Safety_Judgements" ---
        Question = visual.TextStim(
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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

        self.saftey_judgement_page = [
            Question,
            Vehicle_image,
            Sub_Question,
            Sub_Question_2,
            Sub_Question_3,
            slider,
            slider_2,
            slider_3,
        ]

        # --- Initialize components for Routine "AV_Judgements" ---
        AV_Question = visual.TextStim(
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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
            win=self.win,
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

        self.av_judgements_page = [
            AV_Question,
            car_image,
            car_image_2,
            slider_4,
            slider_5,
        ]

        # --- Initialize components for Routine "Thanks" ---
        Thank_You = visual.TextStim(
            win=self.win,
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
            win=self.win,
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
            self.win,
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

        self.thanks_page = [Thank_You, Consent_remind, button_3, key_resp_3]

        # Create some handy timers
        self.globalClock = core.Clock()  # to track the time since experiment started
        self.routineTimer = (
            core.Clock()
        )  # to track time remaining of each (possibly non-slip) routine

    def updateComponent(self, component, frame, tStart, tGlobal):
        # initalise component if not started yet
        if (
            component.status == NOT_STARTED
            and self.tThisFlip >= 0.0 - self.frameTolerance
        ):
            # keep track of start time/frame for later
            component.frameNStart = self.frameN  # exact frame index
            component.tStart = self.t  # local t and not account for scr refresh
            component.tStartRefresh = self.tThisFlipGlobal  # on global time
            self.win.timeOnFlip(component, "tStartRefresh")  # time at next scr refresh
            # add timestamp to datafile
            self.thisExp.timestampOnFlip(self.win, f"{component.name}.started")
            component.setAutoDraw(True)

        # --- Stimulus Type Specific Updates ---
        if isinstance(component, (visual.Slider)) and component.status == STARTED:
            if component.getRating() is not None and component.status == STARTED:
                self.continueRoutine = False
        # --- condition routine end for textboxes ---
        if isinstance(component, (visual.TextStim)) and component.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                component.tStop = self.t  # not accounting for scr refresh
                component.frameNStop = self.frameN  # exact frame index
                # add timestamp to datafile
                self.thisExp.timestampOnFlip(self.win, f"{component.name}.stopped")
                component.setAutoDraw(False)

        # --- condition routine end for images ---
        if isinstance(component, (visual.ImageStim)) and component.status == STARTED:
            if bool(1.0):
                # keep track of stop time/frame for later
                component.tStop = self.t  # not accounting for scr refresh
                component.frameNStop = self.frameN  # exact frame index
                # add timestamp to datafile
                self.thisExp.timestampOnFlip(self.win, f"{component.name}.stopped")
                component.setAutoDraw(False)
        # --- checking for button clicks ----
        if isinstance(component, visual.ButtonStim):
            if component.status == STARTED:
                # check whether button has been pressed
                if component.isClicked:
                    if not component.wasClicked:
                        component.timesOn.append(
                            component.buttonClock.getTime()
                        )  # store time of first click
                        component.timesOff.append(
                            component.buttonClock.getTime()
                        )  # store time clicked until
                    else:
                        component.timesOff[
                            -1
                        ] = component.buttonClock.getTime()  # update time clicked until
                    if not component.wasClicked:
                        continueRoutine = False  # end routine when button is clicked
                        None
                    component.wasClicked = True  # if button is still clicked next frame, it is not a new click
                else:
                    component.wasClicked = (
                        False  # if button is clicked next frame, it is a new click
                    )
            else:
                component.wasClicked = (
                    False  # if button is clicked next frame, it is a new click
                )
                # keep track of stop time/frame for later
                component.tStop = self.t  # not accounting for scr refresh
                component.frameNStop = self.frameN  # exact frame index
                # add timestamp to datafile
                self.thisExp.timestampOnFlip(self.win, f"{component.name}.stopped")
                component.setAutoDraw(False)

        # --- listening on keyboard ---
        if isinstance(component, keyboard.Keyboard):
            waitOnFlip = False
            if (
                component.status == NOT_STARTED
                and tThisFlip >= 0.0 - self.frameTolerance
            ):
                # keep track of start time/frame for later
                component.frameNStart = frameN  # exact frame index
                component.tStart = t  # local t and not account for scr refresh
                component.tStartRefresh = tThisFlipGlobal  # on global time
                self.win.timeOnFlip(
                    component, "tStartRefresh"
                )  # time at next scr refresh
                # add timestamp to datafile
                self.thisExp.timestampOnFlip(self.win, f"{component.name}.started")
                component.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                self.win.callOnFlip(component.clock.reset)  # t=0 on next screen flip
                self.win.callOnFlip(
                    component.clearEvents, eventType="keyboard"
                )  # clear events on next screen flip
            if component.status == STARTED and not waitOnFlip:
                theseKeys = component.getKeys(keyList=["space"], waitRelease=False)
                component._key_resp_allKeys.extend(theseKeys)
                if len(component._key_resp_allKeys):
                    component.keys = component._key_resp_allKeys[
                        -1
                    ].name  # just the last key pressed
                    component.rt = component._key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False

    # --- Prepare to start Routine ---

    def initRoutine(self, componentList):
        self.continueRoutine = True
        self.routineForceEnded = False

        for thisComponent in componentList:
            if hasattr(thisComponent, "reset"):
                thisComponent.reset()
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, "status"):
                thisComponent.status = NOT_STARTED

            # update keyboard component parameters for each repeat
            if isinstance(thisComponent, keyboard.Keyboard):
                thisComponent.keys = []
                thisComponent.rt = []
                thisComponent._key_resp_allKeys = []

        # reset timers
        self.t = 0
        self._timeToFirstFrame = self.win.getFutureFlipTime(clock="now")
        self.frameN = -1

    def endRoutine(self, componentList, inTrial=False):
        # --- Ending Routine ---
        log_obj = self.thisExp
        if inTrial:
            log_obj = self.Trials

        for thisComponent in componentList:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

            # --- log slider data ---
            if isinstance(thisComponent, visual.Slider):
                log_obj.addData("slider.response", thisComponent.getRating())
                log_obj.addData("slider.rt", thisComponent.getRT())

            # --- log and ButtonStim data ---
            if isinstance(thisComponent, visual.ButtonStim):
                log_obj.addData(
                    f"{thisComponent.name}.numClicks", thisComponent.numClicks
                )
                if thisComponent.numClicks:
                    log_obj.addData(
                        f"{thisComponent.name}.timesOn", thisComponent.timesOn
                    )
                    log_obj.addData(
                        f"{thisComponent.name}.timesOff", thisComponent.timesOff
                    )
                else:
                    log_obj.addData(f"{thisComponent.name}.timesOn", "")
                    log_obj.addData(f"{thisComponent.name}.timesOff", "")

            # --- log keyboard responses ---
            if isinstance(thisComponent, keyboard.Keyboard):
                if thisComponent.keys in ["", [], None]:  # No response was made
                    thisComponent.keys = None
                log_obj.addData(f"{thisComponent.name}.keys", thisComponent.keys)
                if thisComponent.keys != None:  # we had a response
                    log_obj.addData(f"{thisComponent.name}.rt", thisComponent.rt)

        self.thisExp.nextEntry()
        # the Routine "Intro_Page" was not non-slip safe, so reset the non-slip timer
        self.routineTimer.reset()

    def runRoutine(self, trialComponents, inTrial=False):
        self.initRoutine(trialComponents)
        # --- Run Routine ---
        while self.continueRoutine:
            # get current time
            self.t = self.routineTimer.getTime()
            self.tThisFlip = self.win.getFutureFlipTime(clock=self.routineTimer)
            self.tThisFlipGlobal = self.win.getFutureFlipTime(clock=None)
            self.frameN = (
                self.frameN + 1
            )  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            for thisComponent in trialComponents:
                self.updateComponent(thisComponent)

            # check for quit (typically the Esc key)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if (
                not self.continueRoutine
            ):  # a component has requested a forced-end of Routine
                self.routineForceEnded = True
                break
            self.continueRoutine = (
                False  # will revert to True if at least one component still running
            )
            for thisComponent in trialComponents:
                if (
                    hasattr(thisComponent, "status")
                    and thisComponent.status != FINISHED
                ):
                    self.continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if (
                self.continueRoutine
            ):  # don't flip if this routine is over or we'll get a blank screen
                self.win.flip()

        self.endRoutine(trialComponents, inTrial)

    def run(self):

        self.runRoutine(self.intro_page)

        # set up handler to look after randomisation of conditions etc
        self.Trials = data.TrialHandler(
            nReps=5.0,
            method="random",
            extraInfo=self.expInfo,
            originPath=-1,
            trialList=[None],
            seed=None,
            name="Trials",
        )
        self.thisExp.addLoop(self.Trials)  # add the loop to the experiment
        thisTrial = self.Trials.trialList[
            0
        ]  # so we can initialise stimuli with some values
        for thisTrial in self.Trials:
            currentLoop = self.Trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    exec("{} = thisTrial[paramName]".format(paramName))

            self.runRoutine(self.start_page, inTrial=True)
            # Run 'Begin Routine' code from Simulator 'print("Hello world")'
            self.runRoutine(self.Sim, inTrial=True)

            self.runRoutine(self.saftey_judgement_page, inTrial=True)
            self.runRoutine(self.av_judgements_page, inTrial=True)
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
self.win.close()
core.quit()
