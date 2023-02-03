# file cipher klasik - One Time Pad

import random

def shuffleText(text):
    l = list(text)
    random.shuffle(l)
    return(l)

def removeNonAlphabetCharacter(string):
    str = ''.join(i for i in string if i.isalpha())
    return str

def encryptOTPCipher(plaintext, key):
    encryptedText = []

    #PlainText setting
    plaintext = removeNonAlphabetCharacter(plaintext)
    print(f"Plaintext yang diinput :\n{plaintext.upper()}")
    plaintext = list(plaintext.upper())
    
    #Key setting
    key = removeNonAlphabetCharacter(key)
    key = key.upper()
    key = shuffleText(key) # Shuffle key
    
    if (len(plaintext) < len(key)):
        # Potong Key
        generatedKey = []
        for i in range(0,len(plaintext)):
            generatedKey.append(key[i])

        print("Key yang dipakai untuk enkripsi :")
        print(''.join(generatedKey))
   
    for i in range (len(plaintext)):
        asciiText = ord(plaintext[i])
        asciiKey = ord(generatedKey[i])
        encryptedValue = "" + chr(((asciiText + asciiKey) % 26) + ord('A'))
        encryptedText.append(encryptedValue)

    print("Hasil enkripsi :")
    return("".join(encryptedText))

def decryptOTPCipher(encryptedText, key):
    decryptedText = []

    #Cipher setting
    encryptedText = removeNonAlphabetCharacter(encryptedText)
    encryptedText = list(encryptedText.upper())
    
    #Key setting
    key = removeNonAlphabetCharacter(key)
    key = key.upper()
    key = shuffleText(key) #Shuffle

    if (len(encryptedText) < len(key)):
        # Potong Key
        generatedKey = []
        for i in range(0,len(encryptedText)):
            generatedKey.append(key[i])

        print("Key yang dipakai untuk dekripsi :")
        print(''.join(generatedKey))
   
    for i in range (len(encryptedText)):
        asciiText = ord(encryptedText[i])
        asciiKey = ord(generatedKey[i])
        decryptedValue = "" + chr((((asciiText - asciiKey) + 26) % 26) + ord('A'))
        decryptedText.append(decryptedValue)

    print("Hasil dekripsi :")
    return("".join(decryptedText))


