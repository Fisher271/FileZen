# **FileZen Documentation**

## **Опис програми (Українська)**

**FileZen** — це зручний інструмент для організації файлів із простим та зрозумілим графічним інтерфейсом. Він дозволяє впорядковувати файли **за типами** або **за датою створення (роками та місяцями)**. Програма має підтримку двох мов — **Української** та **Англійської**.

### **Особливості**
- **Сортування за типами файлів** (наприклад, документи, відео, зображення, музика).
- **Сортування за датами** (папки створюються за роком і місяцем).
- Зрозумілий інтерфейс, розроблений за допомогою **Tkinter**.
- Можливість перемикання мови інтерфейсу.
- **Кнопка "Скасувати"** для миттєвої зупинки процесу сортування.
- Журнал помилок (`app.log`) для діагностики.

### **Як використовувати**
1. **Запуск програми**:
   - Запустіть FileZen через інтерпретатор Python.
2. **Вибір мови**:
   - Натисніть кнопку **"Українська"** або **"English"** для налаштування інтерфейсу.
3. **Огляд папки**:
   - Використовуйте кнопку **"Огляд"** для вибору директорії, в якій будуть організовуватися файли.
4. **Вибір типу сортування**:
   - За типами файлів: створюються папки з розподілом на типи файлів (документи, відео тощо).
   - За датами: створюються папки з розподілом за роками і місяцями.
5. **Початок сортування**:
   - Натисніть **"Запустити"**. Програма розпочне організацію файлів.
6. **Зупинка процесу**:
   - Використовуйте кнопку **"Скасувати"** для припинення роботи.
7. **Результати**:
   - Перевірте організовані файли у вибраній папці.

#### **Автор іконки**

Іконка створена [Smashicons](https://www.flaticon.com/ru/free-icon/bonsai_1471402?term=%D0%B1%D0%BE%D0%BD%D1%81%D0%B0%D0%B9&page=1&position=7&origin=tag&related_id=1471402).

##### **Автор фону**

Фон створений [Q Garden Cyprus](https://pin.it/452ryNsSA)


---

## **Program Description (English)**

**FileZen** is a user-friendly file organization tool with a clean graphical interface. It allows you to arrange files **by type** or **by creation date (years and months)**. The program supports two languages: **Ukrainian** and **English**.

### **Features**
- **Sort by file type** (e.g., documents, videos, images, music).
- **Sort by creation date** (folders created by year and month).
- User-friendly GUI built with **Tkinter**.
- Multilingual interface with a language switcher.
- **Cancel button** to immediately stop the sorting process.
- Error logging (`app.log`) for diagnostics.

### **How to Use**
1. **Run the program**:
   - Launch FileZen using Python.
2. **Select Language**:
   - Use the **"Українська"** or **"English"** button to set the interface language.
3. **Choose a Folder**:
   - Click **"Browse"** to select the folder for file organization.
4. **Select Sorting Type**:
   - By type: Creates folders based on file types (e.g., documents, images, videos).
   - By date: Creates folders grouped by year and month.
5. **Start Sorting**:
   - Click **"Run"** to begin organizing the files.
6. **Stop Sorting**:
   - Press the **"Cancel"** button to halt the process.
7. **Check Results**:
   - View the organized files in the selected folder.

---

## **System Requirements**
- **Python**: Version 3.x
- **Modules**:
  - `tkinter` (for GUI)
  - `Pillow` (for image handling)
  - `organize_files`, `sort_by_date` (core logic)
- **Required Files**:
  - `icon/favicon.ico`: Program's icon.
  - `icon/background.jpg`: GUI background.

---

## **Error Log**
All application errors are logged in the `app.log` file for easier debugging and error tracking.

---

## **Quick Start**
1. Clone the repository:
   ```bash
   git clone https://github.com/Fisher271/FileZen.git


#### **Icon Author**
The icon was created by [Smashicons](https://www.flaticon.com/free-icon/bonsai_1471402?term=bonsai&page=1&position=7&origin=tag&related_id=1471402).

##### **Background Author**

Background created by [Q Garden Cyprus](https://pin.it/452ryNsSA)