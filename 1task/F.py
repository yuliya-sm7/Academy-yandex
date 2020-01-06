n = int(input())
matrix = list()
for _ in range(n):
    matrix.append(list(int(i) for i in input().split()))
matrix.sort(key = lambda row: row[1])
max_count = 0
count = 1
t_out = 
for z in matrix:
    if z[1] < 
print(matrix)