import pygame.sprite

import Debug

###
# Sprite
###
sprite_count = 0

def sliceSprite( src, x, y ):
	pass

class Sprite( pygame.sprite.Sprite ):
	angle = False
	
	def __init__( self ):
		global sprite_count

		super( Sprite, self ).__init__( )

		sprite_count += 1
		Debug.track( "Sprite Count", sprite_count )

	def update( self, ticks ):
		# Update rect pos to sprite pos
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]

###
# Animated Sprite
###
class AnimatedSprite( Sprite ):
	
	def addAnimState( self, name, start, end, fps ):
		pass

	def setAnimState( self, name ):
		pass

	def update( self, ticks ):
		state = self.states[ self.state ]
		
		# Update rect pos to sprite pos
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]
		
		# If there have been enough ticks since the last update
		if ticks - self._last_update > state['delay']:
			# Increase frame
			self._frame += 1
			
			# Check frame is valid
			if self._frame < state['start']: self._frame = state['start']
			if self._frame > state['end']: self._frame = state['start']
			
			# Set image to 
			self.image = self.images[ self._frame ]
			self._last_update = ticks
			
			if self.angle != False:
				self.image = pygame.transform.rotate( self.image, self.angle )