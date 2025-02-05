import tkinter as tk
from tkinter import filedialog
import openpyxl as xlx
import xlwt as xl

def create_file_dialog():
    root = tk.Tk()
    root.withdraw()

def get_file_path_bank():
    file = filedialog.askopenfilename(title="Choose bank excel", filetypes=[("Excel files", "*.xlsx")])
    return file

def get_file_path_hash():
    file = filedialog.askopenfilename(title="Choose Hash excel", filetypes=[("Excel files", "*.xls")])
    return file


def main():
    bank_file = get_file_path_bank()
    try:
        bank_wb = xlx.load_workbook(filename=bank_file)
        bank_ws = bank_wb.worksheets[0]
        bank_ws['A12'] = "test"
        bank_wb.save(bank_file)
    except:
        print("File is opne close it and retry")


if __name__ == "__main__":
    main()