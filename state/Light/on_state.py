__author__ = 'cwong_000'

import off_state

class LightOn():

    def switch(self):
        return off_state.LightOff()

    def display(self):
        return "The Light is on!"