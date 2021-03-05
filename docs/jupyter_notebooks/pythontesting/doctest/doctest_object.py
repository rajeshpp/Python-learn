class MyOwnObject:
	def __init__(self, name, number):
		self.name = name
		self.number = number

def create_new_MyOwnObject(name, number):
	"""
	>>> create_new_MyOwnObject('First Object', 1) #doctest: +ELLIPSIS
	<doctest_object.MyOwnObject object at 0x...>
	"""
	return MyOwnObject(name, number)


'''
>>> python -m doctest doctest_object.py -v

Trying:
    create_new_MyOwnObject('First Object', 1) #doctest: +ELLIPSIS
Expecting:
    <doctest_object.MyOwnObject object at 0x...>
ok
3 items had no tests:
    doctest_object
    doctest_object.MyOwnObject
    doctest_object.MyOwnObject.__init__
1 items passed all tests:
   1 tests in doctest_object.create_new_MyOwnObject
1 tests in 4 items.
1 passed and 0 failed.
Test passed.

'''