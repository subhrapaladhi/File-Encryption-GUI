from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("200x160")

def encrypt_image():
    inputFile = filedialog.askopenfile(mode="r")
    if inputFile is not None:
        fileName = inputFile.name
        print(fileName)
        key = keyInput.get(1.0,END)
        print(key)
        fileData = open(fileName,"rb")
        image = fileData.read()
        fileData.close()
        image = bytearray(image)
        
        for index,val in enumerate(image):
            image[index] = val^int(key)
        
        fileData2 = open(fileName,"wb")
        fileData2.write(image)
        fileData2.close()

btn = Button(root, text="encrypt image",command=encrypt_image)
btn.place(x=70,y=10)

keyInput = Text(root,height=1,width=10)
keyInput.place(x=50,y=50)

root.mainloop()