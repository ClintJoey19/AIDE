from pdf_reader.extractor import get_order_code

if __name__ == "__main__":
    pdf = "./pdf_folder/try.pdf"
    print(get_order_code(pdf))