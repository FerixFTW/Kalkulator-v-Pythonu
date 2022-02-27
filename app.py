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
    print("----------------")
    print("> parsing input: ",args)
    result = logic.interpret(args)
    print("----------------")
    ## TODO: Call append_history
    eel.post_result(result)

#
eel.start('index.html')
