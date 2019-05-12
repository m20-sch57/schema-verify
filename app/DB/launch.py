## -*- coding: utf-8 -*-

import importlib.util

def get_funcs(file):
    name = "test"
    sup = importlib.util.spec_from_file_location(name, file)
    funcs = importlib.util.module_from_spec(sup)
    sup.loader.exec_module(funcs)
    return funcs


file = input()
#funcs = module()
funcs = get_funcs("./" + file)
a = []
try:
    a = list(map(int, input().split()))
except:
    a = []
#run = file + ".main(" + ', '.join(map(str, a)) + ")"
res = funcs.main(*a)
ans = []
def add(lst):
    global ans
    for i in lst:
        if (type(i) == int):
            ans.append(i)
        else:
            add(i)
add(res)
print(ans)