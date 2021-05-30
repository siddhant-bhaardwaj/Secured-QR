from tkinter import *
import cv2
from pyzbar.pyzbar import decode
from tkinter import messagebox

root = Tk()
root['background']='#1B2631'        
root.title("scan QR")
root.geometry('400x400')
root.iconbitmap('icon.ico')
result=''

label= Label(root,text='insert secret key here',bg='#1B2631',fg='white',font='Helvetica 14 bold')
label.pack(pady=5)
e = Entry(root,borderwidth=4,width=20)
e.focus()
e.bind()
e.pack()
def scan():
    result=''
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    camera = True

    while camera == True:
        success,Frame=cap.read()
            
        for code in decode(Frame):
            msg = code.data.decode('utf-8')
            val = int(e.get())
            for i in range(0, len(msg)):
                result = result + chr(ord(msg[i]) - val)
                
                #popup
            def popup():
                messagebox.showinfo('your message',result) 
            popup()    
                
        cv2.imshow('Scan QR',Frame)
        k=cv2.waitKey(1)
        if k == 27:
            cv2.DistroyAllWindows()


icon = PhotoImage(file='camicon.png')
label = Button(image=icon,command=scan)
label.pack(pady=10)

quit_button = Button(root, text= 'EXIT',borderwidth=5,command=root.destroy,font='Helvetica 14 bold',bg='#ff9933')
quit_button.pack()

mainloop()
