import unittest
from unittest.mock import patch, mock_open
from resources import load_translations, load_background, load_icon
from PIL import Image, ImageTk
import tkinter as tk
import os


class TestResources(unittest.TestCase):

    def setUp(self):
        """Set up paths for testing."""
        self.test_translations_path = "resources/test_translations.json"
        self.test_background_path = "icon/test_background.jpg"
        self.test_icon_path = "icon/test_icon.ico"

    @patch("resources.os.path.exists")
    @patch("resources.open", new_callable=mock_open, read_data='{"en": {"title": "Test Title"}}')
    def test_load_translations_success(self, mock_file, mock_exists):
        """Test if translations load successfully."""
        mock_exists.return_value = True  # Simulate file existence
        translations = load_translations(self.test_translations_path)
        self.assertIn("en", translations)
        self.assertEqual(translations["en"]["title"], "Test Title")

    @patch("resources.os.path.exists")
    def test_load_translations_file_not_found(self, mock_exists):
        """Test behavior when translations file is not found."""
        mock_exists.return_value = False  # Simulate file absence
        translations = load_translations(self.test_translations_path)
        self.assertEqual(translations, {})  # Should return an empty dictionary

    @patch("resources.os.path.exists")
    @patch("resources.Image.open")
    @patch("resources.ImageTk.PhotoImage")
    def test_load_background_success(self, mock_photoimage, mock_image_open, mock_exists):
        """Test if background image loads successfully."""
        mock_exists.return_value = True  # Simulate file existence
        mock_image = mock_image_open.return_value
        mock_image.size = (1000, 800)  # Simulated image dimensions
        result = load_background(self.test_background_path)
        self.assertTrue(mock_photoimage.called)  # Ensure PhotoImage was called
        # Should return an ImageTk.PhotoImage object
        self.assertIsNotNone(result)

    @patch("resources.os.path.exists")
    def test_load_background_file_not_found(self, mock_exists):
        """Test behavior when background image is not found."""
        mock_exists.return_value = False  # Simulate file absence
        result = load_background(self.test_background_path)
        self.assertIsNone(result)  # Should return None

    @patch("tkinter.Tk.iconbitmap")
    @patch("resources.os.path.exists")
    def test_load_icon_success(self, mock_exists, mock_iconbitmap):
        """Test if icon loads successfully."""
        mock_exists.return_value = True  # Simulate file existence

        # Create the expected path with normalized formatting
        expected_path = os.path.normpath(os.path.abspath(self.test_icon_path))

        app = tk.Tk()
        load_icon(app, self.test_icon_path)

        # Ensure iconbitmap was called with the correct normalized absolute path
        mock_iconbitmap.assert_called_with(expected_path)

    @patch("resources.os.path.exists")
    def test_load_icon_file_not_found(self, mock_exists):
        """Test behavior when icon file is not found."""
        mock_exists.return_value = False  # Simulate file absence
        app = tk.Tk()
        load_icon(app, self.test_icon_path)
        # No assertion needed as function logs error without crashing


if __name__ == "__main__":
    unittest.main()
