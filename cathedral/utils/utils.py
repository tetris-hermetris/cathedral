def sgn(x):
	return ((x > 0) - (x < 0)) * 1

def normalize(poly_sequence):
	'''Returns flat sequence of polygons'''
	
	return poly_sequence


def declare(name, value):
	globals()[name] = value
	print('from utils', globals())