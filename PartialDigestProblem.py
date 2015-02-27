__author__ = 'Sergey'

# X = [0,2,4,7,10]
DX = [2, 2, 3, 3, 4, 5, 6, 7, 8, 10]
global width, x, y, z, delta, gamma


def PartialDigestProblem(_dx):
    x = []
    width = max(_dx)
    _dx.remove(width)
    x.append(0)
    x.append(width)
    Place(_dx, x, width)


def Place(_dx, _x, _width):
    if len(_dx) == 0:
        print _x
        return

    y = max(_dx)
    z = _width - y

    delta = sorted(distance(y, _x))
    gamma = sorted(distance(z, _x))

    if delta in _dx:
        _x.append(y)
        _dx.remove(delta)
        Place(_dx, _x, _width)
        _x.remove(y)
        _dx.append(delta)

    if z in _dx:
        _x.append(z)
        _dx.remove(gamma)
        Place(_dx, _x, _width)
        _x.remove(z)
        _dx.append(gamma)

    return


def distance(_val, _list):
    d = []
    for i in _list:
        d.append(abs(i - _val))
    return d


PartialDigestProblem(DX)