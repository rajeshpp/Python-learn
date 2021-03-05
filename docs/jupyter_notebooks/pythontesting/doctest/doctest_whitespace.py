def print_items(items_list):
	"""
	>>> print_items(['Ecuador', 'Egypt', 'Estonia']) #doctest: +NORMALIZE_WHITESPACE
	<BLANKLINE>
	  Ecuador
	<BLANKLINE>
	 	Egypt
	<BLANKLINE>
	 Estonia
	"""
	for item in items_list:
		print('\n', item)



'''
>>> python -m doctest doctest_whitespace.py -v

Trying:
    print_items(['Ecuador', 'Egypt', 'Estonia']) #doctest: +NORMALIZE_WHITESPACE
Expecting:
    <BLANKLINE>
      Ecuador
    <BLANKLINE>
            Egypt
    <BLANKLINE>
     Estonia
ok
1 items had no tests:
    doctest_whitespace
1 items passed all tests:
   1 tests in doctest_whitespace.print_items
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

'''