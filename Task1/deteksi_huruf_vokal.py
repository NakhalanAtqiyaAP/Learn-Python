# deteksi huruf vokal
huruf = input("Masukan satu huruf : ")
huruf_vokal = ["a", "i", "u", "e", "o"]
detec = huruf in huruf_vokal

if detec:
    print("huruf vokal")
else:
    print("huruf konsonan")

