from modul import Produk, Transaksi
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kembali():
    print("\n")
    input("Tekan tombol enter untuk kembali...")
    clear_screen()
db = Produk
Tsk = Transaksi


while True :
    clear_screen()
    print("=======================\n    Pilihan \n=======================")
    print("1. Tampil Barang")
    print("2. Tambah Barang")
    print("3. Cari Barang")
    print("4. Edit Barang")
    print("5. Hapus Barang")
    print("6. Transaksi")
    print("0. Selesai")
    pilihan = input("Masukan Pilihan : ")
    
    if pilihan == '1' :
        db.tampil()

    elif pilihan == '2' :
        db.tambah()

    elif pilihan == '3' :
        nama = input("Masukan Nama Yang ingin di Cari : ")
        db.cari(nama)

    elif pilihan == '4' :
        nama = input("Masukan Nama Yang ingin di Edit : ")
        db.update(nama)

    elif pilihan == '5' :
        nama = input("Masukan Nama Yang ingin di Hapus : ")
        db.hapus(nama)
  
    elif pilihan == '6' :
        Tsk.kasir()

    elif pilihan == '0' :
        clear_screen()
        break
        
    else :
        print("Pilihan Tidak Ada di Menu")
        kembali()