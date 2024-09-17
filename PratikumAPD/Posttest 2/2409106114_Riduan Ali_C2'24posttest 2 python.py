nama = input("Masukan nama:")
nim  = input("masukan nim:")
harga_setiap_mobil = 100000000

Diskon_tesla = 0.17
Diskon_toyota = 0.21
Diskon_hyundai = 0.23

harga_setiap_mobil_tesla = harga_setiap_mobil * Diskon_tesla
harga_setiap_mobil_toyota = harga_setiap_mobil * Diskon_toyota
harga_setiap_mobil_hyundai = harga_setiap_mobil * Diskon_hyundai

output = (
    f"jika ingin membeli mobil tesla saya harus membayar {harga_setiap_mobil_tesla} setelah mendapatkan diskon 17%"
    f"jika ingin membeli mobil toyota saya harus membayar {harga_setiap_mobil_toyota} setelah mendapat diskon 21%" 
    f"jika ingin membeli mobil hyundai saya harus membayar {harga_setiap_mobil_hyundai} setelah mendapat diskon 23%"  
          
        ) 
print(output)
