"""
PointsKeeper - is a variable which keeps points set
Format: list of lists: x, y, where x, y - list with double type
"""
_points_set_ = [[1, 2, 3], [4, 0, 6]]


def clear_points_sets(*args):
    global _points_set_
    _points_set_[0].clear()
    _points_set_[1].clear()


def add_points_set(set_):
    global _points_set_
    _points_set_[0] += set_[0]
    _points_set_[1] += set_[1]


def points_set():
    global _points_set_
    return _points_set_
