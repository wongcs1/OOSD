__author__ = 'cwong_000'

class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.age = 0
        self.dead = False

    def change_name(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def incrementage(self):
        self.age += 1
        return self.age

    def kill(self):
        self.dead = True
        return self.dead