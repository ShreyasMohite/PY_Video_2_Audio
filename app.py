from tkinter import *
from tkinter.ttk import Notebook,Progressbar,Combobox
import threading
import time
import tkinter.messagebox
from tkinter import filedialog
import moviepy.editor as m






class ConvertingMedia:
    def __init__(self,root):
        self.root=root
        self.root.title("mp4-to-mp3")
        self.root.geometry("500x300")
        self.root.iconbitmap("logo275.ico")
        self.root.resizable(0,0)

        save_song=StringVar()


        def on_enter1(e):
            but_browse['background']="black"
            but_browse['foreground']="cyan"  
        def on_leave1(e):
            but_browse['background']="SystemButtonFace"
            but_browse['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_convert['background']="black"
            but_convert['foreground']="cyan"  
        def on_leave2(e):
            but_convert['background']="SystemButtonFace"
            but_convert['foreground']="SystemButtonText"



    #=====================================================================#
        def browse():
           global filename
           file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("mp4","*.mp4"),("all files","*.*")))
           lab_file.config(text="file is selected")
           filename=file_path
           

        def Convert_format(): 
            if save_song.get()!=0:
                try:
                    ffmpeg = "C:\\ffmpeg-4.3.1-2020-10-01-essentials_build\\bin\\ffmpeg.exe"
                    ffprobe ="C:\\ffmpeg-4.3.1-2020-10-01-essentials_build\\bin\\ffprobe.exe"    
                    ms=m.VideoFileClip(filename)
                    prg.start(10)
                    ms.audio.write_audiofile("{}.mp3".format(save_song.get()))
                    prg.stop()
                except Exception as e:
                    print(e)
            else:
                tkinter.messagebox.showerror("Error","Please enter song name")

        def convert_thread():
            t1=threading.Thread(target=Convert_format)
            t1.start()
            




    #========================frame========================================#
        mainframe=Frame(self.root,width=500,height=300,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        top_frame=Frame(mainframe,width=495,height=265,relief="ridge",bd=3)
        top_frame.place(x=0,y=0)

        task_bar_frame=Frame(mainframe,width=495,height=30,relief="ridge",bd=3)
        task_bar_frame.place(x=0,y=265)

    #=====================================================================#

        lab_frame=LabelFrame(top_frame,text="Convert Mp4 To Mp3",width=490,height=258,font=('times new roman',12,'bold'),bg="cyan")
        lab_frame.place(x=0,y=0)

    #=====================================================================#

        but_browse=Button(lab_frame,text="Browse",width=15,font=('times new roman',12,'bold'),cursor="hand2",command=browse)
        but_browse.place(x=160,y=20)
        but_browse.bind("<Enter>",on_enter1)
        but_browse.bind("<Leave>",on_leave1)

        lab_file=Label(lab_frame,text="Select the file",font=('times new roman',12,'bold'),bg="cyan")
        lab_file.place(x=190,y=80)

        lab_enter_name=Label(lab_frame,text="Enter Name to save",font=('times new roman',11,'bold'),bg="cyan")
        lab_enter_name.place(x=90,y=160)

        
        ent_name=Entry(lab_frame,width=18,font=('times new roman',14,'bold'),relief="ridge",bd=3,textvariable=save_song)
        ent_name.place(x=60,y=190)

        but_convert=Button(lab_frame,text="Convert",width=15,font=('times new roman',12,'bold'),cursor="hand2",command=convert_thread)
        but_convert.place(x=330,y=190)
        but_convert.bind("<Enter>",on_enter2)
        but_convert.bind("<Leave>",on_leave2)


        prg=Progressbar(task_bar_frame,length=489,orient=HORIZONTAL,mode='indeterminate')
        prg.place(x=0,y=0)



if __name__ == "__main__":
    root=Tk()
    app=ConvertingMedia(root)
    root.mainloop()