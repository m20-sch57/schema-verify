## -*- coding: utf-8 -*-

try:
    import folder_working as FW
    import problems as P
except ImportError:
    from app.DB import folder_working as FW
    from app.DB import problems as P   
    
#тут всякие глобальные переменные

own_dir = "/.submits"
_name = "/.name.txt"

def id_in_DB(ind):
    return FW.is_folder(own_dir + FW.make_path(ind))

def user_in_DB(user):   
    return get_id_by_name(user) != -1   

def init_user(ind):
    path = FW.make_path(str(ind))
    FW.create_folder(own_dir + path)
    FW.create_file(own_dir + path, "/.password.txt")
    FW.create_file(own_dir + path, _name)
    FW.write_text(own_dir + path, _name, "unnamed")
    
def set_password(user, password):
    if id_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.write_text(path, "/.password.txt", [password])

def set_name(ind, user):
    if id_in_DB(ind):
        if get_id_by_name(user) != -1:
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
    if get_id_by_name(user) != -1:
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

def make_admin(user):
    user = get_id_by_name(user)
    if id_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.create_file(path, "/.admin")
        
def is_admin(user):
    user = get_id_by_name(user)
    if not(id_in_DB(user)):
        return 0
    return FW.file_exists(own_dir + FW.make_path(user) + "/.admin")

def make_not_admin(user):
    user = get_id_by_name(user)
    if id_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.delete_file(path, "/.admin")    

def get_password(user):
    user = get_id_by_name(user)
    if id_in_DB(user):
        path = own_dir + FW.make_path(user) + "/.password.txt"
        return "".join(FW.to_string(path))
    else:
        return ""

def new_task(user, task):
    user = get_id_by_name(user)
    if not(FW.folder_exists(own_dir + FW.make_path(user))):
        return 1
    if not(FW.folder_exists(own_dir + FW.make_path(user) + FW.make_path(str(task)))):
        FW.create_folder(own_dir + FW.make_path(user) + FW.make_path(task))
    return 0

def new_submit(user, task, text):
    new_task(user, task)
    user = get_id_by_name(user)
    path = own_dir + FW.make_path(user) + FW.make_path(str(task))
    num = len(FW.getdirs(path))
    name = FW.make_path(str(num))
    FW.create_file(path, name)
    FW.write_text(path, name, text)

def init():
    FW.create_folder(own_dir)
    