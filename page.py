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
import os
from stable_baselines3 import DQN
from pygame_ped_env.envs import RLCrossingSim
from sb3_contrib.common.wrappers import ActionMasker
from sb3_contrib.common.maskable.utils import get_action_masks
from gym import Env
import numpy as np


def mask_fn(env: Env) -> np.ndarray:
    # Do whatever you'd like in this function to return the action mask
    # for the current env. In this example, we assume the env has a
    # helpful method we can rely on.
    return env.action_masks()


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
        # if any(isinstance(self.componentList, Env)):
        #     return

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
        # if any(isinstance(self.componentList, Env)):
        #     return

        for thisComponent in self.componentList:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
            # autoDraw sets status, so if no autoDraw set manually
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
        responsePage = False
        for component in self.componentList:
            # initalise component if not started yet
            if component.status == NOT_STARTED and tThisFlip >= 0.0 - FRAME_TOLERANCE:
                # keep track of start time/frame for later
                component.frameNStart = frameN  # exact frame index
                component.tStart = t  # local t and not account for scr refresh
                component.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                window.timeOnFlip(component, "tStartRefresh")
                # add timestamp to datafileEnv
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
                # continue

            # --- Stimulus Type Specific Updates ---
            # --- condition routine end for sliders ---
            # if isinstance(component, visual.Slider) and component.status == STARTED:
            # --- condition routine end for textboxes ---
            # if isinstance(component, visual.TextStim) and component.status == STARTED:
            # --- condition routine end for images ---
            # if isinstance(component, visual.ImageStim) and component.status == STARTED:
            # --- checking for button clicks ----
            elif isinstance(component, visual.ButtonStim):
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
            elif (
                isinstance(component, keyboard.Keyboard) and component.status == STARTED
            ):
                theseKeys = component.getKeys(keyList=["space"], waitRelease=False)
                component._key_resp_allKeys.extend(theseKeys)
                if len(component._key_resp_allKeys):
                    component.keys = component._key_resp_allKeys[
                        -1
                    ].name  # just the last key pressed
                    component.rt = component._key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # check for sliders here instead of looking through component list again
            elif isinstance(component, visual.Slider):
                responsePage = True

        # check for slider values and next button click if a response page
        if responsePage:
            # override basic button logic
            continueRoutine = True
            ratings = []
            # have to loop over components again after update for slider values
            for component in self.componentList:
                if isinstance(component, visual.Slider):
                    ratings.append(component.getRating())
                elif isinstance(component, visual.ButtonStim):
                    nextClick = component.wasClicked
            # if all sliders have a value and next button has been clicked move on
            if all(ratings) and nextClick:
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


class SimPage(Page):
    def __init__(
        self,
        page_name,
        log_experiment,
        log_trial=None,
        component_list=[],
        sim_area=(640, 480),
    ):
        super().__init__(page_name, log_experiment, log_trial, component_list)

        self.coeff_map = {
            -3: float(1 / 4),
            -2: float(1 / 3),
            -1: float(1 / 2),
            0: float(1),
            1: float(2),
            2: float(3),
            3: float(4),
        }

        self.colours = [
            "blue",
            "silver",
            "white",
            "red",
            "yellow",
            "green",
            "brown",
            "orange",
        ]

        wkdir = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(
            wkdir,
            "data",
            "env_logs",
        )

        os.makedirs(log_path, exist_ok=True)

        self.path_to_models = os.path.join(wkdir, "models")

        shapedRL_load_path = os.path.join(self.path_to_models, "maskedDQN_1.0_1.0_1.0")
        simpleRL_load_path = os.path.join(self.path_to_models, "maskedDQN")

        env = RLCrossingSim(
            sim_area=sim_area,
            scenarioList=[0, 1],  # [*range(0, 19)],
            human_controlled_ped=True,
            human_controlled_car=False,
            headless=False,
            seed=42,
            basic_model=simpleRL_load_path,
            attr_model=shapedRL_load_path,
            log_path=log_path,
        )
        self.env = ActionMasker(env, mask_fn)

    def changeModel(self, model_path):
        self.env.modelA = self.env.load_model(model_path)

    def runScenario(self, scenario, sjData=None):
        if scenario < 2:
            model_path = os.path.join(
                self.path_to_models,
                f"maskedDQN_{np.round(self.coeff_map[sjData['speed'][-1]],2)}_{np.round(self.coeff_map[sjData['position'][-1]],2)}_{np.round(self.coeff_map[sjData['steering'][-1]],2)}",
            )
            try:
                self.changeModel(model_path)
            except:
                import shutil

                shutil.copy(
                    os.path.join(self.path_to_models, "maskedDQN_1.0_1.0_1.0.zip"),
                    model_path + ".zip",
                )
                self.changeModel(model_path)

        obs = self.env.reset(scenario=scenario)
        done = False
        while not done:
            if self.env.scenarioName in ("H2", "H_l", "H_r"):
                obs, reward, done, info = self.env.step({"obs": obs})
            else:
                obs, reward, done, info = self.env.step(
                    self.env.modelL.predict(
                        obs, action_masks=get_action_masks(self.env)
                    ),
                )

        return info

    def close(self, saveDir="./", info=None):
        self.env.env.close(saveDir=saveDir, info=info)
