import unittest
import numpy as np
from Code.PointsKeeper.PointsKeeper import clear_points_sets, add_points_set, remove_last_set, points_sets


class PointsKeeperTestCase(unittest.TestCase):
    def test_clear_points_sets(self):
        clear_points_sets()
        points_set = (np.arange(3), np.array([4, 5, 6]))
        ans = [points_set]
        add_points_set(points_set)
        self.assertEqual(ans, points_sets())
        clear_points_sets()
        self.assertEqual([], points_sets())

    def test_add_points(self):
        clear_points_sets()
        points_set = (np.arange(3), np.array([4, 5, 6]))
        ans = [points_set]
        add_points_set(points_set)
        self.assertEqual(ans, points_sets())

    def test_remove_last_set(self):
        clear_points_sets()
        points_set = (np.arange(3), np.array([4, 5, 6]))
        points_set2 = (np.arange(3), np.array([7, 8, 9]))
        ans = [points_set, points_set2]
        add_points_set(points_set)
        add_points_set(points_set2)
        self.assertEqual(ans, points_sets())
        remove_last_set()
        ans.pop()
        self.assertEqual(ans, points_sets())

    def test_points_sets(self):
        self.assertIsInstance(points_sets(), list)
