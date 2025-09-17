#Program login

user_input = input()
username = input("masukan username anda : ")
password = input("masukan password anda : ")

if username == "admin" and password == "1234":
    print("login berhasil")
else:
    print("login gagal")

# Program cek ada berapa password

username = input("masukan username anda : ")
password = input("masukan password anda : ")

cek_pass = len(password)

if cek_pass <= 6:
    print("password terlalu pendek")
else:
    print("Login berhasil")

