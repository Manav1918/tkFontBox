from tkinter import *
from tkFontBox import FontChooser

def getFont():
    global fc
    try:
        fc.deiconify()
    except Exception as e: #In the first open fontChooser window object have to be created.
        print(e)
        fc = FontChooser(root)#then, will have to open fontChooser again.
    def printFont():
        fn = fc.fontCombo.get()
        fs = fc.fontSizeCombo.get()
        txtbox.config(font=(fn,fs))
        fc.fontCombo.set(fn)
        fc.fontSizeCombo.set(fs)
##            
        fc.withdraw()
    
##        font = fc.getFont()
##        txtbox.config(font=font)
    fc.openFontDialog.config(command=printFont)
    
root = Tk()
root.resizable(0,0)
root.title('Tk Font Chooser Example')
mainFrame = Frame(root)
mainFrame.pack(fill=BOTH)

leftFrame = Frame(mainFrame,width=50,bg='gray')
leftFrame.pack(side=LEFT,fill=BOTH)   
openFontDialog = Button(leftFrame,width=30,bg='goldenrod1',fg='black',
                        text='Open Font Dialog',command=getFont)
openFontDialog.pack(anchor=SE)

rightFrame = Frame(mainFrame,bg='goldenrod2')
rightFrame.pack(side=RIGHT,fill=BOTH)
# a text box in right frame
txtbox = Text(rightFrame)
txtbox.pack(fill=BOTH)

root.mainloop()
