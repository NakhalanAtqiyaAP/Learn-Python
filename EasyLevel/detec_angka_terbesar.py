input_loop =int(input("Masukan mau berapa kali loop : "))
angka = []
i = 1
while i <= input_loop:
 daftar_angka = int(input(f"Masukan angka ke-{i} : "))
 angka.append(daftar_angka)
 i += 1


hasil = max(angka)
print(f"Angka paling terbesar adalah {hasil} ")