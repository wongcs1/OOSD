__author__ = 'cwong_000'

class UsPhoneNumber():

    def __init__(self, areacode, prefix, number):
        self.areacode = areacode
        self.prefix = prefix
        self.number = number

    def displaynumber(self):
        print(self.areacode + "-" + self.prefix + "-" + self.number)


    @property
    def areacode(self):
        return self._area_code

    #Check if the area code is valid before setting it
    #area code must be 3 digits long
    @areacode.setter
    def areacode(self, newareacode):
        if len(newareacode) != 3:
            raise ValueError
        self._areacode = newareacode


    @property
    def prefix(self):
        return self._prefix

    #Check if the prefix is valid before setting it
    #prefix must be 3 digits long
    @prefix.setter
    def prefix(self, newprefix):
       if len(newprefix) != 3:
           raise ValueError
       self._prefix = newprefix


    @property
    def number(self):
        return self._number

    #Check if the prefix is valid before setting it
    #prefix must be 4 digits long
    @number.setter
    def number(self, newnumber):
        if len(newnumber) != 4:
            raise ValueError
        self._number = newnumber
