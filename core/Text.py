import pygame.font

###
# Text
###
class Text( ):
	font = None
	text = ""
	anti_alias = False
	color = (255,255,255)
	surface = None
	dirty = False

	def __init__( self, size=12, fonts="Helvetica, Arial, sans-serif" ):
		# Initialise the pygame font library, will only run once
		pygame.font.init( )

		# Load font family
		fontfamily = pygame.font.match_font( fonts )

		# Create font
		self.font = pygame.font.Font( fontfamily, size )

	def render( self, on_surface, pos, text=None ):
		# Default text to previously stored value
		if text == None:
			text = self.text

		if text != self.text:
			self.dirty = True

		# Check text is dirty (has changed) before creating surface
		if self.dirty:
			# Render text to a surface
			self.surface = self.font.render( unicode(text), self.anti_alias, self.color )
			self.rect = self.surface.get_rect( )

			# Position rect
			self.rect.left = pos[0]
			self.rect.top = pos[1]

		# Blit text to 'on_surface'
		on_surface.blit( self.surface, self.rect )

		# Set text to not dirty
		self.dirty = False