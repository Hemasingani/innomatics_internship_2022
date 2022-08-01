n, *line = input().split()
m = list(map(int, line))
arr = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int , input().split()))
initial = 0
for i in arr:
    if i in A:
        initial+=1
    if i in B:
        initial-=1
print(initial) 