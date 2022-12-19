# def balik_teks(teks):
#     result = ''
#     for i in teks:
#         result = i + result
#     return result
# teks  = input()
# print(balik_teks(teks))
# # print(teks == balik_teks(teks))
# ==========================================
sentence = input()
listString = list(sentence)
# for i in listString:
#    if i.isdigit() == True:
#        print(i)
# print(listString)
# ==========================================
i = 0 
while i < len(listString):
    if i%2 == 0:
        listString[i] = listString[i].upper()
    i += 1
hasil = " ".join(listString)
print(hasil)
# =========================================
# def gabung(str1,str2):
#     return str1 +" "+str2

# string1 = input()
# string2 = input()

# gb = gabung(string1,string2)
# print(gb)
# =========================================
# kata = input()
# vokal = ['a','i','u','e','o']
# baru = []
# for i in kata:
#     if i in vokal:
#         baru += i.upper()
#     else:
#         baru += "_"
# print("".join(baru))
# ==========================================
# teks = sentence.replace(" ","\n")
# print(" ".join(sentence))
# ==========================================
# def kecil(w1):
#     return " ".join(w1).lower()
# hasil = kecil(sentence)
# print(hasil)
# ==========================================
# def buang(w1,w2):
#     n1 = w1.replace(" ","")
#     n2 = w2.replace(" ","")
#     return n1+" "+n2
# str1=input()
# str2=input()
# print(buang(str1,str2))