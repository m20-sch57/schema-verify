import os
import subprocess as SP
import master as M
import problems as P
from subprocess import Popen as run


def run_schema(userID, taskID, submitID, testID):
    path = "app/static/submits" + "/" + str(userID) + "/" + str(taskID) + "/" + str(submitID)
    #test = "app/static/.tasks" + "/" + str(taskID) + "/" + str(testID) + ".txt"
    ans = "verdict"
    inp = P.get_test_input(taskID, testID)
    out = P.get_test_output(taskID, testID)    
    try:        
        process = run(["python3", "launch.py"], stdin=SP.PIPE, stdout=SP.PIPE)
        data = process.communicate(bytes(path + "\n" + inp, "utf-8"))
        process.kill()
        res = data[0].decode("utf-8")
        if res == out:
            ans = "OK"
        else:
            ans = "WA"
    except:
        ans = "CE"
    
    #M.new_result(userID, taskID, submitID, testID)
    M.add_verdict(userID, taskID, submitID, ans)
    
 