#deteksi hari

input_hari = int(input("Masukan hari(dalam angka) : "))


match input_hari:
        case 1 :
           print("Senin")
        case 2 :
           print("Selasa")
        case 3 :
            print("Rabu")
        case 4 :
           print("Kamis")
        case 5 :
            print("Jum'at")
        case 6 :
           print("Sabtu")
        case 7 :
            print("Minggu")
        case _ :
          print("Kesalahan Inputan")
        
      