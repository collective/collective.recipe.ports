import ConfigParser
import os

BASE=8000

def ports():
    for port in range(BASE,BASE*2):
        yield port

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        self.options['port'] = str(None)

        # If there is no ports.cfg file specified, create one in the current working dir.
        if not 'config' in self.options:
            filename = os.path.join(self.buildout['buildout']['directory'], 'ports.cfg')
            # Don't overwrite if exists
            if 'ports.cfg' not in os.listdir(self.buildout['buildout']['directory']):
                self.options['config'] = filename
                config = open(filename, 'w')
                config.write("[ports]\n")
                config.close()
            self.options['config'] = filename

        # Now use configparser to read in the ports
        filename = self.options['config'] 
        cp = ConfigParser.RawConfigParser()
        cp.read(filename)

        # At this point we can check cp.items() for in-use ports
        # and start assigning ports.
        filename = self.options['config'] 
        port = ports()
        items = cp.items(self.name) 
        if items != []:
            while port.next() not in [i[1] for i in items]:
                config = open(filename, 'ab')
                config.write("%s = %s\n" % ("thing", str(port.next())))
                config.close()
                break
        else:
            config = open(filename, 'ab')
            config.write("%s = %s\n" % ("thing", str(port.next())))
            config.close()

    def install(self):
        return tuple()

    def update(self):
        return tuple()
