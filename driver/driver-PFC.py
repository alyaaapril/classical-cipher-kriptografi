# file test untuk Playfair Cipher
#from pathlib import Path

#from PlayfairCipher import *
import sys

sys.path.append(r"../src/")

# aku gatau gimana cara import function dri folder yg berbeda
# ini tes nya dibuat di folder yg sama dengan filenya

# Change Key Matrix
key = input("Your Key:")
key = playfair.removeSpecialCharacter(key)
key = key.replace(" ", "")
key = key.upper()

arr_key = playfair.key_into_arr(key)
print(arr_key)
key_matrix = playfair.full_arrkey(arr_key)
print(key_matrix)
mtrix = playfair.matrix(0, 5, 5)
cip_mat = playfair.matrix_cipher(mtrix, key_matrix)
print(cip_mat)
playfair.square(cip_mat)

# Check the location of each char in key
idx_locate = input("location of index: ")
print(playfair.idxlocator(idx_locate, cip_mat))

# input plaintext
plaintxt = input("Plain Text: ")
plaintxt = playfair.removeSpecialCharacter(plaintxt)
plaintxt = plaintxt.replace(" ", "")
plaintxt = plaintxt.upper()

# Encryption
playfair.encrypt(plaintxt, cip_mat)

# Decryption
cipher_text = input("\nCipher Text: ")
cipher_text = cipher_text.replace(" ","")
cipher_text = cipher_text.upper()
playfair.decrypt(cipher_text, cip_mat)