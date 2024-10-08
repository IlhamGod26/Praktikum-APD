pengguna = [{'username': 'Riduan', 'password': 'IlhamGod', 'role': 'admin'}]
produk = []



while True:
    print("HI, Selamat datang di Sistem Pembelian Lampu Projie")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Login")
    print("2. Daftar")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == '1':
        print("Login")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        user = None
        for u in pengguna:
            if u['username'] == username and u['password'] == password:
                user = u
                break
        if user is None:
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
                    for i, p in enumerate(produk):
                        print(f"{i+1}. {p[0]} - Stok: {p[1]}, Harga: {p[2]} RP")
                elif pilihan_admin == '2':
                    nama_produk = input("Masukkan nama produk: ")
                    stok = int(input("Masukkan jumlah stok: "))
                    harga = int(input("Masukkan harga produk: "))
                    produk.append([nama_produk, stok, harga])
                    print(f"Produk {nama_produk} berhasil ditambahkan!")
                elif pilihan_admin == '3':
                    print("Produk Tersedia:")
                    for i, p in enumerate(produk):
                        print(f"{i+1}. {p[0]} - Stok: {p[1]}, Harga: {p[2]} RP")
                    pilihan_produk = int(input("Pilih nomor produk yang ingin diubah: ")) - 1
                    if 0 <= pilihan_produk < len(produk):
                        produk[pilihan_produk][0] = input("Masukkan nama baru produk: ")
                        produk[pilihan_produk][1] = int(input("Masukkan jumlah stok baru: "))
                        produk[pilihan_produk][2] = int(input("Masukkan harga baru: "))
                        print("Produk berhasil diubah!")
                    else:
                        print("Pilihan tidak valid!")
                elif pilihan_admin == '4':
                    print("Produk Tersedia:")
                    for i, p in enumerate(produk):
                        print(f"{i+1}. {p[0]} - Stok: {p[1]}, Harga: {p[2]} Rp")
                    pilihan_produk = int(input("Pilih nomor produk yang ingin dihapus: ")) - 1
                    if 0 <= pilihan_produk < len(produk):
                        del produk[pilihan_produk]
                        print("Produk berhasil dihapus!")
                    else:
                        print("Pilihan tidak valid!")
                elif pilihan_admin == '5':
                    print("Keluar Jadi Pengguna")
                    break
                else:
                    print("Pilihan tidak valid!")
            
            else:
                print("Menu Buat Pembeli Lampu Projie")
                print("1. Tampilkan Produk")
                print("2. Logout")
                pilihan_user = input("Masukkan pilihan: ")
                
                if pilihan_user == '1':
                    print("Produk Tersedia:")
                    for i, p in enumerate(produk):
                        print(f"{i+1}. {p[0]} - Stok: {p[1]}, Harga: {p[2]} RP")
                elif pilihan_user == '2':
                    break
                else:
                    print("Pilihan tidak valid!")
    
    elif pilihan == '2':
        print("Halo Pengguna baru! Ayo buat akun dulu")
        username_baru = input("Masukkan username: ")
        password_baru = input("Masukkan password: ")
        pengguna.append({'username': username_baru, 'password': password_baru, 'role': 'pengguna'})
        print(f"Akun Anda berhasil terdaftar dengan ID: {username_baru}")
    
    elif pilihan == '3':
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid!")