from helpers.Vector2D import *
from Sprite import Sprite, AnimatedSprite

###
# Object
###
class Object( ):
	sprite = None

	def __init__( self ):
		pass

###
# PhysicalObject
###
class PhysicalObject( Object ):
	location = None

	def __init__( self, location ):
		self.location = location

###
# MoveableObject
###
class MoveableObject( PhysicalObject ):
	cur_speed = None
	max_speed = None
	direction = None
	
	def move( self, vector ):
		self.location = Vector2D.addVectors( self.location, vector )
