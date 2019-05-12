## -*- coding: utf-8 -*-

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

def lexical_check(user, task, schema):
    try:
        res = TS.translate_all(schema)
        M.new_submit(user, task, res, ".py")
        return "Testing in progress" #Accepted For Testing
    except:
        M.new_submit(user, task, "", ".py")
        return "CE"
    
def test_check(user, task, submit):
    cnt = P.tests_num(task)
    for i in range(cnt):
        res = RS.run_schema(user, task, submit, i)
        M.add_verdict(user, task, submit, res)
    res = M.get_verdicts(user, task, submit)
    for i in range(1, len(res)):
        if res[i] != "OK":
            return res[i] + str(i)
    return "OK"    

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
    print(current_verdict(0, 0, 0))