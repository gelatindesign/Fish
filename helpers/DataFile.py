import yaml

import core.Debug

###
# loadYAML
###
def loadYAML( src ):
	data = False

	try:
		fp = open( src, 'r' )
	except:
		core.Debug.track( "error", "Could not open file, '%s'" % src )
		return False

	try:
		data = yaml.load( fp )
	except:
		core.Debug.track( "error", "Data file invalid YAML, '%s'" % src )

	return data