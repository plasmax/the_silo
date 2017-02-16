import os
import re
import sys
import platform

try:
    os.environ['DOCS_CONTEXT']
except:
    if platform.system() == 'Darwin':
        application = r'Nuke\d+\.\d+v\d+.app'
    elif platform.system() == 'Windows':
        application = r'Nuke\d+\.\d+.exe'
    else:
        raise RuntimeError('OS {0} is not supported'.format(platform.system()))

    match = re.search(application, sys.executable)
    if not match:
        raise RuntimeError('Import nukecontexts from within Nuke')

__version__ = '0.1.0'
__all__ = []

import nuke
import json

silo_location = os.path.dirname(os.path.abspath(__file__))

nuke.pluginAddPath('{0}/gizmos'.format(silo_location))

MENU_NAME = 'The Silo'
silo_menu = nuke.menu('Nuke').addMenu(MENU_NAME)

with open('{0}/silo_data.json'.format(silo_location), 'r') as fp:
    silo_data = json.load(fp)

for gizmo_name, gizmo in silo_data['gizmos']:
    silo_menu.addCommand('Gizmos/{0}'.format(gizmo_name),
                         'nuke.nodes.{0}()'.format(gizmo))

for script_name, script in silo_data['scripts']:
    silo_menu.addCommand('Scripts/{0}'.format(script_name), str(script))

silo_menu.addSeparator()
silo_menu.addCommand('Version', 'nuke.message("The Silo version {0}")'.format(__version__))
silo_menu.addCommand('Contribute', 'import webbrowser;webbrowser.open(\'https://github.com/florianeinfalt/the_silo\')')
