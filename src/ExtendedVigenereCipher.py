# Program cipher klasik - extended vigenere cipher
# 256 karakter ascii
from tkinter.messagebox import showinfo

import fileOperation
from pathlib import Path

def isEqualLength(plaintext, key):
    if (len(plaintext) == len(key)) :
        return True
    else : 
        return False

def repeatKey(plaintextLength, key) :
    key = list(key)
    actualKey = []
    for i in (range(plaintextLength)):
        actualKey.append(key[i % len(key)])

    return actualKey

def encryptExtendedVigenereCipher(plaintext, key):
    encryptedText = []

    plaintext = list(plaintext)
    key = list(key)

    if (not(isEqualLength(plaintext, key))):
        key = repeatKey(len(plaintext), key)
   
    for i in range (len(plaintext)):
        asciiText = ord(plaintext[i])
        asciiKey = ord(key[i])
        encryptedValue = "" + chr(((asciiText + asciiKey) % 256) )
        encryptedText.append(encryptedValue)

    return("".join(encryptedText))

def decryptExtendedVigenereCipher(encryptedText, key):
    decryptedText = []

    encryptedText = list(encryptedText)
    key = list(key)

    if (not(isEqualLength(encryptedText, key))):
        key = repeatKey(len(encryptedText), key)

    for i in range (len(encryptedText)):
        decryptedValue ="" + chr((ord(encryptedText[i]) - ord(key[i]) + 256) % 256)
        decryptedText.append(decryptedValue)

    return("".join(decryptedText))

def encryptBinaryExtendedVigenereCipher(pathFile, key):
    f = fileOperation.readBinaryFile(pathFile)
    binary = f.decode("ISO-8859-1") # decode ke char
    encryptedText = encryptExtendedVigenereCipher(binary, key) # enkripsi dengan fungsi enkripsi 256 ASCII
    file_extension = Path(pathFile).suffix
    fileOperation.writeBinaryFile(f"encryption{file_extension}", encryptedText.encode("ISO-8859-1")) # ubah kembali file ke file extension yang sesuai
    print(f" Nama file enkripsi adalah encryption{file_extension}\n")
    showinfo("File encryption success", f"File saved with name encryption{file_extension}, please check it !")

def decryptBinaryExtendedVigenereCipher(pathFile, key):
    f = fileOperation.readBinaryFile(pathFile) 
    binary = f.decode("ISO-8859-1") # decode ke char
    decryptedText = decryptExtendedVigenereCipher(binary, key) # dekripsi dengan fungsi enkripsi 256 ASCII
    file_extension = Path(pathFile).suffix
    #print(decryptedText.encode("ISO-8859-1"))
    fileOperation.writeBinaryFile(f"decryption{file_extension}", decryptedText.encode("ISO-8859-1")) # ubah kembali file ke file extension yang sesuai
    print(f" Nama file enkripsi adalah encryption{file_extension}\n")
    showinfo("File decryption success", f"File saved with name decryption{file_extension}, please check it !")