from genericpath import getctime
import os
import datetime
import shutil


def sort_by_year_and_month(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            # Отримання часу створення файлу
            creation_time = getctime(file_path)
            creation_date = datetime.datetime.fromtimestamp(creation_time)

            # Формування шляху до папки "рік/місяць"
            year_folder = os.path.join(folder_path, str(creation_date.year))
            month_folder = os.path.join(
                year_folder, creation_date.strftime('%B'))

            # Створення папок, якщо вони ще не існують
            os.makedirs(month_folder, exist_ok=True)

            # Переміщення файлу
            shutil.move(file_path, month_folder)
            print(
                f"Moved {file_name} to {year_folder}/{creation_date.strftime('%B')}")
