from mypkg.power import power

class TestZero:
	def test_ten(self):
		assert power(0, 10, 1000) == 0
	
	def test_hundred(self):
		assert power(0, 100, 1000) == 0

