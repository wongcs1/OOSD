__author__ = 'cwong_000'

import re

class UsAddress():

    def __init__(self, recipient="", org="", addresslineone="", addresslinetwo="", city="", state="", postcode=""):
        self.recipient = recipient
        self.org = org
        self.addresslineone = addresslineone
        self.addresslinetwo = addresslinetwo
        self.city = city
        self.state = state
        self.postcode = postcode

    @property
    def recipient(self):
        return self._recipient

    #Check if the recipient is valid before setting it
    #recipient can not be left blank(no length)
    @recipient.setter
    def recipient(self, newrecipient):
        if len(newrecipient) < 1:
            raise ValueError
        else:
            self._recipient = newrecipient


    @property
    def addresslineone(self):
        return self._addresslineone

    #Check if the address line is valid before setting it
    #address line can not be left blank(no length)
    @addresslineone.setter
    def addresslineone(self, newaddress):
        if len(newaddress) < 1:
            raise ValueError
        else:
            self._addresslineone = newaddress


    @property
    def city(self):
        return self._city

    #Check if the city is valid before setting it
    #city can not be left blank(no length)
    @city.setter
    def city(self, newcity):
        if len(newcity) < 1:
            raise ValueError
        else:
            self._city = newcity


    @property
    def state(self):
        return self._state

    #Check if the postcode is valid before setting it
    #area must be 2 letters long in total
    @state.setter
    def state(self, newstate):
        validateformat = re.compile('^[A-Z]{2}$')
        if validateformat.match(newstate) != None:
            self._state = newstate
        else:
            raise ValueError


    @property
    def postcode(self):
        return self._postcode

    #Check if the postcode is valid before setting it
    #area must not exceed 9 digits long in total
    @postcode.setter
    def postcode(self, newpostcode):
        validateformat = re.compile('^[0-9]{9}$')
        if validateformat.match(newpostcode) != None:
            self._postcode = newpostcode
        else:
            raise ValueError

    #Building the address string and returns it
    def generateaddressstring(self):
        addressstring = ""

        addressstring += "Addressee: " + self.recipient + "\n"

        if(len(self.org) > 0):
            addressstring += "Organisation: " + self.org + "\n"

        addressstring += "Address: " + self._addresslineone + "\n"

        if len(self.addresslinetwo) > 0:
            addressstring += self.addresslinetwo + "\n"

        addressstring += "City: " + self.city + "\n"

        addressstring += "State: " + self.state + "\n"

        addressstring += "Post Code: " + self.postcode + "\n"

        return addressstring

    def __str__(self):
        return self.generateaddressstring()