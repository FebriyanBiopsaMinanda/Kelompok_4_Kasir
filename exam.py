import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


import os

def clear_console():
    os.system('cls')
    
    
while True :
    clear_console()
    print("=======================\n    PILIHAN MENU \n=======================")
    print("1. READ DATA ")  #FEBRIYAN BIOPSA MINANDA
    print("2. JUMLAH MISSING VALUE")
    print("3. EDIT DATA")
    print("4. UBAH NUMERIK")
    print("5. DATA FEATURE SCALLING")
    print("0. selesai")
    menu = input("Pilihan Menu : ") 
    
    
    # READ DATA
    if menu == '1' :
        try :
            read_csv = pd.read_csv('soal.csv')
            
            clear_console()
            print("=======================\n    DATA \n=======================")
            print(read_csv, '\n')
        except :
            print(f"\n=======================\n  Something Wrong  \n=======================")
    
    # MISSING VALUE
    elif menu == '2' :
        try :
            kolom  = []
                
            for head in read_csv :
                kolom.append(head)
                
            print(f"Nama Kolom : {kolom}")
            pilihan = input("Masukan Kolom : ")
            
            read_kolom = read_csv[pilihan]
            banyak_missing = read_kolom.isnull().sum().sum()
            
            clear_console()
            print(f"=======================\n  Banyak Missing = {banyak_missing}  \n=======================")
        except :
            print(f"\n=======================\n  Something Wrong  \n=======================")
        
    # EDIT DATA    
    elif menu == '3' :
        try :
            kolom  = []
            
            for head in read_csv :
                kolom.append(head)
            
            clear_console()
            print("\n=======================\n    EDIT DATA \n=======================")   
            print(f"Nama Kolom : {kolom}")
            pilihan = input("Masukan Kolom : ")
            index = 0
            for row in read_csv[pilihan].isnull() :
                try :
                    print("\n=======================\n    TYPE DATA \n=======================")
                    print("1. String")  #FEBRIYAN BIOPSA MINANDA
                    print("2. Integer")
                    if row == True :
                        pilih = input("Masukan Pilihan : ")
                        
                        if pilih == '1' :
                            value = input("\nMasukan Data (str): ")
                        elif pilih == '2' :
                            value = int(input("\nMasukan Data (int): "))
                        read_csv.loc[index] = read_csv.loc[index].fillna(value = value)
                        ubah = read_csv.loc[index]
                except ValueError:
                    pass
                index = index + 1
            print("\n=======================\n    DATA \n=======================")
            print(read_csv, '\n')
        except :
            print(f"\n=======================\n  Something Wrong  \n=======================") 
            
            
    # UBAH NUMERIK        
    elif menu == '4' :
        try :
            label = LabelEncoder()
            ubah
            
            clear_console()
            print("=======================\n    DATA  \n=======================\n")
            print(read_csv, '\n')
            for col in read_csv.columns.values :
                if read_csv[col].dtypes == 'object' :
                    data = read_csv[col].append(read_csv[col])
                    label.fit(data.values)
                    read_csv[col] = label.transform(read_csv[col])
            
            print("\n=======================\n    DATA NUMERIK \n=======================")
            print(read_csv, '\n')
        except :
            print(f"\n=======================\n  Something Wrong  \n=======================")
            
            
    # FEATURE SCALLING 
    elif menu == '5' :
        try :
            ubah
            kolom  = ['nama_barang', 'jumlah_barang', 'jenis_barang']
            
            scalling = MinMaxScaler()
            data = read_csv.loc[0:, kolom]
            scale = scalling.fit_transform(data)
            data = scale

            read_csv.loc[0:, kolom] = data
            
            clear_console()
            print("=======================\n    FEATURE SCALLING \n=======================")
            print(read_csv, '\n')
        except :
            print(f"\n=======================\n  Something Wrong  \n=======================")
        
    elif menu == '0' :
        break
    
    else : #FEBRIYAN BIOPSA MINANDA
        print("PILIHAN TIDAK ADA DI MENU\n")
    input("\n\nEnter untuk Melanjutkan...")