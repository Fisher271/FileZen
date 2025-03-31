import tkinter as tk
# For folder selection dialog and progress bar
from tkinter import filedialog, ttk
from resources import load_translations, load_background, load_icon
from gui_helpers import create_canvas, add_progress_bar, add_language_buttons, add_undo_button
from event_handler import update_texts, switch_language
from undo_manager import UndoManager
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Initialize main application window
app = tk.Tk()
app.title("FileZen")
app.geometry("740x600")

# Load external resources, such as translations, background image, and icon
try:
    translations = load_translations("resources/translations.json")
    background_photo = load_background("icon/background.jpg")
    load_icon(app, "icon/favicon.ico")
except Exception as e:
    logging.error(f"Error loading resources: {e}")
    translations = {}
    background_photo = None

# Initialize variables for application state
current_language = tk.StringVar(value="uk")  # Default language is Ukrainian
folder_path = tk.StringVar()
sort_option = tk.StringVar(value="type")
progress_var = tk.DoubleVar()

# Create and configure the main canvas for the UI
canvas = create_canvas(app, background_photo)

# Text elements for user interface
lang_translations = translations.get(current_language.get(), {})
elements = {
    'title': canvas.create_text(
        370, 100,
        text=lang_translations.get("title", "FileZen"),
        font=("Helvetica", 30, "bold"), fill="white"
    ),
    'choose_folder': canvas.create_text(
        370, 200,
        text=lang_translations.get(
            "choose_folder", "Choose folder for sorting:"),
        font=("Helvetica", 12), fill="white"
    ),
    'sort_by': canvas.create_text(
        370, 320,
        text=lang_translations.get("sort_by", "Choose sorting method:"),
        font=("Helvetica", 14), fill="white"
    ),
}

# Label to display selected folder path
folder_label = tk.Label(
    app,
    text=" ",  # Empty initial text
    bg="#A9A9A9",
    fg="black",
    anchor="w"
)
folder_label.place(x=200, y=220, width=370)

# Configure buttons and their behavior
elements['browse_button'] = tk.Button(
    app,
    text=lang_translations.get("browse", "Browse"),
    bg="#A9A9A9",
    width=10,
    height=1,
    command=lambda: browse_directory()
)
elements['browse_button'].place(x=320, y=250)

elements['type_button'] = tk.Radiobutton(
    app,
    text=lang_translations.get("type", "Type"),
    variable=sort_option,
    value="type",
    bg="#A9A9A9",
    width=15,
    anchor="w"
)
elements['type_button'].place(x=200, y=350)

elements['date_button'] = tk.Radiobutton(
    app,
    text=lang_translations.get("date", "Date"),
    variable=sort_option,
    value="date",
    bg="#A9A9A9",
    width=15,
    anchor="w"
)
elements['date_button'].place(x=400, y=350)

elements['run_button'] = tk.Button(
    app,
    text=lang_translations.get("run", "Run"),
    bg="#A9A9A9",
    width=15,
    height=1,
    command=lambda: run_application()
)
elements['run_button'].place(x=300, y=400)

# Add a progress bar to show sorting progress
add_progress_bar(app, canvas, progress_var)

# Add language switcher buttons
add_language_buttons(
    app,
    canvas,
    switch_language,
    update_texts,
    current_language,
    elements,  # Pass UI elements for dynamic updates
    translations  # Pass translations for localization
)

# Initialize undo functionality
undo_manager = UndoManager()

# Define function to handle undo action


def undo_action():
    try:
        # Undo file organization actions
        undo_manager.undo("organize_files")
        logging.info("Undo action executed successfully.")
    except Exception as e:
        logging.error(f"Error executing undo: {e}")


# Add Undo button to the interface
add_undo_button(app, canvas, undo_action, current_language, elements)

# Define function for folder selection


def browse_directory():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)  # Save selected path
        folder_label.config(text=folder)  # Update label with folder path
        logging.info(f"Folder selected: {folder}")
    else:
        error_message = lang_translations.get(
            "error", "Error: No folder selected")
        folder_label.config(text=error_message)  # Show localized error
        logging.warning("No folder selected.")

# Define function to start sorting process


def run_application():
    selected_folder = folder_path.get()
    if selected_folder:
        logging.info(f"Running application in folder: {selected_folder}")
        # Add sorting logic here
    else:
        logging.warning("No folder selected. Cannot proceed.")


# Start the Tkinter main event loop
app.mainloop()
