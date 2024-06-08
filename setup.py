from setuptools import setup

APP = ['YouTubeDownloader.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'images/icon.icns',
    'packages': ['tkinter', 'customtkinter', 'threading', 'pytube'],
    'includes': ['tkinter', 'customtkinter', 'threading', 'pytube'],
    'plist': {
        'CFBundleName': 'YouTube Downloader',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
        'CFBundleIdentifier': 'de.simoma.youtubedownloader',
        'CFBundleDevelopmentRegion': 'Deutsch',
        'CFBundleDisplayName': 'YouTube Downloader',
        'NSHumanReadableCopyright': '© 2024 Simon Litges. All rights reserved.',
        'CFBundleGetInfoString': 'YouTube Downloader 1.0.0',
        'CFBundleExecutable': 'YouTubeDownloader'
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
