nA = int(input())
matrixA = list()
for _ in range(nA):
    matrixA.append(list(int(i) for i in input().split()))
nB = int(input())
matrixB = list()
for _ in range(nB):
    matrixB.append(list(int(i) for i in input().split()))

answer = list()
answer_len = 0
command = input()

if command == "INNER":
    for rowA in matrixA:
        for rowB in matrixB:
            if rowA[0] == rowB[0]:
                answer.append([rowA[0], rowA[1], rowB[1]])
                answer_len += 1

if command == "LEFT":
    answer_len = len(matrixA)
    for rowA in matrixA:
        flag = False
        for rowB in matrixB:
            if rowA[0] == rowB[0]:
                flag = True
                answer.append([rowA[0], rowA[1], rowB[1]])
        if not flag:
            answer.append([rowA[0], rowA[1], None])

if command == "RIGHT":
    answer_len = len(matrixB)
    for rowB in matrixB:
        flag = False
        for rowA in matrixA:
            if rowA[0] == rowB[0]:
                flag = True
                answer.append([rowA[0], rowA[1], rowB[1]])
        if not flag:
            answer.append([rowB[0], None, rowB[1]])


if command == "FULL":
    answer_len = len(matrixA)
    for rowA in matrixA:
        flag = False
        for rowB in matrixB:
            if rowA[0] == rowB[0]:
                flag = True
                answer.append([rowA[0], rowA[1], rowB[1]])
        if not flag:
            answer.append([rowA[0], rowA[1], None])
    for rowB in matrixB:
        flag = False
        for rowA in matrixA:
            if rowA[0] == rowB[0]:
                flag = True
        if not flag:
            answer.append([rowB[0], None, rowB[1]])
            answer_len += 1

print(answer_len)
for row in answer:
    for i in row:
        if i == None:
            print("NULL", end = ' ')
        else:
            print(i, end = ' ')
    print('')