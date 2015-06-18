__author__ = 'cwong_000'

import on_state
import off_state

class Light:

    def __init__(self):
        #light is keep off at the start
        self.light_state = off_state.LightOff()

    def display(self):
        return self.light_state.display()

    def switch(self):
        self.light_state = self.light_state.switch()