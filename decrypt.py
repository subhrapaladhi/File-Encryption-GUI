from tkinter import *
from tkinter import filedialog
from Crypto.Cipher import AES
import hashlib

fileName = ""
def chooseFile():
    inputFile = filedialog.askopenfile(mode="r")
    global fileName
    fileName = inputFile.name

def DecryptFile():
    password = str(passInput.get(1.0,END)).encode()
    
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC # Block cipher mode
    IV = "6wwaPx0X9GEDH4oI"

    cipher = AES.new(key, mode, IV)
    
    file = open(fileName,"rb")
    EncryptedfileData = file.read()
    file.close()

    decryptedFileData = cipher.decrypt(EncryptedfileData)
    decryptedFileData.rstrip(b'0')

    file = open(fileName, "wb")
    file.write(decryptedFileData)
    file.close()
        
        
root = Tk()
root.geometry("400x300")

title = Label(root, text = "File Decrypter") 
title.config(font =("Courier", 20))
title.place(x=100,y=20) 

l = Label(root, text="Give the password")
l.place(x=65,y=80)

passInput = Text(root,height=1,width=20)
passInput.place(x=205,y=80)


btn = Button(root, text="Choose File",command=chooseFile)
btn.place(x=150,y=150)

btn = Button(root, text="Decrypt File",command=DecryptFile)
btn.place(x=150,y=210)

root.mainloop()