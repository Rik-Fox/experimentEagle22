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
from psychopy import gui, visual, core, data, logging
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
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

from expPages import initPages


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
        self.logname = (
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
            originPath=os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "experimentEagle22.py"
            ),
            savePickle=True,
            saveWideText=True,
            dataFileName=self.logname,
        )
        # save a log file for detail verbose info
        logFile = logging.LogFile(self.logname + ".log", level=logging.EXP)
        logging.console.setLevel(
            logging.WARNING
        )  # this outputs to the screen, not a file

        self.endExpNow = False  # flag for 'escape' or other condition => quit the exp
        self.FRAME_TOLERANCE = 0.001  # how close to onset before 'same' frame

        # Start Code - component code to be run after the window creation

        # --- Setup the Window ---
        self.win = visual.Window(
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

        self.Pages = {page.name: page for page in initPages(self.win, self.thisExp)}

        # Create some handy timers
        # to track the time since experiment started
        self.globalClock = core.Clock()
        # to track time remaining of each (possibly non-slip) routine
        self.routineTimer = core.Clock()

    def runRoutine(self, page):

        page.init()
        # _timeToFirstFrame = self.win.getFutureFlipTime(clock="now")
        continueRoutine = True
        routineForceEnded = False
        frameN = -1

        # --- Run Routine ---
        while continueRoutine:

            # update/draw components on each frame
            continueRoutine = page.update(
                self.win,
                self.FRAME_TOLERANCE,
                # number of completed frames (so 0 is the first frame)
                frameN=frameN + 1,
                t=self.routineTimer.getTime(),
                tThisFlip=self.win.getFutureFlipTime(clock=self.routineTimer),
                tThisFlipGlobal=self.win.getFutureFlipTime(clock=None),
            )

            # check for quit (typically the Esc key)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            # a component has requested a forced-end of Routine
            if not continueRoutine:
                routineForceEnded = True
                page._expLog.addData("routineForceEnded", routineForceEnded)
                break
            # will revert to True if at least one component still running
            continueRoutine = False
            for thisComponent in page.componentList:
                if (
                    hasattr(thisComponent, "status")
                    and thisComponent.status != FINISHED
                ):
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            # don't flip if this routine is over or we'll get a blank screen
            if continueRoutine:
                self.win.flip()

        page.end()

        self.thisExp.nextEntry()
        # the Routines are not non-slip safe, so reset the non-slip timer
        self.routineTimer.reset()

    def run(self):

        self.runRoutine(self.Pages["intro_page"])

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

        trialPages = ["start_page", "Sim", "saftey_judgement_page", "av_judgement_page"]
        for page in trialPages:
            self.Pages[page].setTrialLogObj(self.Trials)

        for thisTrial in self.Trials:  # loop trial nReps times
            for page in trialPages:  # loop through each page in each trial
                self.runRoutine(self.Pages[page])
        # completed 5.0 repeats of 'Trials'

        self.runRoutine(self.Pages["thanks_page"])

        # --- End experiment ---
        # Flip one final time so any remaining win.callOnFlip()
        # and win.timeOnFlip() tasks get executed before quitting
        self.win.flip()

        # these shouldn't be strictly necessary (should auto-save)
        self.thisExp.saveAsWideText(self.logname + ".csv", delim="auto")
        self.thisExp.saveAsPickle(self.logname)
        logging.flush()
        # make sure everything is closed down
        self.win.close()
        core.quit()


if __name__ == "__main__":
    ExperimentRunner().run()
