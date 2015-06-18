__author__ = 'cwong_000'

import light

my_light = light.Light()

#print out "The Light is off!"
print(my_light.display())

#switch the light state to on
my_light.switch()

#print out "The Light is on!"
print(my_light.display())