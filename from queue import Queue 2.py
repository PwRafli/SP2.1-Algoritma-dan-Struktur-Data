from queue import Queue

def tambah_data(q):
    """Menambahkan data ke dalam queue."""
    if q.qsize() < q.maxsize:
        data = input("masukkan data: ")
        q.put(data)
        print(f"Data '{data}' berhasil ditambahkan.")
    else:
        print("Data penuh")

def keluarkan_data(q):
    """Mengeluarkan data dari queue jika ada."""
    if not q.empty():
        return q.get()
    else:
        print("Queue kosong, tidak ada data untuk dikeluarkan.")
        return None

def tampilkan_status(q):
    """Menampilkan status queue."""
    print("Jumlah data dalam queue: ", q.qsize())
    print("Isi queue: ", list(q.queue))
    print("Apakah queue penuh? ", q.full())
    print("Apakah queue kosong? ", q.empty())

def main():
    angka = int(input("masukkan banyak angka: "))
    q = Queue(maxsize=angka)
    print("data awal: ", q.qsize())

    for i in range(5):
        tambah_data(q)

    tampilkan_status(q)

    while q.qsize():
        tanya = input("apakah ingin mengeluarkan data? (y/n): ")
        if tanya.lower() == "y":
            data_keluar = keluarkan_data(q)
            if data_keluar is not None:
                print(f"Data yang dikeluarkan: {data_keluar}")

    # Menambahkan data tambahan
    for item in ["castorice", "Jingliu", "Acheron", "Lingsha", "Rappa"]:
        q.put(item)

    print("\nElemen dequeue dari queue:")
    while not q.empty():
        print(keluarkan_data(q))

    tampilkan_status(q)

    # Menambahkan angka ke queue
    q.put(angka)
    tampilkan_status(q)

if __name__ == "__main__":
    main()