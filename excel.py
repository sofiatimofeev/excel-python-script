import tkinter as tk
from tkinter import filedialog
import openpyxl as xlx
import xlrd as xl

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
    bank_file = get_file_path_hash()
    print(bank_file)

if __name__ == "__main__":
    main()