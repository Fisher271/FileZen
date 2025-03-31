import os
import json
import logging
from PIL import Image, ImageTk

# Configure logging for debugging and tracking application state
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def load_translations(file_path):
    """
    Loads translation data from a JSON file.

    Args:
        file_path (str): The path to the translations JSON file.

    Returns:
        dict: A dictionary containing translations, or an empty dictionary if an error occurs.
    """
    if not os.path.exists(file_path):
        logging.error(
            f"Translations file not found at {file_path}. Returning empty dictionary.")
        return {}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            translations = json.load(f)
            logging.info(f"Translations loaded successfully from {file_path}")

            # Validate that the content of the JSON file is a dictionary
            if not isinstance(translations, dict):
                logging.error(
                    f"Invalid format in {file_path}. Expected a dictionary structure.")
                return {}
            return translations
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding error at {file_path}: {e}")
        return {}
    except Exception as e:
        logging.error(
            f"Unexpected error loading translations from {file_path}: {e}")
        return {}


def load_background(file_path):
    """
    Loads a background image for the application.

    Args:
        file_path (str): The path to the background image file.

    Returns:
        PhotoImage or None: The loaded image as a PhotoImage object, or None if an error occurs.
    """
    if not os.path.exists(file_path):
        logging.error(
            f"Background image not found at {file_path}. Returning None.")
        return None

    try:
        background_img = Image.open(file_path)
        background_photo = ImageTk.PhotoImage(background_img)
        logging.info(f"Background image loaded successfully from {file_path}")
        return background_photo
    except Exception as e:
        logging.error(
            f"Unexpected error loading background image from {file_path}: {e}")
        return None


def load_icon(app, file_path):
    """
    Sets the application icon.

    Args:
        app (Tk): The main Tkinter application instance.
        file_path (str): The path to the icon file.

    Returns:
        None: Logs success or failure messages regarding the icon setup.
    """
    if not os.path.exists(file_path):
        logging.error(f"Icon file not found at {file_path}. No icon applied.")
        return

    try:
        app.iconbitmap(file_path)
        logging.info(f"Icon loaded successfully from {file_path}")
    except Exception as e:
        logging.error(f"Unexpected error loading icon from {file_path}: {e}")
