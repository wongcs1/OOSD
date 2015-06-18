__author__ = 'cwong_000'

class MyError(Exception):
#class MyError(IndexError):

    ERROR_MESSAGE = "This is my error!"

	def __init__(self, data):
		self.data = data

	def __str__(self):
		return self.ERROR_MESSAGE


# Raise MyError
def oops():
    raise MyError(" Value")


try:
    oops()
except IndexError:
    print "Index error!"
except MyError as e:
    print(e)
finally:
    pass