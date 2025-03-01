def asalMi(sayi):
    if sayi < 2:
        return f"{sayi} bir asal sayı değildir."

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return f"{sayi} bir asal sayı değildir."

    return f"{sayi} bir asal sayıdır."


print(asalMi(13))  # Çıktı: 13 bir asal sayıdır.
print(asalMi(22)) # Çıktı: 22 bir asal sayı değildir.
