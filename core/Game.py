import pygame
import Config

from Event import Event, AlertEvent
from Control import KeyboardController, MouseController, KeyboardInputEvent, MouseInputEvent
from Actor import ControlMap, Player, ControlledActorListener

import Debug

###
# Game
###
class Game( ):
	run = None
	em = None
	screen = None
	players = []
	
	def __init__( self, em ):
		self.run = True

		# Event Manager
		self.em = em

		# Register Control Listeners
		self.em.registerListener( KeyboardController() )
		self.em.registerListener( MouseController() )

	def tick( self ):
		for e in pygame.event.get( ):
			if e.type == pygame.QUIT:
				self.run = False
				return
			
			elif e.type == pygame.KEYDOWN or e.type == pygame.KEYUP:
				self.em.post( KeyboardInputEvent(e) )

			elif e.type == pygame.MOUSEBUTTONDOWN or e.type == pygame.MOUSEBUTTONUP or e.type == pygame.MOUSEMOTION:
				self.em.post( MouseInputEvent(e) )

		Config.screen.fill( (0,0,0) )

		Debug.renderTrack( )

		pygame.display.flip( )

	def addPlayer( self, player_name, controls_file ):
		if len( self.players ) < Config.max_players:
			#control_map = ControlMap( controls_file )
			#actor = actor_type( control_map )
			actor = Player( player_name, ControlMap("default") )
			self.players.append( [player_name, actor] )
			self.em.registerListener( ControlledActorListener() )
		else:
			self.em.post( AlertEvent(
				"You have already reached the maximum number of players"
			))
			return False
