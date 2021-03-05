def divide(dividend, divisor):
	"""
	>>> divide(7, 2)
	3.5
	>>> divide(7, 0)
	Traceback (most recent call last):
	...
	ZeroDivisionError: division by zero
	"""
	return dividend / divisor



'''
>>> python -m doctest doctest_tb.py -v

Trying:
    divide(7, 2)
Expecting:
    3.5
ok
Trying:
    divide(7, 0)
Expecting:
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
ok
1 items had no tests:
    doctest_tb
1 items passed all tests:
   2 tests in doctest_tb.divide
2 tests in 2 items.
2 passed and 0 failed.
Test passed.



>>> 
'''