def tampilkan_produk(produk):
    print("Produk Tersedia:")
    if produk:
        for nama, info in produk.items():
            print(f"{nama} - Stok: {info['stok']},  Harga: RP {info['harga']}")
    else:
        print("Tidak ada produk yang tersedia.")


def tambah_produk(produk):
    nama_produk = input("Masukkan nama produk: ")
    stok = int(input("Masukkan jumlah stok: "))
    harga = int(input("Masukkan harga produk: "))
    produk[nama_produk] = {'stok': stok, 'harga': harga}
    print(f"Produk {nama_produk} berhasil ditambahkan!")


def ubah_produk(produk):
    nama_produk = input("Masukkan nama produk yang ingin diubah: ")
    if nama_produk in produk:
        produk[nama_produk]['stok'] = int(input("Masukkan jumlah stok baru: "))
        produk[nama_produk]['harga'] = int(input("Masukkan harga baru: "))
        print("Produk berhasil diubah!")
    else:
        print("Produk tidak ditemukan!")


def hapus_produk(produk):
    nama_produk = input("Masukkan nama produk yang ingin dihapus: ")
    if nama_produk in produk:
        del produk[nama_produk]
        print("Produk berhasil dihapus!")
    else:
        print("Produk tidak ditemukan!")


def menu_admin(produk):
    while True:
        print("\nMenu Admin")
        print("1. Tampilkan Produk")
        print("2. Tambah Produk")
        print("3. Ubah Produk")
        print("4. Hapus Produk")
        print("5. Logout")
        pilihan_admin = input("Masukkan pilihan: ")

        if pilihan_admin == '1':
            tampilkan_produk(produk)
        elif pilihan_admin == '2':
            tambah_produk(produk)
        elif pilihan_admin == '3':
            ubah_produk(produk)
        elif pilihan_admin == '4':
            hapus_produk(produk)
        elif pilihan_admin == '5':
            print("Logout")
            break
        else:
            print("Pilihan tidak valid!")


def menu_pembeli(produk):
    while True:
        print("\nMenu Pembeli Lampu Projie")
        print("1. Tampilkan Produk")
        print("2. Beli Produk")
        print("3. Logout")
        pilihan_user = input("Masukkan pilihan: ")

        if pilihan_user == '1':
            tampilkan_produk(produk)
        elif pilihan_user == '2':
            beli_produk(produk)
        elif pilihan_user == '3':
            break
        else:
            print("Pilihan tidak valid!")


def beli_produk(produk):
    if not produk:
        print("Tidak ada produk yang tersedia untuk dibeli.")
        return
    tampilkan_produk(produk)
    nama_produk = input("Masukkan nama produk yang ingin dibeli: ")
    if nama_produk in produk:
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
        if jumlah <= produk[nama_produk]['stok']:
            total_harga = jumlah * produk[nama_produk]['harga']
            produk[nama_produk]['stok'] -= jumlah
            print(f"Anda berhasil membeli {jumlah} {nama_produk}. Total harga: {total_harga} RP")
        else:
            print("Stok tidak mencukupi!")
    else:
        print("Produk tidak ditemukan.")


def pembelian_lampu_projie():
    pengguna = {
        'Riduan': {'password': 'IlhamGod', 'role': 'admin'}
    }
    produk = {}

    while True:
        print("\nHI, Selamat datang di Sistem Pembelian Lampu Projie")
        print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
        print("1. Login")
        print("2. Daftar")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            print("\nSilakan Login Dulu")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            user = pengguna.get(username)

            if user is None or user['password'] != password:
                print("Username atau password salah. Coba lagi.")
                continue

            if user['role'] == 'admin':
                menu_admin(produk)
            else:
                menu_pembeli(produk)

        elif pilihan == '2':
            print("\nHalo Pengguna baru! Ayo buat akun dulu")
            username_baru = input("Masukkan username: ")
            password_baru = input("Masukkan password: ")
            if username_baru in pengguna:
                print("Username sudah terdaftar. Coba username lain.")
            else:
                pengguna[username_baru] = {'password': password_baru, 'role': 'pengguna'}
                print(f"Akun Anda berhasil terdaftar dengan username: {username_baru}")

        elif pilihan == '3':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid!")
pembelian_lampu_projie()