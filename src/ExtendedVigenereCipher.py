# Program cipher klasik - extended vigenere cipher
# 256 karakter ascii

import fileOperation

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

    binaryText = fileOperation.readBinaryFile(plaintext)
    binaryKey = fileOperation.readBinaryFile(key)
    binaryText = list(binaryText)
    binaryKey = list(binaryKey)

    if (not(isEqualLength(binaryText, binaryKey))):
        binaryKey = repeatKey(len(binaryText), binaryKey)
   
    for i in range (len(binaryText)):
        encryptedValue = (binaryText[i] + binaryKey[i]) % 256
        encryptedText.append(encryptedValue)

    return(encryptedText)

def decryptExtendedVigenereCipher(encryptedText, key):
    decryptedText = []

    binaryText = fileOperation.readBinaryFile(encryptedText)
    binaryKey = fileOperation.readBinaryFile(key)
    binaryText = list(binaryText)
    binaryKey = list(binaryKey)

    if (not(isEqualLength(binaryText, binaryKey))):
        binaryKey = repeatKey(len(binaryText), binaryKey)

    for i in range (len(binaryText)):
        decryptedValue =(((binaryText[i] - binaryKey[i]) + 256) % 256)
        decryptedText.append(decryptedValue)

    return(decryptedText)