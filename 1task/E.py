import json
string = input()
d = json.loads(string)

del_dict = 0
del_list = 0

def f(z):
    empty = True
    global del_dict, del_list
    if type(z) == dict:
        for k in z.keys():
            empty = f(z[k]) and empty
        if len(z) == 0 or empty:
            del_dict += 1
            return True
    elif type(z) == list:
        for i in z:
            empty = f(i) and empty
        if len(z) == 0 or empty:
            del_list += 1
            return True
    return False

f(d)
print(del_dict, del_list)
