import pytest

@pytest.mark.x
def test_type():
    assert type(1 + 2) is int

@pytest.mark.number
def test_add_int():
    assert 5 + 2 == 7
    
@pytest.mark.skip
def test_string():
    assert 'u' in 'sun'

@pytest.mark.string
def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'


'''
>>> pytest "test_multiple_simple (2).py" -v -m x
test_multiple_simple (2).py::test_type PASSED                            [100%]

>>> pytest "test_multiple_simple (2).py" -v -m number 
test_multiple_simple (2).py::test_add_int PASSED                         [100%]

>>> pytest "test_multiple_simple (2).py" -v -m string 
test_multiple_simple (2).py::test_string PASSED                          [ 50%]
test_multiple_simple (2).py::test_add_string PASSED                      [100%]

>>> pytest "test_multiple_simple (2).py" -v
test_multiple_simple (2).py::test_type PASSED                            [ 25%]
test_multiple_simple (2).py::test_add_int PASSED                         [ 50%]
test_multiple_simple (2).py::test_string SKIPPED                         [ 75%]
test_multiple_simple (2).py::test_add_string PASSED                      [100%]

'''