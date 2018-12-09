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
"""

def runtime_exit_print():
    print("ARE YOU STUPID? I CAN'T WORK THERE")

self = os.getcwd()
home = "/folder"
root = self + home

def create_folder(path):
    path = root + path
    try:
        os.mkdir(path)
        print("created successfully")
        return 0
    except:
        try:
            os.makedirs(path)
            print("created successfully")
            return 0
        except:
            print("failed to create")
            return 1

def create_file(path, filename):
    path = root + path
    filename = path + filename
    create_folder(path)
    try:
        fout = open(filename, "w")
        fout.close()
        print("successfully created file")
        return 0
    except:
        print("failed to create the file")
        return 1

def delete_folder(path):
    path = root + path
    if not(os.path.isdir(path)):
        print("no such directory")
        return 1
    try:
        os.rmdir(path)
        print("deleted successfully")
        return 0
    except:
        try:
            shutil.rmtree(path)
            print("deleted successfully")
            return 0
        except:
            return 1

def init():
    if not(os.path.isdir(root)):
        try:
            os.mkdir(root)
            print("root folder initialized")
            return 0
        except:
            try:
                os.makedirs(root)
                print("root folder initialized")
                return 0
            except:
                print("failed to init")
                return 1
    return 1

def reinit():
    if os.path.isdir(root):
        delete_folder("")
    try:
        os.mkdir(root)
        print("root folder reinitialized")
        return 0
    except:
        try:
            os.makedirs(root)
            print("root folder reinitialized")
            return 0
        except:
            print("failed to reinit")
            return 1

def make_path(s):
    if s == "" or s[0] == '/':
        return s
    return "/" + s
        
        
#init просто создает рабочую директорию folder
#reinit ее удаляет и создает заново
    
    

    
    
            