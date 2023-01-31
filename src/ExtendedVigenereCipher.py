# Program cipher klasik vifenere cipher
# 26 huruf alfabet

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

    plaintext = list(plaintext.upper())
    key = list(key.upper())

    if (not(isEqualLength(plaintext, key))):
        key = repeatKey(len(plaintext), key)
   
    for i in range (len(plaintext)):
        asciiText = ord(plaintext[i])
        asciiKey = ord(key[i])
        encryptedValue = "" + chr((asciiText + asciiKey) % 256)
        encryptedText.append(encryptedValue)

    return("".join(encryptedText))

def decryptExtendedVigenereCipher(encryptedText, key):
    decryptedText = []

    encryptedText = list(encryptedText.upper())
    key = list(key.upper())

    if (not(isEqualLength(encryptedText, key))):
        key = repeatKey(len(encryptedText), key)
   
    for i in range (len(encryptedText)):
        asciiText = ord(encryptedText[i])
        asciiKey = ord(key[i])
        decryptedValue = "" + chr(((asciiText - asciiKey) + 256) % 256)
        decryptedText.append(decryptedValue)

    return("".join(decryptedText))