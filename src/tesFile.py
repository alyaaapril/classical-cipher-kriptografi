from fileOperation import *
from ExtendedVigenereCipher import *

namaFile = input("Masukkan nama file : ")
key = input("Masukkan file key : ")
#print(readFile(namaFile))
print(f"Hasil baca File {namaFile}: ")
print(readBinaryFile(namaFile))

print(f"\nTipe data hasil bacaan {namaFile}: ")
print(type(readBinaryFile(namaFile)))

# Belum berhasil write ke binary
'''
print(f"\nHasil enkripsi File {namaFile} dengan key {key}: ")
encryption = encryptExtendedVigenereCipher(namaFile, key)
print(encryption)
encryptionFile = writeBinaryFile('encrypted.dat', encryption)
'''


