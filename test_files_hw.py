import csv
import os.path
import time
import zipfile
import requests
import xlrd
from selenium import webdriver
from selene import browser
from pypdf import PdfReader
from openpyxl import load_workbook


CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE) # получаем абсолютный путь к текущей директории
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'files') # делаем склейку пути к текущей директории и папке files
ZIP_DIR = os.path.join(CURRENT_DIRECTORY, 'resources') # делаем склейку пути к текущей директории и папке resources

# TODO Запаковать кодом в zip архив несколько разных файлов: pdf, xlsx, csv;
# TODO Положить его в ресурсы;

def test_create_zip():
    file_names = ['CSV_for_test.csv',
                  'XLSX_for_test.xlsx',
                  'PDF_for_test.pdf']

    archive_path = os.path.join(ZIP_DIR , 'archive.zip')

    with zipfile.ZipFile(archive_path, 'w') as zf:
        for file in file_names:
            file_path = os.path.join(TMP_DIR, file)
            zf.write(file_path, file)

# TODO Реализовать чтение и проверку содержимого каждого файла из архива не распаковывая сам архив;
