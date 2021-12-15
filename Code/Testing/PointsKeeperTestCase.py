import unittest
from Code.PointsKeeper.PointsKeeper import clear_points_sets, add_points_set, points_set


class PointsKeeperTestCase(unittest.TestCase):
    def test_clear_points_sets(self):
        clear_points_sets()
        points_set_ = [[*range(3)], [4, 5, 6]]
        add_points_set(points_set_)
        self.assertEqual(points_set_, points_set())
        clear_points_sets()
        self.assertEqual([[[], []]], points_set())

    def test_add_points(self):
        clear_points_sets()
        points_set_ = [[*range(3)], [4, 5, 6]]
        add_points_set(points_set_)
        self.assertEqual(points_set_, points_set())

    def test_points_sets(self):
        self.assertIsInstance(points_set(), list)
