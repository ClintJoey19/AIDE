from pdf_reader.extractor import get_order_code
from automation.automate_data_entry import automate
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app_title = "AIDE"

        self.setWindowTitle(self.app_title)

        box = QVBoxLayout()

        # title
        title = QLabel(self.app_title)
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        box.addWidget(title)

        # functionalities label
        func_label = QLabel("Choose automation function: ")
        font = func_label.font()
        font.setPointSize(12)
        func_label.setFont(font)
        func_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        box.addWidget(func_label)

        # available tasks
        self.data_entry_cb = QCheckBox("Data Entry")
        box.addWidget(self.data_entry_cb)

        # action btn
        action_btn = QPushButton("Start")
        action_btn.clicked.connect(self.run)
        box.addWidget(action_btn)

        widget = QWidget()
        widget.setLayout(box)
        self.setCentralWidget(widget)

    def run(self):
        if (self.data_entry_cb.isChecked()):
            print("Checked")
            pdf = "./pdf_folder/try.pdf"
            codes = self.run_extract(pdf)
            automate(codes)
        else:
            print("Not Checked")

    def run_extract(self, pdf):
        code = get_order_code(pdf)
        return code

def set_Ui():
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    app.exec()

if __name__ == "__main__":
    set_Ui()

    # pdf = "./pdf_folder/try.pdf"
    # codes = get_order_code(pdf)
    # automate(codes)