"""
PointsKeeper - is a variable which keeps points set
Format: list of lists: x, y, where x, y - list with double type
"""
_points_set_ = [([1, 2, 3], [6, 8, 1])]


def clear_points_sets(*args):
    global _points_set_
    _points_set_.clear()


def add_points_set(set_):
    global _points_set_
    _points_set_.append(set_)


def points_set():
    global _points_set_
    return _points_set_
