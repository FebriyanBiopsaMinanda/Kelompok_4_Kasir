#KELOMPOK 4
#5210411203_Febriyan Biopsa Minanda
#5210411227_Revy Ravly Sabbathino Sahetapy
#5210411246_Febriana Fatimah Putri

import mysql.connector
import os
import datetime
import random

def rupiah(uang) :
    x = str(uang)
    if len(x) <= 3 :
        return "Rp." + x + '.000'
    else :  #Kelompok 4
        a = x[:-3]
        b = x[-3:]
        return "Rp." + a + '.' + b 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def kembali():
    print("\n")
    input("Tekan tombol enter untuk kembali...")
    clear_screen()#Kelompok 4

class Pegawai :
    def __init__(self, nama, alamat, tgl_lahir) :
        self.nama = nama#Kelompok 4
        self.alamat = alamat
        self.tgl_lahir = tgl_lahir

class Produk:
    def connector():
        return mysql.connector.connect (host = "localhost" , user = "root" , password = "" , database = "kasirpbo")
     #Kelompok 4
    def tampil():
        con = Produk.connector()
        cur = con.cursor()
        cur.execute("SELECT * FROM databarang")
        print(f"\n\t\tDATA BARANG")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Nama\t: {x[0]}")#Kelompok 4
            print(f"Harga\t: {x[1]}/{x[2]}\n") 
        print("==============================================\n\n")
        kembali()
        

    def tambah():
        try :
            con = Produk.connector()
            cur = con.cursor()
            nama = input("Masukan Nama\t: ")
            harga = input("Masukan Harga\t: ")
            satuan = input("Masukan Satuan\t: ")
            sql = ("INSERT INTO databarang (nama , harga , satuan) VALUES (%s,%s,%s)")
            data = ( nama, harga, satuan)
            cur.execute(sql,data)#Kelompok 4
            con.commit()
            print ("\nData Berhasil diTambahkan")
        except :
            print("\nData Tidak Berhasil Di Tambahkan")
        kembali()

    def cari(nama ):
        con = Produk.connector()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM databarang  WHERE nama LIKE '%{nama}%'")
        print(f"\nHasil Pencarian dari {nama}")
        print("==============================================")
        for x in cur.fetchall() :
            print(f"Nama\t: {x[0]}")#Kelompok 4
            print(f"Harga\t: {x[1]}/{x[2]}")  
        print("==============================================\n\n")
        kembali()

    def update(nama):
        con = Produk.connector()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM databarang  WHERE nama LIKE '%{nama}%'")
        try :
            for x in cur.fetchall() :#Kelompok 4
                if nama in x[0] :
                    harga = input("Masukan Harga Baru : ")
                    sql = ("UPDATE databarang SET harga=%s WHERE nama LIKE %s")
                    data = (harga, nama)
                    cur.execute(sql, data)
                    con.commit()
                    print(f"\nHarga {nama} Berhasil Di Edit")
                    print("==============================================")
                    print(f"Nama\t: {x[0]}")
                    print(f"Harga\t: {harga}/{x[2]}")  
                    print("==============================================\n\n")
        except :
            print("\nData Tidak Berhasil Di Edit")
        kembali()
#Kelompok 4
    def hapus(nama):
        con = Produk.connector()
        cur = con.cursor()
        cur.execute(f"SELECT * FROM databarang  WHERE nama LIKE '%{nama}%'")
        try :
            for x in cur.fetchall() :
                if nama in x[0] :
                    cur.execute(f"DELETE FROM databarang WHERE nama LIKE '%{nama}%'")
                    con.commit()
                    print(f"\n{nama} Berhasil Di Hapus")
        except :
            print("Data Tidak Berhasil Di Hapus")
        kembali()
    

class Transaksi :
    def kasir() :
        try :#Kelompok 4
            kd_transaksi = (f"U2F{random.randint(1,10)}KASIR{random.choice('KELOMPOK4')}")
            localtime = datetime.datetime.now()
            con = Produk.connector()
            cur = con.cursor()
                
            cur.execute("SELECT * FROM databarang")
            print("\n\t\tLIST NAMA BARANG")
            print("==============================================")
            for x in cur.fetchall() :
                print(f"  {x[0]} : {x[1]}/{x[2]}") 
            print("==============================================\n\n")
            data = []
            jmlhbrg = []#Kelompok 4
            price = []
            while True :
                nama = input("Masukan Nama Barang : ")
                cur.execute(f"SELECT * FROM databarang  WHERE nama LIKE '%{nama}%'")
                for x in cur.fetchall() :
                    barang = x[0]
                    harga = int(x[1])
                    jmlh = int(input("Masukan Jumlah Barang : "))
                    subjmlh = harga * jmlh
                    data.append(barang)
                    jmlhbrg.append(jmlh)
                    price.append(subjmlh)
                next = input("Lanjut (y/t) :")
                total = 0
                    
                if next == 'y' :#Kelompok 4
                    cur.execute(f"SELECT * FROM databarang  WHERE nama LIKE '%{nama}%'")
                    for x in cur.fetchall() :
                        barang = x[0]
                        harga = int(x[1])
                        
                    
                elif next == 't' :
                    break

            for item in price :
                total += item
            print(f"Barang\t: {data}")
            print(f"Harga\t: {price}")#Kelompok 4
            print(f"Total\t: {total}")
            uang = int(input("Masukan Uang Bayar : "))
            clear_screen()
            print("\t\tKASIR KELOMPOK 4")
            print("==============================================")
            print(f"Kode\t: {kd_transaksi}\nTGL\t: {localtime.date()}")
            print(f"Pegawai\t: Admin\n")
            print("==============================================")
            print(f"Barang\t\t: {data}")
            print(f"Jumlah Barang\t: {jmlhbrg}")
            print(f"Harga\t\t: {price}")
            print("==============================================\n")
            print(f"Total\t\t: {rupiah(total)}")
            print(f"Uang\t\t: {rupiah(uang)}")
            if (uang > total) :
                print(f"Kembalian\t: {rupiah(uang - total)}")
            elif (uang == total) :
                print ("Uang Pas")
            elif (uang < total) :
                print (f"Uang Kurang\t: {rupiah(uang - total)}")
        except :#Kelompok 4
            print("\nEror / Transaksi Gagal")
        kembali()