import OneTimePad

plain = "There is a function shuffle in the random module. Note that it shuffles in-place so you first have to convert your string to a list of characters, shuffle it, then join the result again."
key = "Shuffling a sequence of numbers have always been an useful utility and the question that has appeared in many company placement interviews as well. Knowing more than one method to achieve this can always be a plus. Let’s discuss certain ways in which this can be achieved."

encryption = OneTimePad.encryptOTPCipher(plain, key)
print(encryption)

print(OneTimePad.decryptOTPCipher(encryption, key))