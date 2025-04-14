from queue import Queue

# Inisialisasi queue
angka = int(input("Masukkan kapasitas maksimal queue: "))
q = Queue(maxsize=angka)
data_list = []  # Untuk penyimpanan dan pengelolaan
data_set = set()  # Untuk mengecek data yang sudah ada

def tampilkan_data():
    print("\n📦 Data saat ini:")
    if data_list:
        for idx, data in enumerate(data_list):
            print(f"{idx + 1}. {data}")
    else:
        print("❌ Tidak ada data.")

def simpan_ke_file():
    with open("data_queue.txt", "w") as file:
        for item in data_list:
            file.write(f"{item}\n")
    print("✅ Data berhasil disimpan ke file 'data_queue.txt'.")

while True:
    print("\n📋 Menu:")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Hapus data pertama")
    print("4. Hapus data berdasarkan nama")
    print("5. Hapus data berdasarkan nomor")
    print("6. Hapus semua data")
    print("7. Simpan data ke file")
    print("8. Keluar")

    pilihan = input("Pilih menu (1-8): ").strip()

    if pilihan == "1":
        if q.full():
            print("⚠️  Queue penuh! Tidak bisa menambah data.")
            continue
        data = input("Masukkan data: ").strip()
        if not data:
            print("⚠️  Error: Data tidak boleh kosong!")
        elif data in data_set:
            print("⚠️  Data sudah ada!")
        else:
            q.put(data)
            data_list.append(data)
            data_set.add(data)
            print("✅ Data berhasil ditambahkan.")
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        if data_list:
            removed = q.get()
            data_list.remove(removed)
            data_set.discard(removed)
            print(f"🗑️ Data '{removed}' dihapus dari queue.")
        else:
            print("❌ Tidak ada data untuk dihapus.")
    elif pilihan == "4":
        nama = input("Masukkan nama data yang ingin dihapus: ").strip()
        if nama in data_list:
            data_list.remove(nama)
            data_set.discard(nama)
            q.queue.remove(nama)
            print(f"🗑️ Data '{nama}' berhasil dihapus.")
        else:
            print("❌ Data tidak ditemukan.")
    elif pilihan == "5":
        tampilkan_data()
        try:
            nomor = int(input("Masukkan nomor data yang ingin dihapus: "))
            if 1 <= nomor <= len(data_list):
                nama = data_list[nomor - 1]
                data_list.remove(nama)
                data_set.discard(nama)
                q.queue.remove(nama)
                print(f"🗑️ Data nomor {nomor} ('{nama}') berhasil dihapus.")
            else:
                print("⚠️  Nomor tidak valid.")
        except ValueError:
            print("⚠️  Input bukan angka.")
    elif pilihan == "6":
        konfirmasi = input("Yakin ingin menghapus semua data? (y/n): ").lower()
        if konfirmasi == "y":
            data_list.clear()
            data_set.clear()
            with q.mutex:
                q.queue.clear()
            print("🗑️ Semua data berhasil dihapus.")
    elif pilihan == "7":
        simpan_ke_file()
    elif pilihan == "8":
        print("\n🚪 Keluar dari program.")
        break
    else:
        print("⚠️  Pilihan tidak valid.")

