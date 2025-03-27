# FileZen Documentation

## Опис програми (Українська)

FileZen — це графічний інтерфейс для організації файлів у вибраній папці. Програма дозволяє впорядковувати файли за типами або за роками та місяцями їх створення. Інтерфейс підтримує дві мови: Українську та Англійську.

### Особливості:
1. Організація файлів за типами.
2. Організація файлів за датою створення (роками та місяцями).
3. Інтуїтивно зрозумілий графічний інтерфейс на основі Tkinter.
4. Можливість перемикання між двома мовами.
5. **Кнопка "Скасувати" для зупинки процесу сортування**.

### Вимоги до системи:
- Python 3.x
- Модулі: tkinter, PIL (Pillow), organize_files, sort_by_date
- Наявність файлів `favicon.ico` та `background.jpg` у папці `icon`

### Інструкція з використання:
1. Запустіть програму FileZen.
2. Виберіть бажану мову, натиснувши на кнопку "Українська" або "English" у правому верхньому куті.
3. Натисніть "Огляд" та виберіть папку, яку потрібно впорядкувати.
4. Виберіть спосіб сортування:
   - **За типами файлів**: Файли будуть організовані у папки відповідно до їх типу (наприклад, зображення, документи, відео тощо).
   - **За роками і місяцями**: Файли будуть організовані за датою їх створення.
5. Натисніть кнопку "Запустити", щоб розпочати організацію.
6. **Якщо потрібно зупинити сортування, натисніть кнопку "Скасувати".**
7. Перевірте результати в обраній папці.

### Журнал помилок:
- У разі помилок вони будуть збережені у файлі `app.log` для подальшого аналізу.

---

## Program Description (English)

FileZen is a graphical interface tool designed to help organize files in a selected folder. The program allows users to sort files by type or by their creation date (years and months). The interface supports two languages: Ukrainian and English.

### Features:
1. Organize files by type.
2. Organize files by creation date (years and months).
3. Intuitive GUI built using Tkinter.
4. Language switching capability.
5. **Cancel button to stop the sorting process.**

### System Requirements:
- Python 3.x
- Modules: tkinter, PIL (Pillow), organize_files, sort_by_date
- Availability of `favicon.ico` and `background.jpg` in the `icon` folder

### Usage Instructions:
1. Launch the FileZen program.
2. Choose your preferred language by clicking "Українська" or "English" in the top-right corner.
3. Click "Browse" and select the folder you want to organize.
4. Choose the sorting method:
   - **By file types**: Files will be grouped into folders based on their type (e.g., images, documents, videos, etc.).
   - **By years and months**: Files will be sorted into folders by their creation date.
5. Click the "Run" button to start organizing.
6. **If you need to stop the sorting process, click the "Cancel" button.**
7. Check the results in the selected folder.

### Error Log:
- In case of errors, they will be saved in the `app.log` file for further debugging.

## Credits
- Icons provided by [Smashicons](https://www.flaticon.com/ru/free-icon/bonsai_1471402?term=%D0%B1%D0%BE%D0%BD%D1%81%D0%B0%D0%B9&page=1&position=7&origin=tag&related_id=1471402)
- Background procided by Q Garden Cyprus (https://pin.it/4uWkvn0vk)