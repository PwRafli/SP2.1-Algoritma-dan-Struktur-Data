from classstack import stack
def main():
    s = stack();
    pilih = "Y";
    while (pilih == "Y"):        
        print("|menu aplikasi stack|");
        print("1. push");
        print("2. pop object");
        print("3. cek empty");
        print("4. tampilan objeck terakhir");
        print("5. panjang dari stack");
        print("============================")

        pilihan = str(input("masukkan pilihan:"));
        if pilihan == "1":
            print("hallo");
            obj = str(input("objeck yang ingin ditambhakan:"));
            s.push(obj);
            print("objeck " + s.pop() + " dihapus");
        elif pilihan == "2":
            print("objeck" + s.pop() + "dihapus");
        elif pilihan == "3":
            print(s.isEmpty());
        elif pilihan == "4":
            print("objeck terakhir: " + s.peek());
        else:
            print("panjang dari stack adalah: " + str(s.size()));

if __name__ == "__main__":
    main()