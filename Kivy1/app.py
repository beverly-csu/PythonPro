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
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class MainScreen(Screen):                                                       # создаем класс-наследник класса Screen
    def __init__(self, **kwargs):                                               # описываем собственный конструктор
        super().__init__(**kwargs)                                              # вызываем конструктор родительского класса
        v_layout = BoxLayout(orientation='vertical', padding=8, spacing=8)
        h_layout = BoxLayout()
        txt = Label(text='Выбери экран')

class MyApp(App):                                                               # создаем класс-наследник класса App
    def build(self):                                                            # переопределяем метод build
        sm = ScreenManager()                                                    # создаем экземпляр класса ScreenManager()
        return sm                                                               # возвращаем наш экземпляр


MyApp().run()
