import os
import shutil
import logging
from datetime import datetime
from undo_manager import UndoManager

# Configure logging for tracking file organization activities
logging.basicConfig(
    filename='organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

undo_manager = UndoManager()


def organize_files(folder_path):
    """
    Organizes files in the specified folder into subfolders based on their types.

    Args:
        folder_path (str): Path to the folder containing files to organize.

    Raises:
        FileNotFoundError: If the specified folder does not exist.

    Returns:
        None
    """
    if not os.path.exists(folder_path):
        logging.error(f"Folder does not exist: {folder_path}")
        raise FileNotFoundError(f"Folder does not exist: {folder_path}")

    # File type categorization based on extensions
    extensions = {
        "Documents": [".pdf", ".docx", ".txt", ".xls", ".xlsx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Archives": [".zip", ".rar"],
    }

    processed_files = set()  # Tracks already organized files

    for file_name in os.listdir(folder_path):
        if file_name in processed_files:
            continue  # Skip files already processed

        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            category = _get_file_category(file_name, extensions)
            target_folder = os.path.join(folder_path, category)
            _move_file(file_path, target_folder, category)
            processed_files.add(file_name)


def sort_by_type(folder_path, progress_var=None, cancel_flag=None, app=None, show_message=None):
    """
    Organizes files in the specified folder by their types and updates progress if applicable.

    Args:
        folder_path (str): Path to the folder containing files.
        progress_var (DoubleVar, optional): Progress tracker variable.
        cancel_flag (Event, optional): Flag to cancel sorting.
        app (Tk, optional): Tkinter instance for GUI updates.
        show_message (function, optional): Function to show messages in the GUI.

    Returns:
        None
    """
    logging.info("Sorting files by type...")
    organize_files(folder_path)
    logging.info("Files sorted by type successfully!")


def sort_by_date(folder_path, progress_var=None, cancel_flag=None, app=None, show_message=None):
    """
    Organizes files into subfolders based on their creation date.

    Args:
        folder_path (str): Path to the folder containing files.
        progress_var (DoubleVar, optional): Progress tracker variable.
        cancel_flag (Event, optional): Flag to cancel sorting.
        app (Tk, optional): Tkinter instance for GUI updates.
        show_message (function, optional): Function to show messages in the GUI.

    Raises:
        FileNotFoundError: If the specified folder does not exist.

    Returns:
        None
    """
    if not os.path.exists(folder_path):
        logging.error(f"Folder does not exist: {folder_path}")
        raise FileNotFoundError(f"Folder does not exist: {folder_path}")

    files = os.listdir(folder_path)
    processed_files = set()  # Tracks already organized files

    for file_name in files:
        if file_name in processed_files:
            continue  # Skip files already processed

        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            creation_time = os.path.getmtime(file_path)
            year, month = datetime.utcfromtimestamp(
                creation_time).strftime('%Y-%m').split('-')
            target_folder = os.path.join(folder_path, year, month)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, target_folder)
            processed_files.add(file_name)
            logging.info(f"Moved {file_name} to {year}/{month}")


def _get_file_category(file_name, extensions):
    """
    Determines the category of the file based on its extension.

    Args:
        file_name (str): Name of the file.
        extensions (dict): Dictionary mapping categories to file extensions.

    Returns:
        str: Category name for the file.
    """
    for category, exts in extensions.items():
        if any(file_name.lower().endswith(ext) for ext in exts):
            return category
    return "Others"


def _move_file(file_path, target_folder, category):
    """
    Moves a file to the specified folder based on its category.

    Args:
        file_path (str): Full path to the file being moved.
        target_folder (str): Destination folder path.
        category (str): Category name for logging.

    Returns:
        None
    """
    os.makedirs(target_folder, exist_ok=True)
    shutil.move(file_path, target_folder)
    logging.info(f"Moved {os.path.basename(file_path)} to {category}")
