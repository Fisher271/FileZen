import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from organize_files import organize_files
from sort_by_date import sort_by_year_and_month
import logging
import os
import sys

# Налаштування логування
logging.basicConfig(filename='app.log', level=logging.ERROR)

# Поточна мова (за замовчуванням Українська)
current_language = "uk"

# Тексти для інтерфейсу різними мовами
translations = {
    "uk": {
        "title": "FileZen",
        "choose_folder": "Виберіть папку для сортування:",
        "browse": "Огляд",
        "sort_by": "Оберіть спосіб сортування:",
        "type": "За типами файлів",
        "date": "За роками і місяцями",
        "run": "Запустити",
        "warning": "Попередження",
        "no_folder": "Будь ласка, виберіть папку!",
        "success_type": "Файли впорядковані за типами!",
        "success_date": "Файли впорядковані за роками та місяцями!",
        "error": "Помилка",
        "no_sort": "Будь ласка, оберіть спосіб сортування!"
    },
    "en": {
        "title": "FileZen",
        "choose_folder": "Select a folder to organize:",
        "browse": "Browse",
        "sort_by": "Choose sorting method:",
        "type": "By file types",
        "date": "By years and months",
        "run": "Run",
        "warning": "Warning",
        "no_folder": "Please select a folder!",
        "success_type": "Files organized by type!",
        "success_date": "Files organized by year and month!",
        "error": "Error",
        "no_sort": "Please choose a sorting method!"
    }
}

# Функції для зміни мови


def switch_language(lang):
    global current_language
    current_language = lang
    update_texts()


def update_texts():
    # Оновлення текстів у Canvas
    canvas.itemconfig(title_text, text=translations[current_language]["title"])
    canvas.itemconfig(choose_folder_text,
                      text=translations[current_language]["choose_folder"])
    canvas.itemconfig(
        sort_by_text, text=translations[current_language]["sort_by"])
    type_button.config(text=translations[current_language]["type"])
    date_button.config(text=translations[current_language]["date"])
    run_button.config(text=translations[current_language]["run"])
    browse_button.config(text=translations[current_language]["browse"])

# Функція для кнопки "Скасувати"


def cancel_operation():
    cancel_flag.set(True)
    messagebox.showinfo("Скасування", "Операція скасована!")

# Функція для вибору папки


def choose_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

# Основна функція організації файлів


def run_organizer():
    global cancel_flag
    cancel_flag.set(False)  # Скидаємо прапорець скасування
    folder = folder_path.get()
    if not folder:
        messagebox.showwarning(
            translations[current_language]["warning"],
            translations[current_language]["no_folder"]
        )
        return
    if sort_option.get() == "type":
        for progress in organize_files(folder):  # організатор повертає прогрес
            if cancel_flag.get():
                break
        if not cancel_flag.get():
            messagebox.showinfo(
                translations[current_language]["success_type"],
                translations[current_language]["success_type"]
            )
    elif sort_option.get() == "date":
        for progress in sort_by_year_and_month(folder):  # прогрес сортування
            if cancel_flag.get():
                break
        if not cancel_flag.get():
            messagebox.showinfo(
                translations[current_language]["success_date"],
                translations[current_language]["success_date"]
            )
    else:
        messagebox.showerror(
            translations[current_language]["error"],
            translations[current_language]["no_sort"]
        )


# Отримання базового шляху
if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# Головне вікно
app = tk.Tk()
app.title(translations[current_language]["title"])
app.geometry("740x600")

# Ініціалізація змінної для кнопки "Скасувати" після створення вікна
cancel_flag = tk.BooleanVar(value=False)

# Додаємо іконку
try:
    icon_path = os.path.join(base_path, "icon/favicon.ico")
    app.iconbitmap(icon_path)
except Exception as e:
    logging.error(f"Не вдалося завантажити іконку: {e}")

# Додаємо фон
try:
    background_path = os.path.join(base_path, "icon/background.jpg")
    background_image = Image.open(background_path)
    background_image = background_image.resize((740, 600))  # Зміна розміру
    background_photo = ImageTk.PhotoImage(background_image)
except Exception as e:
    logging.error(f"Не вдалося завантажити фон: {e}")
    background_photo = None

canvas = tk.Canvas(app, width=740, height=600)
canvas.pack(fill="both", expand=True)

if background_photo:
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Змінні
folder_path = tk.StringVar()
sort_option = tk.StringVar()

# Елементи GUI
title_text = canvas.create_text(370, 100, text=translations[current_language]["title"], font=(
    "Helvetica", 30, "bold"), fill="white")
choose_folder_text = canvas.create_text(
    370, 200, text=translations[current_language]["choose_folder"], fill="white", font=("Helvetica", 12))
canvas.create_window(370, 230, window=tk.Entry(
    app, textvariable=folder_path, width=50, bg="#A9A9A9"))
browse_button = tk.Button(
    app, text=translations[current_language]["browse"], command=choose_folder, bg="#A9A9A9")
canvas.create_window(370, 260, window=browse_button)
sort_by_text = canvas.create_text(
    370, 300, text=translations[current_language]["sort_by"], fill="white", font=("Helvetica", 14))
type_button = tk.Radiobutton(
    app, text=translations[current_language]["type"], variable=sort_option, value="type", bg="#A9A9A9")
canvas.create_window(370, 330, window=type_button)
date_button = tk.Radiobutton(
    app, text=translations[current_language]["date"], variable=sort_option, value="date", bg="#A9A9A9")
canvas.create_window(370, 360, window=date_button)
run_button = tk.Button(
    app, text=translations[current_language]["run"], command=run_organizer, bg="#A9A9A9")
canvas.create_window(370, 400, window=run_button)

# Кнопка для скасування
cancel_button = tk.Button(
    app, text="Скасувати", command=cancel_operation, bg="#A9A9A9"
)
canvas.create_window(370, 450, window=cancel_button)

# Кнопки для зміни мови
language_uk_button = tk.Button(
    app, text="Українська", command=lambda: switch_language("uk"), bg="#A9A9A9")
canvas.create_window(630, 20, window=language_uk_button)
language_en_button = tk.Button(
    app, text="English", command=lambda: switch_language("en"), bg="#A9A9A9")
canvas.create_window(700, 20, window=language_en_button)

# Запуск програми
app.mainloop()
