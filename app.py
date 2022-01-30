##### app.py | JS-PY Interface
#     Logic is handled in calLogic.py
#
import eel
import calLogic as logic
#
eel.init('web')
#

@eel.expose
def parseInput(args):
    result = logic.interpret(args)
    eel.postResult(result)

#
eel.start('index.html')
