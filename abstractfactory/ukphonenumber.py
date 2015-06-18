__author__ = 'cwong_000'

class UkPhoneNumber():

    def __init__(self, areacode, prefix, number):
        self.areacode = areacode
        self.prefix = prefix
        self.number = number

    #display the phone number
    def displaynumber(self):
        if len(self.prefix) == 0:
            print("(" + self.areacode + ") " + self.number)
        else:
            print("(" + self.areacode + ") " + self.prefix + " " + self.number)

    @property
    def areacode(self):
        return self._areacode

    #Check if the area code is valid before setting it
    #area code must be between 3 to 6 digits long
    @areacode.setter
    def areacode(self, newareacode):
        if len(newareacode) < 3 or len(newareacode) > 6:
            raise ValueError
        else:
        self._areacode = newareacode

    @property
    def prefix(self):
        return self._prefix

    #Check if the prefix is valid before setting it
    #prefix must be between 3 or 4 digits long
    @prefix.setter
    def prefix(self, newprefix):
       if (len(newprefix) < 3 or len(newprefix) > 4):
            raise ValueError
       else:
        self._prefix = newprefix

    @property
    def number(self):
        return self._number

    #Check if the number is valid before setting it
    @number.setter
    def number(self, newnumber):
        #calculate the possible max and min length for the number with its areacode and prefix in place
        #areacode, prefix and number together must not exceed 11 numbers in total
        minlength = 10 - (len(self.areacode) + len(self.prefix))
        maxlength = self.minlength + 1

        if len(newnumber) < minlength or len(newnumber) > maxlength:
            raise ValueError
        else:
            self._number = newnumber
