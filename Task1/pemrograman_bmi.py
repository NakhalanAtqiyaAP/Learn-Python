# Program BMI(hitung kebutuhan air)
berat_badan = int(input("Masukan berat badan : "))
tinggi_badan = int(input("Masukan tinggi badan : "))

tinggi_m = tinggi_badan / 100
hasil = berat_badan / (tinggi_m * tinggi_m)

if hasil > 30 :
    print("Anda obesitas dengan hasil ", round(hasil, 2))
elif hasil >= 25 and hasil <= 29.9 :
    print("Anda Gemuk dengan hasil ", round(hasil, 2))
elif hasil >= 18.5 and hasil <= 24.9 :
    print("Anda Normal dengan hasil ", round(hasil, 2))
else :
    print("Anda Kurus dengan hasil ", round(hasil, 2))

