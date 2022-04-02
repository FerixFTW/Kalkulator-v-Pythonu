##### app.py
# Main Python-JavaScript interface
# Intended to work in tandem with calLogic.py
#
import eel
import traceback
import calLogic as logic
import graphing as graph
from datetime import datetime
#
def log(args,exception):
    timestamp = datetime.now()
    with open("logfile.txt","a",encoding="utf-8") as logfile:
        logfile.write("------------------\n")
        logfile.write(str(timestamp)+"\n")
        logfile.write("-\n")
        logfile.write("args: "+str(args)+"\n")
        logfile.write("-\n")
        logfile.write(str(exception)+"\n")
        logfile.write("-\n")
        logfile.write(traceback.format_exc())
        logfile.write("------------------\n")
#
eel.init('web')
#
# TODO: Install from github page or curl or website
@eel.expose
def parse_input(args,ans):
    result = "err"
    try:
        result = logic.interpret(args,ans)
    except Exception as e:
        log(args,e)
    eel.append_history(args,result)
    eel.post_result(result)
#
@eel.expose
def parse_graph(args):
    try:
        graph.parse_y(args)
    except Exception as e:
        log(args,e)
#
eel.start('index.html')
#
