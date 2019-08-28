from collections import Counter

n = int(input())
array = list(int(i) for i in input().split())

'''
array.sort()
for i in array:
    print(i, end = ' ')
'''

'''
estimation = Counter(array)
max_count = 0
max_ans = 0
for k in estimation.keys():
    if estimation[k] > max_count:
        max_count = estimation[k]
        max_ans = k
    elif estimation[k] == max_count and k > max_ans:
        max_ans = k
print(max_ans)
'''

'''
mem = dict()
def recurent(z):
    if z < 3:
        return z
    else:
        if z not in mem:
            mem[z] = recurent(z-1) + recurent(z-3)
        return mem[z]
res = list()
for z in array:
    res.append(recurent(z))
print(res)
'''

