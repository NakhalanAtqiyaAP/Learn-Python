kalimat = str(input("Masukan Kalimat :"))
hasil ={}
to_lower = kalimat.lower().replace(" ","")

for i in to_lower: #i mengambil setiap satu huruf di to_lower
    if i in hasil: #jika i terbaca maka tambahkan ke hasil
        hasil[i] += 1
    else :  #jika belum buat entri baru dengan nilai 1
        hasil[i] = 1
      
print(hasil)      