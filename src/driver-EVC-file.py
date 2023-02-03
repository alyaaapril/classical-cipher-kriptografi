from fileOperation import *
from ExtendedVigenereCipher import *

namaFile = input("Masukkan nama file : ")
key = input("Masukkan file key : ")

print(f"Hasil baca File {namaFile}: ")
print(readBinaryFile(namaFile))

print(f"\nTipe data hasil bacaan {namaFile}: ")
print(type(readBinaryFile(namaFile)))

print(f"\nHasil enkripsi File {namaFile} dengan key {key}: ")
encryption = encryptExtendedVigenereCipher(namaFile, key)
print(encryption)
encryptionFile = writeBinaryFile('encrypted.dat', encryption)

print(f"\nHasil dekripsi File enkripsi sebelumnya dengan key {key}: ")
decryption = decryptExtendedVigenereCipher(encryptionFile, key)
print(decryption)
encryptionFile = writeBinaryFile('decrypted.dat', encryption)