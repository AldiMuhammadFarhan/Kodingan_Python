b,p,l = input().split(" ")
B,P,L = int(b),int(p),int(l)

if B <= 10 and P <= 40 and L <= 90:
    print("S")
elif B <= 14 and P <= 60 and L <= 120:
    print("M")
elif B <= 18 and P <= 80 and L <= 180:
    print("L")
elif B <= 25 and P <= 100 and L <= 220:
    print("X")
else:
    print("X")