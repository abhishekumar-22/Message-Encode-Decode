#Message Encode Decode
#Author - Abhishek Kumar

#Import necessary modules and libraries
from tkinter import *
import tkinter as tk
import base64

#Main window
main_window=Tk()
main_window.geometry('500x480')
main_window.resizable(0,0)
main_window['bg']='black'
main_window.iconbitmap('message_icon.ico')
main_window.title('Message Encode Decode')

#Text in main window
Label(main_window,text='ENCODE DECODE',font='arial 20 bold',fg='pink',bg='black').place(x=140,y=20)

#Variables in program
message=StringVar()
password=StringVar()
mode=StringVar()
enc_message=StringVar()
global select_text
select_text=False

#Function to encode the message
def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i])+ord(key_c))%256))    
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#Function to decode the message
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256+ord(message[i])-ord(key_c))%256))   
    return "".join(dec)

#Function to set the mode of message
#i.e. Encode OR Decode
def Mode():
    if(menu.get()=='Encode'):
        enc_message.set(Encode(password.get(),message.get()))
    elif(menu.get()=='Decode'):
        enc_message.set(Decode(password.get(),message.get()))
    else:
        enc_message.set('Invalid Mode')

#Function to reset
def Reset():
    message.set("")
    password.set("")
    mode.set("")
    enc_message.set("")
    menu.set("Select Mode")

#Function to exit window   
def Exit():
    main_window.destroy()

#Message box
Label(main_window,font='arial 12 bold',text='MESSAGE',fg='blue',bg='black').place(x=220,y=60)
Entry(main_window,font ='arial 10',textvariable=message,bg='ghost white',width=60).place(x=48,y=95)

#Key (Password) box
Label(main_window,font='arial 12 bold',text='KEY',fg='red',bg='black').place(x=243,y=130)
Entry(main_window,font='arial 10',textvariable=password,bg='ghost white',width=60,show='*').place(x=48,y=160)

#Mode menu
menu = StringVar(main_window)
menu.set("Select Mode")
drop = OptionMenu(main_window,menu,'Encode','Decode')
drop.place(x=207,y=203)

#Result box
Label(main_window,font='arial 12 bold',text='RESULT', fg='yellow',bg='black').place(x=220,y=288)
Entry(main_window,font='arial 10 bold',textvariable=enc_message,bg ='ghost white',width=60).place(x=48,y=320)

#Result button
Button(main_window,font='arial 10 bold',text='RESULT',padx=2,bg ='LightGray',command=Mode).place(x=220,y=360)

#Reset button
Button(main_window,font='arial 10 bold',text='RESET',width=6,command=Reset,bg='LimeGreen',padx=2).place(x=170,y=412)

#Exit button
Button(main_window,font='arial 10 bold',text='EXIT',width=6,command=Exit,bg='OrangeRed',padx=2,pady=2).place(x=290,y=412)

#Loop to active main window until the user close the window
main_window.mainloop()
