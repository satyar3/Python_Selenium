import pytest


# Similar to testng data provider
@pytest.mark.parametrize("input_val , result", [(1, 11), (2, 22), (3, 34)])
def test_Params(input_val, result):
    assert input_val * 11 == result
