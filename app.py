##### app.py | JS-PY Interface
#     Logic is handled in calLogic.py
#
import eel
import calLogic as logic
#
eel.init('web')
#
# TODO: Figure out .exe packaging for python, send console stdout
#       to a logging file with dynamic dating.
#       As much functionality to reduce bullshit in disposition.
# TODO: Finalise base calculator functionality before tackling
#       graphing calculator.
@eel.expose
def parse_input(args,ans):
    result = "err"
    logic.log(["----------------"])
    logic.log(["parsing input:",args])
    try:
        result = logic.interpret(args,ans)
    except Exception as e:
        logic.log(e)
    logic.log(["----------------"])
    eel.append_history(args,result)
    eel.post_result(result)

#
eel.start('index.html')
