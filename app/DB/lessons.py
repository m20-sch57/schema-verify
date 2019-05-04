## -*- coding utf-8 -*-

try:
    import folder_working as FW
    import problems as P
except ImportError:
    from app.DB import folder_working as FW
    from app.DB import problems as P

own_dir = "/lessons"
_name = "/.name.txt"
_tasks = "/.tasks.txt"

def new_lesson():
    x = FW.getdirs(own_dir)
    num = -1
    for i in x:
        num = max(num, int(i))
    num += 1
    path = own_dir + FW.make_path(num)
    FW.create_folder(path)
    FW.create_file(path, _name)
    FW.create_file(path, _tasks)
    return num

def get_name(ind):
    path = "/" + str(ind)
    return FW.read_str(own_dir + path + _name) 

def get_id_by_name(lesson):
    x = FW.getdirs(own_dir)
    for ind in x:
        cur = FW.read_str(own_dir + FW.make_path(ind) + _name)
        if cur == lesson:
            return int(ind)
    return -1

def lesson_exists(ind):
    return FW.folder_exists(own_dir + FW.make_path(ind))

def set_name(ind, name):
    if get_id_by_name(name) != -1 or not(lesson_exists(ind)):
        return 1
    FW.write_text(own_dir + FW.make_path(ind), _name, name)
    return 0

def lessons_list():
    lst = list(map(int, FW.getdirs(own_dir)))
    lst.sort()
    return lst

def add_lesson(name):
    if (get_id_by_name(name) != -1):
        return
    x = new_lesson()
    set_name(x, name)
    
    
def add_task(lesson_name, task_name):
    lesson_name = FW.make_path(lesson_name)
    if lesson_exists(lesson_name) and P.task_exists(task_name):
        FW.add_text(own_dir + lesson_name, _tasks, [str(task_name) + "\n"])

def tasks_list(lesson):
    lesson = FW.make_path(lesson)
    ans = []
    for i in FW.to_string(own_dir + lesson + _tasks):
        ans.append(i.strip())
    return ans

def add_task_to_pos(lesson_name, task_name, pos):
    if lesson_exists(lesson_name) and P.task_exists(task_name):
        pos -= 1
        lst = tasks_list(lesson_name)
        ans = []
        if len(lst) < pos:
            pos = len(lst)
        for i in range(pos):
            ans.append(lst[i] + "\n")
        ans.append(task_name + "\n")
        for i in range(pos, len(lst)):
            ans.append(lst[i] + "\n")
        FW.write_text(own_dir + FW.make_path(lesson_name), _tasks, ans)
        

def remove_task(lesson_name, task_name):
    task_name = str(task_name)
    lesson_name = FW.make_path(lesson_name)
    if lesson_exists(lesson_name) and P.task_exists(task_name):
        tasks = tasks_list(lesson_name)
        new_tasks = []
        cnt = 0
        for i in tasks:
            if i != task_name or cnt:
                new_tasks.append(i + "\n")
            else:
                cnt = 1
        FW.write_text(own_dir + lesson_name, _tasks, new_tasks)
                
def init():
    FW.create_folder(own_dir)

