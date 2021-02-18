import pytest

def test_type():
    assert type(1 + 2) is int
    
def test_add_int():
    assert 5 + 2 == 7
    
@pytest.mark.skip(reason='Temporarily disabled')    
def test_string():
    assert 'u' in 'sun'
    
def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'


'''
>>> pytest "test_multiple_simple (3).py" -v
test_multiple_simple (3).py::test_type PASSED                            [ 25%]
test_multiple_simple (3).py::test_add_int PASSED                         [ 50%]
test_multiple_simple (3).py::test_string SKIPPED                         [ 75%]
test_multiple_simple (3).py::test_add_string PASSED                      [100%]

>>> pytest "test_multiple_simple (3).py" -v -rs
test_multiple_simple (3).py::test_type PASSED                            [ 25%]
test_multiple_simple (3).py::test_add_int PASSED                         [ 50%]
test_multiple_simple (3).py::test_string SKIPPED                         [ 75%]
test_multiple_simple (3).py::test_add_string PASSED                      [100%]
=========================== short test summary info ===========================
SKIP [1] test_multiple_simple (3).py:9: Temporarily disabled

'''