## -*- coding: utf-8 -*-

#comment to push 3

import importlib.util

try:
    import translate_schema as TS
    import master as M
    import problems as P
    import run_schema as RS
except ImportError:
    from app.DB import translate_schema as TS
    from app.DB import master as M
    from app.DB import problems as P
    from app.DB import run_schema as RS

def compile_module(user, task, submit):
    path = "." + FW.home + M.own_dir + FW.make_path(user) + FW.make_path(task) + FW.make_path(submit) + ".py"
    name = str(user) + '_' + str(task) + '_' + str(submit)
    spec = importlib.util.spec_from_file_location(name, path)
    prog = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prog)
    return prog

def lexical_check(user, task, submit):
    try:
        schema = FW.to_string(M.own_dir + FW.make_path(user) + FW.make_path(task) + FW.make_path(submit) + ".txt")
        res = TS.translate_all(schema)
        M.new_submit(user, task, res, ".py")
        compile_module(user, task, submit)
        M.add_verdict(user, task, submit, "Testing in progress")
        return "Testing in progress" #Accepted For Testing
    except:
        M.new_submit(user, task, "", ".py")
        M.add_verdict(user, task, submit, "CE")
        return "CE"
    
def test_check(user, task, submit):
    cnt = P.tests_num(task)
    sup = M.get_verdicts(user, task, submit)
    if len(sup):
        M.write_verdict(sup[0])
    for i in range(cnt):
        res = RS.run_schema(user, task, submit, i)
        M.add_verdict(user, task, submit, res)
    res = M.get_verdicts(user, task, submit)
    return current_verdict(user, task, submit)

def current_verdict(user, task, submit):
    res = M.get_verdicts(user, task, submit)
    if not(len(res)):
        return "N/D"
    if res[0] == "CE":
        return "CE"
    for i in range(1, len(res)):
        if res[i] != "OK":
            return res[i] + str(i)

if __name__ == "__main__":
    print(test_check(0, 0, 0))