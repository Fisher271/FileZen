import tkinter as tk
from tkinter import ttk
import logging


def create_canvas(app, background_photo=None):
    """
    Creates and configures a canvas for the application.

    Args:
        app (Tk): The main Tkinter application instance.
        background_photo (PhotoImage, optional): An optional background image for the canvas.

    Returns:
        Canvas: A fully configured canvas widget.
    """
    canvas = tk.Canvas(app, width=740, height=600)
    canvas.pack(fill="both", expand=True)
    if background_photo:
        try:
            canvas.create_image(0, 0, image=background_photo, anchor="nw")
        except Exception as e:
            logging.error(f"Error adding background image: {e}")
    return canvas


def add_progress_bar(app, canvas, progress_var):
    """
    Adds a progress bar to the canvas for indicating task progression.

    Args:
        app (Tk): The main Tkinter application instance.
        canvas (Canvas): The canvas where the progress bar will be embedded.
        progress_var (DoubleVar): Variable to track the progress percentage.

    Returns:
        Progressbar: A configured progress bar widget.
    """
    try:
        progress_bar = ttk.Progressbar(app, variable=progress_var, maximum=100)
        canvas.create_window(370, 550, window=progress_bar, width=300)
        return progress_bar
    except Exception as e:
        logging.error(f"Error adding progress bar: {e}")
        return None


def add_language_buttons(app, canvas, switch_language, update_texts, current_language, elements, translations):
    """
    Adds language selection buttons (Ukrainian and English) to the interface.

    Args:
        app (Tk): The main Tkinter application instance.
        canvas (Canvas): The canvas where the buttons will be placed.
        switch_language (function): Function to change the application's language.
        update_texts (function): Function to dynamically update text elements.
        current_language (StringVar): Current selected language variable.
        elements (dict): Dictionary of UI components to update dynamically.
        translations (dict): Loaded translations for supported languages.

    Returns:
        None
    """
    try:
        # Ukrainian language button
        language_uk_button = tk.Button(
            app,
            text="Українська",
            command=lambda: switch_language(
                "uk", current_language, update_texts, canvas, elements, translations),
            bg="#D3D3D3", fg="black"
        )
        canvas.create_window(630, 20, window=language_uk_button)

        # English language button
        language_en_button = tk.Button(
            app,
            text="English",
            command=lambda: switch_language(
                "en", current_language, update_texts, canvas, elements, translations),
            bg="#D3D3D3", fg="black"
        )
        canvas.create_window(700, 20, window=language_en_button)
    except Exception as e:
        logging.error(f"Error adding language buttons: {e}")


def add_undo_button(app, canvas, undo_action, current_language, elements):
    """
    Adds an Undo button to the canvas with multilingual support.

    Args:
        app (Tk): The main Tkinter application instance.
        canvas (Canvas): The canvas where the Undo button will be placed.
        undo_action (function): Function to perform the undo operation.
        current_language (StringVar): Currently selected language to localize button text.
        elements (dict): Dictionary to manage and update UI components.

    Returns:
        None
    """
    try:
        # Text options for supported languages
        lang_text = {
            "en": "Undo",
            "uk": "Скасувати"
        }

        # Get button text based on the current language, defaulting to English
        button_text = lang_text.get(current_language.get(), "Undo")

        # Create the Undo button
        elements['undo_button'] = tk.Button(
            app,
            text=button_text,
            command=undo_action,
            bg="#A9A9A9", fg="black",
            width=15,
            height=1,
        )
        canvas.create_window(357, 450, window=elements['undo_button'])
    except Exception as e:
        logging.error(f"Error adding Undo button: {e}")
