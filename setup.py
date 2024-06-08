from setuptools import setup

APP = ['YouTubeDownloader.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'images/icon.icns',
    'packages': ['tkinter', 'customtkinter', 'threading', 'pytube'],
    'includes': ['tkinter', 'customtkinter', 'threading', 'pytube']
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
