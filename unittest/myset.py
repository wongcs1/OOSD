__author__ = 'cwong_000'

class MySet:

    def __init__(self, items):

        self.set = []
        if items != None:
            for i in items:
                 self.additem(i)

    #Add item to set - if item is already present in set, nothing will happen
    def additem(self, item):
        if item not in set:
            set.append(item)

    #Remove item from set - if item is not present in set, nothing will happen
    def removeitem(self, item):

        if item in self.set:
            self.set.remove(item)

    #Check if set is empty
    def isempty(self):
        if len(self.set) < 1:
            return True
        else:
            return False

    #Check if the given item is present within set
    def hasitem(self, item):

        if item in self.items:
            return True
        else:
            return False

    #Returns a new set that is the intersection of self and otherset.
    def intersection(self, otherset):

        intersect = [x for x in otherset if x in self.items]

        return intersect


    #Returns a new set that is the union of self and otherset
    def union(self, otherset):

        output = MySet(None)

        for i in otherset:
            output.add_item(i)

        for i in self.set:
            output.add_item(i)

        return otherset


    #Returns True if self is a subset of otherset
    def issubsetof(self, otherset):

        output = True

        #check if the given set(otherset) has a smaller length than the set
        #set can't be a subset of otherset if it is larger than otherset
        if len(otherset) < len(self.set):
            output = False
        else:
            count = 0

            while count < len(self.set) and output is True:
                if self.set[count] not in otherset:
                    output = False

                count += 1

        return output

    #Check if otherset has same value as the set
    def is_equal_to(self, otherset):

        return self.items == otherset

