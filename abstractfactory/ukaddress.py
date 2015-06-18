__author__ = 'cwong_000'

import re

class UkAddress():

    def __init__(self, recipient="", org="", buildingname="", addressline="", locality="", city="", postcode=""):
        self.recipient = recipient
        self.org = org
        self.buildingname = buildingname
        self.addressline = addressline
        self.locality = locality
        self.city = city
        self.postcode = postcode


    @property
    def postcode(self):
        return self._postcode

    #Check if the postcode is valid before setting it
    #area must not exceed 7(in ~4+~3 format) digits/letters long in total
    @postcode.setter
    def postcode(self, newpostcode):
        validateformat = re.compile('^[A-Z0-9]{4}\s[A-Z0-9]{3}$')
        if validateformat.match(newpostcode) != None:
            self._postcode = newpostcode
        else:
            raise ValueError


    @property
    def recipient(self):
        return self._recipient

    #Check if the recipient is valid before setting it
    #recipient can not be left blank(no length)
    @recipient.setter
    def recipient(self, new_recipient):
        if len(new_recipient) < 1:
            raise ValueError
        else:
            self._recipient = new_recipient


    @property
    def addressline(self):
        return self._addressline

    #Check if the address line is valid before setting it
    #address line can not be left blank(no length)
    @addressline.setter
    def addressline(self, newaddressline):
        if len(newaddressline) < 1:
            raise ValueError
        else:
            self._addressline = newaddressline


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


    #Building the address string and returns it
    def generateaddressstring(self):
        addressstring = ""

        addressstring += "Addressee: " + self.recipient + "\n"

        if(len(self.org) > 0):
            addressstring += "Organisation: " + self.org

        if(len(self.building_name) > 0):
            addressstring += "Building: " + self.buildingname + "\n"

        addressstring += "Address: " + self.addressline + "\n"

        if(len(self.locality) > 0):
            addressstring += "Locality: " + self.locality + "\n"

        addressstring += "City: " + self.city + "\n"

        addressstring += "Post Code: " + self.postcode + "\n"

        return addressstring

    def __str__(self):
        return self.generateaddressstring()