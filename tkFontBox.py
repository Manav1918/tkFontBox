from tkinter import *
from tkinter import ttk
from tkinter import font

class FontChooser(Toplevel):
    def __init__(self,parent,winname='Font Chooser'):
        Toplevel.__init__(self,parent)
        self.parent = parent
        self.winname = winname
        self.allfontSizes = [i for i in range(8,73,2)]
        self.title(winname)
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW",self.donothing)
        self.createWidgets()
    def donothing(self):
        self.withdraw()#when user presses close(X) button,just hide the fontChooser window.
    def showSampleSizeandFont(self,event):
        fn = self.fontCombo.get()
        fs = self.fontSizeCombo.get()
        self.sampletxtbox.config(font=(fn,fs))
    def createWidgets(self):
        self.mainFrame = Frame(self)
        self.mainFrame.pack(fill=BOTH)

        self.leftFrame = Frame(self.mainFrame,width=50,bg='gray')
        self.leftFrame.pack(side=LEFT,fill=BOTH,padx=5)
        Label(self.leftFrame,text='Font Family',bg='gray',font='bold').grid(row=0,column=0)
        self.fontCombo = ttk.Combobox(self.leftFrame,values=font.families())
        self.fontCombo.grid(row=1,column=0)
        self.fontCombo.set('Arial')
        Label(self.leftFrame,text='Font Size',bg='gray',font='bold').grid(row=2,column=0)
        self.fontSizeCombo = ttk.Combobox(self.leftFrame,values=self.allfontSizes)
        self.fontSizeCombo.grid(row=3,column=0)
        self.fontSizeCombo.set(8)
        self.fontSizeCombo.bind("<<ComboboxSelected>>",self.showSampleSizeandFont)
        self.fontCombo.bind("<<ComboboxSelected>>",self.showSampleSizeandFont)
        self.rightFrame = Frame(self.mainFrame,bg='goldenrod2')
        self.rightFrame.pack(side=RIGHT,fill=BOTH)

        self.sampletxtbox=Text(self.rightFrame,height=20)
        self.sampletxtbox.insert(END,'''This Font Dialog Box is made by:
Pawan Kumar
CompanyName: CID An Education Hub
Visit our YT Channel to learn Application Development from python.
Youtube Channel name: CID An Education Hub
''')
        self.sampletxtbox.pack(side=BOTTOM)
        
        self.openFontDialog = Button(self,width=30,bg='goldenrod1',fg='black',
                                text='Done!')
        self.openFontDialog.pack(side=BOTTOM,pady=10)


#------------- test running---------
if __name__ == "__main__":
    def getFont():
        global fc
        try:
            fc.deiconify()
        except Exception as e: #when user pressed close button of fontChooser window
            print(e)            # then, print error that window is destroyed.
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
    root.title('Example program to call fontChooser Dialog')
    root.resizable(0,0)
##    fc = FontChooser(root) #not required now
##    fc.withdraw()         # not required now
    f = Frame(root)
    f.pack(fill=BOTH,padx=5)
    
    yscrollbar = Scrollbar(f)
    yscrollbar.pack(side = RIGHT, fill = Y)

    txtbox = Text(f)
    txtbox.pack(fill=BOTH,padx=5)
    txtbox.config(yscrollcommand = yscrollbar.set)
    yscrollbar.config( command = txtbox.yview)
    btn = Button(text='Open Font Box',width=20,bg='black',fg='white',padx=10,pady=10,command=getFont)
    btn.pack(pady=5)
    root.mainloop()
        
