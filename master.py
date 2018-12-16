import folder_working as FW

#тут всякие глобальные переменные

#submits - map<string, map<string, int> >, где submits[user][task] - число посылок юзера user по задаче task 

submits = dict()
own_dir = "/.submits"

def save():
    global submits, own_dir
    a = 0
    #сохранение
    
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
            now2 = now + FW.make_path(task)
            submits[user][task] = len(FW.getdirs(now2))
    
def new_user(user):
    if user not in submits:
        submits[user] = dict()
        