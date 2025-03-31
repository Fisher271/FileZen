import logging


def update_texts(canvas, elements, translations, current_language):
    """
    Updates text elements in the graphical interface dynamically based on the chosen language.

    Args:
        canvas (Tkinter Canvas): Canvas object where text elements are drawn.
        elements (dict): Dictionary of GUI components that require text updates.
        translations (dict): Language translation data loaded from a JSON file.
        current_language (StringVar): Holds the code of the currently selected language.

    Returns:
        None
    """
    lang = current_language.get()
    if lang not in translations:
        logging.warning(f"Language '{lang}' not found. Defaulting to 'en'.")
        lang = "en"  # Default to English if language is not found

    try:
        # Update text elements on the canvas
        canvas.itemconfig(elements['title'], text=translations.get(
            lang, {}).get("title", "FileZen"))
        canvas.itemconfig(elements['choose_folder'], text=translations.get(
            lang, {}).get("choose_folder", "Choose Folder:"))
        canvas.itemconfig(elements['sort_by'], text=translations.get(
            lang, {}).get("sort_by", "Choose sorting method:"))

        # Dynamically update button texts based on the selected language
        if 'browse_button' in elements:
            elements['browse_button'].config(
                text=translations.get(lang, {}).get("browse", "Browse"))
        if 'type_button' in elements:
            elements['type_button'].config(
                text=translations.get(lang, {}).get("type", "Type"))
        if 'date_button' in elements:
            elements['date_button'].config(
                text=translations.get(lang, {}).get("date", "Date"))
        if 'run_button' in elements:
            elements['run_button'].config(
                text=translations.get(lang, {}).get("run", "Run"))
        if 'undo_button' in elements:
            elements['undo_button'].config(
                text=translations.get(lang, {}).get("undo", "Undo"))

        logging.info(f"GUI texts successfully updated for language: {lang}")

    except KeyError as e:
        logging.error(f"KeyError during text updates: {e}")
    except Exception as e:
        logging.error(f"Unexpected error during text updates: {e}")


def switch_language(lang, current_language, update_texts, canvas, elements, translations):
    """
    Handles language switching and updates text elements in the graphical interface accordingly.

    Args:
        lang (str): Code of the language to switch to (e.g., 'en', 'uk').
        current_language (StringVar): Holds the code of the currently selected language.
        update_texts (function): Function to refresh text elements dynamically.
        canvas (Tkinter Canvas): Canvas object where text elements are drawn.
        elements (dict): Dictionary of GUI components that require text updates.
        translations (dict): Language translation data loaded from a JSON file.

    Returns:
        None
    """
    try:
        # Verify that the chosen language exists in translations
        if lang not in translations:
            logging.warning(
                f"Language '{lang}' is not available in translations.")
            return

        # Update the current language setting
        current_language.set(lang)
        logging.info(f"Language switched successfully to: {lang}")

        # Refresh text elements based on the updated language
        update_texts(canvas, elements, translations, current_language)

    except KeyError as e:
        logging.error(f"KeyError during language switching: {e}")
    except Exception as e:
        logging.error(f"Unexpected error during language switching: {e}")
