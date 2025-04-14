from queue import Queue

angka = int(input("masukkan bannyak angka:"));
q = Queue(maxsize=angka);
print("data awal: ", q.qsize());

for i in range(5):
    if q.qsize() < angka:
        q.put(input("masukkan data:"));
    else:
        print("data penuh");

q.put(input("masukkan data: "));
print("data hasil: ", q.qsize());
print(list(q.queue));

while q.qsize():
    tanya = input("apakah ingin mengeluarkan data?");
    if tanya == "y":
        print(q.get());

q.put("castorice");
q.put("Jingliu");
q.put("Acheron");
q.put("Lingsha");
q.put("Rappa");

print("\nFull: ", q.full());
print("\nElemen dequeue dari queue");
print(q.get());
print(q.get());
print(q.get());
print(q.get());
print(q.get());

print("\nKosong: ", q.empty());
q.put(angka);
print("\nKosong: ", q.empty());
print("\nFull: ", q.full());

