## -*- coding utf-8 -*-

try:
    import folder_working as FW
    import problems as P
except ImportError:
    from app.DB import folder_working as FW
    from app.DB import problems as P

own_dir = "/.lessons"

def lesson_exists(name):
    name = FW.make_path(name)
    return FW.file_exists(own_dir + name)

def lessons_list():
    return FW.getdirs(own_dir)

def add_lesson(name):
    if (lesson_exists(name)):
        return
    name = FW.make_path(name)
    FW.create_file(own_dir, name)
    
def add_task(lesson_name, task_name):
    lesson_name = FW.make_path(lesson_name)
    if lesson_exists(lesson_name) and P.task_exists(task_name):
        FW.add_text(own_dir, lesson_name, [task_name + "\n"])

def tasks_list(lesson):
    lesson = FW.make_path(lesson)
    ans = []
    for i in FW.to_string(own_dir + lesson):
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
        FW.write_text(own_dir, FW.make_path(lesson_name), ans)
        

def remove_task(lesson_name, task_name):
    lesson_name = FW.make_path(lesson_name)
    if lesson_exists(lesson_name) and P.task_exists(task_name):
        tasks = tasks_list(lesson_name)
        new_tasks = []
        cnt = 1
        for i in tasks:
            if i != task_name and cnt:
                cnt = 0
                new_tasks.append(i + "\n")
        FW.write_text(own_dir, lesson_name, new_tasks)
                
def init():
    FW.make_fodler(own_dir)
        
        