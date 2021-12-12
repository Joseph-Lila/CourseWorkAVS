"""
PointsKeeper - is a variable which keeps points sets
Format: list of tuples(x, y), where x, y - np.arrays
"""
_points_sets_ = []


def clear_points_sets():
    global _points_sets_
    _points_sets_.clear()


def add_points_set(set_):
    global _points_sets_
    _points_sets_.append(set_)


def remove_last_set():
    global _points_sets_
    if len(_points_sets_) != 0:
        _points_sets_.pop()


def points_sets():
    global _points_sets_
    return _points_sets_
