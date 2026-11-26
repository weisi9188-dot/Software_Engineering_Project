import unittest

from prototype.cochange import calculate_cochanges, related_to


class TestCoChange(unittest.TestCase):
    def test_directional_association(self):
        commits = [
            {"sha": "c1", "files": ["A.py", "B.py"]},
            {"sha": "c2", "files": ["A.py", "B.py"]},
            {"sha": "c3", "files": ["A.py"]},
            {"sha": "c4", "files": ["A.py", "C.py"]},
        ]
        result = calculate_cochanges(commits, min_support=2)
        a_to_b = related_to(result, "A.py")
        b_to_a = related_to(result, "B.py")
        self.assertEqual(len(a_to_b), 1)
        self.assertEqual(a_to_b[0]["target"], "B.py")
        self.assertEqual(a_to_b[0]["score"], 0.5)
        self.assertEqual(b_to_a[0]["score"], 1.0)
        self.assertEqual(a_to_b[0]["commits"], ["c1", "c2"])

    def test_duplicate_filename_not_counted_twice(self):
        commits = [
            {"sha": "c1", "files": ["A.py", "A.py", "B.py"]},
            {"sha": "c2", "files": ["A.py", "B.py"]},
        ]
        result = calculate_cochanges(commits, min_support=2)
        self.assertEqual(result["file_counts"]["A.py"], 2)
        self.assertEqual(related_to(result, "A.py")[0]["support"], 2)

    def test_large_commit_filtered(self):
        commits = [
            {"sha": "format", "files": ["A.py", "B.py", "C.py", "D.py"]},
            {"sha": "c1", "files": ["A.py", "B.py"]},
            {"sha": "c2", "files": ["A.py", "B.py"]},
        ]
        result = calculate_cochanges(commits, max_files_per_commit=3, min_support=2)
        self.assertEqual(result["accepted_commits"], 2)
        self.assertEqual(result["skipped_large_commits"], 1)
        self.assertEqual(result["file_counts"]["C.py"] if "C.py" in result["file_counts"] else 0, 0)

    def test_minimum_support_threshold(self):
        result = calculate_cochanges(
            [{"sha": "c1", "files": ["A.py", "B.py"]}], min_support=2
        )
        self.assertEqual(related_to(result, "A.py"), [])

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            calculate_cochanges([], min_support=0)


if __name__ == "__main__":
    unittest.main()
