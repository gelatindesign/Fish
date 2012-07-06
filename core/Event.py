import Debug

###
# Event
# @desc Superclass for any events that might be generated
# 	by an object and sent to the EventManager
###
class Event( ):
	name = "Generic Event"
	def __init__( self, data=None ):
		self.data = data

class EventListener( ):
	pass

###
# Basic Events
###
class TickEvent( Event ):
	def __init__( self, event ):
		self.name = "Tick Event"

class AlertEvent( Event ):
	def __init__( self, event ):
		self.name = "Alert Event"
		Debug.log( event )

###
# EventManager
# @desc Responsible for coordinating most communication
# 	between the Model, View & Controller
###
class EventManager( ):

	def __init__( self ):
		self.listeners = []

	def registerListener( self, listener ):
		self.listeners.append( listener )

	def unregisterListener( self, listener ):
		pass

	def post( self, event ):
		if not isinstance( event, TickEvent ):
			Debug.log( "Event: " + event.name )

		# Event is broadcast to all listeners
		for listener in self.listeners:
			listener.notify( event )
