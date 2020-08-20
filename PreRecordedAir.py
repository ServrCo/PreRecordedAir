from tkinter import *
from os import system

MainWindow = Tk()

MainWindow.title("PreRecordedAir")

Label(MainWindow, text="Welcome to PreRecordedAir! Please enter the correct details and press \"stream!\"").grid(row=0, column=0)
Label(MainWindow, text="").grid(row=1, column=0)
Label(MainWindow, text="Enter your streaming service's URL below:").grid(row=2, column=0)

StreamURL = Entry(MainWindow, width=50)
StreamURL.grid(row=3, column=0)
StreamURL.delete(0, END)
StreamURL.insert(0, "rtmp://")

Label(MainWindow, text="").grid(row=4, column=0)
Label(MainWindow, text="Enter your stream key below: ").grid(row=5, column=0)

StreamKey = Entry(MainWindow, width=60)
StreamKey.grid(row=6, column=0)

Label(MainWindow, text="").grid(row=7, column=0)
Label(MainWindow, text="Enter the file path to your video file below: ").grid(row=8, column=0)

FilePath = Entry(MainWindow, width=60)
FilePath.grid(row=9, column=0)

Label(MainWindow, text="").grid(row=10, column=0)
Label(MainWindow, text="When you are ready to go live, press the \"Stream!\" button.").grid(row=11, column=0)

def Start():
    print("Start Function Called.")
    SystemCommand = "start ffmpeg -re -i \"%s\" -c copy -f flv %s/%s" % (FilePath.get(), StreamURL.get(), StreamKey.get())
    print(SystemCommand)
    system(SystemCommand)

def Abort():
    MsgBox = MainWindow.messagebox.askquestion ('ABORT STREAM','Are you sure you want to abort the stream?',icon = 'warning')
    if MsgBox == 'yes':
           system("taskkill /IM \"ffmpeg.exe\" /F")   
    else:
        MainWindow.messagebox.showinfo('okay','okay') 

StreamButton = Button(MainWindow, text="Stream!", command=Start)
StreamButton.grid(row=12, column=0)
AbortButton = Button(MainWindow, text="ABORT!", command=Abort)
AbortButton.grid(row=13, column=0)

Label(MainWindow, text="").grid(row=14, column=0)
MainWindow.mainloop()