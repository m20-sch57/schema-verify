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
"""

self = os.getcwd()
home = "/folder"
root = self + home
logs = root + "/log.txt"

def log(s):
    fout = open(logs, "a")
    print(s, file=fout)
    fout.close()

def write(path, filename, text):
    filename = root + path + filename
    if not(os.path.isfile):
        return 1
    try:
        fout = open(filename, "w")
        for i in text:
            print(i, file=fout)
        fout.close()
        return 0
    except:
        return 1

def add_write(path, filename, text):
    filename = root + path + filename
    if not(os.path.isfile):
        return 1
    try:
        fout = open(filename, "a")
        for i in text:
            print(i, file=fout)
        fout.close()
        return 0
    except:
        return 1

def get_text(path, filename):
    filename = root + path + filename
    ans = ""
    if os.path.isfile(filename):
        try:
            fin = open(filename, "r")
            for i in fin.readlines():
                ans += i
                ans += "\n"
            ans = ans[:-1]
            return ans
        except:
            return ""
    return ""

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
        
def delete_file(path):
    path = root + path
    if not(os.path.isfile(path)):
        log("no such file : " + path)
        return 1
    try:
        os.remove(path)
        log("deleted file successfully : " + path)
    except:
        log("failed to delete file : " + path)

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

def make_path(s):
    if s == "" or s[0] == '/':
        return s
    return "/" + s
        
        
#init просто создает рабочую директорию folder
#reinit ее удаляет и создает заново