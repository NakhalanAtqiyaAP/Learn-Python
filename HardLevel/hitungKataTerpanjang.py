input_user = str(input("Masukan Kata-kata :"))
pemisah = input_user.split()
panjang_kata = ""
panjang_keseluruhan = 0
for i in pemisah:
    if len(i) > panjang_keseluruhan:
        panjang_kata =  i
        panjang_keseluruhan = len(i)

print(f"Kata paling panjang ada {panjang_kata}")
print(f"Jumlah kata ada {panjang_keseluruhan}")