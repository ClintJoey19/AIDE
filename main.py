from pdf_reader.extractor import get_order_code
from automation.automate_data_entry import automate
import sys
from PyQt6.QtCore import QSize, Qt, QFileInfo
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog
)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app_title = "AIDE"
        self.pdf_path = None

        self.setWindowTitle(self.app_title)

        box = QVBoxLayout()

        # title
        title = QLabel(self.app_title)
        font = title.font()
        font.setPointSize(20)
        font.setBold(True)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        box.addWidget(title)

        # invoice input label
        invoice_input = QLabel("Choose invoice (PDF): ")
        font = invoice_input.font()
        font.setPointSize(11)
        invoice_input.setFont(font)
        invoice_input.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        box.addWidget(invoice_input)

        # invoice file input
        self.invoice_file = QPushButton("Select a file")
        self.invoice_file.setShortcut("Ctrl+O")
        self.invoice_file.clicked.connect(self.open_invoice_pdf)
        box.addWidget(self.invoice_file)

        # functionalities label
        func_label = QLabel("Choose automation function: ")
        font = func_label.font()
        font.setPointSize(11)
        func_label.setFont(font)
        func_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        box.addWidget(func_label)

        # available tasks
        self.data_entry_cb = QCheckBox("Data Entry")
        box.addWidget(self.data_entry_cb)

        # action btn
        self.action_btn = QPushButton("Start")
        self.action_btn.setShortcut("Ctrl+R")
        self.action_btn.clicked.connect(self.run)
        box.addWidget(self.action_btn)

        widget = QWidget()
        widget.setLayout(box)
        self.setFixedSize(QSize(300, 200))
        self.setCentralWidget(widget)

    def run(self):
        if (self.data_entry_cb.isChecked()):
            self.action_btn.setEnabled(False)
            pdf = "./pdf_folder/try.pdf"
            codes = self.run_extract(pdf)
            automate(codes)
            self.action_btn.setEnabled(True)

    def open_invoice_pdf(self):
        # todo: get pdf absolute path
        print("pdf url")

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