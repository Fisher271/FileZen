from genericpath import getctime
from undo_manager import UndoManager
import os
import datetime
import shutil
import logging

# Configure logging for file sorting operations
logging.basicConfig(
    filename='sorter.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

undo_manager = UndoManager()


def sort_by_date(files):
    """
    Saves the original state of files and initiates sorting by date.

    Args:
        files (list): List of files to be sorted.

    Returns:
        None
    """
    # Save the current state of files for undo functionality
    undo_manager.save_state("sort_by_date", files)

    # Logic for sorting files by date can be added here
    logging.info("Sorting by date is complete.")


def sort_by_year_and_month(folder_path):
    """
    Sorts files into subfolders by year and month based on their modification time.

    Args:
        folder_path (str): Path to the folder containing files to be sorted.

    Raises:
        FileNotFoundError: If the specified folder does not exist.

    Returns:
        None
    """
    if not os.path.exists(folder_path):
        logging.error(f"Folder does not exist: {folder_path}")
        raise FileNotFoundError(f"Folder does not exist: {folder_path}")

    processed_files = set()  # Tracks files that have been processed
    created_folders = set()  # Caches folders that have already been created

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Skip items that are not files
        if not os.path.isfile(file_path):
            logging.warning(f"Skipping non-file: {file_path}")
            continue

        try:
            # Use modification time instead of creation time for file sorting
            creation_time = os.stat(file_path).st_mtime
            creation_date = datetime.datetime.fromtimestamp(creation_time)

            # Log modification time for debugging purposes
            logging.info(
                f"File {file_name} has modification time: {creation_date.strftime('%Y-%m-%d')}")

            # Construct the target folder path based on year and month
            year_folder = os.path.join(folder_path, str(creation_date.year))
            month_folder = os.path.join(
                year_folder, creation_date.strftime('%m-%B'))

            # Create folders if they don't already exist
            if month_folder not in created_folders:
                logging.info(f"Creating folder: {month_folder}")
                os.makedirs(month_folder, exist_ok=True)
                created_folders.add(month_folder)

            # Move the file to its corresponding folder
            destination_path = os.path.join(month_folder, file_name)
            shutil.move(file_path, destination_path)

            # Mark file as processed and log its movement
            processed_files.add(file_name)
            logging.info(f"Moved {file_name} to {destination_path}")

        except Exception as e:
            logging.error(
                f"Unexpected error while processing file {file_name}: {e}")
            continue

    logging.info("Sorting by year and month completed successfully.")
