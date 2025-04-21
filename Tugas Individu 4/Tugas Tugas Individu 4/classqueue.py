class Queue:
    def __init__(self):
        self.items = []
        self.max_size = 5  # Ukuran maksimal queue

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            print("Queue penuh! Tidak dapat menambahkan data.")
        else:
            self.items.append(item)
            print(f"Data {item} ditambahkan ke queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue kosong! Tidak dapat menghapus data.")
            return None
        else:
            removed_item = self.items.pop(0)  # Menghapus item dari depan
            print(f"Data {removed_item} dihapus dari queue.")
            return removed_item

    def queue_length(self):
        return len(self.items)

    def max_queue_size(self):
        return self.max_size

    def check_empty(self):
        return self.is_empty()

    def check_full(self):
        return self.is_full()