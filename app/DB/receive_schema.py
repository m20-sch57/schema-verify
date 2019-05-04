## -*- coding utf-8 -*-

import translate_schema as TS
import master as M
import problems as P
import run_schema as RS

def lexical_check(user, task, schema):
    try:
        res = TS.get(schema)
        M.new_submit(user, task, res)
        return "AFT" #Accepted For Testing
    except:
        M.new_submit(user, task, "")
        return "CE"
    
def test_check(user, task, submit):
    cnt = P.tests_num(task)
    for i in range(cnt):
        RS.run_schema(user, task, submit, i)
    res = M.get_verdicts(user, task, submit)
    for i in range(len(res)):
        if res[i] != "OK":
            return res[i] + str(i)
    return "OK"    

print(test_check(0, 0, 0))