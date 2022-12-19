p,q = input().split(" ")
P,Q = int(p) , int(q)
hitung  =  P**2 + Q**2 + 1
if hitung % 4 == 0:
    print(hitung)
else:
    print(-1)