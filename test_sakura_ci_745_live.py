import unittest

from sakura_ci_745_live import clamp_quantity


class QuantityBoundsTest(unittest.TestCase):
    def test_clamps_negative_quantity_to_zero(self):
        self.assertEqual(clamp_quantity(-3, 8), 0)

    def test_negative_capacity_has_no_room(self):
        self.assertEqual(clamp_quantity(3, -8), 0)

    def test_retains_values_in_range(self):
        self.assertEqual(clamp_quantity(5, 8), 5)

    def test_clamps_to_capacity(self):
        self.assertEqual(clamp_quantity(12, 8), 8)

    def test_zero_capacity_has_no_room(self):
        self.assertEqual(clamp_quantity(3, 0), 0)
