from pdf_reader.extractor import get_order_code
from automation.automate_data_entry import automate

if __name__ == "__main__":
    pdf = "./pdf_folder/try.pdf"
    codes = get_order_code(pdf)
    automate(codes)