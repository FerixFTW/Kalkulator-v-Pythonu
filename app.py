##### app.py | JS-PY Interface
#     Logic is handled in calLogic.py
#
import eel
import calLogic as logic
import graphing as graph
#
eel.init('web')
#
# TODO: Figure out .exe packaging for python, send console stdout
#       to a logging file with dynamic dating.
#       As much functionality to reduce bullshit in disposition.
# TODO: Direct keyboard input
# TODO: Log file or at least exception output to a file
#       Exceptions are preferred as there is no need to output working code.
@eel.expose
def parse_input(args,ans):
    result = "err"
    logic.log(["----------------"])
    logic.log(["parsing input:",args])
    try:
        result = logic.interpret(args,ans)
    except Exception as e:
        logic.log([e])
    logic.log(["----------------"])
    eel.append_history(args,result)
    eel.post_result(result)
#
@eel.expose
def parse_graph(args):
    graph.parse_y(args)
#
eel.start('index.html')
