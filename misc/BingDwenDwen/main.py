from tkinter import *
from turtle import RawTurtle
import ctypes, platform

if platform.system() == 'Windows': 
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()

def draw(*args):
    draw_bdd(t)

def save(*args):
    save_image(root,canvas)

def main():
    global t,root,canvas
    root = Tk()
    root.geometry('600x700+500+60')
    root.config(bg='white')
    root.title('老王在瞎画。。。。。。')
    root.resizable(False, False)
    canvas = Canvas(root, width=600, height=600)
    canvas.place(x=0,y=50)
 
    t = RawTurtle(canvas)
    t.hideturtle()

    draw()
    
    buttonReset = TxButton(root,type='primary',size='small',text='Reset',command=draw)
    buttonReset.place(x = 5, y = 5)

    buttonDownload = TxButton(root,size='small',text='Download',command=save)
    buttonDownload.place(x = 100, y = 5)

    root.mainloop()
 
if __name__ == '__main__':
 
    main()