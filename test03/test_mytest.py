from mypkg.power import power

def test_mod(mod):
	assert power(2, 4, 10000) == 16
	assert power(2, 10, mod.modulus) == 0

