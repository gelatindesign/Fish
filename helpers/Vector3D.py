###
# Vector3D
# Helper for calculating and manipulating 3D vectors
###

UP = [-1, 0, 0]
RIGHT  = [0, -1, 0]
DOWN = [1, 0, 0]
LEFT  = [0, 1, 0]

def addVectors(v1, v2):
	vout = range(3)
	for i in range(3):
		vout[i] = v1[i] + v2[i]
	return vout

def subtractVectors(v1, v2):
	vout = range(3)
	for i in range(3):
		vout[i] = v1[i] - v2[i]
	return vout

def multiplyVectors(v1, v2):
	vout = range(3)
	for i in range(3):
		vout[i] = v1[i] * v2[i]
	return vout

def divideVectors(v1, v2):
	vout = range(3)
	for i in range(3):
		vout[i] = v1[i] / v2[i]
	return vout

