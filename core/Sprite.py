import pygame.sprite

import Config
import Debug

###
# Sprite
###
sprite_count = 0

def sliceSprite( src, x, y ):
	pass

class Sprite( pygame.sprite.Sprite ):
	visible = False
	pos = None
	angle = False
	zindex = 1
	
	def __init__( self ):
		super( Sprite, self ).__init__( )

		global sprite_count
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

	def __init__( self, src, zindex = 1 ):
		super( AnimatedSprite, self ).__init__( )
		
		self.images = []
		self.frames = 0
		self.states = {}
		#self.pos = pos
		self.zindex = zindex
		
		self.src_image = pygame.image.load( Config.sprite_path+src ).convert_alpha( )
		self.src_width, self.src_height = self.src_image.get_size( )
		
		self.inflate_amount = 0
		
		self._last_update = 0
		self._frame = 0
		self.state = ''
	
	def addAnimState( self, name, start, end, fps ):
		self.frames += (end - start + 1)
		self.states[ name ] = { 'start': start, 'end': end, 'delay': (1000 / fps) }


	def setAnimState( self, name ):
		if self.state != name:
			if len(self.images) == 0:
				self.frame_width = self.src_width / self.frames
				for i in range( self.frames ):
					self.images.append( self.src_image.subsurface(i * self.frame_width, 0, self.frame_width, self.src_height) )
				
				self.image = self.images[0]
				self.rect = self.image.get_rect( )
				
				#self.rect.inflate_ip( self.inflate_amount, self.inflate_amount )
				
				self.rect.x = self.pos[0]
				self.rect.y = self.pos[1]
			
			self.state = name
			self._frame = self.states[ name ]['start']
			self._last_update = 0

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