gaji_pokok = 2000000
# berapa_kali_lembur = int(input("Berapa kali lembur :"))
jam_lembur = int(input("Masukan Berapa jam Lembur :"))

if jam_lembur < 5 and jam_lembur >= 0:
    bonus_gaji = gaji_pokok + 50000 
    print("Anda mendapatkan gaji "f"Rp {bonus_gaji:,.0f}".replace(",","."))
elif jam_lembur == 5 :
    bonus_gaji = gaji_pokok + 75000 
    print("Anda mendapatkan gaji "f"Rp {bonus_gaji:,.0f}".replace(",","."))
else :
    print("Udah tutup woi")
    

   