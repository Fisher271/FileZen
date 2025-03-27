import os
import shutil


def organize_files(folder_path):
    extensions = {
        "Documents": [".pdf", ".docx", ".txt", ".xls", ".xlsx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Archives": [".zip", ".rar"],
    }

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            for category, exts in extensions.items():
                if any(file_name.lower().endswith(ext) for ext in exts):
                    target_folder = os.path.join(folder_path, category)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, target_folder)
                    print(f"Moved {file_name} to {category}")
                    # Повертаємо прогрес
                    yield f"Moved {file_name} to {category}"
                    break
