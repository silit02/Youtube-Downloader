from pytube import YouTube
from sys import argv

#Überprüfung der Parameter
if len(argv) < 2 or len(argv) > 3:
    print("usage:",argv[0],"<link> [path]")
    exit()

link = argv[1]
yt = YouTube(link)

#Informationen über das Video ausgeben
print("Videoinformationen:")
print("\tTitel:", yt.title)
print("\tKanal:",yt.author)
print("\tAufrufe:", yt.views)

#Einstellungen für Download festlegen
yd = yt.streams.get_highest_resolution()
path = '/Users/simon/Downloads'
if len(argv) > 2:
    path = argv[2]

#Download ausführen
print("\nDownload nach",path,"läuft...")
yd.download(path)
print("Download abgeschlossen")
