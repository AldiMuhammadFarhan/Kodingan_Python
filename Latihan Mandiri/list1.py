# my_list = ["aldi","Muhammad","farhan"]

# for i in my_list:
#     # x = isinstance(i,str)
#     print(i,end=" ")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# lis1 = [a,b]
# tup1 = (c,d,lis1)

# tup1[2][1] = sum(lis1)
# tup1[2][0] = 10

# print(tup1)

# a = input()
# b = input()
# c = input()
# d = input()

# tup1 = (a,b,c,d)
# tup2 = (tup1[2:]*3)

# print(tup1 + tup2)

# my_tuple6 = (1, 2, 1, (4, 5), [1, 2],"A")

# print(my_tuple6[1])
# print(my_tuple6[-1])
# print(my_tuple6[3][1])
# print(my_tuple6[1:4])
# print(my_tuple6.index(2))
# print((4, 5) in my_tuple6)
# print(my_tuple6[:])

# data6 = [9.1, 82, 73, 6.4, 45, 36]



# sum_data1 = 0

# sum_data2 = 0

# for elemen in data6:

#    if isinstance (elemen, int):

#       sum_data1 += elemen

#    else:

#       sum_data2 += elemen

# print (sum_data1, sum_data2)

# data9 = [31, 55, 97]

# tmp = data9[1: ]

# for i in range (len (data9)):

#     if (i % 2 == 0):

#       data9.extend (tmp)

#     else:

#       data9.append(i)

# print(len(data9))

# data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# data2 = []

# for elemen in data1:

#   if elemen % 2 == 1:

#     data2.append(elemen)
# print(data2)

# set2 = {"nama", (1,2), "dia", [1, 2]}

# print(set2)

# tmp1 = []

# tmp2 = []

# for i in range(10):

#      tmp1.append(i*i)

# for i in range(20):

#     tmp2.append(i)

# set9 = set(tmp1 + tmp2)

# print(len(set9))

# set4 = {1, 2, 1, 3, 4, 1}

# set4.add(1)

# set4.update([4, 2, 5, 7, 1, 3])

# set4.add(tuple([1]))

 

# print(len(set4))

# tuple3 = 1, 4, 9, 7, 8, 0, 10

# print(tuple3.index(11))

# tuple2 = (1, 1, 2, 4, 5, 8, 10 , 11 , 45, 1)

# print(tuple2.count(1))

# tuple1 = [tuple(), (1), (1, 2), 5, ("Joni", (12, 1))]

# tmp = 1,

# print(tuple1)
# print(tmp)


# data4 = [10, 11, 12, 14, 15]

# abc =  data4[0] //2

# print(data4[abc])

# data7 = [12, 1, 456, 145, 1456, 2, 77]

# data8 = data7[-5 : -3]

# print(sum(data8))

# x = int(input())

# data5=[]

# for i in range (10):

#    data5.append(2 * i)

# print(data5.index(x))


# tmp1 = [ ]

# for i in range(10):

#   tmp1.append(i)

# tmp2 = tmp1 * 3

# set8 = set(tmp1 + tmp2)

# print(set8)

# set3 = {"Aku", True, "Cinta", 1, False, "Coding"}

# print(set3[0], set3[2], set3[-1])

# set5 = set()

# for i in range(10):

#     set5.add(3*i)

# set5.remove(0)

# set5.remove(28)

# print(set5)

# tuple6 = 1, 2, 4, 5, (7, 8), (1, ),2

 

# if (7, 8) in tuple6:

#   if (2, ) in tuple6:

#     print("one",end= " ")

#   else:

#     print("two", end= " ")

# if (1, ) in tuple6:

#   print("three")

# A = [ ]

# for i in range(10):

#     A.append(6*i + i)

# B = tuple(A)

# print(B[9])

# tmp = [1, 3, 6, 6 , 1, 7]

# tuple5 = tuple(tmp)

 

# print(tuple5)


# q =  {1 : "aldi", 2:"ganteng",3:"selalu"}
# p =  {1 : "mf", 2:"terus",3:"berkarisma"}
# e =  {1 : "wk", 2:"aya",3:"ok"}

# for a,b,c in zip(q.values(),p.values(),e.values()):
#     print("{1} {1} {1}".format(a,b,c))


# dict6 = {1: 'satu', 2: 'dua', 3: [1, 2, 3], 4: {1: 'senin', 2: 'selasa'}, 10: (1, 2)}
# ini = 0
# for v, k in dict6.items():

#     if len(k) > 2:

#       ini = ini + v

# print(ini)



# dict9 = {1: 'dua'}

# dict9.clear()

# dict9 = {2: 1, True: 2, False: 5, 1: False, 5: True}

# dict9.pop(0)

# dict9.popitem()

# print(len(dict9))


# dict3 = {1: 'satu', 2: 'dua', '3': True, 'A': 4}
# print(dict3.get(4))


# dict2 = {1: 'satu', 2: 'dua', '3': True}
# print(dict2[3])

# dict5 = {1: 'satu', 'satu': 1, [1, 2]: (1, 2)}
# print(dict5[1])

# dict10 = dict([(1, 'satu'), ('satu', 1), (2, '2'), ('3',3)])
# dict10.pop(1)
# dict10.pop('2')
# print(len(dict10))


# dict7 = {2: 1, True: 2, False: 5, 1: False, 5: True}
# sum = 0
# for k in dict7:

#   if dict7[k] in dict7:

#     sum = sum + dict7[dict7[k]]

# print(sum)


# dict4 = {1: 'satu', 2: 'dua', (3, 4): [1, 2, 3], 'four': {1: 'senin', 2: 'selasa'}}
# if('dua' in dict4):

#   print(2)
# elif ((3, 4) in dict4):

#   print(dict4[(3,4)][2])
# else:

#   print("Null")


# dict8 = {2: 1, True: 2, False: 5, 1: False, 5: True}
# dict8[0] = "saya"
# dict8[True] = "dia"
# dict8["saya"] = 1

# print(len(dict8))