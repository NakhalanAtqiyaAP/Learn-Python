input_user = str(input("Masukan kata : "))
to_nospace = input_user.replace(" ", "").lower()
palindrome_teks = to_nospace[::-1]
print(palindrome_teks)

if palindrome_teks == to_nospace:
    print(f"Adalah palindrome teks {palindrome_teks}")
else:
    print(f"Bukan palindrome teks {palindrome_teks}")