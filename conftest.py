import os
import zipfile
import pytest

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE) # получаем абсолютный путь к текущей директории
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'files') # делаем склейку пути к текущей директории и папке files
ZIP_DIR = os.path.join(CURRENT_DIRECTORY, 'resources') # делаем склейку пути к текущей директории и папке resources

# TODO Запаковать кодом в zip архив несколько разных файлов: pdf, xlsx, csv;
# TODO Положить его в ресурсы;

# Фикстура для создания архива из файлов и удаления после выполнения тестов
@pytest.fixture(scope="session", autouse=True)
def create_zip():
    file_names = ['CSV_for_test.csv',
                  'XLSX_for_test.xlsx',
                  'PDF_for_test.pdf']

    archive_path = os.path.join(ZIP_DIR , 'archive.zip')

    with zipfile.ZipFile(archive_path, 'w') as zf:
        for file in file_names:
            file_path = os.path.join(TMP_DIR, file)
            zf.write(file_path, file)

    yield

    if os.path.exists(archive_path):
        os.remove(archive_path)
        print(f"\nАрхив {archive_path} удален")