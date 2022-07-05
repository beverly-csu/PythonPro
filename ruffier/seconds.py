from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty


class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.done = False
        self.current = 0
        self.total = total
        my_text = 'Прошло секунд: ' + str(self.current)
        super().__init__(text=my_text)
    
    def restart(self, total, **kwargs):
        pass

    def start(self):
        pass

    def change(self, dt):
        pass
