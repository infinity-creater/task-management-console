import unittest
import os
import tempfile
import json

import task_manager
import storage


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Create a temporary JSON file for each test."""

        self.temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".json"
        )

        self.temp_file.close()

        # Save the original storage file name
        self.original_file_name = storage.FILE_NAME

        # Use temporary file for testing
        storage.FILE_NAME = self.temp_file.name

        with open(
            self.temp_file.name,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump([], file)

        self.manager = task_manager.TaskManager()

    def tearDown(self):
        """Remove temporary file after each test."""

        # Restore original file name
        storage.FILE_NAME = self.original_file_name

        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_add_valid_task(self):
        task = self.manager.add_task(
            "Study Python",
            "Practice Python functions",
            "High",
            "2026-12-20"
        )

        self.assertEqual(task["id"], "T001")
        self.assertEqual(task["status"], "Pending")

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task(
                "",
                "Description",
                "High",
                "2026-12-20"
            )

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            self.manager.add_task(
                "Study",
                "Python study",
                "Urgent",
                "2026-12-20"
            )

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            self.manager.add_task(
                "Study",
                "Python study",
                "High",
                "20/12/2026"
            )

    def test_search_task(self):
        self.manager.add_task(
            "Learn Python",
            "Study functions and classes",
            "Medium",
            "2026-12-20"
        )

        results = self.manager.search_tasks("Python")

        self.assertEqual(len(results), 1)
        self.assertEqual(
            results[0]["title"],
            "Learn Python"
        )

    def test_complete_task(self):
        task = self.manager.add_task(
            "Complete Assignment",
            "Submit project",
            "High",
            "2026-12-20"
        )

        result = self.manager.complete_task(task["id"])

        self.assertTrue(result)

        self.assertEqual(
            self.manager.find_task(task["id"])["status"],
            "Completed"
        )

    def test_delete_task(self):
        task = self.manager.add_task(
            "Delete Me",
            "Testing delete",
            "Low",
            "2026-12-20"
        )

        result = self.manager.delete_task(task["id"])

        self.assertTrue(result)

        self.assertIsNone(
            self.manager.find_task(task["id"])
        )

    def test_filter_by_priority(self):
        self.manager.add_task(
            "High Task",
            "Important",
            "High",
            "2026-12-20"
        )

        self.manager.add_task(
            "Low Task",
            "Normal",
            "Low",
            "2026-12-20"
        )

        results = self.manager.filter_by_priority("High")

        self.assertEqual(len(results), 1)

        self.assertEqual(
            results[0]["priority"],
            "High"
        )


if __name__ == "__main__":
    unittest.main()