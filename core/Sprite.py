import pygame.sprite

import Debug

###
# Sprite
###
sprite_count = 0

class Sprite( pygame.sprite.Sprite ):
	
	def __init__( self ):
		global sprite_count

		super( Sprite, self ).__init__( )

		sprite_count += 1
		Debug.track( "Sprite Count", sprite_count )

###
# Animated Sprite
###
class AnimatedSprite( Sprite ):
	pass