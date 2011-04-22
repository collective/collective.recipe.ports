import ConfigParser
import os

BASE = 8000


def ports():
    for port in range(BASE, BASE * 2):
        yield port


class Recipe(object):
    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

        # If there is no ports.cfg file specified, create one in the current
        # working dir.
        if not 'config' in self.options:
            filename = os.path.join(self.buildout['buildout']['directory'],
                'ports.cfg')

            # Don't overwrite if exists
            if 'ports.cfg' not in os.listdir(
                self.buildout['buildout']['directory']):
                self.options['config'] = filename
                config = open(filename, 'w')
                config.write("[ports]\n")
                config.close()

            self.options['config'] = filename

        # Use configparser to read in the ports
        filename = self.options['config']
        cp = ConfigParser.RawConfigParser()
        cp.read(filename)

        # Fire up the port generator
        port = ports()

        # This is nasty. Maybe we can get buildout to give us better info?
        # If the section does not exist, create it then assign a port.
        sections = []
        for section in self.buildout.keys():
            try:
                self.buildout[section]
                sections.append(section)
            except:
                # At this point we can check cp.items() for in-use ports
                # and start assigning ports.
                parameters = cp.items(self.name)
                if parameters != []:
                    values = [i[1] for i in parameters]
                    assign = str(port.next())
                    if assign not in values:
                        self.options[section] = str(assign)
                        config = open(filename, 'ab')
                        config.write("%s = %s\n" % (section, assign))
                        config.close()
                else:
                    assign = str(port.next())
                    self.options[section] = str(assign)
                    config = open(filename, 'ab')
                    config.write("%s = %s\n" % (section, assign))
                    config.close()

    def install(self):
        return tuple()

    def update(self):
        return tuple()
