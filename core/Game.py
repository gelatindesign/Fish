import pygame
from core.Event import Event
from core.Control import KeyboardController, MouseController, KeyboardInputEvent, MouseInputEvent

###
# Game
###
class Game( ):
	run = None
	config = []
	players = []
	
	def __init__( self, screen, em ):
		self.screen = screen
		self.run = True

		# Event Manager
		self.em = em

		# Register Control Listeners
		self.em.registerListener( KeyboardController(self) )
		self.em.registerListener( MouseController(self) )

	def tick( self ):
		for e in pygame.event.get( ):
			if e.type == pygame.QUIT:
				self.run = False
				return
			
			elif e.type == pygame.KEYDOWN or e.type == pygame.KEYUP:
				self.em.post( KeyboardInputEvent(e) )

			elif e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.MOUSEBUTTONUP or e.type == pygame.MOUSEMOTION:
				self.em.post( MouseInputEvent(e) )

	def addPlayer( self, player_name, actor_type, controls_file ):
		if len( self.players ) < self.config.max_players:
			#control_map = ControlMap( controls_file )
			#actor = actor_type( control_map )
			actor = ControllableActor( )
			self.players.append( [player_name, actor] )
			self.em.registerListener( ControlledActorListener() )
		else:
			EventHandler.post( AlertEvent(
				"You have already reached the maximum number of players"
			))
			return False
