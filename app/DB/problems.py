## -*- coding utf-8 -*-

import folder_working as FW

tasks = dict()
own_dir = "/.tasks"
tests_dir = "/tests"

def add_task(task):
    FW.create_folder(own_dir + FW.make_path(task))
    tests = own_dir + FW.make_path(task) + tests_dir
    FW.create_folder(tests)

def add_test(task, test, answer):
    path = own_dir + FW.make_path(task) + tests_dir
    num = len(FW.getdirs(path))
    name = str(num)
    FW.create_file(path, FW.make_path(name + ".txt"))
    FW.write_text(path, FW.make_path(name + ".txt"), test)
    FW.create_file(path, FW.make_path(name + ".ans"))
    FW.write_text(path, FW.make_path(name + ".ans"), answer)
    
def add_tests(task, tests, answer):
    for i in range(len(tests)):
        add_test(task, tests[i], answer[i])
        
def add_statements(task, text):
    path = own_dir + FW.make_path(task)
    FW.create_file(path, "/statements.txt")
    FW.write_text(path, "/statements.txt", text)
    
def get_statements(task):
    path = own_dir + FW.make_path(task) + "/statements.txt"
    answer = "".join(FW.to_string(path))
    return answer
        
def get_test_input(task, num):
    path = own_dir + FW.make_path(task) + tests_dir + "/" + str(num) + ".txt"
    return "".join(FW.to_string(path))
    
def get_test_output(task, num):
    path = own_dir + FW.make_path(task) + tests_dir + "/" + str(num) + ".ans"
    return "".join(FW.to_string(path))    
    
      