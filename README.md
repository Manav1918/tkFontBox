# tkFontBox
This simple python program can be used to make FontChooser dialog in Tkinter Applications.

**how to use?**
1.  Copy this py file into your current directory .
2.  In your python program, just import it like this.
    <br>**from tkFontBox import FontChooser**
3.  In your python program of tkinter Application, wherever you want, create a method like this:
```
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
```
Here, getFont() method can be called by any of your TButtons,menus etc. to get the font family name and font size and use them.
under printFont() method "fn" is the variable to get **font name** and "fs" for **font size** and "txtbox" (in line 20) is the tkinter textBox in which you may want to change the font name and size you selected.

Main Window Example Program.
![image](https://user-images.githubusercontent.com/41276382/153012021-2e7ac198-ad77-48da-9be0-f214aa91c85b.png)

FontBox Window ScreenShot.
![image](https://user-images.githubusercontent.com/41276382/153012267-5be0d232-3e45-46b0-8ffa-891bfef44868.png)

Affected main Window Text of textbox
![image](https://user-images.githubusercontent.com/41276382/153012503-37a39bf3-fad3-4ed0-8d56-cfc7bbd1848d.png)
