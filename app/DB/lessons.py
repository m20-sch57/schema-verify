## -*- coding utf-8 -*-

import folder_working as FW

own_folder = "/.lessons"

def add_lesson(name):
    name = FW.make_path(name)
    FW.create_file(own_folder, name)
    
def add_task(lesson_name, task_name):
    lesson_name = make_path(lesson_name)
    if folder_exists(own_path + lesson_name) and folder_exists("/.tasks" + FW.make_path(task_name)):
        FW.add_text(own_dir, lesson_name, [task_name + "\n"])

def remove_task(lesson_name, task_name):
    lesson_name = make_path(lesson_name)
    if folder_exists(own_path + lesson_name) and folder_exists("/.tasks" + FW.make_path(task_name)):
        tasks = to_string(own_path + lesson_name)
        new_tasks = []
        for i in tasks:
            if i != taskname:
                new_tasks.append(i + "\n")
        FW.write_text(own_dir, lesson_name, new_tasks)
                
        
        