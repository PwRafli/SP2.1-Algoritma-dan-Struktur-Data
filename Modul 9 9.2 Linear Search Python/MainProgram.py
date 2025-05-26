import ClassLinear
import random

# Fungsi untuk menghasilkan array data secara acak
def GenerateElement():
    return random.sample(range(1, 100), 10)  # 10 angka acak dari 1 sampai 99

def MainMenu():
    element = GenerateElement()
    print("Data array: ", element)
    pilih = "y"
    while pilih.lower() == "y":
        print("\n[Menu Aplikasi Searching Data]")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Recursive Binary Search")
        print("=========================")

        pilihan = int(input("Masukkan pilihan: "))
        cariData = int(input("Masukkan data yang ingin dicari: "))

        if pilihan == 1:
            SearchLinear = ClassLinear.LinearSearching()
            Linear = SearchLinear.ProsesLinear(element, cariData)
            if Linear != -1:
                print("Data", cariData, "ditemukan pada indeks ke-:", Linear)
            else:
                print("Data tidak ditemukan")
        else:
            print("Menu sorting belum lengkap...")

        pilih = input("\nIngin mencari lagi? (y/n): ")

if __name__ == "__main__":
    MainMenu()

