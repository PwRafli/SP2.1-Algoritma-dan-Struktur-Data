from queue import Queue

def tambah_data(q):
    """Menambahkan data ke dalam queue."""
    if q.qsize() < q.maxsize:
        data = input("Masukkan data untuk ditambahkan: ")
        q.put(data)
        print(f"Data '{data}' berhasil ditambahkan.")
    else:
        print("Queue sudah penuh, tidak bisa menambahkan data.")

def hapus_data(q):
    """Mengeluarkan data dari queue jika ada."""
    if not q.empty():
        data_keluar = q.get()
        print(f"Data yang dikeluarkan: {data_keluar}")
    else:
        print("Queue kosong, tidak ada data untuk dikeluarkan.")

def tampilkan_status(q):
    """Menampilkan status queue."""
    print("Jumlah data dalam queue: ", q.qsize())
    print("Isi queue: ", list(q.queue))
    print("Apakah queue penuh? ", q.full())
    print("Apakah queue kosong? ", q.empty())

def main():
    angka = int(input("Masukkan banyak angka: "))
    q = Queue(maxsize=angka)
    print("Data awal: ", q.qsize())

    # Menambahkan data awal
    for i in range(5):
        tambah_data(q)

    tampilkan_status(q)

    # Mengelola pengeluaran data
    while True:
        tanya = input("Apakah ingin mengeluarkan data? (y/n): ")
        if tanya.lower() == "y":
            hapus_data(q)
        elif tanya.lower() == "n":
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' atau 'n'.")

    # Menambahkan data tambahan
    for item in ["castorice", "Jingliu", "Acheron", "Lingsha", "Rappa"]:
        if not q.full():
            q.put(item)
            print(f"Data '{item}' berhasil ditambahkan.")
        else:
            print("Queue sudah penuh, tidak bisa menambahkan data tambahan.")

    print("\nElemen dequeue dari queue:")
    while not q.empty():
        hapus_data(q)

    tampilkan_status(q)

    # Menambahkan angka ke queue
    if not q.full():
        q.put(angka)
        print(f"Data '{angka}' berhasil ditambahkan ke queue.")
    tampilkan_status(q)

if __name__ == "__main__":
    main()