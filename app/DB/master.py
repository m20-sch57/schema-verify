## -*- coding: utf-8 -*-

try:
    import folder_working as FW
    import problems as P
except ImportError:
    from app.DB import folder_working as FW
    from app.DB import problems as P   
    
#тут всякие глобальные переменные

own_dir = "/submits"
res_dir = "/results"
_name = "/.name.txt"

def new_num(user, task):
    path = own_dir + FW.make_path(user) + FW.make_path(task)
    cnt = 0
    mx = 0
    for i in FW.getdirs(path):
        x = i.split(".")
        try:
            now = int(x[0])
        except Exception:
            now = -1
        if (now > mx):
            cnt = 1
            mx = now
        elif now == mx:
            cnt += 1
    if cnt > 1:
        return mx + 1
    return mx

def id_in_DB(ind):
    return FW.is_folder(own_dir + FW.make_path(ind))

def user_in_DB(user):   
    return get_id(user) != -1   

def init_user(ind):
    path = FW.make_path(str(ind))
    FW.create_folder(own_dir + path)
    FW.create_folder(res_dir + path)
    FW.create_file(own_dir + path, "/.password.txt")
    FW.create_file(own_dir + path, _name)
    FW.write_text(own_dir + path, _name, "unnamed")
    
def set_password(user, password):
    if id_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.write_text(path, "/.password.txt", [password])

def set_name(ind, user):
    if id_in_DB(ind):
        if get_id(user) != -1:
            return 1
        path = own_dir + FW.make_path(ind)
        FW.write_text(path, _name, [user])
        return 0
    return 1

def new_user():
    x = FW.getdirs(own_dir)
    num = -1
    for i in x:
        num = max(num, int(i))
    num += 1
    init_user(num)
    return num
    
def new_user_by_name(user, password):
    if get_id(user) != -1:
        return 1
    x = new_user()
    set_name(x, user)
    set_password(x, password)
    return 0
           
def get_id_by_name(name):
    x = FW.getdirs(own_dir)
    for c in x:
        now = FW.read_str(own_dir + FW.make_path(c) + _name)
        if now == name:
            return int(c)
    return -1    

def get_id(smth):
    if (type(smth) == int):
        return smth
    return get_id_by_name(smth)

def make_admin(user):
    user = get_id(user)
    if id_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.create_file(path, "/.admin")
        
def is_admin(user):
    user = get_id(user)
    if not(id_in_DB(user)):
        return 0
    return FW.file_exists(own_dir + FW.make_path(user) + "/.admin")

def make_not_admin(user):
    user = get_id(user)
    if id_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.delete_file(path, "/.admin")    

def get_password(user):
    user = get_id(user)
    if id_in_DB(user):
        path = own_dir + FW.make_path(user) + "/.password.txt"
        return "".join(FW.to_string(path))
    else:
        return ""

def new_task(user, task):
    user = get_id(user)
    if not(FW.folder_exists(own_dir + FW.make_path(user))):
        return 1
    if not(FW.folder_exists(own_dir + FW.make_path(user) + FW.make_path(str(task)))):
        FW.create_folder(own_dir + FW.make_path(user) + FW.make_path(task))
    if not(FW.folder_exists(res_dir + FW.make_path(user) + FW.make_path(str(task)))):
        FW.create_folder(res_dir + FW.make_path(user) + FW.make_path(task))
    
    return 0

def new_submit(user, task, text, submit_type):
    new_task(user, task)
    user = get_id(user)
    path = own_dir + FW.make_path(user) + FW.make_path(get_id(task))
    path2 = res_dir + FW.make_path(user) + FW.make_path(get_id(task))
    num = new_num(user, task)
    name = FW.make_path(str(num) + submit_type)
    add_result(user, task, num)
    FW.create_file(path, name)
    FW.write_text(path, name, text)

def add_result(user, task, submit):
    if not(id_in_DB(get_id(user))):
        return 1
    path = res_dir + FW.make_path(user) + FW.make_path(task)
    if not(FW.folder_exists(path)):
        new_task(user, task)
    x = FW.getdirs(path)
    now = submit
    FW.create_file(path, FW.make_path(now))

def write_verdict(user, task, ind, text):
    path = res_dir + FW.make_path(user) + FW.make_path(task)
    if FW.file_exists(path + FW.make_path(ind)):
        FW.write_text(path, FW.make_path(ind), text)

def add_verdict(user, task, ind, text):
    path = res_dir + FW.make_path(user) + FW.make_path(task)
    if FW.file_exists(path + FW.make_path(ind)):
        FW.add_text(path, FW.make_path(ind), text + "\n")    

def get_verdicts(user, task, ind):
    path = res_dir + FW.make_path(user) + FW.make_path(task) + FW.make_path(ind)
    res = FW.to_string(path)
    ans = []
    for i in res:
        now = i.strip()
        if now:
            ans.append(now)
    return ans

def verdicts_list(user, task):
    user = get_id(user)
    path = res_dir + FW.make_path(user) + FW.make_path(task)
    ans = list(map(int, FW.getdirs(path)))
    return ans
    
def init():
    FW.create_folder(own_dir)
    FW.create_folder(res_dir)

#print(verdicts_list(0, 0))
#new_submit(0, 0, ["scheme (in1 in2 main (out1)\n", "\tin1 in2 and out1\n", "end\n"], ".txt")