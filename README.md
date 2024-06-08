# YouTube Downloader

Der YouTube-Downloader ist in der Lage, YouTube-Videos als mp4-Datei herunterzuladen. Es handelt sich um eine Application für MacOS-Systeme.

## Verwendung

Zum Download eines Videos wird der entsprechende YouTube-Link zum Video benötigt. Durch Eingabe dieses Links und dem anschließenden Klick auf _Download_ startet der Download. Der Benutzer wird aufgefordert einen Speicherort für das Video auszuwählen.

Während des Downloads lässt sich der Fortschritt am Fortschrittsbalken und an der Prozentangabe ablesen. Sobald der Download abgeschlossen ist, wird eine entsprechende Meldung angezeigt. 

## Installation

Zur Installation kann das bereitgestellte Release-Package verwendet werden. Die gelieferte Datei _YouTubeDownloader.app_ muss nur in das lokale Verzeichnis _Programme_ (Englisch: _Applications_) verschoben werden und kann dann genutzt werden. 

Wollen Sie die App selbst bauen wollen, folgen Sie bitte den Anweisungen im Abschnitt _Build_.

## Build

1. Erstellen einer virtuellen Umgebung:
```bash
python3 -m venv venv
```

2. Aktivieren der virtuellen Umgebung
```bash
source venv/bin/activate
```

3. Installation der Dependencies
```bash 
pip3 install -r reqirements.txt
```

4. Packen der App
```bash
python3 setup.py py2app
```

Die dann gepackte App ist im Ordner _dist_ zu finden. 

## Command-Line-Tool

Die Funktionalität des Tools ist mit dem Programm _ytload.py_ auch als Command-Line-Tool verfügbar. 

```
usage: ytload.py <link> [path]
```

Der optionale Parameter _path_ gibt den Speicherort des Videos an. Standardmäßig ist der Download-Ordner des Users gewählt. 

Der Link zum YouTube-Video muss dabei in Anführungszeichen übergeben werden. 
