a = []

def read():
    global a
    a = []
    fin = open("info.txt", "r")
    a = list(map(int, fin.readline().split()))
    fin.close()

def save():
    global a
    fout = open("info.txt", "w")
    for i in a:
        print(i, file=fout, end=' ')
    fout.close()
    
def get(i):
    global a
    if (i >= len(a)):
        return "list index out of range"
    return a[i]
    
def add(i):
    global a
    a.append(i)

def delete():
    global a
    a.pop()

def main():
    global a
    f = 0
    while True:
        n = input().split()
        if (n[0] == "read"):
            read()
        if (n[0] == "save"):
            save()
        if (n[0] == "get" and len(n) > 1):
            print(get(int(n[1])))
        if (n[0] == "end"):
            return
        if (n[0] == "add" and len(n) > 1):
            add(int(n[1]))
        if (n[0] == "del"):
            delete()
            
main()