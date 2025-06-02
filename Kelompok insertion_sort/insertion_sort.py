# insertion_sort_module.py

# insertion_sort_module.py

class InsertionSorter:
    def __init__(self, data):
        self.data = data

    def sort(self, descending=False):
        arr = self.data.copy()
        order = "descending" if descending else "ascending"
        print(f"\n--- Proses sorting ({order}) ---")

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            print(f"Iterasi {i}: key = {key}, array = {arr}")

            if descending:
                while j >= 0 and key > arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
            else:
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1

            arr[j + 1] = key
            print(f"         setelah penyisipan: {arr}")

        return arr

