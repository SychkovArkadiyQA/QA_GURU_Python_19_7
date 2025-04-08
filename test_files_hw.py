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
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE  ) # получаем абсолютный путь к текущей директории
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'files') # делаем склейку пути к текущей директории и папки files
if not os.path.exists(TMP_DIR):
    os.mkdir(TMP_DIR)

# TODO Запаковать кодом в zip архив несколько разных файлов: pdf, xlsx, csv;