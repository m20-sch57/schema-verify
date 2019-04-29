import os
import subprocess as SP
from subprocess import Popen as run


def run_schema(userID, taskID, submitID, testID):
    path = ".folder/.submits" + "/" + str(userID) + "/" + str(taskID) + "/" + str(submitID)
    test = ".folder/.tasks" + "/" + str(taskID) + "/"

#x = os.system("python3")
process = run(["python3", "launch.py"], stdin=SP.PIPE, stdout=SP.PIPE)
data = process.communicate(bytes("sample\n1 0", "utf-8"))
res = data[0].decode("utf-8")
print(res)
process.kill()   