# Program cipher klasik vifenere cipher
# 26 huruf alfabet

def isEqualLength(plaintext, key):
    if (len(plaintext) == len(key)) :
        return True
    else : 
        return False

def removeSpace(string):
    return string.replace(" ", "")

def removeSpcialCharacter(string):
    str = ''.join(i for i in string if i.isalnum())
    return str

def removeNumber(string):
    str = ''.join([i for i in string if not i.isdigit()])
    return str

def repeatKey(plaintextLength, key) :
    key = list(key)
    actualKey = []
    for i in (range(plaintextLength)):
        actualKey.append(key[i % len(key)])

    return actualKey

def encryptStandardVigenereCipher(plaintext, key):
    encryptedText = []

    #Remove space
    plaintext = removeSpace(plaintext)
    key = removeSpace(key)

    plaintext = list(plaintext.upper())
    key = list(key.upper())

    if (not(isEqualLength(plaintext, key))):
        key = repeatKey(len(plaintext), key)
   
    for i in range (len(plaintext)):
        asciiText = ord(plaintext[i])
        asciiKey = ord(key[i])
        encryptedValue = "" + chr(((asciiText + asciiKey) % 26) + ord('A'))
        encryptedText.append(encryptedValue)

    return("".join(encryptedText))

def decryptStandardVigenereCipher(encryptedText, key):
    decryptedText = []

    #Remove space
    encryptedText = removeSpace(encryptedText)
    key = removeSpace(key)

    encryptedText = list(encryptedText.upper())
    key = list(key.upper())

    if (not(isEqualLength(encryptedText, key))):
        key = repeatKey(len(encryptedText), key)
   
    for i in range (len(encryptedText)):
        asciiText = ord(encryptedText[i])
        asciiKey = ord(key[i])
        decryptedValue = "" + chr((((asciiText - asciiKey) + 26) % 26) + ord('A'))
        decryptedText.append(decryptedValue)

    return("".join(decryptedText))