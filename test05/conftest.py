import os
import os.path
import sys
import pytest

sys.path.append(os.path.join(os.getcwd(), '.'))
sys.path.append(os.path.join(os.getcwd(), '..'))

def pytest_addoption(parser):
	parser.addoption('--poweroftwo', action='store', default=None,
		help='Exponent for power of two testing')

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


def pytest_configure(config):
	p2 = config.getvalue('poweroftwo')
	if p2 != None:
		config.p2 = int(p2)
	else:
		config.p2 = None

