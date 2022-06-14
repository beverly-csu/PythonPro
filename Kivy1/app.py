from kivy.app import App                                                        # подключаем класс приложения
from kivy.uix.label import Label                                                # подключаем виджет "Надпись"
from kivy.uix.button import Button                                              # подключаем виджет "Кнопка"
from kivy.uix.boxlayout import BoxLayout                                        # подключаем виджет расположения объектов
from kivy.uix.screenmanager import ScreenManager, Screen                        # подключаем виджет "Экран"


class ScrButton(Button):                                                        # создаем класс-наследник класса Button
    def __init__(self, screen, direction='right', goal='main', **kwargs):       # описываем собственный конструктор
        super().__init__(**kwargs)                                              # вызываем конструктор родительского класса
        self.screen = screen                                                    # поле с объектом класса ScreenManager
        self.direction = direction                                              # поле, описывающее вид перехода от окна к окну
        self.goal = goal                                                        # поле, хранящее название окна, к которому будет совершен переход
    def on_press(self):                                                         # функция, которая обрабатывает нажатие на кнопку
        self.screen.manager.transition.direction = self.direction               # устанавливаем вид перехода
        self.screen.manager.current = self.goal                                 # устанавливаем на какой экран нам надо переместиться


class MainScreen(Screen):                                                       # создаем класс-наследник класса Screen
    def __init__(self, **kwargs):                                               # описываем собственный конструктор
        super().__init__(**kwargs)                                              # вызываем конструктор родительского класса
        v_layout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        h_layout = BoxLayout()
        txt = Label(text='Выбери экран')
        v_layout.add_widget(ScrButton(self, direction='down', goal='first', text='1'))
        v_layout.add_widget(ScrButton(self, direction='left', goal='second', text='2'))
        v_layout.add_widget(ScrButton(self, direction='up', goal='third', text='3'))
        v_layout.add_widget(ScrButton(self, direction='right', goal='fourth', text='4'))
        h_layout.add_widget(txt)
        h_layout.add_widget(v_layout)
        self.add_widget(h_layout)


class MyApp(App):                                                               # создаем класс-наследник класса App
    def build(self):                                                            # переопределяем метод build
        sm = ScreenManager()                                                    # создаем экземпляр класса ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm                                                               # возвращаем наш экземпляр


MyApp().run()
