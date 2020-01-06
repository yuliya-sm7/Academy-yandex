n = int(input()) 
a = [int(i) for i in input().split()] 
 
a.sort() 
print(" ".join(str(i) for i in a))