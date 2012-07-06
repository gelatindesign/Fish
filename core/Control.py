from Event import Event, EventListener
from Actor import ActorActionRequest
import Config

import Debug

###
# Controller
###
class Controller( EventListener ):
	pass

###
# KeyboardController
###
class KeyboardInputEvent( Event ):
	name = "Keyboard Input Event"

class KeyboardController( Controller ):
	def notify( self, event ):
		if isinstance( event, KeyboardInputEvent ):
			# Handle keyboard input
			# Check controllable actor's maps
			try:
				Debug.log( "Keyboard: %s" % event.data.unicode )
			except:
				Debug.log( "Keyboard: %s" % event.data.key )

###
# MouseController
###
class MouseInputEvent( Event ):
	name = "Mouse Input Event"

class MouseController( Controller ):
	def notify( self, event ):
		if isinstance( event, MouseInputEvent ):
			for actor in Config.game.players:
				Config.game.em.post( ActorActionRequest(actor) )
