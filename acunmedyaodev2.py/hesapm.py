def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
    elif islem == '-':
        return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
    elif islem == '*':
        return f"{sayi1} * {sayi2} = {sayi1 * sayi2}"
    elif islem == '/':
        if sayi2 == 0:
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"
    else:
        return "Geçersiz işlem türü!"

print(hesap_makinesi(7, 4, '+'))  # Çıktı: 7 + 4 = 11
print(hesap_makinesi(200, 2, '/')) # Çıktı: 200 / 2 = 100.0
print(hesap_makinesi(4, 0, '/'))  # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
print(hesap_makinesi(45, 2, '%'))  # Çıktı: Geçersiz işlem türü!
