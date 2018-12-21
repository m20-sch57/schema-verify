import folder_working as FW

#тут всякие глобальные переменные

#submits - map<string, map<string, vector<string> > > , где submits[user][task] - список имен посылок юзера user по задаче task 
#в пред строчке лажа - обязательно разобраться

submits = dict()
own_dir = "/.submits"
    
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
            for sub in FW.getdirs(now2):
                submits[user][task].append(sub)
    
def set_passwrod(user, password):
    global submits, own_dir
    if user in submits:
        path = own_dir + FW.make_path(user)
        FW.write_text(path, "/.password.txt", password)

def new_user(user, password):
    global submits, own_dir
    if user not in submits:
        submits[user] = dict()
        path = own_dir + FW.make_path(user)
        FW.create_folder(path)
        FW.create_file(path, "/.password.txt")
        set_password(user, password)

def get_password(user):
    global submits, own_dir
    if user in submits:
        path = own_dir + FW.make_path(user)
        return FW.read_text(path + "/.passwrod.txt")[0]
    else:
        return ""


def new_task(user, task):
    global submits, own_dir
    if task not in submits[user]:
        submits[user][task] = []
        FW.create_folder(own_dir + FW.make_path(user) + FW.make_path(task))

def new_submit(user, task, submit, text):
    global submits, own_dir
