## -*- coding: utf-8 -*-

import importlib.util

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

def compile_module(user, task, submit):
    path = "." + FW.home + M.own_dir + FW.make_path(user) + FW.make_path(task) + FW.make_path(submit) + ".py"
    name = str(user) + '_' + str(task) + '_' + str(submit)
    spec = importlib.util.get_spec_from_file_location(name, path)
    prog = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prog)
    return prog

def lexical_check(user, task, submit):
    try:
        schema = FW.to_string(M.own_dir + FW.make_path(user) + FW.make_path(task) + FW.make_path(submit) + ".txt")
        res = TS.translate_all(schema)
        M.new_submit(user, task, res, ".py")
        compile_module(user, task, submit)
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