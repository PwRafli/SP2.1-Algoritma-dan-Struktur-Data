from queue import Queue

angka = int(input("Masukkan kapasitas maksimal queue: "))
q = Queue(maxsize=angka)
print("Data awal: ", q.qsize())

data_set = set()  # untuk mendeteksi data duplikat

for i in range(angka):
    data = input(f"Masukkan data ke-{i+1}: ").strip()
    if not data:
        print("⚠️  Error: Data tidak boleh kosong!")
        continue
    if data in data_set:
        print("⚠️  Data sudah ada!")
        continue
    if q.full():
        print("⚠️  Queue sudah penuh!")
        break
    q.put(data)
    data_set.add(data)

# Coba menambahkan data baru
data_baru = input("Masukkan data tambahan: ").strip()
if not data_baru:
    print("⚠️  Error: Data tidak boleh kosong!")
elif q.full():
    print("⚠️  Tidak bisa menambah, queue penuh.")
elif data_baru in data_set:
    print("⚠️  Data sudah ada!")
else:
    q.put(data_baru)
    data_set.add(data_baru)

# Tampilkan hasil
print("\n📦 Hasil akhir queue:")
print("Jumlah data:", q.qsize())
print("Isi queue:", list(q.queue))

# Coba dequeue
if not q.empty():
    removed = q.get()
    print("🚮 Data dikeluarkan dari queue:", removed)
    data_set.discard(removed)
else:
    print("⚠️  Tidak ada data untuk di-dequeue.")

# Tambahkan beberapa data lagi
for name in ["castorice", "Jingliu", "Acheron", "Lingsha", "Rappa"]:
    if q.full():
        print(f"⚠️  Tidak bisa menambah '{name}', queue penuh.")
    elif name in data_set:
        print(f"⚠️  Data '{name}' sudah ada.")
    else:
        q.put(name)
        data_set.add(name)
        print(f"✅ '{name}' berhasil ditambahkan.")

print("\n✅ Apakah queue penuh? ", q.full())

print("\n🚮 Elemen-elemen yang dikeluarkan dari queue:")
while not q.empty():
    removed = q.get()
    print("Dequeued:", removed)
    data_set.discard(removed)

print("\n❌ Apakah queue kosong? ", q.empty())

# Tambahkan data baru lagi setelah kosong
q.put("AngkaBaru")
data_set.add("AngkaBaru")
print("\n✅ Apakah queue kosong? ", q.empty())
print("✅ Apakah queue penuh? ", q.full())
