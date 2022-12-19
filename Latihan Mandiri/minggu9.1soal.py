def convert(s) :
    ans = ''
    for x in s :
        if x != '.' and x != ',' and x != ')' :    #UNTUK MENGCONVERT STRING MENTAH MENJADI BILANGAN
            ans += x

    return int(ans)

## MAIN

rupiah = 'Kemarin (sabtu) saya mendapat beasiswa (Rp 10.110.330), \
kemudian mendapat doorpize sebesar (Rp 1.000.320).'

rupiah = rupiah.split()
n = len(rupiah) 

nominal = []
for i in range(n) :
    if 'Rp' in rupiah[i] :
        x = convert(rupiah[i+1])
        nominal.append(x)

total = sum(nominal)
print(f'Rp{total:,}')
