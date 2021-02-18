import cal
import pytest

@pytest.mark.parametrize('input_1, input_2, result',
                        [(1, 2, 3),
                        (5.2, 2.4, 7.6),
                        ('winter', ' season', 'winter season')])

def test_add(input_1, input_2, result):
    assert cal.add(input_1, input_2) == result


'''
>>> pytest test_parametrized_addition.py -v

test_parametrized_addition.py::test_add[1-2-3] PASSED                    [ 33%]
test_parametrized_addition.py::test_add[5.2-2.4-7.6] PASSED              [ 66%]
test_parametrized_addition.py::test_add[winter- season-winter season] PASSED [100%]
'''