import ConfigParser
import os

default = """[ports]
instance1 = 8080
zeo = 8100
"""

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):

        # If there is no ports.cfg file specified, create one in the current working dir.

        if not 'config' in self.options:
            filename = os.path.join(self.buildout['buildout']['directory'], 'ports.cfg')
            config = open(filename, 'w')
            config.write(default)
            config.close()

        # Now use configparser to read in the ports
        return tuple()

    def update(self):
        return tuple()
