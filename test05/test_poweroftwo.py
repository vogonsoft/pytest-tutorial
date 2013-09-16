from mypkg.power import power
import pytest
import math

class TestPowerOfTwo:
	def test_p2_basic(self):
		if pytest.config.p2:
			print 'Testing for %d' % pytest.config.p2
			assert power(2, pytest.config.p2, 1000000) == \
				(math.pow(2, pytest.config.p2) % 1000000)

