#Program diskon

barang_belanjaan = int(input("Masukan total belanjaan : "))
if barang_belanjaan >= 5000000:
    diskon = barang_belanjaan * 0.20
    total = barang_belanjaan - diskon
    print("total belanjaan adalah " f"Rp {total:,.0f}".replace(",","."), " dengan diskon 20%")
elif barang_belanjaan >= 2000000 :
    diskon = barang_belanjaan * 0.10
    total = barang_belanjaan - diskon
    print("total belanjaan adalah " f"Rp {total:,.0f}".replace(",","."), " dengan diskon 10%")
else:
    print("total belanjaan adalah ", f"Rp {barang_belanjaan:,.0f}".replace(",","."),)


