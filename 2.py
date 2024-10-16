nilai1 = int(input("Masukkan nilai pertama: "))
nilai2 = int(input("Masukkan nilai kedua: "))
nilai3 = int(input("Masukkan nilai ketiga: "))

if nilai1 >= nilai2 and nilai1 >= nilai3:
    print("Nilai terbesar adalah", nilai1)
elif nilai2 >= nilai1 and nilai2 >= nilai3:
    print("Nilai terbesar adalah", nilai2)
else:
    print("Nilai terbesar adalah", nilai3)
