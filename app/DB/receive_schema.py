## -*- coding: utf-8 -*-

import translate_schema as TS
import master as M
import problems as P
import run_schema as RS

def lexical_check(user, task, schema):
    try:
        res = TS.translate_all(schema)
        M.new_submit(user, task, res, ".py")
        return "AFT" #Accepted For Testing
    except:
        M.new_submit(user, task, "", ".py")
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


#print(lexical_check(0, 0, ["scheme () main (out1)", "\tout1=1", "end"]))