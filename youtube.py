from tkinter import *
from pytube import YouTube


'''
Tk() used to initialize tkinter to create display window
geometry() used to set the window’s width and height
resizable(0,0) set the fix size of window
title() used to give the title of window
'''
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube video downloader")

'''
link is a string type variable that stores the youtube video link that the user enters.
Entry() widget is used when we want to create an input text field.
width sets the width of entry widget
textvariable used to retrieve the value of current text variable to the entry widget
place() use to place the widget at a specific position
'''
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)

link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', 
       padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()