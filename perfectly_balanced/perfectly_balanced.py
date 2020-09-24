# [2019-01-14] Challenge #372 [Easy] Perfectly balanced

# https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

# Given a string containing only the characters x and y, find whether there are the same number of xs and ys.

# balanced("xxxyyy") => true
# balanced("yyyxxx") => true
# balanced("xxxyyyy") => false
# balanced("yyxyxxyxxyyyyxxxyxyx") => true
# balanced("xyxxxxyyyxyxxyxxyy") => false
# balanced("") => true
# balanced("x") => false

def cap_text(text):
    return text.capitalize()


def balanced(xy_str):
	x_count = 0
	for letter in xy_str:
		if letter == 'x':
			x_count += 1
	if x_count == (len(xy_str) / 2):
		return True	
	else:
		return False