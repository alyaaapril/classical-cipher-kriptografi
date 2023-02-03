# file test untuk Standard Vigenere Cipher

import StandardVigenereCipher

plaintext = '''Dinas Pendidikan Kota Ternate meminta kepada pihak sekolah dan 
orang tua siswa untuk jenjang pendidikan SD dan SMP se-Kota Ternate 
untuk melarang para siswa membawa permainan lato-lato'''
key = input("masukkan key : ")

encryptedText = StandardVigenereCipher.encryptStandardVigenereCipher(plaintext,key)
decryptedText = StandardVigenereCipher.decryptStandardVigenereCipher(encryptedText, key)

print("Encrypted Text : ")
print(encryptedText)
print("Decrypted Text : ")
print(decryptedText)