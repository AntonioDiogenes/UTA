from tkinter import *
from tkinter.ttk import Progressbar
from pytube import YouTube
import moviepy.editor as mp
import re
import os

def downloadMp3():
        # recebe o link vindo do entry_01
        link = Entry_01.get()
        
        # diretorio onde vai o arquivo
        path = Entry_02.get()
        
        yt = YouTube(link)
        ys = yt.streams.filter(only_audio=True).first().download(path)
        
        for file in os.listdir(path):
            if re.search('mp4',file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0]+".mp3")
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
                      
def downloadMp4():
        # recebe o link vindo do entry_01
        link = Entry_01.get()
        
        # diretorio onde vai o arquivo
        path = Entry_02.get()
        
        yt = YouTube(link)
        ys = yt.streams.filter(only_audio=True).first().download(path)
        Retorno['text'] = 'Download Completo :D'


main_windown = Tk()
main_windown.title("PyMusic")
img = PhotoImage(file='C:/Users/anton/Documents/01_IFRN/PyMusic/IMG/python_logo.png')
main_windown.iconphoto(True,img)

#cria um label com um texto
Label_Titulo = Label(main_windown,text='PyMusic',font = ("Arial", 50))
Label_Image = Label(main_windown, text='',image=img)
Label_SubTitulo = Label(main_windown,text='By: 𝓔𝓶𝓮𝓻𝓪𝓵𝓭')
Label_01 = Label(main_windown, text = "link do video : ",font = ("Arial", 13))
Label_02 = Label(main_windown,text='path:',font = ("Arial", 13))

#cria uma caixa de entrada pra passar o link
Entry_01 = Entry(main_windown,width = 50)
Entry_02 = Entry(main_windown,width = 50)

#cria o botao com o comando de baixar
Buttom_01 = Button(main_windown, text = "baixar Mp3",padx=50, command = downloadMp3)
Buttom_02 = Button(main_windown, text = "baixar Mp4",padx=50, command = downloadMp4)

#cria um label com um retorno pro usuario
Retorno = Label(main_windown,text='')

#coloca todos os componentes em um grid
Label_Image.grid(column=3,row=0)
Label_Titulo.grid(column=2,row=0)
Label_SubTitulo.grid(column=2,row=1)
Label_01.grid(column=1,row=2)
Entry_01.grid(column=2,row=2)
Label_02.grid(column=1,row=3)
Entry_02.grid(column=2,row=3)
Buttom_01.grid(column=2,row=4)
Buttom_02.grid(column=2,row=5)
Retorno.grid(column=2,row=6)

mainloop()
        
            