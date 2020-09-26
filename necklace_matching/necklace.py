
# return true if two strings are a matching necklace
def same_necklace(a, b):
	concat_b = b + b
	return a in concat_b

