import importlib.util
import pathos.multiprocessing as MP
import dill

try:
    import master as M
    import problems as P
    import folder_working as FW
except ImportError:
    from app.DB import master as M
    from app.DB import problems as P
    from app.DB import folder_working as FW

def get_prog_module(userID, taskID, submitID):
    #global prog
    path = "." + FW.home + M.own_dir + FW.make_path(userID) + FW.make_path(taskID) + FW.make_path(submitID) + ".py"
    #path = "./1.py"
    name = str(userID) + "_" + str(taskID) + "_" + str(submitID)
    #name = "testname"
    spec = importlib.util.spec_from_file_location(name, path)
    prog = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prog)
    return prog
    
def get_pool():
    pool = MP.Pool(processes = 1)
    return pool

def close_pool(pool):
    #pool.join()
    pool.close()

#prog = __import__("math")

def main(a, prog):
    return prog.main(*a)

def run_on_test(pool, prog, inputs, output):
    #try:
        #print(prog.main(*inputs))
        func = pool.apply_async(prog.main, args = inputs)
        #func = pool.map(prog.main, inputs)
        res = func.get()
        ans = []
        def add(lst, ans):
            #global ans
            for i in lst:
                if (type(i) == int):
                    ans.append(i)
                else:
                    add(i, ans) 
        add(res, ans)
        if ans == output:
            return "OK"
        return "WA"
    #except Exception:
        return "RE"
                  
def run(userID, taskID, submitID):
    try:
        #get_prog_module(userID, taskID, submitID)
        prog = get_prog_module(userID, taskID, submitID)
    except:
        M.add_verdict(userID, taskID, submitID, "CE")
        return
    pool = get_pool()
    try:
        for i in range(P.tests_num(taskID)):
            inputs = list(map(int, P.get_test_input(taskID, i).split()))
            output = list(map(int, P.get_test_output(taskID, i).split()))
            res = run_on_test(pool, prog, inputs, output)
            #print(res)
            M.add_verdict(userID, taskID, submitID, res)
    except ImportError:
        close_pool(pool)
        print("YES")
    finally:
        print("NO")
    close_pool(pool)
    
#print(run(0, 0, 9))
