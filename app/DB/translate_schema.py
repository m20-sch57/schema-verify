## -*- coding: utf-8 -*-

def is_good(sym):
    return ord('a') <= ord(sym) <= ord('z') or ord('A') <= ord(sym) <= ord('Z') or ord('0') <= ord(sym) <= ord('9')

def to_letters(word):
    ans = ""
    for i in word:
        if is_good(i):
            ans += i
    return ans

def split(line, sep = [" ", ","]):
    line = line.strip()
    ans = [""]
    for i in line:
        if i in sep:
            ans.append("")
            continue
        else:
            ans[-1] += i
    return ans

def translate_args(args):
    args = list(map(to_letters, split(args)))
    return "(" + ", ".join(args) + ")"

def translate_name(name):
    name = split(name)
    args = "("
    r_name = ""
    out = "("
    is_a = 0
    is_o = 0
    for i in name:
        if i == "scheme":
            continue
        if i[0] == "(":
            if is_a == 2:
                is_o = 1
            else:
                is_a = 1
        if is_a == 1:
            if args == "(":
                args += to_letters(i)
            else:
                args += " " + to_letters(i)
        elif is_o == 1:
            if out == "(":
                out += to_letters(i)
            else:
                out += " " + to_letters(i)
        else:
            r_name += i
        if i[-1] == ")":
            is_a = 2
    ans = ["", ""]
    args += ")"
    out += ")"
    args = translate_args(args)
    out = translate_args(out)
    ans[0] = "def " + r_name + args + ":"
    ans[1] = "return " + out
    return ans

def translate_var(line):
    line = split(line)
    if line[0] != "local":
        return 5 / 0
    ans = []
    for i in line:
        if i == "local":
            continue
        ans.append(i.strip() + " = " + "False")
    return ans

def translate_line(line):
    if not(line):
        return ""
    if to_letters(line) == "end":
        return ""
    args = "("
    r_name = ""
    out = "("
    line = split(line)
    is_a = 0
    is_o = 0
    for i in line:
        if i[0] == '(':
            if is_a == 2:
                is_o = 1
            else:
                is_a = 1
        word = to_letters(i)                
        if is_a == 1:
            if args == '(':
                args += word
            else:
                args += ' ' + word
        elif is_o == 1:
            if out == '(':
                out += word
            else:
                out += ' ' + word            
        else:
            r_name += word
        if i[-1] == ')':
            is_a = 2
    args += ")"
    s_args = list(map(to_letters, split(args)))
    out += ")"
    args = translate_args(args)
    out = translate_args(out)
    if r_name == "and" or r_name == "or":
        return out + " = " + s_args[0] + " " + r_name + " " + s_args[1]
    elif r_name == "not":
        return out + " = not" + args
    else:
        return out + " = " + r_name + args
    
def translate_scheme(lines):
    tab = "    "
    name = translate_name(lines[0])
    beg = 2
    ln = [name[0]]
    try:
        local = translate_var(lines[1])
        for i in local:
            ln.append(tab + i)
    except:
        beg = 1
    for i in range(beg, len(lines)):
        if translate_line(lines[i]):
            ln.append(tab + translate_line(lines[i]))
    ln += [tab + name[1]]
    return ln

def translate_all(lines):
    cur = []
    ans = []
    for i in lines:
        if to_letters(i) == "end":
            ans += translate_scheme(cur)
            ans.append("")
            cur = []
        elif to_letters(i):
            cur.append(i)
    if not(ans):
        raise TypeError
    return ans


def get(filename):
    fin = open(filename, "r")
    ans = translate_all(fin.readlines())
    return ans