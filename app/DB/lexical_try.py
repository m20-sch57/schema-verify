## -*- coding: utf-8 -*-

def translate_name(name):
    ans = []
    name = name.split()
    name1 = []
    for i in name:
        if len(name1) == 0:
            name1.append(i)
        else:
            if name1[-1][-1] == ',':
                name1[-1] += (" " + i)
            else:
                name1.append(i)
    name = name1
    ans = "def " + name[2] + ' ' + name[1] + ':\n'
    return [ans, name[-1]]

def is_good(a):
    return ord('a') <= ord(a) <= ord('z') or ord('A') <= ord(a) <= ord('Z') or ord('0') <= ord(a) <= ord('9')

def to_list(line):
    a = line.split()
    for i in range(len(a)):
        while len(a) != 0 and not(is_good(a[i][0])):
            a[i] = a[i][1:]
        while len(a) != 0 and not(is_good(a[i][-1])):
            a[i] = a[i][:-1]
    return a

def translate_var(var):
    var = var.split()
    var = var[1:]
    var = to_list(' '.join(var))
    ans = ""
    for i in var:
        ans += (i + " = False; ")
    ans = ans[:-1]
    ans += "\n"
    return ans

def getchars(word):
    pos = 0
    while pos < len(word) and not(is_good(word[pos])):
        pos += 1
    word = word[pos:]
    pos = -1
    while pos >= 0 and not(is_good(word[pos])):
        pos -= 1
    if pos != 0:
        word = word[:pos]
    return word

def translate_line(line):
    if line == "":
        return ""
    line = line.split()
    line1 = [line[0]]
    for i in range(1, len(line)):
        if line1[-1] == "" or line[-1][-1] == ',':
            line1[-1] += ' ' + line[i]
        else:
            line1.append(line[i])
    line = line1
    if line[2] == 'and' or line[2] == 'or':
        ans = line[3] + " = " + getchars(line[0]) + " " + line[2] + " " + getchars(line[1]) + "\n"
        return ans
    ans = line[3] + " = " + line[2] + line[0] + line[1] + "\n"
    return ans

def translate(func):
    tab = "    "
    if func == []:
        return []
    ans = []
    name = func[0]
    name = translate_name(name)
    ans = [name[0]]
    output = to_list(name[1])
    beg = 1
    if (func[1].split()[0] == "local"):
        ans.append(tab + translate_var(func[1]))
    for i in range(2, len(func)):
        if func[i].split()[0] == "end":
            break
        else:
            ans.append(tab + translate_line(func[i]))
    ans += "    return " + name[1] + "\n"
    return ans
    
    
def get(lines):
    cur = []
    ans = []
    for i in lines:
        if i == "\n":
            ans += translate(cur)
            ans += ["\n"]
            cur = []
        else:
            cur.append(i)
    ans += translate(cur)
    return ans

fin = open("received.txt", "r")
a = fin.readlines()
print(a)
print("".join(get(a)))