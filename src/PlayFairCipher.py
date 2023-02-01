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

    # Change 5x5 matrix into square form
    def square(cipher_matrix):
        id_row = 0
        id_col = 0
        for i in range(len(cipher_matrix)):
            for j in range(len(cipher_matrix[i])):
                print(cipher_matrix[i][j], end = "    ")
            print()

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

    # PLAINTEXT
    # ENCRYPTION
    def encrypt(plaintx, cipher_matrix):
        i = 0
        for idx in range(0, len(plaintx)+1, 2):
            if idx < len(plaintx)-1:
                #check if there's the same char in current and next index
                if plaintx[idx] == plaintx[idx+1]:
                    plaintx=plaintx[:idx+1]+'X'+plaintx[idx+1:]
        #check if length of plain text is odd
        if len(plaintx)%2 != 0:
            plaintx=plaintx[:]+'X'
        print("Cipher Text: ", end=" ")
        while i < len(plaintx):
            lt_curr = list()
            lt_curr = playfair.idxlocator(plaintx[i], cipher_matrix)
            lt_next = list()
            lt_next = playfair.idxlocator(plaintx[i+1], cipher_matrix)
            #If couple of char located in the same column
            if lt_curr[1] == lt_next[1]:
                print(f"{cipher_matrix[(lt_curr[0]+ 1)% 5][lt_curr[1]]}{cipher_matrix[(lt_next[0]+ 1)% 5][lt_next[1]]}", end= " ")
            #If couple of char located in the same row
            elif lt_curr[0] == lt_next[0]:
                print(f"{cipher_matrix[lt_curr[0]][(lt_curr[1]+ 1)%5]}{cipher_matrix[lt_next[0]][(lt_next[1]+ 1)% 5]}", end = " ")
            else:
                print(f"{cipher_matrix[lt_curr[0]][lt_next[1]]}{cipher_matrix[lt_next[0]][lt_curr[1]]}", end = " ")
            i += 2

    # DECRYPTION
    def decrypt(ciphertx, cipher_matrix):
        i = 0
        for idx in range(0, len(ciphertx)+1, 2):
            if idx < len(ciphertx)-1:
                #check if there's the same char in current and next index
                if ciphertx[idx] == ciphertx[idx+1]:
                    ciphertx=ciphertx[:idx+1]+'X'+ciphertx[idx+1:]
        #check if length of plain text is odd
        if len(ciphertx)%2 != 0:
            ciphertx=ciphertx[:]+'X'
        print("Plain Text: ", end = " ")
        while i < len(ciphertx):
            lt_curr = list()
            lt_curr = playfair.idxlocator(ciphertx[i], cipher_matrix)
            lt_next = list()
            lt_next = playfair.idxlocator(ciphertx[i+1], cipher_matrix)
            #If couple of char located in the same column
            if lt_curr[1] == lt_next[1]:
                print(f"{cipher_matrix[(lt_curr[0]- 1)% 5][lt_curr[1]]}{cipher_matrix[(lt_next[0]- 1)% 5][lt_next[1]]}", end= " ")
            #If couple of char located in the same row
            elif lt_curr[0] == lt_next[0]:
                print(f"{cipher_matrix[lt_curr[0]][(lt_curr[1]- 1)%5]}{cipher_matrix[lt_next[0]][(lt_next[1]- 1)% 5]}", end = " ")
            else:
                print(f"{cipher_matrix[lt_curr[0]][lt_next[1]]}{cipher_matrix[lt_next[0]][lt_curr[1]]}", end = " ")
            i += 2



