from tkinter import *
from tkinter import filedialog
from Crypto.Cipher import AES
import hashlib

def padFileData(file):
    while(len(file)%16 !=0):
        file +=b'0'
    return file

fileName = ""
def chooseFile():
    inputFile = filedialog.askopenfile(mode="r")
    global fileName
    fileName = inputFile.name

def encryptFile():
    password = str(passInput.get(1.0,END)).encode()
    
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC # Block cipher mode
    IV = "6wwaPx0X9GEDH4oI"

    cipher = AES.new(key, mode, IV)
    
    file = open(fileName,"rb")
    fileData = file.read()
    file.close()
    
    paddedData = padFileData(fileData)

    encryptedData = cipher.encrypt(paddedData)

    file = open(fileName, "wb")
    file.write(encryptedData)
    file.close()
        

root = Tk()
root.geometry("400x300")

title = Label(root, text = "File Encrypter") 
title.config(font =("Courier", 20))
title.place(x=100,y=20) 

l = Label(root, text="Set the password")
l.place(x=75,y=80)

passInput = Text(root,height=1,width=20)
passInput.place(x=220,y=80)


btn = Button(root, text="Choose File",command=chooseFile)
btn.place(x=150,y=150)

btn = Button(root, text="Encrypt File",command=encryptFile)
btn.place(x=140,y=210)

root.mainloop()