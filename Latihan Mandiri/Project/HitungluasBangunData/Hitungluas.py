def luaspersegi(s):
    '''
    untuk menghitung luas persegi dengan mengembalikan nilai hasil
    '''
    hasil = s**2
    return hasil

print(luaspersegi(4))

def luaspersegipanjang(p,l):
    '''
    untuk menghitung luas persegi panjang dengan mengembalikan nilai hasil
    '''
    hasil = p*l
    return hasil

print(luaspersegipanjang(3,4))

def luassegitiga(a,t):
    '''
    untuk menghitung luas segitiga dengan mengembalikan nilai hasil
    '''
    hasil = (1/2) * a * t
    return hasil

print(luassegitiga(6,3))

def luaslingkaran(r):
    '''
    untuk menghitung luas lingkaran dengan mengembalikan nilai hasil
    '''
    if r%7 == 0:
        hasil = 22/7 * r**2
        return hasil
    else:
        hasil = 3,14 * r**2
        return hasil

print(luaslingkaran(7))
print(luaslingkaran(10))

def luasbelahketupat(d1,d2):
    '''
    untuk menghitung luas belah ketupat dengan mengembalikan nilai hasil
    '''
    hasil = (1/2) * d1 * d2
    return hasil

print(luasbelahketupat(4,6))

def luastrapesium(s1,s2,t):
    '''
    untuk menghitung luas trapesium dengan mengembalikan nilai hasil
    '''
    hasil = (1/2) * (s1 + s2) * t
    return hasil

print(luastrapesium(1,3,5))
