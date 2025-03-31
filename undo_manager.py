import os
import logging

# Configure logging for UndoManager operations
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class UndoManager:
    """
    Manages the undo functionality for file operations, allowing restoration
    of files to their original state after sorting.
    """

    def __init__(self):
        """
        Initializes the UndoManager instance, storing states for various sorting types.
        """
        self.states = {}  # Dictionary to store the original states of files.

    def save_state(self, sort_type, files):
        """
        Saves the original state of files before applying sorting operations.

        Args:
            sort_type (str): The type of sorting operation (e.g., "organize_files", "sort_by_date").
            files (list): List of file paths to save their original state.

        Returns:
            None
        """
        self.states[sort_type] = {
            file: os.path.basename(file) for file in files}
        logging.info(f"Original state saved for sorting type: {sort_type}")

    def undo(self, sort_type):
        """
        Restores files to their original state for the specified sorting type.

        Args:
            sort_type (str): The type of sorting operation to undo.

        Returns:
            None
        """
        if sort_type not in self.states:
            logging.warning(
                f"No undo data available for sorting type: {sort_type}.")
            return

        for file, original_path in self.states[sort_type].items():
            if os.path.exists(file):  # Verify if the file still exists
                # Move the file back to its original path
                os.rename(file, original_path)
                logging.info(f"File restored: {file} -> {original_path}")

        logging.info(f"Undo operation completed for sorting type: {sort_type}")
