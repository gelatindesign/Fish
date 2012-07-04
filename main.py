###
# Fish Game
# @author Gelatin Design
# @version dev.1
###

# Import External Libraries
import pygame

# Initialise External Objects
pygame.init( )
pygame.display.set_mode( [1024, 768] )

# Import Core Libraries
from core.Game import Game
from core.Event import EventManager

# Initialise Core Objects
config = {}
config.screen = [1024, 768] 

event_manager = EventManager( )
game = Game( screen, event_manager )

# Global Settings

game.addPlayer( "TestPlayer", 0, 0 )

# --- Main Game Loop --- #
while game.run:
	game.tick( )

# Exit
print "Application Terminated"
pygame.quit ( )
