a = int(input())
b = int(input())
c = int(input())

i = 1

suku = i**b

while i<c and suku<c:
    print(suku)
    suku = (1 + i * a)**b
    i += 1
   