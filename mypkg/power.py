#!/usr/bin/python

import sys

def power(p, q, m):
	'''power(p, q, m) -> p ^ q (mod m)
	'''
	r = 1
	while q > 0:
		if q % 2 == 1:
			r = (r * p) % m
		q = q / 2
		p = (p * p) % m
	return r

def main(argv):
	if len(argv) < 4:
		print '''power.py
Usage: python power.py <p> <q> <m>
Calculates p^q(mod m)
		'''
		sys.exit(0)
	print 'Number: %s' % argv[1]
	p = int(argv[1])
	q = int(argv[2])
	m = int(argv[3])
	r = power(p, q, m)
	print 'p^q(mod m) = %d' % r

if __name__ == '__main__':
	main(sys.argv)

