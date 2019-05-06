## -*- coding: utf-8 -*-

try:
    import translate_schema as TS
    import master as M
    import problems as P
    import run_schema as RS
    import launch_schema as LS
except ImportError:
    from app.DB import translate_schema as TS
    from app.DB import master as M
    from app.DB import problems as P
    from app.DB import run_schema as RS
    from app.DB import launch_schema as LS

def lexical_check(user, task, schema):
    try:
        res = TS.translate_all(schema)
        M.new_submit(user, task, res, ".py")
        return "Testing in progress" #Accepted For Testing
    except:
        M.new_submit(user, task, "", ".py")
        return "CE"
    
def test_check(user, task, submit):
    LS.run(user, task, submit)
    res = M.get_verdicts(user, task, submit)
    for i in range(len(res)):
        if res[i] != "OK":
            return res[i] + str(i)
    return "OK"    


#print(lexical_check(0, 0, ["scheme (in1 in2 main (out1)\n", "\t(in1 in2) and (out1)\n", "end\n"]))