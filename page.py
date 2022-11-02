from psychopy import visual
from psychopy.hardware import keyboard
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


class Page(object):
    def __init__(
        self, page_name, log_experiment, log_trial=None, component_list=[]
    ) -> None:
        self.name = page_name
        self.componentList = component_list
        self._expLog = log_experiment
        if log_trial == None:
            self._trialLog = self._expLog
        else:
            self._trialLog = log_trial

    def getTrialLogObj(self):
        return self._trialLog

    def setTrialLogObj(self, log_obj):
        self._trialLog = log_obj

    def init(self):
        for thisComponent in self.componentList:
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

    def end(self):
        for thisComponent in self.componentList:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
            elif hasattr(thisComponent, "status"):
                thisComponent.status = FINISHED

            # --- log slider data ---
            if isinstance(thisComponent, visual.Slider):
                self._trialLog.addData("slider.response", thisComponent.getRating())
                self._trialLog.addData("slider.rt", thisComponent.getRT())

            # --- log and ButtonStim data ---
            if isinstance(thisComponent, visual.ButtonStim):
                self._trialLog.addData(
                    f"{thisComponent.name}.numClicks", thisComponent.numClicks
                )
                if thisComponent.numClicks:
                    self._trialLog.addData(
                        f"{thisComponent.name}.timesOn", thisComponent.timesOn
                    )
                    self._trialLog.addData(
                        f"{thisComponent.name}.timesOff", thisComponent.timesOff
                    )
                else:
                    self._trialLog.addData(f"{thisComponent.name}.timesOn", "")
                    self._trialLog.addData(f"{thisComponent.name}.timesOff", "")

            # --- log keyboard responses ---
            if isinstance(thisComponent, keyboard.Keyboard):
                if thisComponent.keys in ["", [], None]:  # No response was made
                    thisComponent.keys = None
                self._trialLog.addData(f"{thisComponent.name}.keys", thisComponent.keys)
                if thisComponent.keys != None:  # we had a response
                    self._trialLog.addData(f"{thisComponent.name}.rt", thisComponent.rt)

    def update(self, window, FRAME_TOLERANCE, frameN, t, tThisFlip, tThisFlipGlobal):
        continueRoutine = True
        for component in self.componentList:
            # initalise component if not started yet
            if component.status == NOT_STARTED and tThisFlip >= 0.0 - FRAME_TOLERANCE:
                # keep track of start time/frame for later
                component.frameNStart = frameN  # exact frame index
                component.tStart = t  # local t and not account for scr refresh
                component.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                window.timeOnFlip(component, "tStartRefresh")
                # add timestamp to datafile
                self._expLog.timestampOnFlip(window, f"{component.name}.started")
                if hasattr(component, "setAutoDraw"):
                    component.setAutoDraw(True)
                else:
                    # only keyboard doesnt have setAutoDraw
                    component.status = STARTED
                    # t=0 on next screen flip
                    window.callOnFlip(component.clock.reset)
                    # clear events on next screen flip
                    window.callOnFlip(component.clearEvents, eventType="keyboard")
                # move to next component and wait for next flip to update this initalised component
                continue

            # --- Stimulus Type Specific Updates ---
            # --- condition routine end for sliders ---
            # if isinstance(component, visual.Slider) and component.status == STARTED:
            # --- condition routine end for textboxes ---
            # if isinstance(component, visual.TextStim) and component.status == STARTED:
            # --- condition routine end for images ---
            # if isinstance(component, visual.ImageStim) and component.status == STARTED:
            # --- checking for button clicks ----
            if isinstance(component, visual.ButtonStim):
                if component.status == STARTED:
                    # check whether button has been pressed
                    if component.isClicked:
                        if not component.wasClicked:
                            # store time of first click
                            component.timesOn.append(component.buttonClock.getTime())
                            # store time clicked until
                            component.timesOff.append(component.buttonClock.getTime())
                            # end routine when button is clicked
                            continueRoutine = False
                        else:
                            # update time clicked until
                            component.timesOff[-1] = component.buttonClock.getTime()

                        component.wasClicked = True  # if button is still clicked next frame, it is not a new click
                    else:
                        # if button is clicked next frame, it is a new click
                        component.wasClicked = False
                else:
                    # if button is clicked next frame, it is a new click
                    component.wasClicked = False
                    # keep track of stop time/frame for later
                    component.tStop = t  # not accounting for scr refresh
                    component.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    self._expLog.timestampOnFlip(window, f"{component.name}.stopped")
                    component.setAutoDraw(False)
                    continueRoutine = False
            # --- listening on keyboard ---
            if isinstance(component, keyboard.Keyboard) and component.status == STARTED:
                theseKeys = component.getKeys(keyList=["space"], waitRelease=False)
                component._key_resp_allKeys.extend(theseKeys)
                if len(component._key_resp_allKeys):
                    component.keys = component._key_resp_allKeys[
                        -1
                    ].name  # just the last key pressed
                    component.rt = component._key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False

        # TODO: refactor this to not be 2 logic checks over an array
        if any(isinstance(comp, visual.Slider) for comp in self.componentList):
            ratings = [
                component.getRating()
                for component in self.componentList
                if isinstance(component, visual.Slider)
            ]
            if all(ratings):
                continueRoutine = False

        # set up for ending the routine if not continuing
        if not continueRoutine:
            # keep track of stop time/frame for later
            component.tStop = t  # not accounting for scr refresh
            component.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            self._expLog.timestampOnFlip(window, f"{component.name}.stopped")
            if hasattr(component, "setAutoDraw"):
                component.setAutoDraw(False)

        return continueRoutine
