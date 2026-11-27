import unittest

from sakura_ci_745_workflow import accepted_count


class AcceptedCountTest(unittest.TestCase):
    def test_within_capacity(self):
        self.assertEqual(accepted_count(4, 7), 4)

    def test_request_exceeds_capacity(self):
        self.assertEqual(accepted_count(9, 7), 7)

    def test_no_capacity(self):
        self.assertEqual(accepted_count(8, 0), 0)

    def test_negative_request_is_zero(self):
        self.assertEqual(accepted_count(-2, 7), 0)

    def test_negative_capacity_is_zero(self):
        self.assertEqual(accepted_count(8, -2), 0)


if __name__ == "__main__":
    unittest.main()
