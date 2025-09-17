saldo = 1000000
pilihan = 0

while pilihan != 4 :
    print("\n=== Menu ATM ===")
    print("1. Lihat Saldo")
    print("2. Tarik Saldo")
    print("3. Setor Saldo")

    pilihan = int(input("Pilih menu 1-4 : "))
    
    if pilihan == 1 :
        print("Saldo anda adalah "f"Rp {saldo:,.0f}".replace(",","."))
    elif pilihan == 2 :
      tarik_saldo = int(input("Jumlah yang ingin di tarik : "))
      if tarik_saldo <= saldo :
        saldo -= tarik_saldo
        print("Berhasil menarik saldo sebesar "f"Rp {tarik_saldo:,.0f}".replace(",","."))
        print("\n Sisa saldo anda adalah "f"Rp {saldo:,.0f}".replace(",","."))
      else :
        print("Tidak bisa menarik, karena lebih dari saldo")
    elif pilihan == 3:
      setor_saldo = int(input("Masukan jumlah yang ingin di setor : "))
      saldo += setor_saldo
      print(f"Berhasil setor saldo dengan jumlah setor saldo Rp {setor_saldo:,.0f}".replace(",","."))
      print("\n Sisa saldo anda adalah "f"Rp {saldo:,.0f}".replace(",","."))
    elif pilihan == 4 :
      print("Terima kasih telah memakai ATM")
    else:
      print("Inputan tidak valid")
