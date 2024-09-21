jenismobil = input("Masukkan jenis mobil (tesla, toyota, hyundai, tidak jadi beli mobil):")
harga = int(input("Masukkan harga mobil:"))

if jenismobil == "tesla":
    diskon = harga * 0.17
    hsd = harga - diskon
    print(f"Harga mobil Tesla setelah diskon: {hsd}")
elif jenismobil == "toyota":
    diskon = harga * 0.21
    hsd = harga - diskon
    print(f"Harga mobil Toyota setelah diskon: {hsd}")
elif jenismobil == "hyundai":
    diskon = harga * 0.23
    hsd = harga - diskon
    print(f"Harga mobil Hyundai setelah diskon: {hsd}")
elif jenismobil == "tidak jadi beli mobil":
    print("Tidak jadi membeli mobil")
else:
    print("Bu Navira tidak tertarik membeli mobil ini")