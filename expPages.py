import os
from psychopy import visual, core
from psychopy.hardware import keyboard
from page import Page


def initPages(win, log_obj):
    # --- Initialize components for each Routine ---
    Title = visual.TextBox2(
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
        name="Title",
        autoLog=True,
    )
    SubTitle = visual.TextBox2(
        win,
        text="When you comence each trial you will be asked to click to continue after which you will see the simulator below to control the pedestrian (circled) please use the arrow keys, or the W,A,S and D keys if you prefer",
        font="Open Sans",
        pos=(0.0, 0.25),
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
        name="SubTitle",
        autoLog=True,
    )
    arrows = visual.ImageStim(
        win=win,
        name="arrows",
        image=os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "images",
            "SeekPng.com_arrow-keys-png_3271603.png",
        ),
        mask=None,
        anchor="center",
        ori=0.0,
        pos=(-0.4, -0.2),
        size=(0.225, 0.15),
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
        image=os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "images",
            "SeekPng.com_wasd-png_1791627.png",
        ),
        mask=None,
        anchor="center",
        ori=0.0,
        pos=(0.4, -0.2),
        size=(0.225, 0.15),
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
        win=win,
        name="Sim",
        image=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "images", "Simulator.png"
        ),
        mask=None,
        anchor="center",
        ori=0.0,
        pos=(0.0, -0.1),
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
        pos=(0.0, -0.425),
        size=(0.8, 0.1),
        letterHeight=0.04,
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
    key_resp.name = "key_resp"

    intro_page = Page(
        "intro_page",
        log_obj,
        component_list=[Title, SubTitle, arrows, wasd, Sim_image, button, key_resp],
    )

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
        text="Click here or hit Space bar\nto start simulator",
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
    key_resp_2.name = "key_resp_2"

    start_page = Page(
        "start_page", log_obj, component_list=[Start_Info, button_2, key_resp_2]
    )

    # --- Initialize components for Routine "Simulation" ---

    # Sim = makeCrossingSim(
    #     load_path=os.path.join(
    #         os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    #         "logs",
    #         "Tue_Sep_27_16:03:45_2022",
    #         "DQN_testing_1",
    #         "best.zip",
    #     )
    # )
    # Sim.name = "Sim"

    sim_page = Page("sim_page", log_obj, component_list=[])

    # --- Initialize components for Routine "Safety_Judgements" ---
    Question = visual.TextStim(
        win=win,
        name="Question",
        text="For the vehicle displayed below\nplease indicate how safe it's behaviour was. ",
        font="Open Sans",
        pos=(0, 0.4),
        height=0.04,
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
        image=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "images", "Car.png"
        ),
        mask=None,
        anchor="center",
        ori=0.0,
        pos=(0, 0.2),
        size=(0.2, 0.2),
        color=[1, 1, 1],
        colorSpace="rgb",
        opacity=None,
        flipHoriz=False,
        flipVert=False,
        texRes=128.0,
        interpolate=True,
        depth=-1.0,
    )
    Sub_Question = visual.TextBox2(
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
        name="Sub_Question",
        autoLog=True,
    )
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
    Sub_Question_2 = visual.TextBox2(
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
        name="Sub_Question_2",
        autoLog=True,
    )
    slider_2 = visual.Slider(
        win=win,
        name="slider",
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
        depth=0,
        readOnly=False,
    )
    Sub_Question_3 = visual.TextBox2(
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
        name="Sub_Question_3",
        autoLog=True,
    )
    slider_3 = visual.Slider(
        win=win,
        name="slider",
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
        depth=0,
        readOnly=False,
    )

    saftey_judgement_page = Page(
        "saftey_judgement_page",
        log_obj,
        component_list=[
            Question,
            Vehicle_image,
            Sub_Question,
            Sub_Question_2,
            Sub_Question_3,
            slider,
            slider_2,
            slider_3,
        ],
    )

    # --- Initialize components for Routine "AV_Judgements" ---
    av_question = visual.TextBox2(
        win,
        text="Please indicate how likely each car display below\nwas controlled by an autonomous algorithm.",
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
        name="av_question",
        autoLog=True,
    )
    car_image = visual.ImageStim(
        win=win,
        name="car_image",
        image=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "images", "Car.png"
        ),
        mask=None,
        anchor="center",
        ori=0.0,
        pos=(-0.0, 0.15),
        size=(0.2, 0.2),  # (0.5, 0.5),
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
        name="slider",
        startValue=None,
        size=(1.0, -0.05),
        pos=(0, 0.05),
        units=None,
        labels=(1, 2, 3, 4, 5),
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
        labelHeight=0.025,
        flip=False,
        ori=0.0,
        depth=0,
        readOnly=False,
    )
    car_image_2 = visual.ImageStim(
        win=win,
        name="car_image_2",
        image=os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "images", "Car_2.png"
        ),
        mask=None,
        anchor="center",
        ori=0.0,
        pos=(-0.0, -0.15),
        size=(0.2, 0.2),  # (0.5, 0.5),
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
        name="slider",
        startValue=None,
        size=(1.0, -0.05),
        pos=(0, -0.25),
        units=None,
        labels=(1, 2, 3, 4, 5),
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
        labelHeight=0.025,
        flip=False,
        ori=0.0,
        depth=0,
        readOnly=False,
    )

    av_judgement_page = Page(
        "av_judgement_page",
        log_obj,
        component_list=[
            av_question,
            car_image,
            car_image_2,
            slider_4,
            slider_5,
        ],
    )

    # --- Initialize components for Routine "Thanks" ---
    Thank_You = visual.TextBox2(
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
        name="Thank_You",
        autoLog=True,
    )
    Consent_remind = visual.TextBox2(
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
        name="Consent_remind",
        autoLog=True,
    )
    button_3 = visual.ButtonStim(
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
    button_3.buttonClock = core.Clock()
    key_resp_3 = keyboard.Keyboard()
    key_resp_3.name = "key_resp_3"

    thanks_page = Page(
        "thanks_page",
        log_obj,
        component_list=[Thank_You, Consent_remind, button_3, key_resp_3],
    )

    return (
        intro_page,
        start_page,
        sim_page,
        saftey_judgement_page,
        av_judgement_page,
        thanks_page,
    )


from pygame_ped_env.agents import (
    RLVehicle,
    KeyboardPedestrian,
)
from stable_baselines3 import DQN
import gym


def makeCrossingSim(load_path, pygame_window_size=[720, 576]):
    agent = RLVehicle(
        [0, pygame_window_size[1] / 2],
        [pygame_window_size[0], pygame_window_size[1] / 2],
        "car",
        "right",
    )

    agent.model = DQN.load(load_path)

    env = agent.model.get_env()
    if env is None:
        agent.model.set_env(
            gym.make(
                "pygame_ped_env:ped_env-v1",
                sim_area=pygame_window_size,
                controllable_sprites=[
                    agent,
                    KeyboardPedestrian(
                        pygame_window_size[0] / 2, pygame_window_size[1] * (7 / 8), "up"
                    ),
                    # RandomPedestrian(pygame_window_size[0] / 2, pygame_window_size[1] * (7 / 8), "up"),
                ],
                headless=False,
                seed=4321,
            )
        )
        env = agent.model.get_env()

    # env.envs[0].env.run()
    return env
