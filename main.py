###
# Fish Game
# @author Gelatin Design
# @version dev.1
###

# Import Config
import core.Config

# Import External Libraries
import pygame

# Initialise External Objects
pygame.init( )
core.Config.screen = pygame.display.set_mode( core.Config.screen_size )


# Import Core Libraries
from core.Game import Game
from core.Event import EventManager
import core.Debug

# Initialise Core Objects

event_manager = EventManager( )
game = Game( event_manager )

# Global Settings

game.addPlayer( "TestPlayer", 0, 0 )
game.addPlayer( "Blah", 0, 0 )

# --- Main Game Loop --- #
while game.run:
	game.tick( )

# Exit
print "Application Terminated"
pygame.quit ( )
