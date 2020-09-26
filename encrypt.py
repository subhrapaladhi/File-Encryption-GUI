from tkinter import *
from tkinter import filedialog
from Crypto.Cipher import AES
import hashlib

root = Tk()
root.geometry("200x160")

def padFileData(file):
    while(len(file)%16 !=0):
        file +=b'0'
    return file

def encryptFile():
    inputFile = filedialog.askopenfile(mode="r")
    if inputFile is not None:
        fileName = inputFile.name
        
        password = str(passInput.get(1.0,END)).encode()
        
        key = hashlib.sha256(password).digest()
        mode = AES.MODE_CBC # Block cipher mode
        IV = "6wwaPx0X9GEDH4oI"

        cipher = AES.new(key, mode, IV)
        
        file = open(fileName,"rb")
        fileData = file.read()
        file.close()
        
        paddedData = padFileData(fileData)
        # print(paddedData)

        encryptedData = cipher.encrypt(paddedData)
        # print(encryptedData)

        file = open(fileName, "wb")
        file.write(encryptedData)
        file.close()
        

btn = Button(root, text="encrypt image",command=encryptFile)
btn.place(x=70,y=10)

passInput = Text(root,height=1,width=10)
passInput.place(x=50,y=50)

root.mainloop()