#не забудь импортировать необходимые элементы!
from re import MULTILINE
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import *

age = 7
name = str()
p1, p2, p3 = 0, 0, 0


class InstrScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instruction = Label(text=txt_instruction)

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

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_test1)
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text="Введите результат:", halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global p1
        p1 = int(self.in_result.text)
        self.manager.current = 'sits'
        

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)
        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result1 = Label(text="Результат:", halign='right')
        self.in_result1 = TextInput(text='0', multiline=False)
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result2 = Label(text="Результат после отдыха:", halign='right')
        self.in_result2 = TextInput(text='0', multiline=False)
        line1.add_widget(lbl_result2)
        line1.add_widget(self.in_result2)

        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global p2, p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
        self.manager.current = 'result'

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScreen(name="instr"))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name="sits"))
        sm.add_widget(PulseScr2(name='pulse2'))
        return sm

# первый вариант
app = HeartCheck()
app.run()
# второй вариант
HeartCheck().run()
