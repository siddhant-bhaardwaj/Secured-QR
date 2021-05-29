from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pyzbar.pyzbar import decode, decode
from PIL import Image
import qrcode
import random
import cv2
result=''
 
  #Windows screen
root = Tk()

root['background']='#1B2631'        
root.title("secured QR")
root.geometry('400x400')
root.iconbitmap('icon.ico')
        

#window1
def window():
    
    
    top = Tk()
    

    #tool screen size
    top['background']='#1B2631'        
    top.title("QR Encoder")
    top.geometry("350x400")
    top.iconbitmap('icon.ico')
        

     #encrypt and gen code
    def encrypt():
        result=''
        message = e.get()
        val = random.randint(2,150)
        
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + val)
               
        e.delete(0,END)
        
        img= qrcode.make(result)
        img.save('QR.png')
        
        
        #popup
        def popup():
                messagebox.showinfo('your secret key',val) 
        popup()   
                        
        #take input form user
       
    label= Label(top,text='Give your input here',bg='#1B2631',fg='white',font='Helvetica 18 bold')
    label.pack(pady=5)
    
    e = Entry(top,borderwidth=4,width=80)
    e.focus()
    e.bind()
    e.pack()
         
              #genrate QR button
                   
    genbutton = Button(top,command=encrypt,text='Click me!',borderwidth=5,font='Helvetica 14 bold',padx=25,pady=5,bg='#ff9933')
    
    genbutton.pack(pady=5)
        
           #quit button
        
    quit_button = Button(top, text= 'EXIT',borderwidth=5,command=top.destroy,font='Helvetica 14 bold',bg='#ff9933')
    quit_button.pack()

    
def window2():
    
    top1 = Tk()
  
            #screen size 
  
    top1['background']='#1B2631'        
    top1.title("QR Decoder")
    top1.geometry("350x400")
    top1.iconbitmap('icon.ico')
    
    #key input
    label= Label(top1,text='insert your secret key here',bg='#1B2631',fg='white',font='Helvetica 12 bold')
    label.pack(pady=5)
  
    e2 = Entry(top1,borderwidth=4,width=15)
    e2.focus()
    e2.bind()
    e2.pack()
         
    #open function + decrypt
    def open():
        
        global filename
        filename =filedialog.askopenfilename(filetypes=(("png files","*.png"),("All files","*.*")))
        e=Entry(top1,font=40) 
        e.insert(END, filename) #show path 
        e.pack()
        
        def decrypt():
            result=''
            d = decode(Image.open(filename))
            val = d[0].data.decode()
            message= val
            val2 = int(e2.get())
            
            for i in range(0, len(message)):
                result = result + chr(ord(message[i]) - val2)
            e2.delete(0,END)
                #popup message
        
            def popup():
                messagebox.showinfo('your message',result) 
            popup()                 
        #show your message
    
        b2_msg = Button(top1,text='Show your message',command=decrypt,bg='#ff9900')
        b2_msg.pack()
     
             
           
            #cam scan QR
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
                val = int(e2.get())
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

    


    #browse btn
    open_button = Button(top1,text='Browse your encrypted QR',font='Helvetica 14 bold',command=open,borderwidth=5,padx=5)
    open_button.pack(pady=15)

    label= Label(top1,text='OR',bg='#1B2631',fg='white',font='Helvetica 12 bold')
    label.pack(pady=5)

    #scan btn
    scan_btn = Button(top1,text='scan QR',font='Helvetica 12 bold',command=scan,borderwidth=5,padx=5)
    scan_btn.pack(pady=15)

    #exit btn
    quit_button = Button(top1, text= 'EXIT', command=top1.destroy,font='Helvetica 14 bold',bg='#ff9933')
    quit_button.pack(pady=5)

#main screen btn 

btn= Button(root,text="QR \n encrypation",borderwidth=5,padx=20,pady=10,command=window,font='Helvetica 14 bold',bg='#ff9933')
btn.pack(pady=5)

btn2= Button(root,text="QR\ndecrypation",borderwidth=5,padx=20,pady=10,command=window2,font='Helvetica 14 bold',bg='#ff9933')
btn2.pack()

btn3 = Button(root, text= 'EXIT',borderwidth=5,command=root.destroy,font='Helvetica 14 bold',bg='#ff9933',padx=20)
btn3.pack(pady=5)

mainloop()
