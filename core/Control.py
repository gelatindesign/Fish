from Event import Event, EventListener
from Actor import ActorActionRequest

import Debug

###
# Controller
###
class Controller( EventListener ):
	def __init__( self, game ):
		self.game = game

###
# KeyboardController
###
class KeyboardInputEvent( Event ):
	def __init__( self, event ):
		self.name = "Keyboard Input Event"

class KeyboardController( Controller ):
	def notify( self, event ):
		if isinstance( event, KeyboardInputEvent ):
			# Handle keyboard input
			# Check controllable actor's maps
			pass

###
# MouseController
###
class MouseInputEvent( Event ):
	def __init__( self, event ):
		self.name = "Mouse Input Event - %s " % ( event.type, )

class MouseController( Controller ):
	def notify( self, event ):
		if isinstance( event, MouseInputEvent ):
			for actor in self.game.players:
				self.game.em.post( ActorActionRequest(actor) )
