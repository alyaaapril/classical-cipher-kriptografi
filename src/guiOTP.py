import sys
import string
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import itertools
from tkinter.messagebox import showinfo

from OneTimePad import *
from fileOperation import *

sys.path.append(r"../")

window = Tk()
window.title("One Time Pad")
window.geometry('800x500')
window.configure(bg="#E0E1E9")

# file explorer window
def open_file_message():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    entry_text = readFile(filename)
    entry_message.insert(END, entry_text)

def open_file_key():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    entry_text = readFile(filename)
    entry_key.insert(END, entry_text)

def add_space(text):
    spacedText = " ".join(text[i:i + 5] for i in range(0, len(text), 5))
    return(spacedText)

def save_file():
    text_file = open("test.txt", "w")
    text_file.write(text_entry1.get(1.0, END))
    text_file.write(text_entry2.get(1.0, END))
    text_file.close()
    showinfo("File saved", "File saved, check your file!")
    text_entry1.delete('1.0', END)
    text_entry2.delete('1.0', END)

def clear_messageKey():
    entry_message.delete(0, END)
    entry_key.delete(0, END)

def clear_text():
    text_entry1.delete('1.0', END)
    text_entry2.delete('1.0', END)

def click_back():
    from viewMainPage import mainPage
    mainPage(window)

# Encryption

def encrypt_message():
    text = entry_message.get()
    raw_key = entry_key.get()

    # Show shuffled key
    otp_key = cutKeyLength(text,shuffleText(raw_key))
    text_entry0.insert(END, otp_key)
    
    encryption = encryptOTPCipher(text, otp_key)
    text_entry1.delete('1.0', END)
    text_entry2.delete('1.0', END)
    text_entry1.insert(END, encryption)
    text_entry2.insert(END, add_space(encryption))

def decrypt_message():
    cipher = entry_message.get()
    key = entry_key.get()
    decryption = decryptOTPCipher(cipher, key)
    text_entry1.delete('1.0', END)
    text_entry2.delete('1.0', END)
    text_entry1.insert(END, decryption)
    text_entry2.insert(END, add_space(decryption))


title = Label(window, text = 'One Time Pad', font = ('Inter', 18), bd=15, bg="#E0E1E9")
title.grid(row=0, column=0)


# INPUT MESSAGE
label_text = Label (window, text = 'Enter your message', font = ('Inter ', 12), bg="#E0E1E9")
label_text.grid(row=1, column=0, stick='w', padx=15, pady=5)

label_keyword = Label (window, text = 'Enter your key', font = ('arial ', 12), bg="#E0E1E9") 
label_keyword.grid(row=3, column=0, stick='w', padx=15, pady=5)

message = StringVar()
key = StringVar()


entry_message = Entry(window, textvariable=message, width=50)
entry_message.grid(row=1, column=1, padx=10, ipady=5)
entry_key = Entry(window, textvariable=key, width=50)
entry_key.grid(row=3, column=1, ipady=5)

# Browse file - plaintext
btn_browseFile = Button(window, height = 1 , width=10, text="Browse a file", font = ('arial ', 10), fg="black", bg="#D3C3B1", command=open_file_message)
btn_browseFile.grid(row=1, column=2)

# Browse file - key
btn_browseFile = Button(window, height = 1 , width=10, text="Browse a file", font = ('arial ', 10), fg="black", bg="#D3C3B1", command=open_file_key)
btn_browseFile.grid(row=3, column=2)

# Clear key & message
btn_clear = Button(window, height =1 , width=20, text="Clear key & message", bg="#B8B8C7", fg="black", font = ('arial ', 10), command=clear_messageKey)
btn_clear.grid(row=5, columnspan=3, pady=2)

# OUTPUT MESSAGE
label_out = Label (window, text = "Here's your result:", font = ('arial', 12), bg="#E0E1E9")
label_out.grid(row=8, column=0, stick="w", padx=15, pady=5)

# Show Shuffle key
label_out0 = Label (window, text = 'Shuffle key', font = ('arial ', 12), bg="#E0E1E9")
label_out0.grid(row=4, column=0, stick="w", padx=15)

text_entry0 = Text(window, width=38, height=1, wrap=WORD)
text_entry0.grid(row=4, column=1, padx=5, pady=5, ipady=5)

# No Space
label_out1 = Label (window, text = 'Message (no space)', font = ('arial ', 12), bg="#E0E1E9")
label_out1.grid(row=9, column=0, stick="w", padx=15)

text_entry1 = Text(window, width=30, height=1, wrap=WORD)
text_entry1.grid(row=9, column=1, padx=10, pady=5, ipady=5)

# Group by 5
label_out2 = Label (window, text = 'Message (group by 5)', font = ('arial ', 12), bg="#E0E1E9")
label_out2.grid(row=10, column=0, stick="w", padx=15)

text_entry2 = Text(window, width=30, height=1, wrap=WORD)
text_entry2.grid(row=10, column=1, padx=10, pady=5, ipady=5)

# Encryption & Decryption
label_option = Label(window, text="Choose one :", font = ('arial ', 12), bd=15, bg="#E0E1E9")
label_option.grid(row=6, columnspan=2, stick ='w')

btn_encrypt = Button(window, text="Encrypt message!", width = "15", font = ('arial ', 10), fg="white", bg="#251F4A", command=encrypt_message)
btn_encrypt.grid(row=7, column=0)
btn_decrypt = Button(window, text="Decrypt message!", width = "15", font = ('arial ', 10), fg="white", bg="#251F4A", command=decrypt_message)
btn_decrypt.grid(row=7, column=1)

#Save as File
btn_save = Button(window, text="Save as a file", width = "10", height = "2", font = ('arial ', 10), fg="white", bg="#251F4A", command=save_file)
btn_save.grid(row=11, columnspan=3)

#Clear
btn_clear = Button(window, height =1 , width=10, text="Clear result", bg="#B8B8C7", fg="black", font = ('arial ', 10), command=clear_text)
btn_clear.grid(row=12, columnspan=3, pady=2)

#Back to homepage
btn_back = Button(window, width=20, bg="#B8B8C7", text="Back to Home Page", command=click_back)
btn_back.place(relx = 0.01, rely = 0.90, anchor ='nw')

