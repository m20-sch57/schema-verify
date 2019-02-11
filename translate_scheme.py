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
    ans = []
    for i in line:
        if i == "local":
            continue
        ans.append(i.strip() + " = " + "False")
    return ans

def translate_line(line):
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
    out += ")"
    args = translate_args(args)
    out = translate_args(out)
    if r_name == "and" or r_name == "or":
    elif r_name == "not":
    else:
        return out + " = " + r_name + args
    

fin = open("received.txt", "r")
print(translate_line(fin.readline()))