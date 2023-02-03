# file cipher klasik - One Time Pad

import random

def shuffleText(text):
    l = list(text)
    random.shuffle(l)
    return("".join(l))

def cutKeyLength(plaintext, key):
    if (len(plaintext) < len(key)):
        key = key[:len(plaintext)]
    return(key)

def removeNonAlphabetCharacter(string):
    str = ''.join(i for i in string if i.isalpha())
    return str

def encryptOTPCipher(plaintext, key):
    encryptedText = []

    #PlainText setting
    plaintext = removeNonAlphabetCharacter(plaintext)
    plaintext = list(plaintext.upper())
    
    #Key setting
    key = removeNonAlphabetCharacter(key)
    key = key.upper()
    key = list(key)
   
    for i in range (len(plaintext)):
        asciiText = ord(plaintext[i])
        asciiKey = ord(key[i])
        encryptedValue = "" + chr(((asciiText + asciiKey) % 26) + ord('A'))
        encryptedText.append(encryptedValue)

    return("".join(encryptedText))

def decryptOTPCipher(encryptedText, key):
    decryptedText = []

    #Cipher setting
    encryptedText = removeNonAlphabetCharacter(encryptedText)
    encryptedText = list(encryptedText.upper())
    
    #Key setting
    key = removeNonAlphabetCharacter(key)
    key = key.upper()
    key = list(key)
   
    for i in range (len(encryptedText)):
        asciiText = ord(encryptedText[i])
        #asciiKey = ord(generatedKey[i])
        asciiKey = ord(key[i])
        decryptedValue = "" + chr((((asciiText - asciiKey) + 26) % 26) + ord('A'))
        decryptedText.append(decryptedValue)

    return("".join(decryptedText))


