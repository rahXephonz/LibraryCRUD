buku = []


def show_buku():
    if len(buku) <= 0:
        print("\nMAAF BELUM ADA DATA BUKU BARU.")
    else:
        print("\nOke,Ini adalah List Bukunya : \n")
        for indeks in range(len(buku)):
            print([indeks], " .", buku[indeks])


def tambah_buku():
    while (True):
        buku_baru = input("Masukan Nama Buku : ")
        buku.append(buku_baru)

        quest = input("Ingin menambah Buku lagi? (y/t) : ")
        if quest == 't':
            break

    print("\nTerima Kasih sudah menambahkan Buku! ^_^")


def edit_buku():
    show_buku()

    if len(buku) <= 0:
        print("SILAHKAN TAMBAH BUKU BARU!.")
    else:
        indeks = int(input("\nNomor Berapa yang ingin diUpdate? : "))
        if len(buku) <= 0:
            print("BELUM ADA DATA BUKU BARU.")
        elif indeks > len(buku):
            print("Input ID Salah!")
        else:
            judul_baru = input("Ganti dengan : ")
            buku[indeks] = judul_baru
            print("Penggantian nama buku menjadi", judul_baru)
            print("\nSukses!")


def hapus_buku():
    show_buku()

    if len(buku) <= 0:
        print("SILAHKAN TAMBAH BUKU BARU!.")
    else:
        indeks = int(input("\nNomor Berapa yang ingin dihapus? : "))
        if indeks > len(buku):
            print("Input ID Salah!")
        else:
            buku.remove(buku[indeks])
            print("\nPenghapusan Buku Berhasil!")


def show_menu():
    print("\n========SELAMAT DATANG DI PROGRAM PERPUSTAKAAN=========")
    print("=================SILAHKAN PILIH MENU==================\n")
    print("[1].Create Buku")
    print("[2].Delete Buku")
    print("[3].Read Buku")
    print("[4].Update Buku")
    print("[5].Keluar")

    menu = input("\nPilih MENU : ")
    if menu == '1':
        tambah_buku()
    elif menu == '2':
        hapus_buku()
    elif menu == '3':
        show_buku()
    elif menu == '4':
        edit_buku()
    elif menu == '5':
        print("Terima Kasih telah menggunakan program ini! ^_^\n")
        exit()


if __name__ == "__main__":

    while (True):
        show_menu()
