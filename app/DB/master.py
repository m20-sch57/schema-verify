## -*- coding: utf-8 -*-

try:
    from app.DB import folder_working as FW
except:
    import folder_working as FW
    
#тут всякие глобальные переменные

own_dir = "/.submits"
    
def set_password(user, password):
    if user_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.write_text(path, "/.password.txt", [password])

def new_user(user, password):
    if not(user_in_DB(user)):
        path = own_dir + FW.make_path(user)
        FW.create_file(path, "/.password.txt")
        set_password(user, password)    

def make_admin(user):
    if user_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.create_file(path, "/.admin")
        
def is_admin(user):
    if not(user_in_DB(user)):
        return 0
    return FW.file_exists(own_dir + FW.make_path(user) + "/.admin")

def make_not_admin(user):
    if user_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.delete_file(path, "/.admin")    

def get_password(user):
    if user_in_DB(user):
        path = own_dir + FW.make_path(user) + "/.password.txt"
        return "".join(FW.to_string(path))
    else:
        return ""

def new_task(user, task):
    if not(FW.is_folder(own_dir + FW.make_path(user))):
        return 1
    if not(FW.is_folder(own_dir + FW.make_path(user) + FW.make_path(task))):
        submits[user][task] = []
        FW.create_folder(own_dir + FW.make_path(user) + FW.make_path(task))
    return 0

def new_submit(user, task, text):
    new_task(user, task)
    path = own_dir + FW.make_path(user) + FW.make_path(task)
    num = len(FW.getdirs(path))
    name = FW.make_path(str(num))
    FW.create_file(path, name)
    FW.write_text(path, name, text)
    
def user_in_DB(user):   
    return FW.is_folder(own_dir + FW.make_path(user))

def init():
    FW.make_fodler(own_dir)