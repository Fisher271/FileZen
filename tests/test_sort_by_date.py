import unittest
from unittest.mock import patch
from sort_by_date import sort_by_year_and_month
import os
import shutil
from datetime import datetime
import logging

# Configure logging for tests
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class TestSortByDate(unittest.TestCase):

    def setUp(self):
        """Set up mock folder and files for testing."""
        self.test_folder = "test_folder"
        self.mock_files = ["file1.txt", "file2.jpg", "file3.mp4"]

        # Dates specifically chosen to ensure different months
        self.mod_times = [
            datetime(2025, 1, 15),  # January
            datetime(2025, 2, 15),  # February
            datetime(2025, 3, 15)   # March
        ]

        # Create mock folder and files
        os.makedirs(self.test_folder, exist_ok=True)
        for i, file_name in enumerate(self.mock_files):
            file_path = os.path.join(self.test_folder, file_name)
            open(file_path, "w").close()
            # Set specific modification times
            mod_time = self.mod_times[i]
            os.utime(file_path, (mod_time.timestamp(), mod_time.timestamp()))
        logging.info(f"Test setup completed. Created files: {self.mock_files}")

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.test_folder):
            shutil.rmtree(self.test_folder)
        logging.info(
            f"Test cleanup completed. Removed folder: {self.test_folder}")

    @patch("os.makedirs")
    @patch("shutil.move")
    def test_sort_by_year_and_month_success(self, mock_shutil_move, mock_os_makedirs):
        """Test if files are sorted by year and month successfully."""
        sort_by_year_and_month(self.test_folder)

        for i, file_name in enumerate(self.mock_files):
            mod_time = self.mod_times[i]
            year = mod_time.strftime('%Y')
            # Matches updated function format
            month = mod_time.strftime('%m-%B')
            target_folder = os.path.join(self.test_folder, year, month)

            # Check makedirs call
            logging.debug(f"Expected makedirs call for: {target_folder}")
            try:
                mock_os_makedirs.assert_any_call(target_folder, exist_ok=True)
            except AssertionError:
                logging.error(f"makedirs not called for: {target_folder}")
                # For debugging
                print("Actual calls:", mock_os_makedirs.call_args_list)
                raise

            # Check file move
            file_path = os.path.join(self.test_folder, file_name)
            logging.debug(
                f"Expected file move: {file_path} -> {target_folder}")
            mock_shutil_move.assert_any_call(
                file_path, os.path.join(target_folder, file_name))

        # Verify calls count
        self.assertEqual(mock_os_makedirs.call_count, len(self.mod_times),
                         "makedirs was not called expected number of times.")
        self.assertEqual(mock_shutil_move.call_count, len(self.mock_files),
                         "Files were not moved expected number of times.")

    @patch("shutil.move")
    def test_non_file_items_skipped(self, mock_shutil_move):
        """Test that non-file items are skipped."""
        os.makedirs(os.path.join(self.test_folder, "subfolder"), exist_ok=True)
        sort_by_year_and_month(self.test_folder)
        logging.info("Testing skipped non-file items.")

        # Ensure only files were moved
        self.assertEqual(mock_shutil_move.call_count, len(self.mock_files),
                         "Non-file items were not skipped correctly.")
        logging.debug("Non-file items test passed successfully.")


if __name__ == "__main__":
    unittest.main()
