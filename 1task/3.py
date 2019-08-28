n = int(input())
array = list(int(i) for i in input().split())

mem = dict()
mem[0] = 0
mem[1] = 1
mem[2] = 2

'''def recurent(z):
    if z < 3:
        return z
    else:
        if z not in mem:
            mem[z] = recurent(z-1) + recurent(z-3)
        return mem[z]
        '''
for z in array:
    if z not in mem:
        stack = list()
        check = list()
        stack.append(z)
        check.append(z)
        while check:
            x = check.pop(0)
            if x-1 not in stack and x-1 not in mem:
                stack.append(x-1)
                check.append(x-1)
            if x-3 not in stack and x-3 not in mem:
                stack.append(x-3)
                check.append(x-3)
        stack.sort(reverse = True)
        while stack:
            k = stack.pop()
            mem[k] = mem[k-1] + mem[k-3]        
    print(mem[z], end = ' ')

