import eel
import calLogic as logic
#
eel.init('web')
#
#####   Move calculator logic to a separate file
#       All logic is performed in the sepearate
#       file, app.py is only an interface between
#       JS and Python

@eel.expose
def parseInput(args):
    result = logic.interpret(args)
    eel.postResult(result)

#
eel.start('index.html')
