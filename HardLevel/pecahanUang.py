pecahan_uang = [10000, 5000, 1000, 500]
input_user = int(input("Masukan angka : "))

print("\n Rincian Pecahan")
for i in pecahan_uang :
    lembar = input_user // i
    input_user = input_user % i
    if lembar > 0 :
        print(f"{lembar} x {i}")

