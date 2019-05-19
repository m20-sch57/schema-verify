## -*- coding: utf-8 -*-

try:
    import folder_working as FW
except ImportError:
    from app.DB import folder_working as FW


tasks = dict()
own_dir = "/tasks"
_name = "/.name.txt"
tests_dir = "/tests"
solve_dir = "/.solution.txt"

def get_name(ind):
    path = "/" + str(ind)
    return FW.read_str(own_dir + path + _name) 
    
def get_id_by_name(task):
    x = FW.getdirs(own_dir)
    for ind in x:
        cur = FW.read_str(own_dir + FW.make_path(ind) + _name)
        if cur == task:
            return int(ind)
    return -1
    
def add_solution(ind, text):
    path = own_dir + FW.make_path(ind)
    if not(FW.file_exists(path + solve_dir)):
        FW.create_file(path, solve_dir)
    FW.write_text(path, solve_dir, text)
    
def del_solution(ind):
    path = own_dir + FW.make_path(ind)
    if (FW.file_exists(path + solve_dir)):
        FW.delete_file(path, solve_dir)

def set_name(ind, name):
    path = "/" + str(ind)
    if get_id_by_name(name) != -1:
        return 1
    if not(task_exists(ind)):
        return 1
    FW.write_text(own_dir + path, _name, name)
    return 0

def task_exists(name):
    name = FW.make_path(name)
    return FW.folder_exists(own_dir + name)

def init_task(ind):
    name = FW.make_path(str(ind))
    FW.create_folder(own_dir + name + tests_dir)
    FW.create_file(own_dir + name, _name)
    FW.write_text(own_dir + name, _name, "untitled")
    FW.create_file(own_dir + name, "/statements.txt")

def add_task():
    x = FW.getdirs(own_dir)
    num = -1
    for i in x:
        num = max(num, int(i))
    num += 1
    name = FW.make_path(num)
    FW.create_folder(own_dir + name)
    init_task(num)
    return num

def add_task_by_name(name):
    ind = add_task()
    set_name(ind, name)

def add_test(task, test, answer):
    path = own_dir + FW.make_path(str(task)) + tests_dir
    num = len(FW.getdirs(path))
    name = str(num // 2)
    FW.create_file(path, FW.make_path(name + ".txt"))
    FW.write_text(path, FW.make_path(name + ".txt"), test)
    FW.create_file(path, FW.make_path(name + ".ans"))
    FW.write_text(path, FW.make_path(name + ".ans"), answer)
    
def add_tests(task, tests, answer):
    for i in range(len(tests)):
        add_test(task, tests[i], answer[i])
        
def add_statements(task, text):
    path = own_dir + FW.make_path(str(task))
    FW.write_text(path, "/statements.txt", text)
    
def get_statements(task):
    path = own_dir + FW.make_path(task) + "/statements.txt"
    answer = FW.to_string(path)
    for i in range(len(answer)):
        answer[i] = answer[i].strip()
    return answer
        
def get_test_input(task, num):
    path = own_dir + FW.make_path(task) + tests_dir + "/" + str(num) + ".txt"
    return "".join(FW.to_string(path))
    
def get_test_output(task, num):
    path = own_dir + FW.make_path(task) + tests_dir + "/" + str(num) + ".ans"
    return "".join(FW.to_string(path))    
    
def tests_num(task):
    return len(FW.getdirs(own_dir + FW.make_path(task) + tests_dir)) // 2

def tasks_list():
    return FW.getdirs(own_dir)

def init():
    FW.create_folder(own_dir)
