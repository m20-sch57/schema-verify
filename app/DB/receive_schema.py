## -*- coding utf-8 -*-

import translate_schema as TS

def lexical_check(schema):
    try:
        res = TS.get(""
    return True
    
def test_check(user, task, schema):
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
