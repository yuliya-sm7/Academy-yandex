n = int(input()) 
a = [int(i) for i in input().split()] 
 
a.sort() 
for i in a:
    print(i, end = ' ')