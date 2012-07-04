###
# Vector2D
# Helper for calculating and manipulating 2D vectors
###

UP = [-1, 0]
RIGHT  = [0, -1]
DOWN = [1, 0]
LEFT  = [0, 1]

def addVectors(v1, v2):
	vout = range(2)
	for i in range(2):
		vout[i] = v1[i] + v2[i]
	return vout

def subtractVectors(v1, v2):
	vout = range(2)
	for i in range(2):
		vout[i] = v1[i] - v2[i]
	return vout

def multiplyVectors(v1, v2):
	vout = range(2)
	for i in range(2):
		vout[i] = v1[i] * v2[i]
	return vout

def divideVectors(v1, v2):
	vout = range(2)
	for i in range(2):
		vout[i] = v1[i] / v2[i]
	return vout

