##### app.py | JS-PY Interface
#     Logic is handled in calLogic.py
#
import eel
import calLogic as logic
#
eel.init('web')
#

@eel.expose
def parse_input(args):
    print("> parsing input: ",args)
    result = logic.interpret(args)
    eel.post_result(result)

#
eel.start('index.html')
