import os
import os.path
import sys
import pytest

sys.path.append(os.path.join(os.getcwd(), '.'))
sys.path.append(os.path.join(os.getcwd(), '..'))

class Mod:
	def __init__(self):
		self.modulus = 1024

@pytest.fixture()
def mod(request):
	m = Mod()
	def fin():
		print 'Finalizing mod'
	request.addfinalizer(fin)
	return m

