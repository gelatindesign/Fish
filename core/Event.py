from Debug import Debug

###
# Event
# @desc Superclass for any events that might be generated
# 	by an object and sent to the EventManager
###
class Event( ):
	def __init__( self ):
		self.name = "Generic Event"

class EventListener( ):
	pass

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
		#if not isInstance( event, TickEvent ):
		Debug( "Event: " + event.name )

		# Event is broadcast to all listeners
		for listener in self.listeners:
			listener.notify( event )
