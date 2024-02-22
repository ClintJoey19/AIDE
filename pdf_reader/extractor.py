import re
from os import path
from pdfminer.high_level import extract_text

# regex pattern of the product/order code: the pattern should be appropriate for each invoice
order_code_pattern = r'\b\d{6}\b'

def get_order_code(pdf_path):
    text = extract_text(pdf_path)
    code = re.findall(order_code_pattern, text)
    return code

def get_file_name(file_path):
    return path.basename(file_path)