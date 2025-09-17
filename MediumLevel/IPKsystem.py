input_nilai = int(input("Maukan nilai : "))

if input_nilai >= 85 and input_nilai <= 100:
  nilai = "A"
  bobot_IPK = 4
  print(f"Nilai {nilai} dengan bobot IPK {bobot_IPK}")
elif input_nilai >= 70 :
  nilai = "B"
  bobot_IPK = 3
  print(f"Nilai {nilai} dengan bobot IPK {bobot_IPK}")
elif input_nilai >= 55 :
  nilai = "C"
  bobot_IPK = 2
  print(f"Nilai {nilai} dengan bobot IPK {bobot_IPK}")
elif input_nilai >= 40 :
  nilai = "D"
  bobot_IPK = 3
  print(f"Nilai {nilai} dengan bobot IPK {bobot_IPK}")
elif input_nilai < 40 :
  nilai = "E"
  bobot_IPK = 0
  print(f"Nilai {nilai} dengan bobot IPK {bobot_IPK}")