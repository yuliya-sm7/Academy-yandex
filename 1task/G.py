code = input()
length = 0

num = ""
i = 0
while i < len(code):
    i += 1
    while i < len(code) and code[i].isdigit():
        num += code[i]
        i += 1
    if len(num) == 0:
        num = '1'
    length += int(num)
    num = ""  
print(length)