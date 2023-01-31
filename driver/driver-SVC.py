import sys
sys.path.append("..")

from src import StandardVigenereCipher

plaintext = input("masukkan plaintext : ")
key = input("masukkan key : ")

encryptedText = StandardVigenereCipher.encryptStandardVigenereCipher(plaintext,key)
decryptedText = StandardVigenereCipher.decryptStandardVigenereCipher(encryptedText, key)

print("Encrypted Text : ")
print(encryptedText)
print("Decrypted Text : ")
print(decryptedText)