import os
import subprocess as SP
import master as M
from subprocess import Popen as run


def run_schema(userID, taskID, submitID, testID):
    path = "app/static/.submits" + "/" + str(userID) + "/" + str(taskID) + "/" + str(submitID) + ".py"
    test = "app/static/.tasks" + "/" + str(taskID) + "/" + str(testID) + ".txt"
    process = run(["python3", "launch.py"], stdin=SP.PIPE, stdout=SP.PIPE)
    data = process.communicate(bytes("", "utf-8"))
    res = data[0].decode("utf-8")
    M.new_result(userID, taskID, submitID, testID)
    M.add_verdict(userID, taskID, submitID, res)
    process.kill()
 