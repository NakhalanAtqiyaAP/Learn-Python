input_username = input("Masukan username :")
input_password = input("Masukan Password :")

cek_panjang = len(input_password)
cek_kapital = any(char.isupper() for char in input_password)
cek_kecil = any(char.islower() for char in input_password)
cek_angka = any(char.isdigit() for char in input_password)

if cek_panjang >= 6 and cek_kecil == True and cek_kecil == True and cek_angka == True :
    print("Login berhasil")
    print(cek_angka)
    print(cek_kapital)
    print(cek_kecil)
    print(cek_panjang)
else :
    print("Login gagal")
    print(cek_angka)
    print(cek_kapital)
    print(cek_kecil)
    print(cek_panjang)