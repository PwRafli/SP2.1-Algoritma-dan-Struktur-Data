from queue import Queue

# Input kapasitas maksimal queue
angka = int(input("Masukkan banyak maksimal elemen dalam queue: "))
q = Queue(maxsize=angka)

print("\nJumlah data awal:", q.qsize())

# Input data pertama dari user
data_pertama = input("Masukkan data pertama: ")
if not q.full():
    q.put(data_pertama)
    print("Data dimasukkan:", data_pertama)
else:
    print("Queue sudah penuh, tidak bisa memasukkan data pertama.")

print("Jumlah data sekarang:", q.qsize())
print("Isi queue saat ini:", list(q.queue))

# Mengeluarkan data pertama
if not q.empty():
    print("Data di-dequeue:", q.get())
else:
    print("Queue kosong, tidak bisa dequeue.")

# Menambahkan data tambahan
data_tambahan = ["castorice", "Jingliu", "Acheron", "Lingsha", "Rappa"]

for item in data_tambahan:
    if not q.full():
        q.put(item)
        print("Menambahkan:", item)
    else:
        print("Queue penuh, tidak bisa menambahkan:", item)

print("\nApakah queue penuh?", q.full())

# Dequeue semua elemen
print("\nElemen dequeue dari queue:")
while not q.empty():
    print(q.get())

print("\nApakah queue kosong sekarang?", q.empty())

# Menambahkan angka input sebagai data ke dalam queue
if not q.full():
    q.put(angka)
    print(f"\nMenambahkan angka {angka} ke queue.")
else:
    print("\nQueue penuh, tidak bisa menambahkan angka.")

print("Apakah queue kosong?", q.empty())
print("Apakah queue penuh?", q.full())
