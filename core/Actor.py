from Object import MoveableObject
from Event import Event, EventListener

###
# Actor
###
class ActorActionRequest( Event ):
	def __init__( self, actor ):
		self.name = "ActorActionRequest"
		self.actor = actor

class Actor( MoveableObject ):
	controllable = False

	def __init__( self ):
		pass

###
# AiActor
###
class AiActor( Actor ):
	pass

###
# ControlledActor
###
class ControlMap( ):
	keyboard = None
	keyboard_map = None
	mouse = None
	mouse_map = None

	def __init__( self, file ):
		f = DataFileParser( file )
		if f.keyboard:
			self.keyboard = KeyboardController
			self.keyboard_map = f.keyboard
		
		if f.mouse:
			self.mouse = MouseController
			self.mouse_map = f.mouse

class ControlledActor( Actor ):
	name = None
	control_map = None

	def __init__( self, name, control_map ):
		self.name = name
		self.control_map = control_map

class ControlledActorListener( EventListener ):
	def notify( self, event ):
		if isinstance( event, ActorActionRequest):
			Debug( "ControlledActorListener" )