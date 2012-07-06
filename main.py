###
# Fish Game
# @author Gelatin Design
# @version dev.1
###

# Import Config
import core.Config

# Import External Libraries
# - NumPy > http://numpy.scipy.org/
# - PyGame > http://pygame.org
# - PyYAML > http://pyyaml.org
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
core.Config.game = Game( event_manager )

# Global Settings

core.Config.game.addPlayer( "Jeff", 0 )

# --- Main Game Loop --- #
while core.Config.game.run:
	core.Config.game.tick( )

# Exit
print "Application Terminated"
pygame.quit ( )
