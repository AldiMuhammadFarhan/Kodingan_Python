N,D = input().split(" ")
n,d = int(N),int(D)
m = []
t = -1
for i in range(n):
    y = int(input())
    m.append(y)
for i in range(n):
    if(m[i] == d):
        t = i
        break
print(t)





