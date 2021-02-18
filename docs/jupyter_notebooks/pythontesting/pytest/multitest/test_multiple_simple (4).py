import pytest

def test_type():
    assert type(1 + 2) is int
    
def test_add_int():
    assert 5 + 2 == 9
    
@pytest.mark.skip(reason='Temporarily disabled')    
def test_string():
    assert 'u' in 'sun'
    
def test_add_string():
    assert ('sunny' + 'day') == 'sunnyday'


'''
>>> pytest "test_multiple_simple (4).py" -v -rsf

test_multiple_simple (4).py::test_type PASSED                            [ 25%]
test_multiple_simple (4).py::test_add_int FAILED                         [ 50%]
test_multiple_simple (4).py::test_string SKIPPED                         [ 75%]
test_multiple_simple (4).py::test_add_string PASSED                      [100%]

================================== FAILURES ===================================
________________________________ test_add_int _________________________________

    def test_add_int():
>       assert 5 + 2 == 9
E       assert (5 + 2) == 9

test_multiple_simple (4).py:7: AssertionError
=========================== short test summary info ===========================
SKIP [1] test_multiple_simple (4).py:9: Temporarily disabled
FAIL test_multiple_simple (4).py::test_add_int
================ 1 failed, 2 passed, 1 skipped in 0.34 seconds ================

'''