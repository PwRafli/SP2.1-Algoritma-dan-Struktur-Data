# ===== Class BubbleSorting =====
class BubbleSorting:
    def ProsesBubble(self, array):
        for i in range(len(array)):
            swapped = False
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
                    swapped = True
            if not swapped:
                break
            print("Proses Array iterasi ke-", (i + 1), ":", array)
        return array

# ===== Class LinearSearching =====
class LinearSearching:
    def ProsesLinear(self, array, key):
        for i in range(0, len(array)):
            if array[i] == key:
                return i
            else:
                print("Data pada indeks ke-", i, "(", array[i], ") Tidak sama dengan", key)
        return -1

# ===== Function Generate Data =====
def GenerateElement():
    dataelement = [39, 12, 18, 85, 72, 10, 2, 18, 44, 56]
    return dataelement

# ===== Main Menu =====
def MainMenu():
    element = GenerateElement()
    print("Data array awal: ", element)
    pilih = "y"
    while pilih.lower() == "y":
        print("\n=== Menu Aplikasi ===")
        print("1. Bubble Sort")
        print("2. Linear Search")
        print("=====================")
        
        pilihan = int(input("Masukkan pilihan (1/2): "))
        
        if pilihan == 1:
            bubble = BubbleSorting()
            hasil = bubble.ProsesBubble(element.copy())
            print("Data setelah diurutkan (Bubble Sort):", hasil)
        
        elif pilihan == 2:
            cari = int(input("Masukkan data yang ingin dicari: "))
            linear = LinearSearching()
            hasil = linear.ProsesLinear(element, cari)
            if hasil != -1:
                print(f"Data {cari} ditemukan pada indeks ke-{hasil}")
            else:
                print(f"Data {cari} tidak ditemukan dalam array.")
        
        else:
            print("Pilihan tidak tersedia.")
        
        pilih = input("\nApakah ingin mengulang? (y/n): ")

# ===== Program Utama =====
if __name__ == "__main__":
    MainMenu()
