import ConfigParser
import os

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        
        self.options['port'] = str(get_port())

        # If there is no ports.cfg file specified, create one in the current working dir.
        if not 'config' in self.options:
            filename = os.path.join(self.buildout['buildout']['directory'], 'ports.cfg')
            config = open(filename, 'w')
            config.write("[ports]\n")
            config.close()

        # Now use configparser to read in the ports
        cp = ConfigParser.RawConfigParser()
        cp.read(filename)

        # At this point we can check cp.items() for in-use ports,
        # so start assigning ports.
        
        
            

    def install(self):
        return tuple()

    def update(self):
        return tuple()
