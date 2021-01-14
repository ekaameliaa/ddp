import random
import string 

def singleList():
    for i in dataNasabah:
        for j in i:
            dataNasabah2.append(j)

def openFile():
    f = open('nasabah.txt')
    for each_line in f:
        data = each_line.split(",")
        dataNasabah.append([data[0], data[1], int(data[2])])
    f.close()


def menu():
    print("Menu: ")
    print("[1] Buka rekening\n[2] Setoran tunai\n[3] Tarik tunai\n[4] Transfer\n[5] Lihat daftar transfer\n[6] keluar")
print("*** SELAMAT DATANG DI BANK NF ***")
menu()
dataNasabah = []
dataNasabah2 = []
while True:
    pilihan = input('Masukan menu pilihan anda: ')
    if pilihan == '1':
        print('*** BUKA REKENING ***')
        name = input('Masukan nama anda: ')
        setoran_awal = int(input('Masukan setoran awal: '))
        norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
        print('Pembukaan rekening dengan nomor', norek, 'atas nama', name, 'berhasil')
        file_n = open('nasabah.txt', 'a+')
        file_n.write(norek + ',' + name + ',' + str(setoran_awal) + '\n')
        file_n.close()
        print()
        menu()
    elif pilihan == '2':
        print('*** SETORAN TUNAI ***')
        no_rek = input("Masukkan nomor rekening: ")
        nominal = int(input("Masukkan nominal yang akan disetor: "))
        no_rek = no_rek.upper()
        openFile()
        singleList()
        if no_rek in dataNasabah2:
            for i in dataNasabah:
                if i[0] == no_rek :
                    print('Setoran tunai sebesar ', nominal, ' ke rekening ', no_rek, ' berhasil') 
                    i[2] += nominal
                    file_n = open('nasabah.txt', 'w')
                    file_n.write('\n'.join(map(lambda x: ','.join(map(str, x)),  dataNasabah)))
                    file_n.close() 
                    break          
        else:
            print('Nomor rekening tidak terdaftar. Setoran tunai gagal')
        dataNasabah.clear()
        dataNasabah2.clear()
        print()
        menu()
    elif pilihan == '3' : 
        print('*** TARIK TUNAI ***')
        rek_tarik = input("Masukkan nomor rekening: ")
        nominal_tarik = int(input("Masukkan nominal yang akan ditarik: "))
        rek_tarik = rek_tarik.upper()
        openFile()
        singleList()
        if rek_tarik in dataNasabah2:
            for i in dataNasabah:
                if i[0] == rek_tarik:
                    if nominal_tarik > i[2]:
                        print('Saldo tidak mencukupi. Tarik tunai gagal')
                    elif nominal_tarik < i[2]:
                        i[2] -= nominal_tarik
                        file_n = open('nasabah.txt', 'w')
                        file_n.write('\n'.join(map(lambda x: ','.join(map(str, x)),  dataNasabah)))
                        file_n.close()
                        print('Tarik tunai sebesar ', nominal_tarik, ' ke rekening ', rek_tarik, ' berhasil')
                        break
        else:
            print('Nomor rekening tidak terdaftar. Tarik tunai gagal')
        dataNasabah.clear()
        dataNasabah2.clear()           
        print()
        menu()
    elif pilihan == '4' :
        print('*** TRANSFER ***')
        rekSumber = input('Masukkan nomor rekening sumber: ')
        rekTujuan = input('Masukkan nomor rekening tujuan: ')
        nom_Transfer = int(input('Masukkan nominal yang akan ditransfer: '))
        rekSumber = rekSumber.upper()
        rekTujuan = rekTujuan.upper()
        openFile()
        singleList()
        if rekSumber and rekTujuan in dataNasabah2:
            for i in dataNasabah:
                if i[0] == rekSumber:
                    if nom_Transfer > i[2]:
                        print('Saldo tidak mencukupi. Transfer gagal')
                    else:
                        i[2] -= nom_Transfer
                        for j in dataNasabah:
                            if j[0] == rekTujuan:
                                j[2] += nom_Transfer
                                file_n = open('nasabah.txt', 'w')
                                file_n.write('\n'.join(map(lambda x: ','.join(map(str, x)),  dataNasabah)))
                                Transfer = "TRF" + ''.join(random.choice(string.digits) for i in range(3))
                                print("Transfer sebesar", nom_Transfer, "dari rekening",
                                    rekSumber, "ke rekening", rekTujuan, "berhasil.")
                                file_n = open('transfer.txt', 'a+')
                                file_n.write(Transfer + ',' + rekSumber + ',' + rekTujuan + ',' + str(nom_Transfer) + '\n')
                                file_n.close()
                                break
        else: 
            print('Nomor rekening sumber atau rekening tujuan tidak terdaftar. Transfer gagal')           
        dataNasabah.clear()
        dataNasabah2.clear()
        print()
        menu()
    elif pilihan == '5':
        dataTransfer = []
        dataTransferSingle = []
        dataTransferSumber = []
        print('*** LIHAT DATA TRANSFER ***')
        rekTransfer = input('Masukkan nomor rekening sumber transfer: ')
        rekTransfer = rekTransfer.upper()
        file_n = open('transfer.txt')
        for each_line in file_n:
            data = each_line.split(",")
            dataTransfer.append([data[0], data[1], data[2], data[3]]) 
            dataTransferSumber.append(data[1])
        file_n.close()
        for i in dataTransfer:
            for j in i:
                dataTransferSingle.append(j)
        if rekTransfer in dataTransferSumber:
            for k in range(len(dataTransfer)):
                if rekTransfer == dataTransfer[k][1]:
                    print(dataTransfer[k][0], dataTransfer[k][1], dataTransfer[k][2], int(dataTransfer[k][3]))
        elif rekTransfer not in dataTransferSingle:
            print("Nomor rekening sumber tidak terdaftar.")
        else:
            print("Tidak ada data yang ditampilkan")
        print()
        menu()
    elif pilihan == "6":
        print("Terima kasih atas kunjungan Anda...")
        break

        