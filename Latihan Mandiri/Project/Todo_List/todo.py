todo = []
berapa_todo = int(input("Kamu Hari ini ada berapa kegiatan? "))
i = berapa_todo
while i>0:
    kegiatan = input("Kamu hari ini ingin melakukan apa?dan jam berapa? ")
    todo.append(kegiatan)
    i-=1
print(' lalu '.join(todo))