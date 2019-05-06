import importlib.util
import multiprocessing as MP

try:
    import master as M
    import problems as P
    import folder_working as FW
except ImportError:
    from app.DB import master as M
    from app.DB import problems as P
    from app.DB import folder_working as FW

def get_prog_module(userID, taskID, submitID):
    path = "." + FW.home + M.own_dir + FW.make_path(userID) + FW.make_path(taskID) + FW.make_path(submitID) + ".py"
    name = str(userID) + "_" + str(submitID)
    spec = importlib.util.spec_from_file_location(name, path)
    prog = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prog)
    return prog
    
def get_pool():
    pool = MP.Pool(processes = 1)
    return pool

def run_on_test(pool, prog, inputs, output):
    try:
        func = pool.apply_async(prog.main, args = inputs)
        res = func.get(timeout = 0.5)
        ans = []
        def add(lst):
            global ans
            for i in lst:
                if (type(i) == int):
                    ans.append(i)
                else:
                    add(i) 
        add(res)
        if ans == output:
            return "OK\n"
        return "WA\n"
    except Exception:
        return "CE\n"
                  
def run(userID, taskID, submitID):
    try:
        prog = get_prog_module(userID, taskID, submitID)
    except:
        M.add_verdict(userID, taskID, submitID, "CE")
        return
    pool = get_pool()
    for i in range(P.tests_num(taskID)):
        inputs = P.get_test_input(taskID, i)
        output = P.get_test_output(taskID, i)
        res = run_on_test(pool, prog, inputs, output)
        M.add_verdict(userID, taskID, submitID, res)
