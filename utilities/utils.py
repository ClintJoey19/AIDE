import time
from PyQt6.QtCore import QTimer

class ProcessController:
    def __init__(self):
        self.is_finished = False

    def start_process(self):
        for i in range(3):
            time.sleep(1)

        self.is_finished = True
