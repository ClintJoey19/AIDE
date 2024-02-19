import re
from pdfminer.high_level import extract_text

order_code_pattern = r'\b\d{6}\b'

def get_order_code(pdf_path):
    text = extract_text(pdf_path)
    code = re.findall(order_code_pattern, text)
    return code