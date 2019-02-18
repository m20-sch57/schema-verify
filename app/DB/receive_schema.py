schema_folder = []
tests_folder = []
is_schemas_read = False
is_tests_read = False

#void-функции работы с информацией

def read_schemas():
    global schema_folder, is_schemas_read
    t = True
    fin = open("schema_folder", "r")
    
    #тут считывание, но мы еще не согласовали формат
    
    fin.close()

def read_tests():
    global 

def write_schemas():
    global schema_folder, t
    fout = open("schema_folder", "w")
    
    #тут запись, но мы еще не согласовали формат
    
    fout.close()

##конец работы с информацией

#это просто добавление схемы в ящик

def save_schema(user, task, schema):
    global schema_folder, t
    #это костыль на то, инициализирован ли ящик
    if not(t):
        read()

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

def lexical_check(schema):
    #здесь умная компиляция
    return True
    
def test_check(user, task, schema):
    #проверка на тестах, которую мне сейчас лань писать
    return


def receive_schema(user, task, file_name):
    #list of str
    schema = to_string(file_name)
    #bool
    result = lexical_check(schema)
    if (result != True): # схема некорректно написана
        return "Compilation Error"
    test_check(user, task, schema)
    save(user, task, schema)
    return "Accepted For Testing"
