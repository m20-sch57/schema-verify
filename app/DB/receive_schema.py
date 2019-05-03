## -*- coding utf-8 -*-

import translate_schema as TS
import master as M

def lexical_check(user, task, schema):
    try:
        res = TS.get(schema)
        M.new_submit(user, task, res)
        return "AFT" #Accepted For Testing
    M.new_submit(user, task, "")
    return "CE"
    
def test_check(user, task, schema):
    return "OK"    
