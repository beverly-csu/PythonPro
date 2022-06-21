#не забудь импортировать необходимые элементы!
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

age = 7
name = str()
p1, p2, p3 = 0, 0, 0


class InstrScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instruction = Label(text="Empty")
