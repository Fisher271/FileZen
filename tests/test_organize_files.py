import unittest
from unittest.mock import patch, MagicMock, mock_open
from organize_files import organize_files, _get_file_category, _move_file
import os
import shutil


class TestOrganizeFiles(unittest.TestCase):

    def setUp(self):
        """Set up mock folder and files for testing."""
        self.test_folder = "test_folder"
        self.mock_files = ["file1.pdf", "file2.jpg", "file3.mp4", "file4.txt"]
        self.extensions = {
            "Documents": [".pdf", ".docx", ".txt", ".xls", ".xlsx"],
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Videos": [".mp4", ".avi", ".mkv"],
            "Archives": [".zip", ".rar"],
        }

        # Create mock folder and files
        os.makedirs(self.test_folder, exist_ok=True)
        for file_name in self.mock_files:
            open(os.path.join(self.test_folder, file_name), "w").close()

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)

    @patch("organize_files._move_file")
    def test_organize_files_success(self, mock_move_file):
        """Test if files are organized correctly."""
        organize_files(self.test_folder)
        # Check if _move_file was called for each file
        self.assertEqual(mock_move_file.call_count, len(self.mock_files))

    def test_get_file_category(self):
        """Test if file categories are determined correctly."""
        self.assertEqual(_get_file_category(
            "example.pdf", self.extensions), "Documents")
        self.assertEqual(_get_file_category(
            "example.jpg", self.extensions), "Images")
        self.assertEqual(_get_file_category(
            "example.mp4", self.extensions), "Videos")
        self.assertEqual(_get_file_category(
            "example.zip", self.extensions), "Archives")
        self.assertEqual(_get_file_category(
            "example.unknown", self.extensions), "Others")

    @patch("os.makedirs")
    @patch("shutil.move")
    def test_move_file(self, mock_shutil_move, mock_os_makedirs):
        """Test if files are moved to the correct folder."""
        file_path = os.path.join(self.test_folder, "file1.pdf")
        target_folder = os.path.join(self.test_folder, "Documents")
        _move_file(file_path, target_folder, "Documents")

        # Assert the folder was created
        mock_os_makedirs.assert_called_once_with(target_folder, exist_ok=True)
        # Assert the file was moved
        mock_shutil_move.assert_called_once_with(file_path, target_folder)

    def test_organize_files_folder_not_found(self):
        """Test behavior when the folder does not exist."""
        with self.assertRaises(FileNotFoundError):
            organize_files("non_existent_folder")


if __name__ == "__main__":
    unittest.main()
