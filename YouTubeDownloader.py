import tkinter
import customtkinter
import threading
from pytube import YouTube

def startDownload():

    # Disable the download button and Input Field during Download
    downloadButton.configure(state=customtkinter.DISABLED)
    link.configure(state=customtkinter.DISABLED)

    # Reset message and progress
    message.configure(text="")
    pPercentage.configure(text="0%")
    progressBar.set(0)

    # Get Path to Save File
    file_path = customtkinter.filedialog.askdirectory(initialdir="/Users/simon")

    try:
        ytlink =  link.get()
        yt = YouTube(ytlink, on_progress_callback=update_progress)
    except:
        message.configure(text="Ein Fehler ist aufgetreten!")

    threadDownload = threading.Thread(target=downloadVideo, args=(yt, file_path))
    threadDownload.start()

    # Update Title
    title.configure(text=yt.title)
    downloadButton.configure(text="Download läuft ...")
    message.configure(text="Download läuft ...")

def downloadVideo(yt: YouTube, file_path):
    try:
        video = yt.streams.get_highest_resolution()
        video.download(file_path)
        message.configure(text="Download abgeschlossen!")
    except Exception as e:
        message.configure(text=f"Fehler beim Download: {str(e)}")
    finally:
        downloadButton.configure(text="Download")
        downloadButton.configure(state=customtkinter.NORMAL)
        link.configure(state=customtkinter.NORMAL)

def update_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percantage_of_completion = bytes_downloaded / total_size
    per = str(int(percantage_of_completion*100))
    pPercentage.configure(text=per+"%")
    pPercentage.update()
    progressBar.set(percantage_of_completion)
 
# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue") 

# Our app frame
app =  customtkinter.CTk()
app.geometry("700x300")
app.resizable(False, False)
app.title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Fügen Sie hier einen YouTube-Link ein")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var) 
link.pack()

# Download Button
downloadButton = customtkinter.CTkButton(app, text="Download", command=startDownload)
downloadButton.pack(padx=20,pady=20)

# Progress Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# Progressbar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10) 

# MessageBox
message = customtkinter.CTkLabel(app, text="")
message.pack()

# Run app
app.mainloop() 
