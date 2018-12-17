import os
import shutil

"""
os.mkdir(path) - сделать одну папку
os.makedirs(path) - сдедать одну папку, сделав весь путь к ней
os.rmdir(path) - удалить папку
shutil.rmtree(path) - удалить дерево
os.path.isfile(path) - проверка наличия файла
os.path.isdir(path) - проверка наличия папки
os.getcwd() - путь к программе(сама программа в него не входит)
os.remove(path) - удалить файл
os.listdir(path) -посмотреть какие файлы тут есть
"""

def runtime_exit_print():
    print("RUNTIME_ERROR")

self = os.getcwd()
home = "/.folder"
root = self + home
logs = root + "/.log.txt"

def make_path(s):
    if s == "" or s[0] == '/':
        return s
    return "/" + s

def log(s):
    fout = open(logs, "a")
    print(s, file=fout)
    fout.close()

def write_text(path, filename, text):
    filename = root + path + filename
    fout = open(filename, "w")
    for i in text:
        print(i, file = fout, end="")
    fout.close()
    log("written some text in '" + filename + "'")

def getdirs(path):
    path = root + path
    return os.listdir(path)

def create_folder(path):
    path = root + path
    if os.path.isdir(path):
        log("folder already exists : " + path)
        return 0
    try:
        os.mkdir(path)
        log("created folder successfully : " + path)
        return 0
    except:
        try:
            os.makedirs(path)
            log("created folder successfully : " + path)
            return 0
        except:
            log("failed to create folder : " + path)
            return 1

def create_file(path, filename):
    filename = root + path + filename
    create_folder(path)
    try:
        fout = open(filename, "w")
        fout.close()
        log("successfully created file : " + filename)
        return 0
    except:
        log("failed to create the file : " + filename)
        return 1

def delete_folder(path):
    path = root + path
    if not(os.path.isdir(path)):
        log("no such folder : " + path)
        return 1
    try:
        os.rmdir(path)
        log("deleted folder successfully : " + path)
        return 0
    except:
        try:
            shutil.rmtree(path)
            log("deleted folder successfully : " + path)
            return 0
        except:
            log("failed to delete folder : " + path)
            return 1
        
def delete_file(path, filename):
    path = root + path + filename
    if not(os.path.isfile(path)):
        log("no such file : " + path)
        return 1
    try:
        os.remove(path)
        log("deleted file successfully : " + path)
    except:
        log("failed to delete file : " + path)

def read_text(filename):
    #list of str
    answer = []
    fin = open(root + filename, "r")
    answer = fin.readlines()
    fin.close()
    return answer

def init():
    if not(os.path.isdir(root)):
        try:
            os.mkdir(root)
            fout = open(logs, "w")
            print("root folder initialized", file=fout)
            fout.close()
            return 0
        except:
            try:
                os.makedirs(root)
                fout = open(logs, "w")
                print("root folder initialized", file=fout)
                fout.close()
                return 0
            except:
                print("failed to init")
                return 1
    return 1

def reinit():
    if os.path.isdir(root):
        try:
            os.rmdir(root)
        except:
            try:
                shutil.rmtree(root)
            except:
                return 1
    return init()

def folder_exists(path):
    return os.path.isdir(path)

"""def add_user(user):
    
    #Помимо создания папки надо добавлять юзера куда-то
    
    path = make_path(user)
    create_folder(path)

def add_user_task(user, task):
    
    #помимо создания папки надо добавлять этому юзеру задачу
    
    path = make_path(user) + make_path(task)
    create_folder(path)
    
def add_submit(user, task, submit):
    
    #надо добавить юзеру посылку по этой задаче
    
    path = make_path(user) + make_path(task)
    submit = str(submit)
    filename = make_path(submit)
    create_file(path, filename)
    
def write_submit(user, task, submit, text):
    submit = str(submit)
    add_submit(user, task, submit)
    path = make_path(user) + make_path(task)
    filename = make_path(submit)
    write_text(path, filename, text)
    
#последние 2 ф-ции выглядят странно, но я хотел иметь возможность как просто создать файл так и записать код юзера
    
def delete_user(user):
    path = make_path(user)
    remove_folder(path)"""
    
        
#init просто создает рабочую директорию folder
#reinit ее удаляет и создает заново