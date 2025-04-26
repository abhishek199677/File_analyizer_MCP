import pandas as pd 
import fitz   


def parser_csv(file_path):
    return pd.read_csv(file_path)

def parser_excel(file_path):
    return pd.read_excel(file_path)

def parser_pdf(file_path):
    pdf = fitz.open(file_path)  # this will open and read the pdf file
    text = "\n".join([page.get_text() for page in pdf])  # it will get all the text from the pdf file from each page
    return text