pengguna = {
    'Riduan': {'password': 'IlhamGod', 'role': 'admin'}
}
produk = {}

while True:
    print("HI, Selamat datang di Sistem Pembelian Lampu Projie")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Login")
    print("2. Daftar")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == '1':
        print("Silakan Login Dulu")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        user = pengguna.get(username)
        
        if user is None or user['password'] != password:
            print("Username atau password salah. Coba lagi.")
            continue
        
        while True:
            if user['role'] == 'admin':
                print("Menu Admin")
                print("1. Tampilkan Produk")
                print("2. Tambah Produk")
                print("3. Ubah Produk")
                print("4. Hapus Produk")
                print("5. Logout")
                pilihan_admin = input("Masukkan pilihan: ")
                
                if pilihan_admin == '1':
                    print("Produk Tersedia:")
                    if produk:
                        for nama, info in produk.items():
                            print(f"{nama} - Stok: {info['stok']}, Harga: {info['harga']} RP")
                    else:
                        print("Tidak ada produk yang tersedia.")
                elif pilihan_admin == '2':
                    nama_produk = input("Masukkan nama produk: ")
                    stok = int(input("Masukkan jumlah stok: "))
                    harga = int(input("Masukkan harga produk: "))
                    produk[nama_produk] = {'stok': stok, 'harga': harga}
                    print(f"Produk {nama_produk} berhasil ditambahkan!")
                elif pilihan_admin == '3':
                    nama_produk = input("Masukkan nama produk yang ingin diubah: ")
                    if nama_produk in produk:
                        produk[nama_produk]['stok'] = int(input("Masukkan jumlah stok baru: "))
                        produk[nama_produk]['harga'] = int(input("Masukkan harga baru: "))
                        print("Produk berhasil diubah!")
                    else:
                        print("Produk tidak ditemukan!")
                elif pilihan_admin == '4':
                    nama_produk = input("Masukkan nama produk yang ingin dihapus: ")
                    if nama_produk in produk:
                        del produk[nama_produk]
                        print("Produk berhasil dihapus!")
                    else:
                        print("Produk tidak ditemukan!")
                elif pilihan_admin == '5':
                    print("Logout")
                    break
                else:
                    print("Pilihan tidak valid!")
            
            else:
                print("Menu Pembeli Lampu Projie")
                print("1. Tampilkan Produk")
                print("2. Logout")
                pilihan_user = input("Masukkan pilihan: ")
                
                if pilihan_user == '1':
                    print("Produk Tersedia:")
                    if produk:
                        for nama, info in produk.items():
                            print(f"{nama} - Stok: {info['stok']}, Harga: {info['harga']} RP")
                    else:
                        print("Tidak ada produk yang tersedia.")
                elif pilihan_user == '2':
                    break
                else:
                    print("Pilihan tidak valid!")
    
    elif pilihan == '2':
        print("Halo Pengguna baru! Ayo buat akun dulu")
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