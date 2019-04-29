file = input()
funcs = __import__(file)
a = list(map(int, input().split()))
run = file + ".main(" + ', '.join(map(str, a)) + ")"
res = getattr(funcs, "main")(*a)
ans = []
def add(lst):
    global ans
    for i in lst:
        if (type(i) == int):
            ans.append(i)
        else:
            add(i)
add(res)
print(*ans)