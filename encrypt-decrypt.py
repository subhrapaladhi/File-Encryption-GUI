from tkinter import *
from tkinter import filedialog
from Crypto.Cipher import AES
import hashlib

root = Tk()
root.geometry("200x160")

def pad_FileData(file):
    while(len(file)%16 !=0):
        file +=b'0'
    return file

def encrypt_image():
    inputFile = filedialog.askopenfile(mode="r")
    if inputFile is not None:
        fileName = inputFile.name
        # print(fileName)
        
        password = str(passInput.get(1.0,END)).encode()
        
        key = hashlib.sha256(password).digest()
        mode = AES.MODE_CBC # Block cipher mode
        IV = "6wwaPx0X9GEDH4oI"

        cipher = AES.new(key, mode, IV)
        
        file = open(fileName,"rb")
        fileData = file.read()
        file.close()
        
        print(len(fileData))
        fileData = bytearray(fileData)
        print(fileData)
        paddedFile = pad_FileData(fileData)
        print(paddedFile)
        # for index,val in enumerate(fileData):
        #     fileData[index] = val^int(key)
        
        # fileData2 = open(fileName,"wb")
        # fileData2.write(fileData)
        # fileData2.close()

btn = Button(root, text="encrypt image",command=encrypt_image)
btn.place(x=70,y=10)

passInput = Text(root,height=1,width=10)
passInput.place(x=50,y=50)

root.mainloop()