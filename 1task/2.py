from collections import Counter

n = int(input())
array = list(int(i) for i in input().split())

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