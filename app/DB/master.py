## -*- coding: utf-8 -*-
try:
    from app.DB import folder_working as FW
except:
    import folder_working as FW
    
#тут всякие глобальные переменные

#submits - map<string, map<string, vector<string> > > , где submits[user][task] - список имен посылок юзера user по задаче task 
#в пред строчке лажа - обязательно разобраться

submits = dict()
own_dir = "/.submits"
have_read = False
    
def read():
    global submits, own_dir
    submits = dict()
    #list of str
    ls = FW.getdirs(own_dir)
    for user in ls:
        submits[user] = dict()
    for user in ls:
        now = own_dir + FW.make_path(user)
        tasks = FW.getdirs(now)
        for task in tasks:
            submits[user][task] = []
            now2 = now + FW.make_path(task)
            if FW.is_folder(now2):
                for sub in FW.getdirs(now2):
                    submits[user][task].append(sub)
    
def set_password(user, password):
    global submits, own_dir
    if user_in_DB(user):
        path = own_dir + FW.make_path(user)
        FW.write_text(path, "/.password.txt", [password])

def new_user(user, password):
    global submits, own_dir
    if not(user_in_DB(user)):
        submits[user] = dict()
        path = own_dir + FW.make_path(user)
        FW.create_file(path, "/.password.txt")
        set_password(user, password)    

def get_password(user):
    global submits, own_dir
    if user in submits:
        path = own_dir + FW.make_path(user) + "/.password.txt"
        return "".join(FW.to_string(path))
    else:
        return ""

def new_task(user, task):
    global submits, own_dir
    if not(FW.is_folder(own_dir + FW.make_path(user))):
        return 1
    if not(FW.is_folder(own_dir + FW.make_path(user) + FW.make_path(task))):
        submits[user][task] = []
        FW.create_folder(own_dir + FW.make_path(user) + FW.make_path(task))
    return 0

def new_submit(user, task, text):
    global submits, own_dir
    new_task(user, task)
    path = own_dir + FW.make_path(user) + FW.make_path(task)
    num = len(FW.getdirs(path))
    name = FW.make_path(str(num))
    FW.create_file(path, name)
    FW.write_text(path, name, text)
    
def user_in_DB(user):
    global submits, own_dir, have_read
    if not(have_read):
        have_read = True
        read()    
    return user in submits