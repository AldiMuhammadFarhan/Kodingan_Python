def hitungdigitn(n):
    digit = 0
    while n != 0:
        n = int(n / 10)
        digit += 1
    return digit

def main():
    n=int(input(""))
    banyak_digit_n = hitungdigitn(n)
    # Menghilangkan nilai 1 setelah n+1
    # Karena secara default memiliki step 1
    for i in range(1,n+1):
        for j in range(1,4):
            for k in range(1,n+1):
                if(i==n or k==n or i==1 or k==1):
                    print(n,end=" ")
                else:
                    if(k>=i):
                        # Menggunakan operator "*"
                        # operator tersebut dapat mencetak
                        # string yang sama sebanyak nilai sesudah operator
                        #
                        # Contoh :
                        # print("1" * 5)
                        # mencetak "1" sebanyak 5 kali tanpa spasi
                        #
                        # Disclaimer
                        # Saya juga memodifikasi string yang akan diprint
                        print("*",end=" " * banyak_digit_n)
                    else:
                        print(" ", end=" " * banyak_digit_n)
            if(j<3):
                print("|",end=" ")
        print()

if __name__ =='__main__':
    main()