from threading import Thread
from PyQt5.QtCore import *
import threading
import os, sys
import requests

class Famous_saying_thread(QThread):
    """docstring for Famous_saying_thread"""
    update = pyqtSignal(dict)

    def __init__(self):
        super(Famous_saying_thread, self).__init__()

    def run(self):
        url = "https://hitokoto.jijidown.com/v1/api/hitokoto"
        try:
            data = requests.get(url).json()
            self.update.emit(data)
        except Exception:
            pass