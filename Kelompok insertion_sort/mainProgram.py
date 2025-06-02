# main_program.py

from insertion_sort import InsertionSorter

def get_preset_array():
    print("\nPilih data array:")
    print("1. Acak       : [8, 4, 1, 3, 7, 6, 2, 5]")
    print("2. Sudah urut : [1, 2, 3, 4, 5, 6, 7, 8]")
    print("3. Input manual")

    while True:
        choice = input("Pilihan Anda [1/2/3]: ").strip()
        if choice == '1':
            return [8, 4, 1, 3, 7, 6, 2, 5]
        elif choice == '2':
            return [1, 2, 3, 4, 5, 6, 7, 8]
        elif choice == '3':
            return get_user_input()
        else:
            print("Pilihan tidak valid. Coba lagi.")

def get_user_input():
    while True:
        try:
            raw = input("Masukkan angka dipisahkan spasi (contoh: 9 4 16 1 5): ")
            return list(map(int, raw.strip().split()))
        except ValueError:
            print("Input tidak valid. Pastikan hanya angka.")

def get_sort_order():
    while True:
        order = input("Urutkan secara ascending atau descending? [a/d]: ").lower()
        if order in ['a', 'd']:
            return order == 'd'
        print("Pilihan tidak valid. Masukkan 'a' atau 'd'.")

def main():
    print("=== Program Insertion Sort ===")
    array = get_preset_array()
    descending = get_sort_order()

    sorter = InsertionSorter(array)
    print("\nSebelum sort:", array)

    sorted_array = sorter.sort(descending=descending)
    print("\nSesudah sort:", sorted_array)

if __name__ == "__main__":
    main()
