from mypkg.power import power
import pytest

def test_basic():
	assert power(2, 3, 1000) == 9

def test_second():
	assert power(5, 0, 10) == 1

def test_exception():
	with pytest.raises(Exception):
		res = power(0, 0, 2)

