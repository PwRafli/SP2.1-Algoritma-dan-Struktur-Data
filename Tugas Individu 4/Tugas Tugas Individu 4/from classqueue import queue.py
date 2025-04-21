from classqueue import Queue

def main():
    q = Queue()
    pilih = "Y"
    while pilih == "Y":
        print("| Menu Aplikasi Queue |")
        print("1. Tambah Data (enqueue)")
        print("2. Hapus Data (dequeue)")
        print("3. Cek Panjang Queue")
        print("4. Cek Ukuran Maksimal Queue")
        print("5. Cek Jika Queue Kosong")
        print("6. Cek Jika Queue Penuh")
        print("============================")

        pilihan = str(input("Masukkan pilihan: "))
        if pilihan == "1":
            obj = str(input("Data yang ingin ditambahkan: "))
            q.enqueue(obj)
        elif pilihan == "2":
            q.dequeue()
        elif pilihan == "3":
            print(f"Panjang queue saat ini: {q.queue_length()}")
        elif pilihan == "4":
            print(f"Ukuran maksimal queue: {q.max_queue_size()}")
        elif pilihan == "5":
            print(f"Apakah queue kosong? {q.check_empty()}")
        elif pilihan == "6":
            print(f"Apakah queue penuh? {q.check_full()}")
        else:
            print("Pilihan tidak valid.")

        pilih = str(input("Apakah Anda ingin melanjutkan? (Y/N): ")).upper()

if __name__ == "__main__":
    main()