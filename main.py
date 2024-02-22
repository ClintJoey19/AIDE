from pdf_reader.extractor import get_order_code, get_file_name
from automation.automate_data_entry import automate
import sys
from PyQt6.QtCore import QSize, Qt
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
from PyQt6.QtGui import QPixmap

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

        # pdf icon
        self.pdf_icon_label = QLabel(self)
        self.pdf_icon_label.setBaseSize(QSize(40, 60))
        pdf_icon = QPixmap("./assets/pdf.png")
        self.pdf_icon_label.setPixmap(pdf_icon)
        self.pdf_icon_label.setVisible(False)
        box.addWidget(self.pdf_icon_label)

        # selected file
        self.selected_file = QLabel("")
        font = self.selected_file.font()
        font.setPointSize(11)
        font.setItalic(True)
        self.selected_file.setFont(font)
        self.selected_file.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.selected_file.setVisible(False)
        box.addWidget(self.selected_file)

        # invoice file input
        self.invoice_file = QPushButton("Select a file", self)
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
            pdf = self.pdf_path
            if pdf and pdf != "":
                codes = self.run_extract(pdf)
                automate(codes)
            else:
                print("No invoice found")
        else:
            print("Automation type not set")

        self.action_btn.setEnabled(True)

    def open_invoice_pdf(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf)")

        if file_name:
            self.pdf_path = file_name
            self.selected_file.setText(get_file_name(self.pdf_path))
            self.setFixedSize(QSize(300, 250))
            self.pdf_icon_label.setVisible(True)
            self.selected_file.setVisible(True)

    def run_extract(self, pdf):
        code = get_order_code(pdf)
        return code

def main():
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()