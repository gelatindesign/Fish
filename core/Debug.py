from Text import Text
import Config

###
# Log
# @desc Used to print out a message to the terminal
###
def log( message ):
	if Config.show_debug_log:
		print message

###
# Track
# @desc Used for continuous messages in game
###
track_values = {}
track_text = Text( )
track_text.anti_alias = True
def track( key, message ):
	if Config.show_debug_track:
		track_values[key] = message

def renderTrack( ):
	if Config.show_debug_track:
		message = "".join( [m + ": " + `track_values[m]` for m in track_values] )
		track_text.render( Config.screen, [Config.screen_size[0]-200, 20], message )