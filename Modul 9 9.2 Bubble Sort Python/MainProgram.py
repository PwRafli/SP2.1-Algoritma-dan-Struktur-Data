import ClassBubble

from ClassBubble import BubbleSorting

def GenerateElement():
    dataelement = [39, 12, 18, 85, 72, 10, 2, 18, 44, 56]
    return dataelement

def MainMenu():
    element = GenerateElement()
    print("Data array sebelum sorting:", element)
    pilih = "y"
    while pilih == "y":
        print("\n|Menu Aplikasi Sorting Data|")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("=======================")
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            Bubble = SortingBubble.ProsesBubble(element)
            print("Data array setelah sorting menggunakan Bubble Sort:", Bubble)
        else:
            print("Menu sorting belum lengkap...")
        pilih = input("Apakah ingin kembali ke menu? (y/n): ")

if __name__ == "__main__":
    SortingBubble = BubbleSorting()
    MainMenu()
