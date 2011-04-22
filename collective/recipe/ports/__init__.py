import ConfigParser
import os
import sys

BASE=8000

def ports():
    for port in range(BASE,BASE*2):
        yield port

class Recipe(object):
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        port = ports()

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

        # This is nasty. Maybe we can get buildout to give us better info?
        # If the section does not exist, create it then assign a port. 
        sections = []
        for section in self.buildout.keys():
            try:
                self.buildout[section]
                sections.append(section)
            except:
                assign = port.next()
                self.options[section] = str(assign)
                config = open(filename, 'ab')
                config.write("%s = %s\n" % (section, assign))
                config.close()

        # Now use ConfigParser to read in the ports
#        filename = self.options['config'] 
#        cp = ConfigParser.RawConfigParser()
#        cp.read(filename)

        # At this point we can check cp.items() for in-use ports
        # and start assigning ports.
#        filename = self.options['config'] 
#        port = ports()
#        items = cp.items(self.name) 
#
#        if items != []:
#            exists = [i[1] for i in items]
#            for next in exists:
#                if port.next() != next:
#                    config = open(filename, 'ab')
#                    assign = str(port.next())
#                    config.write("%s%s = %s\n" % ("thing", assign, assign))
#                    config.close()
#                    break
#        else:
#            config = open(filename, 'ab')
#            assign = str(port.next())
#            config.write("%s%s = %s\n" % ("thing", assign, assign))
#            config.close()

    def install(self):
        return tuple()

    def update(self):
        return tuple()
