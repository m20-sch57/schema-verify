import folder_working as FW

#тут всякие глобальные переменные

#submits - map<string, map<string, int> > , где submits[user][task] - число посылок юзера user по задаче task 
#в пред строчке лажа - обязательно разобраться

submits = dict()
own_dir = "/.submits"

def save():
    global submits, own_dir
    for user in submits:
        FW.create_folder(own_dir + FW.make_path(user))
        for task in submits[user]:
            FW.create_folder(own_dir + FW.make_path(user) + FW.make_path(task))
            #создадим файлы
    
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
            #считаем файлы
    
def new_user(user):
    if user not in submits:
        submits[user] = dict()
        