# Program cipher kalsik playfair cipher
# 26 huruf alfabet

import sys
sys.path.append('..')

class playfair:
    # KEY 
    def removeSpecialCharacter(string):
        temp = ""
        for i in string:
            if(i.isalpha()):
                temp+=i
        temp = temp.replace(" ", "")
        temp = temp.upper()
        return temp

    # Create Matrix
    def matrix (init, x, y):
        return [[init for i in range(x)] for j in range(y)]

    # Move key into matrix
    def key_into_arr(key):
        key_arr = list()
        for k in key: 
            if k not in key_arr:
                if k == "J":
                    key_arr.append("I")
                else:
                    key_arr.append(k)
        return key_arr

    # Fullfill the rest by alphabet, ASCII code : A(65) - Z(90)
    def full_arrkey(key_arr):
        idx = 0
        for i in range(65,91):
            if chr(i) not in key_arr:
                if chr(74) and i==73 not in key_arr:
                    key_arr.append("I")
                    idx = 1
                elif idx == 0 and i==73 or i==74:
                    pass
                else:
                    key_arr.append(chr(i))
        return key_arr

    # Define 5x5 matrix (initial = 0)
    def matrix_cipher(mtrix, key_matrix):
        idx = 0
        cipher_matrix = mtrix
        for i in range(0, 5):
            for j in range(0, 5):
                cipher_matrix[i][j] = key_matrix[idx]
                idx+=1
        return cipher_matrix

    # locating the index in alfabet character
    def idxlocator(char, cip_mat):
        lt = list()
        if char == "J":
            char == "I"
        for i, j in enumerate(cip_mat):
            for x, y in enumerate(j):
                if char == y:
                    lt.append(i)
                    lt.append(x)
                    return lt


    # prepare the text for encryption or decryption
    def prepare_text(text):
        for idx in range(0, len(text)+1, 2):
            if idx < len(text)-1:
                #check if there's the same char in current and next index
                if text[idx] == text[idx+1]:
                    text=text[:idx]+'X'+text[idx+1:]
        if len(text)%2 != 0:
            text=text[:]+'X'
        return text

    # ENCRYPTION
    def encrypt(plaintx, cipher_matrix):
        plaintxt_clean = playfair.prepare_text(plaintx)
        i = 0
        cip = ""
        while i < len(plaintxt_clean):
            lt_curr = list()
            lt_curr = playfair.idxlocator(plaintxt_clean[i], cipher_matrix)
            lt_next = list()
            lt_next = playfair.idxlocator(plaintxt_clean[i+1], cipher_matrix)
            #If couple of char located in the same column
            if lt_curr[1] == lt_next[1]:
                cip += f"{cipher_matrix[(lt_curr[0]+ 1)% 5][lt_curr[1]]}{cipher_matrix[(lt_next[0]+ 1)% 5][lt_next[1]]}"    
            #If couple of char located in the same row
            elif lt_curr[0] == lt_next[0]:
                cip+= f"{cipher_matrix[lt_curr[0]][(lt_curr[1]+ 1)%5]}{cipher_matrix[lt_next[0]][(lt_next[1]+ 1)% 5]}"
            else:
                cip += f"{cipher_matrix[lt_curr[0]][lt_next[1]]}{cipher_matrix[lt_next[0]][lt_curr[1]]}"
            i+=2
        return cip

    # DECRYPTION
    def decrypt(ciphertx, cipher_matrix):
        ciphertxt_clean = playfair.prepare_text(ciphertx)
        i = 0
        plain=""
        while i < len(ciphertxt_clean):
            lt_curr = list()
            lt_curr = playfair.idxlocator(ciphertxt_clean[i], cipher_matrix)
            lt_next = list()
            lt_next = playfair.idxlocator(ciphertxt_clean[i+1], cipher_matrix)
            #If couple of char located in the same column
            if lt_curr[1] == lt_next[1]:
                plain += f"{cipher_matrix[(lt_curr[0]- 1)% 5][lt_curr[1]]}{cipher_matrix[(lt_next[0]- 1)% 5][lt_next[1]]}"
            #If couple of char located in the same row
            elif lt_curr[0] == lt_next[0]:
                plain += f"{cipher_matrix[lt_curr[0]][(lt_curr[1]- 1)%5]}{cipher_matrix[lt_next[0]][(lt_next[1]- 1)% 5]}"
            else:
                plain += f"{cipher_matrix[lt_curr[0]][lt_next[1]]}{cipher_matrix[lt_next[0]][lt_curr[1]]}"
            i += 2
        return plain


