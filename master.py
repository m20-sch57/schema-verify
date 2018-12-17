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
    
def new_user(user):
    global submits, own_dir
    if user not in submits:
        submits[user] = dict()
        FW.create_folder(own_dir + FW.make_path(user))

def new_task(user, task):
    global submits, own_dir
    new_user(user)
    if task not in submits[user]:
        submits[user][task] = []
        FW.create_folder(own_dir + FW.make_path(user) + FW.make_path(task))

def new_submit(user, task, submit, text):
    global submits, own_dir
    new_task(task)
    