# file test untuk Extended Vigenere Cipher

import ExtendedVigenereCipher

plaintext = '''This article is contributed by Ayush Khanduri. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org'''
key = '''team@geeksforgeeks.org'''
key_1 = '''teamvlgjuarakri'''

print("".join(ExtendedVigenereCipher.repeatKey(len(plaintext), key)))
print("\n")
encrypt = ExtendedVigenereCipher.encryptExtendedVigenereCipher(plaintext, key)
print("Hasil Enkripsi :", encrypt)
print("\n")
print(list(encrypt))
print("\nDekripsi dengan kunci salah :")
print(ExtendedVigenereCipher.decryptExtendedVigenereCipher(encrypt, key_1))
print("\nDekripsi dengan kunci benar :",ExtendedVigenereCipher.decryptExtendedVigenereCipher(encrypt, key))

x = '''ÈÍÊà`È×ÙÔÖÒÔÐØ
ÎâãäÐÖÚÕÒ¤ÇÞ´ßäåÏ
°ÓÔÓçÙÝ¶¦ÞÔàÒØÝÌ
¬ÐØâØÖæ¬ÆÒ«Ú
ÆÙ×æáÜÑÉßÚ×èÔÐ¯ÕÙ×ÔÕÛã×
ÞÚèNÒÓÕÆÍà¯Ü×ÔçËÓÕ
ÆÝçÒÞÌÚÔÖ®Î
ÜuåÏã×ÌÊÐÞ
¡ÕáÙÛÊÆØ³Ô×Ò'''
print("\nDekripsi dengan kunci yg di copy di terminal :",ExtendedVigenereCipher.decryptExtendedVigenereCipher(x, key))
