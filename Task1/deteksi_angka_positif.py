angka = int(input("Masukan angka : "))

if angka >= 1 and angka % 2 == 0  :
    print("Positif Genap")
elif angka >= 1 and angka % 2 != 0 :
    print("Positif Ganjil")
else:
    print("Negatif")