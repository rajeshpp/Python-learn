import pytest
import os

@pytest.fixture(scope='module')
def test_file():
	print('\nCreating file')
	f = open('test_file.txt','a+')
	yield f

	print('\nClosing file')
	f.close()


def test_write_ten_lines(test_file):

	print('\nWriting ten lines')
	num_lines_before = sum(1 for line in open(test_file.name))

	for i in range(10):
		test_file.write('X Y Z %d\n' % (i+1))

	test_file.flush()
	num_lines_after = sum(1 for line in open(test_file.name))

	assert (num_lines_after - num_lines_before) == 10


def test_file_size_on_write(test_file):

	print('\nWriting one line')
	size_before = os.stat(test_file.name).st_size
	
	test_file.write('A B C 1\n')
	test_file.flush()

	size_after = os.stat(test_file.name).st_size

	assert (size_after - size_before) > 0


'''
>>> pytest test_file_fixture_scope.py -v -s
test_file_fixture_scope.py::test_write_ten_lines
Creating file

Writing ten lines
PASSED
Closing file

test_file_fixture_scope.py::test_file_size_on_write
Creating file

Writing one line
PASSED
Closing file

======With (scope = 'module') for fixture above.
>>> pytest test_file_fixture_scope.py -v -s
test_file_fixture_scope.py::test_write_ten_lines
Creating file

Writing ten lines
PASSED
test_file_fixture_scope.py::test_file_size_on_write
Writing one line
PASSED
Closing file

'''