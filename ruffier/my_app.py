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

        lbl_name = Label(text="Введите имя:", halign="right")
        self.input_name = TextInput(multiline=False)

        lbl_age = Label(text="Введите возраст:", halign="right")
        self.input_age = TextInput(text="7", multiline=False)

        self.btn = Button(text="Начать", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        
        line1.add_widget(lbl_name)
        line1.add_widget(self.input_name)
        line2.add_widget(lbl_age)
        line2.add_widget(self.input_age)
        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instruction)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global name
        name = self.input_name.text
        self.manager.current = "pulse1"

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScreen(name="instr"))
        return sm

# первый вариант
app = HeartCheck()
app.run()
# второй вариант
HeartCheck().run()
