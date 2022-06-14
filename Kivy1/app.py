from kivy.app import App                                    # подключаем класс приложения
from kivy.uix.label import Label                            # подключаем виджет "Надпись"
from kivy.uix.button import Button                          # подключаем виджет "Кнопка"
from kivy.uix.boxlayout import BoxLayout                    # подключаем виджет расположения объектов
from kivy.uix.screenmanager import ScreenManager, Screen    # подключаем виджет "Экран"


class MainScreen(Screen):
    pass


class MyApp(App):                                           # создаем класс-наследник класса App
    def build(self):                                        # переопределяем метод build
        sm = ScreenManager()                                # создаем экземпляр класса ScreenManager()
        return sm                                           # возвращаем наш экземпляр


MyApp().run()
