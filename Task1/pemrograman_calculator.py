#Program calculator

angka1 = int(input("masukan angka ke-1 : "))
angka2 = int(input("masukan angka ke-2 : "))
calculate = input("masukan mau diapain, opsi +, *, /, % : ")

if calculate == "+":
   hasil = angka1 + angka2
   print("hasil = ", hasil)
elif calculate == "*":
  hasil = angka1 * angka2
  print("hasil = ", hasil)
elif calculate == "/":
  hasil = angka1 / angka2
  print("hasil = ", int(hasil))
elif calculate == "%":
  hasil = angka1 % angka2
  print("hasil = ", hasil)

