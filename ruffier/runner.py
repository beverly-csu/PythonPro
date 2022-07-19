from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout


class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)

    def __init__(self, total=10, steptime=1, autorepeat=True,
                 bcolor=(0.73, 0.15, 0.96, 1),
                 btext_inprogress='Приседание', **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.autorepeat = autorepeat
        self.btext_inprogress = btext_inprogress
        self.animation = (Animation(pos_hint={'top': 0.1}, duration=steptime/2) + 
                          Animation(pos_hint={'top': 1.0}, duration=steptime/2))
        self.animation.on_progress = self.next
        self.btn = Button(size_hint=(1, 0.1), pos_hint={'top': 1.0}, background_color=bcolor)
        self.add_widget(self.btn)
