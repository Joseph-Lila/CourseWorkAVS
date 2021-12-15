_points_set_ = [[], []]


def change_set(x, y):
    global _points_set_
    _points_set_ = [x, y]


def points_set():
    global _points_set_
    return _points_set_
