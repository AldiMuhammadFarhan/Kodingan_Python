import fnmatch
A = input()
N =  int(input())
D = []
for i in range(N):
    Y = input()
    if fnmatch.fnmatch(Y, A) == True:
        D.append(Y)

for j in range(len(D)):
    print(D[j])
