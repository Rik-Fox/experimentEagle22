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
    def __init__(self, page_name, log_obj=None, component_list=[]) -> None:
        self.name = page_name
        self.componentList = component_list
        self._logObj = log_obj

    def getLogObj(self):
        return self._logObj

    def setLogObj(self, log_obj):
        self._logObj = log_obj

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

            # --- log slider data ---
            if isinstance(thisComponent, visual.Slider):
                self._logObj.addData("slider.response", thisComponent.getRating())
                self._logObj.addData("slider.rt", thisComponent.getRT())

            # --- log and ButtonStim data ---
            if isinstance(thisComponent, visual.ButtonStim):
                self._logObj.addData(
                    f"{thisComponent.name}.numClicks", thisComponent.numClicks
                )
                if thisComponent.numClicks:
                    self._logObj.addData(
                        f"{thisComponent.name}.timesOn", thisComponent.timesOn
                    )
                    self._logObj.addData(
                        f"{thisComponent.name}.timesOff", thisComponent.timesOff
                    )
                else:
                    self._logObj.addData(f"{thisComponent.name}.timesOn", "")
                    self._logObj.addData(f"{thisComponent.name}.timesOff", "")

            # --- log keyboard responses ---
            if isinstance(thisComponent, keyboard.Keyboard):
                if thisComponent.keys in ["", [], None]:  # No response was made
                    thisComponent.keys = None
                self._logObj.addData(f"{thisComponent.name}.keys", thisComponent.keys)
                if thisComponent.keys != None:  # we had a response
                    self._logObj.addData(f"{thisComponent.name}.rt", thisComponent.rt)

    def update(self, window, FRAME_TOLERANCE, frameN, t, tThisFlip, tThisFlipGlobal):
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
                self._logObj.timestampOnFlip(window, f"{component.name}.started")
                component.setAutoDraw(True)

            # --- Stimulus Type Specific Updates ---
            # --- condition routine end for sliders ---
            if isinstance(component, (visual.Slider)) and component.status == STARTED:
                if component.getRating() is not None and component.status == STARTED:
                    continueRoutine = False
            # --- condition routine end for textboxes ---
            if isinstance(component, (visual.TextStim)) and component.status == STARTED:
                if bool(1.0):
                    # keep track of stop time/frame for later
                    component.tStop = self.t  # not accounting for scr refresh
                    component.frameNStop = self.frameN  # exact frame index
                    # add timestamp to datafile
                    self._logObj.timestampOnFlip(window, f"{component.name}.stopped")
                    component.setAutoDraw(False)

            # --- condition routine end for images ---
            if (
                isinstance(component, (visual.ImageStim))
                and component.status == STARTED
            ):
                if bool(1.0):
                    # keep track of stop time/frame for later
                    component.tStop = self.t  # not accounting for scr refresh
                    component.frameNStop = self.frameN  # exact frame index
                    # add timestamp to datafile
                    self._logObj.timestampOnFlip(window, f"{component.name}.stopped")
                    component.setAutoDraw(False)
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
                        else:
                            # update time clicked until
                            component.timesOff[-1] = component.buttonClock.getTime()
                        if not component.wasClicked:
                            # end routine when button is clicked
                            continueRoutine = False
                            None
                        component.wasClicked = True  # if button is still clicked next frame, it is not a new click
                    else:
                        # if button is clicked next frame, it is a new click
                        component.wasClicked = False
                else:
                    # if button is clicked next frame, it is a new click
                    component.wasClicked = False
                    # keep track of stop time/frame for later
                    component.tStop = self.t  # not accounting for scr refresh
                    component.frameNStop = self.frameN  # exact frame index
                    # add timestamp to datafile
                    self._logObj.timestampOnFlip(window, f"{component.name}.stopped")
                    component.setAutoDraw(False)

            # --- listening on keyboard ---
            if isinstance(component, keyboard.Keyboard):
                waitOnFlip = False
                if (
                    component.status == NOT_STARTED
                    and tThisFlip >= 0.0 - FRAME_TOLERANCE
                ):
                    # keep track of start time/frame for later
                    component.frameNStart = frameN  # exact frame index
                    component.tStart = t  # local t and not account for scr refresh
                    component.tStartRefresh = tThisFlipGlobal  # on global time
                    # time at next scr refresh
                    window.timeOnFlip(component, "tStartRefresh")
                    # add timestamp to datafile
                    self._logObj.timestampOnFlip(window, f"{component.name}.started")
                    component.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    # t=0 on next screen flip
                    window.callOnFlip(component.clock.reset)
                    # clear events on next screen flip
                    window.callOnFlip(component.clearEvents, eventType="keyboard")
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

        return continueRoutine
