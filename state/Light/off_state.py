__author__ = 'cwong_000'

import on_state

class LightOff():

    def switch(self):
        return on_state.LightOn()

    def display(self):
        return "The Light is off!"