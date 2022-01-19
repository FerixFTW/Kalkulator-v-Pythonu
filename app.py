import eel
import random
from datetime import datetime
#
eel.init('web')
#

@eel.expose
def parseInput(args):
    print(args)
    print(type(args))


#
eel.start('index.html')
