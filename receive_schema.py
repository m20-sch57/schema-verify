

def to_string(file_name):
    #list of str
    answer = []
    fin = open(file_name, "r")
    answer = fin.readlines()
    fin.close()
    #единственный изыестный мне способ очистить файл на питоне
    clear = open(file_name, "w")
    clear.close()
    
    #здесь должно быть удаление файла
    
    return answer


def receive_schema(user, task, file_name):
    #list of str
    s = to_string(file_name)
    #bool
    result = lexical_check(s)
    if (result != True): # схема некорректно написана
        return "Compilation Error"
    test_check(s)
    save(user, task, file_name)
    return "Accepted For Testing"