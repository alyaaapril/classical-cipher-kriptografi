from fileOperation import *
from ExtendedVigenereCipher import *
from pathlib import Path
#namaFile = 'D:\SEM6\Kriptografi dan Koding\Code\Tugas1\classical-cipher-kriptografi\src\eanya.jpg'
#key = input("Masukkan file key : ")
#
#print(f"\nHasil enkripsi File : ")
#encryptBinaryExtendedVigenereCipher(namaFile, key)
#
#file2 = input("Masukkan nama file : ")
#key2 = input("Masukkan file key : ")
#
#d = fileOperation.readBinaryFile('D:\SEM6\Kriptografi dan Koding\Code\Tugas1\classical-cipher-kriptografi\src\eanya.jpg')
#print(d)
#print(f"\nHasil dekripsi File enkripsi sebelumnya dengan key : ")
#decryptBinaryExtendedVigenereCipher(file2, key2)

encryptBinaryExtendedVigenereCipher('D:\SEM6\Kriptografi dan Koding\Code\Tugas1\classical-cipher-kriptografi\src\eanya.jpg', 'coba')
decryptBinaryExtendedVigenereCipher('D:\SEM6\Kriptografi dan Koding\Code\Tugas1\encryption.jpg', 'coba')
