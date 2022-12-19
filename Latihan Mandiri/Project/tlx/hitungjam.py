time = int(input())
jam = time // 3600
print(jam)
menit = (time - jam*3600) // 60
print(menit)
detik = (time - jam*3600) - menit*60
print(detik)