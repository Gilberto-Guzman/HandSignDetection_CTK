import tkinter
import tkinter.messagebox
import customtkinter

import os
from PIL import Image
from pygame import mixer

import cv2
import numpy as np
import math
from cvzone.ClassificationModule import Classifier
from cvzone.HandTrackingModule import HandDetector


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Light")
# Themes: "blue" (standard), "green", "dark-blue"
# customtkinter.set_default_color_theme("blue")

# Global sound variable
Sound = True
# Global high contrast Theme
Contrast = False


class Start_Window(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window
        self.title("Traductor de Lenguaje de Señas Méxicano")
        # self.geometry(f"{800}x{600}")
        # self.resizable(False, False)
        self.attributes("-fullscreen", True)

        # center window on screen
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # x = int((screen_width - 800) / 2)
        # y = int((screen_height - 600) / 2)
        # self.geometry(f"+{x}+{y}")

        # load images
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "imgs")

        self.image_play = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "play.png")), size=(150, 150)
        )

        # load and create background image
        self.image_start_background = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "start_background.png")),
            size=(self.winfo_screenwidth(), self.winfo_screenheight()),
        )
        self.label_start_background = customtkinter.CTkLabel(
            self, image=self.image_start_background, text=""
        )
        self.label_start_background.grid(row=0, column=0)

        # load sounds
        sound_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "sounds")
        mixer.init()
        self.start_button_sound = os.path.join(
            sound_path, "start_button_sound.mp3")

        # buttons
        self.button_play = customtkinter.CTkButton(
            master=self,
            text="",
            height=50,
            width=100,
            command=self.open_main_windown,
            image=self.image_play,
            fg_color="#4FB7FF",
            compound="left",
            hover=False,
        )
        self.button_play.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        self.button_play.bind("<Enter>", self.play_focus_in)
        self.button_play.bind("<Leave>", self.play_focus_out)

    def play_focus_in(self, event):
        self.button_play.configure(
            fg_color="#0097FF", border_width=8, border_color="black"
        )
        mixer.music.load(self.start_button_sound)
        mixer.music.play()

    def play_focus_out(self, event):
        self.button_play.configure(fg_color="#4FB7FF", border_width=0)

    def open_main_windown(self):
        self.main_window = Main_Window(self)
        Start_Window.withdraw(self)


class Main_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window
        self.title("Traductor de Lenguaje de Señas Méxicano")
        self.attributes("-fullscreen", True)

        # load images
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "imgs")

        self.image_handsign = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "handsign.png")), size=(120, 120)
        )
        self.image_configuration = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "configuration.png")), size=(120, 120)
        )
        self.image_instructive = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "instructive.png")), size=(120, 120)
        )

        # load sounds
        sound_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "sounds")
        mixer.init()
        self.handsign_button_sound = os.path.join(
            sound_path, "handsign_button_sound.mp3"
        )
        self.configuration_button_sound = os.path.join(
            sound_path, "configuration_button_sound.mp3"
        )
        self.instructive_button_sound = os.path.join(
            sound_path, "instructive_button_sound.mp3"
        )
        if Contrast == False:
            # buttons
            self.button_handsign = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                command=self.open_handsign_window,
                image=self.image_handsign,
                fg_color="#FF6262",
                compound="left",
                hover=False,
            )
            self.button_handsign.place(
                relx=0.5, rely=0.36, anchor=tkinter.CENTER)
            self.button_handsign.bind("<Enter>", self.handsign_focus_in)
            self.button_handsign.bind("<Leave>", self.handsign_focus_out)

            self.button_configuration = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                command=self.open_configuration_windown,
                image=self.image_configuration,
                fg_color="#59FF6A",
                hover=False,
            )
            self.button_configuration.place(
                relx=0.4, rely=0.7, anchor=tkinter.CENTER)
            self.button_configuration.bind(
                "<Enter>", self.configuration_focus_in)
            self.button_configuration.bind(
                "<Leave>", self.configuration_focus_out)

            self.button_instructive = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                command=self.open_instructive_windown,
                image=self.image_instructive,
                fg_color="#4FB7FF",
                hover=False,
            )
            self.button_instructive.place(
                relx=0.6, rely=0.7, anchor=tkinter.CENTER)
            self.button_instructive.bind("<Enter>", self.instructive_focus_in)
            self.button_instructive.bind("<Leave>", self.instructive_focus_out)
        elif Contrast == True:
            # buttons
            self.button_handsign = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                command=self.open_handsign_window,
                image=self.image_handsign,
                fg_color="#000000",
                compound="left",
                hover=False,
            )
            self.button_handsign.place(
                relx=0.5, rely=0.36, anchor=tkinter.CENTER)
            self.button_handsign.bind("<Enter>", self.handsign_focus_in)
            self.button_handsign.bind("<Leave>", self.handsign_focus_out)

            self.button_configuration = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                command=self.open_configuration_windown,
                image=self.image_configuration,
                fg_color="#000000",
                hover=False,
            )
            self.button_configuration.place(
                relx=0.4, rely=0.7, anchor=tkinter.CENTER)
            self.button_configuration.bind(
                "<Enter>", self.configuration_focus_in)
            self.button_configuration.bind(
                "<Leave>", self.configuration_focus_out)

            self.button_instructive = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                command=self.open_instructive_windown,
                image=self.image_instructive,
                fg_color="#000000",
                hover=False,
            )
            self.button_instructive.place(
                relx=0.6, rely=0.7, anchor=tkinter.CENTER)
            self.button_instructive.bind("<Enter>", self.instructive_focus_in)
            self.button_instructive.bind("<Leave>", self.instructive_focus_out)

    # Functions - window
    def open_handsign_window(self):
        self.handsign_window = Handsign_Window(self)

    def open_configuration_windown(self):
        self.configuration_window = Configuration_Window(self)
        Configuration_Window.withdraw(self)

    def open_instructive_windown(self):
        self.instructive_window = Instructive_Window(self)
        Instructive_Window.withdraw(self)

    # Functions - focus
    def handsign_focus_in(self, event):
        if Contrast == False:
            self.button_handsign.configure(
                fg_color="#FF0000", border_width=8, border_color="black"
            )
        else:
            self.button_handsign.configure(
                fg_color="#000000", border_width=8, border_color="white"
            )
        if Sound == True:
            mixer.music.load(self.handsign_button_sound)
            mixer.music.play()

    def handsign_focus_out(self, event):
        if Contrast == False:
            self.button_handsign.configure(fg_color="#FF6262", border_width=0)
        else:
            self.button_handsign.configure(fg_color="#000000", border_width=0)

    def configuration_focus_in(self, event):
        if Contrast == False:
            self.button_configuration.configure(
                fg_color="#00FF1B", border_width=8, border_color="black"
            )
        else:
            self.button_configuration.configure(
                fg_color="#000000", border_width=8, border_color="white"
            )
        if Sound == True:
            mixer.music.load(self.configuration_button_sound)
            mixer.music.play()

    def configuration_focus_out(self, event):
        if Contrast == False:
            self.button_configuration.configure(
                fg_color="#59FF6A", border_width=0)
        else:
            self.button_configuration.configure(
                fg_color="#000000", border_width=0)

    def instructive_focus_in(self, event):
        if Contrast == False:
            self.button_instructive.configure(
                fg_color="#0097FF", border_width=8, border_color="black"
            )
        else:
            self.button_instructive.configure(
                fg_color="#000000", border_width=8, border_color="white"
            )
        if Sound == True:
            mixer.music.load(self.instructive_button_sound)
            mixer.music.play()

    def instructive_focus_out(self, event):
        if Contrast == False:
            self.button_instructive.configure(
                fg_color="#4FB7FF", border_width=0)
        else:
            self.button_instructive.configure(
                fg_color="#000000", border_width=0)


class Configuration_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window
        self.title("Traductor de Lenguáje de Señas Méxicano")
        self.attributes("-fullscreen", True)

        # load images
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "imgs")

        self.image_return = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "return.png")), size=(120, 120)
        )
        self.image_enable_sound = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "enable_sound.png")), size=(120, 120)
        )
        self.image_disable_sound = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "disable_sound.png")), size=(120, 120)
        )
        self.image_enable_eye = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "enable_eye.png")), size=(120, 120)
        )
        self.image_disable_eye = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "disable_eye.png")), size=(120, 120)
        )

        # load and create background image
        """
        self.image_window_background = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "window_background.png")),
            size=(self.winfo_screenwidth(), self.winfo_screenheight()),
        )
        self.label_window_background = customtkinter.CTkLabel(
            self, image=self.image_window_background, text=""
        )
        self.label_window_background.grid(row=0, column=0)
        """

        # load sounds
        sound_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "sounds")
        mixer.init()
        self.return_button_sound = os.path.join(
            sound_path, "return_button_sound.mp3")
        self.narrator_button_sound = os.path.join(
            sound_path, "narrator_button_sound.mp3")
        self.scaling_button_sound = os.path.join(
            sound_path, "scaling_optionmenu_sound.mp3")
        self.contrast_button_sound = os.path.join(
            sound_path, "contrast_button_sound.mp3")

        if Contrast == False:
            # UI Scaling
            optionmenu_var = customtkinter.StringVar(value="100%")
            self.scaling_optionemenu = customtkinter.CTkOptionMenu(
                master=self,
                values=[
                    "100%",
                    "110%",
                    "120%",
                    "130%",
                    "140%",
                    "150%",
                    "160%",
                    "170%",
                    "180%",
                    "190%",
                    "200%",
                ],
                command=self.change_scaling_event,
                variable=optionmenu_var,
                anchor=tkinter.CENTER,
                font=("Helvetica", 32),
            )
            # self.scaling_optionemenu.pack(padx=20, pady=20)
            self.scaling_optionemenu.place(
                relx=0.5, rely=0.2, anchor=tkinter.CENTER)
            self.scaling_optionemenu.bind(
                "<Enter>", self.scaling_optionemenu_focus_in)

            # buttons
            self.button_return = customtkinter.CTkButton(
                master=self,
                text="",
                height=50,
                width=100,
                command=self.open_main_windown,
                image=self.image_return,
                fg_color="#4FB7FF",
                compound="left",
                hover=False,
            )
            self.button_return.place(
                relx=0.12, rely=0.8, anchor=tkinter.CENTER)
            self.button_return.bind("<Enter>", self.return_focus_in)
            self.button_return.bind("<Leave>", self.return_focus_out)

            if Sound == True:
                self.button_sound = customtkinter.CTkButton(
                    master=self,
                    text="",
                    height=50,
                    width=100,
                    command=self.change_sound_state,
                    image=self.image_enable_sound,
                    fg_color="#4FB7FF",
                    compound="left",
                    hover=False,
                )
                self.button_sound.place(
                    relx=0.5, rely=0.45, anchor=tkinter.CENTER)
                self.button_sound.bind("<Enter>", self.sound_focus_in)
                self.button_sound.bind("<Leave>", self.sound_focus_out)
            else:
                self.button_sound = customtkinter.CTkButton(
                    master=self,
                    text="",
                    height=50,
                    width=100,
                    command=self.change_sound_state,
                    image=self.image_disable_sound,
                    fg_color="#4FB7FF",
                    compound="left",
                    hover=False,
                )
                self.button_sound.place(
                    relx=0.5, rely=0.45, anchor=tkinter.CENTER)
                self.button_sound.bind("<Enter>", self.sound_focus_in)
                self.button_sound.bind("<Leave>", self.sound_focus_out)

            if Contrast == True:
                self.button_contrast = customtkinter.CTkButton(
                    master=self,
                    text="",
                    height=50,
                    width=100,
                    command=self.change_contrast_state,
                    image=self.image_enable_eye,
                    fg_color="#4FB7FF",
                    compound="left",
                    hover=False,
                )
                self.button_contrast.place(
                    relx=0.5, rely=0.8, anchor=tkinter.CENTER)
                self.button_contrast.bind("<Enter>", self.contrast_focus_in)
                self.button_contrast.bind("<Leave>", self.contrast_focus_out)
            else:
                self.button_contrast = customtkinter.CTkButton(
                    master=self,
                    text="",
                    height=50,
                    width=100,
                    command=self.change_contrast_state,
                    image=self.image_disable_eye,
                    fg_color="#4FB7FF",
                    compound="left",
                    hover=False,
                )
                self.button_contrast.place(
                    relx=0.5, rely=0.8, anchor=tkinter.CENTER)
                self.button_contrast.bind("<Enter>", self.contrast_focus_in)
                self.button_contrast.bind("<Leave>", self.contrast_focus_out)
        elif Contrast == True:
            # UI Scaling
            optionmenu_var = customtkinter.StringVar(value="100%")
            self.scaling_optionemenu = customtkinter.CTkOptionMenu(
                master=self,
                values=[
                    "100%",
                    "110%",
                    "120%",
                    "130%",
                    "140%",
                    "150%",
                    "160%",
                    "170%",
                    "180%",
                    "190%",
                    "200%",
                ],
                command=self.change_scaling_event,
                variable=optionmenu_var,
                anchor=tkinter.CENTER,
                font=("Helvetica", 32),
                fg_color="#000000",
                button_color="#000000",
                button_hover_color="#000000",
            )
            # self.scaling_optionemenu.pack(padx=20, pady=20)
            self.scaling_optionemenu.place(
                relx=0.5, rely=0.2, anchor=tkinter.CENTER)
            self.scaling_optionemenu.bind(
                "<Enter>", self.scaling_optionemenu_focus_in)

            # buttons
            self.button_return = customtkinter.CTkButton(
                master=self,
                text="",
                height=50,
                width=100,
                command=self.open_main_windown,
                image=self.image_return,
                fg_color="#000000",
                compound="left",
                hover=False,
            )
            self.button_return.place(
                relx=0.12, rely=0.8, anchor=tkinter.CENTER)
            self.button_return.bind("<Enter>", self.return_focus_in)
            self.button_return.bind("<Leave>", self.return_focus_out)

            if Sound == True:
                self.button_sound = customtkinter.CTkButton(
                    master=self,
                    text="",
                    height=50,
                    width=100,
                    command=self.change_sound_state,
                    image=self.image_enable_sound,
                    fg_color="#000000",
                    compound="left",
                    hover=False,
                )
                self.button_sound.place(
                    relx=0.5, rely=0.45, anchor=tkinter.CENTER)
                self.button_sound.bind("<Enter>", self.sound_focus_in)
                self.button_sound.bind("<Leave>", self.sound_focus_out)
            else:
                self.button_sound = customtkinter.CTkButton(
                    master=self,
                    text="",
                    height=50,
                    width=100,
                    command=self.change_sound_state,
                    image=self.image_disable_sound,
                    fg_color="#000000",
                    compound="left",
                    hover=False,
                )
                self.button_sound.place(
                    relx=0.5, rely=0.45, anchor=tkinter.CENTER)
                self.button_sound.bind("<Enter>", self.sound_focus_in)
                self.button_sound.bind("<Leave>", self.sound_focus_out)

            if Contrast == True:
                self.button_contrast = customtkinter.CTkButton(
                    master=self,
                    text="",
                    height=50,
                    width=100,
                    command=self.change_contrast_state,
                    image=self.image_enable_eye,
                    fg_color="#000000",
                    compound="left",
                    hover=False,
                )
                self.button_contrast.place(
                    relx=0.5, rely=0.8, anchor=tkinter.CENTER)
                self.button_contrast.bind("<Enter>", self.contrast_focus_in)
                self.button_contrast.bind("<Leave>", self.contrast_focus_out)
            else:
                self.button_contrast = customtkinter.CTkButton(
                    master=self,
                    text="",
                    height=50,
                    width=100,
                    command=self.change_contrast_state,
                    image=self.image_disable_eye,
                    fg_color="#000000",
                    compound="left",
                    hover=False,
                )
                self.button_contrast.place(
                    relx=0.5, rely=0.8, anchor=tkinter.CENTER)
                self.button_contrast.bind("<Enter>", self.contrast_focus_in)
                self.button_contrast.bind("<Leave>", self.contrast_focus_out)

    def return_focus_in(self, event):
        if Contrast == False:
            self.button_return.configure(
                fg_color="#0097FF", border_width=8, border_color="black"
            )
        else:
            self.button_return.configure(
                fg_color="#000000", border_width=8, border_color="white"
            )
        if Sound == True:
            mixer.music.load(self.return_button_sound)
            mixer.music.play()

    def return_focus_out(self, event):
        if Contrast == False:
            self.button_return.configure(fg_color="#4FB7FF", border_width=0)
        else:
            self.button_return.configure(fg_color="#000000", border_width=0)

    def sound_focus_in(self, event):
        if Contrast == False:
            self.button_sound.configure(
                fg_color="#0097FF", border_width=8, border_color="black"
            )
        else:
            self.button_sound.configure(
                fg_color="#000000", border_width=8, border_color="white"
            )
        if Sound == True:
            mixer.music.load(self.narrator_button_sound)
            mixer.music.play()

    def sound_focus_out(self, event):
        if Contrast == False:
            self.button_sound.configure(fg_color="#4FB7FF", border_width=0)
        else:
            self.button_sound.configure(fg_color="#000000", border_width=0)

    def contrast_focus_in(self, event):
        if Contrast == False:
            self.button_contrast.configure(
                fg_color="#0097FF", border_width=8, border_color="black"
            )
        else:
            self.button_contrast.configure(
                fg_color="#000000", border_width=8, border_color="white"
            )
        if Sound == True:
            mixer.music.load(self.contrast_button_sound)
            mixer.music.play()

    def contrast_focus_out(self, event):
        if Contrast == False:
            self.button_contrast.configure(fg_color="#4FB7FF", border_width=0)
        else:
            self.button_contrast.configure(fg_color="#000000", border_width=0)

    def scaling_optionemenu_focus_in(self, event):
        if Sound == True:
            mixer.music.load(self.scaling_button_sound)
            mixer.music.play()

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def change_sound_state(self):
        global Sound
        Sound = not Sound
        if Sound == True:
            self.button_sound.configure(
                image=self.image_enable_sound,
            )
        else:
            self.button_sound.configure(
                image=self.image_disable_sound,
            )

    def change_contrast_state(self):
        global Contrast
        Contrast = not Contrast
        if Contrast == True:
            self.button_contrast.configure(
                image=self.image_enable_eye,
            )
            self.configuration_window = Configuration_Window(self)
            Configuration_Window.withdraw(self)
            customtkinter.set_appearance_mode("Dark")
        else:
            self.button_contrast.configure(
                image=self.image_disable_eye,
            )
            self.configuration_window = Configuration_Window(self)
            Configuration_Window.withdraw(self)
            customtkinter.set_appearance_mode("Light")
        self.update_idletasks()

    def open_main_windown(self):
        self.main_window = Main_Window(self)
        Configuration_Window.withdraw(self)


class Instructive_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window
        self.title("Traductor de Lenguáje de Señas Méxicano")
        # self.geometry(f"{800}x{600}")
        # self.resizable(False, False)
        self.attributes("-fullscreen", True)

        # center window on screen
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()
        # x = int((screen_width - 800) / 2)
        # y = int((screen_height - 600) / 2)
        # self.geometry(f"+{x}+{y}")

        # load images
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "imgs")

        self.image_return = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "return.png")), size=(120, 120)
        )

        self.image_handsign = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "handsign.png")), size=(120, 120)
        )
        self.image_configuration = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "configuration.png")), size=(120, 120)
        )
        self.image_instructive = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "instructive.png")), size=(120, 120)
        )

        # load and create background image
        """
        self.image_window_background = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "white_background.png")),
            size=(self.winfo_screenwidth(), self.winfo_screenheight()),
        )
        self.label_window_background = customtkinter.CTkLabel(
            self, image=self.image_window_background, text=""
        )
        self.label_window_background.grid(row=0, column=0)
        """
        # load sounds
        sound_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "sounds")
        mixer.init()
        self.return_button_sound = os.path.join(
            sound_path, "return_button_sound.mp3")
        self.handsign_label_sound = os.path.join(
            sound_path, "handsign_label_sound.mp3")
        self.configuration_label_sound = os.path.join(
            sound_path, "configuration_label_sound.mp3"
        )

        # labels
        self.label_handsign = customtkinter.CTkLabel(
            master=self,
            text="Activa la cámara para la\ndetección del lenguaje de señas.",
            font=("Helvetica", 32),
        )
        self.label_handsign.place(relx=0.6, rely=0.2, anchor=tkinter.CENTER)
        self.label_handsign.bind("<Enter>", self.label_handsign_focus_in)

        self.label_configuration = customtkinter.CTkLabel(
            master=self,
            text="Modifica parametros de\naccesibilidad en la aplicación.",
            font=("Helvetica", 32),
        )
        self.label_configuration.place(
            relx=0.6, rely=0.5, anchor=tkinter.CENTER)
        self.label_configuration.bind(
            "<Enter>", self.label_configuration_focus_in)
        if Contrast == False:
            # example buttons
            self.button_handsign = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                image=self.image_handsign,
                fg_color="#FF6262",
                compound="left",
                hover=False,
            )
            self.button_handsign.place(
                relx=0.14, rely=0.2, anchor=tkinter.CENTER)

            self.button_configuration = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                image=self.image_configuration,
                fg_color="#59FF6A",
                compound="left",
                hover=False,
            )
            self.button_configuration.place(
                relx=0.14, rely=0.5, anchor=tkinter.CENTER)

            # functional button
            self.button_return = customtkinter.CTkButton(
                master=self,
                text="",
                height=50,
                width=100,
                command=self.open_main_windown,
                image=self.image_return,
                fg_color="#4FB7FF",
                compound="right",
                hover=False,
            )
            self.button_return.place(
                relx=0.87, rely=0.8, anchor=tkinter.CENTER)
            self.button_return.bind("<Enter>", self.return_focus_in)
            self.button_return.bind("<Leave>", self.return_focus_out)
        elif Contrast == True:
            # example buttons
            self.button_handsign = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                image=self.image_handsign,
                fg_color="#000000",
                compound="left",
                hover=False,
            )
            self.button_handsign.place(
                relx=0.14, rely=0.2, anchor=tkinter.CENTER)

            self.button_configuration = customtkinter.CTkButton(
                master=self,
                text="",
                height=100,
                width=100,
                image=self.image_configuration,
                fg_color="#000000",
                compound="left",
                hover=False,
            )
            self.button_configuration.place(
                relx=0.14, rely=0.5, anchor=tkinter.CENTER)

            # functional button
            self.button_return = customtkinter.CTkButton(
                master=self,
                text="",
                height=50,
                width=100,
                command=self.open_main_windown,
                image=self.image_return,
                fg_color="#000000",
                compound="right",
                hover=False,
            )
            self.button_return.place(
                relx=0.87, rely=0.8, anchor=tkinter.CENTER)
            self.button_return.bind("<Enter>", self.return_focus_in)
            self.button_return.bind("<Leave>", self.return_focus_out)

    def return_focus_in(self, event):
        if Contrast == False:
            self.button_return.configure(
                fg_color="#0097FF", border_width=8, border_color="black"
            )
        else:
            self.button_return.configure(
                fg_color="#000000", border_width=8, border_color="white"
            )
        if Sound == True:
            mixer.music.load(self.return_button_sound)
            mixer.music.play()

    def return_focus_out(self, event):
        if Contrast == False:
            self.button_return.configure(fg_color="#4FB7FF", border_width=0)
        else:
            self.button_return.configure(fg_color="#000000", border_width=0)

    def label_handsign_focus_in(self, event):
        if Sound == True:
            mixer.music.load(self.handsign_label_sound)
            mixer.music.play()

    def label_configuration_focus_in(self, event):
        if Sound == True:
            mixer.music.load(self.configuration_label_sound)
            mixer.music.play()

    def open_main_windown(self):
        self.main_window = Main_Window(self)
        Configuration_Window.withdraw(self)


class Handsign_Window(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        cap = cv2.VideoCapture(0)
        detector = HandDetector(maxHands=1)
        classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

        # offset nos permite agrandar un poco mas la imagen de la mano
        offset = 20
        imgSize = 300

        folder = "Data/C"
        counter = 0

        # labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
        # "W", "X", "Y", "Z"]
        labels = ["A", "B", "C"]

        while True:
            try:
                success, img = cap.read()
                imgOutput = img.copy()
                hands, img = detector.findHands(img)

                if Contrast == False:
                    cv2.rectangle(imgOutput, (20, 10),
                                  (610, 70), (0, 0, 255), -1)
                    cv2.putText(imgOutput, 'Presiona "S" o "C" para salir.', (25, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3, cv2.LINE_AA)
                elif Contrast == True:
                    cv2.rectangle(imgOutput, (20, 10),
                                  (610, 70), (0, 0, 0), -1)
                    cv2.putText(imgOutput, 'Presiona "S" o "C" para salir.', (25, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3, cv2.LINE_AA)

                # Si hay algo en las manos...
                if hands:
                    hand = hands[0]
                    x, y, w, h = hand['bbox']

                    imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

                    # Nos da el bounding box que necesitamos
                    imgCrop = img[y - offset:y + h +
                                  offset, x - offset:x + w + offset]

                    imgCropShape = imgCrop.shape

                    aspectRatio = h / w

                    if aspectRatio > 1:
                        # imgSize seral igual a 300
                        k = imgSize / h
                        wCal = math.ceil(k * w)
                        imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                        imgResizeShape = imgResize.shape
                        wGap = math.ceil((imgSize - wCal) / 2)
                        imgWhite[:, wGap:wCal + wGap] = imgResize
                        prediction, index = classifier.getPrediction(
                            imgWhite, draw=False)
                        print(prediction, index)
                    else:
                        k = imgSize / w
                        hCal = math.ceil(k * h)
                        imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                        imgResizeShape = imgResize.shape
                        hGap = math.ceil((imgSize - hCal) / 2)
                        imgWhite[hGap:hCal + hGap, :] = imgResize
                        prediction, index = classifier.getPrediction(
                            imgWhite, draw=False)

                    if Contrast == False:
                        cv2.rectangle(imgOutput, (x - offset, y - offset - 50),
                                      (x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
                        cv2.putText(imgOutput, labels[index], (x, y - 26),
                                    cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
                        cv2.rectangle(imgOutput, (x - offset, y - offset),
                                      (x + w + offset, y + h + offset), (255, 0, 255), 4)
                    elif Contrast == True:
                        cv2.rectangle(imgOutput, (x - offset, y - offset - 50),
                                      (x - offset + 90, y - offset - 50 + 50), (0, 0, 0), cv2.FILLED)
                        cv2.putText(imgOutput, labels[index], (x, y - 26),
                                    cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
                        cv2.rectangle(imgOutput, (x - offset, y - offset),
                                      (x + w + offset, y + h + offset), (0, 0, 0), 4)
                    # cv2.imshow("ImageCrop", imgCrop)
                    # cv2.imshow("ImageWhite", imgWhite)

                cv2.imshow("Image", imgOutput)
                key = cv2.waitKey(1)
                if key == ord("s") or key == ord("S") or key == ord("c") or key == ord("C"):
                    Handsign_Window.withdraw(self)
                    cv2.destroyAllWindows()
                    break
            except:
                print('Error')


if __name__ == "__main__":
    app = Start_Window()
    app.mainloop()
