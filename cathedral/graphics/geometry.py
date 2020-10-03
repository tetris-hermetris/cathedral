from math import sin, cos, atan2, hypot, sqrt, radians
from statistics import mean


def angle(p1, p2, units='rad'):
    '''takes two points as (x, y) and optional units as 'rad' or 'deg'
    
    returns angle between points to x axis

    >>> a = angle((0, 50), (40, 90), 'deg')
    >>> a
    45.00
    '''

    deltaX = p2[0] - p1[0]
    deltaY = p2[1] - p1[1]
    rad = atan2(deltaY, deltaX)
    if units == 'rad':
        return rad
    elif units == 'deg':
        return rad * (180/pi)


def move(point, angle, distance, units='rad'):
    '''takes point as (x, y), angle in radians and distance
    
    returns new point, default units is radians'''
    if units == 'deg':
        angle = radians(angle)
    newX = point[0] + cos(angle) * distance
    newY = point[1] + sin(angle) * distance
    return newX, newY


def rotate(point, pivot, angle, units='rad'):

    if units == 'deg':
        angle = radians(angle)

    s = sin(angle)
    c = cos(angle)
    x, y = point
    xpv, ypv = pivot

    x -= xpv
    y -= ypv

    return (x * c - y * s) + xpv, x * s + y * c) + ypv


def moveToPoint(p1, p2, distance, absolute=False):
    if absolute:
        return move(p1, angle(p1, p2), distance)
    else:
        distance /= 100
        x1, y1 = p1
        x2, y2 = p2
        return x1 + (x2 - x1) * distance, y1 + (y2 - y1) * distance


def populatePoints(poly):
    poly, *tags = poly
    new_points = []
    for i in range(len(poly)):
        new_points += [middle(poly[i-1], poly[i]), poly[i]]
    return tuple(new_points), *tags


def middle(p1, p2):
    ''''''
    return p1[0] + (p2[0] - p1[0]) / 2, p1[1] + (p2[1] - p1[1]) / 2


def dist(P, P2):
    '''distance between 2 points, given as (x, y)'''
    dX, dY = P2[0] - P[0], P2[1] - P[1]
    return hypot(dX, dY)


def perimeter(poly):
    poly, *tags = poly
    perimeter = 0
    for i in len(poly):
        perimeter += dist(poly[i-1], poly[i])

    return perimeter


def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def isInside(p0, p1, p2, point):
    '''True or False if point is inside triangle'''

    d1 = sign(point, p0, p1)
    d2 = sign(point, p1, p2)
    d3 = sign(point, p2, p0)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


def isInsidePoly(poly, point):
    '''True or False if point is inside polygon'''
    poly, *tags = poly
    if sum(isInside(poly[n], poly[n-1], poly[n-2], point) for n in range(len(poly))):
        return True
    else:
        return False


def intersect(p1, p2, p3, p4):
    '''Intersection point of two lines p1-p2 and p3-p4'''

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    d = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)

    if d:
        uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / d
        uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / d
    else:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = x1 + uA * (x2 - x1)
    y = y1 + uA * (y2 - y1)

    return x, y


def angle_point(x, y):

    # angle of vector ((0, 0), (x, y))
    if y == 0:
        y += .000001
    if y >= 0:
        if x >= 0:
            return y / (x + y)
        else:
            return 1 - x / (-x + y)
    else:
        if x < 0:
            return 2 - y / (-x - y)
        else:
            return 3 + x / (x - y)


def angle3(p0, p1, p2):
    '''angle between two lines p0-p1 and p1-p2'''

    xa = p0[0] - p1[0]
    ya = p0[1] - p1[1]
    xb = p2[0] - p1[0]
    yb = p2[1] - p1[1]

    a = ((angle_point(xb, yb) - angle_point(xa, ya)) * 90)
    if a > 0:
        return a
    else:
        return 360 + a


def tr_center(p1, p2, p3):
    '''arithmetic mean between 3 points'''
    return (mean((p1[0], p2[0], p3[0])), mean((p1[1], p2[1], p3[1])))


def cut(f1, f2):
    f1, *tags = f1
    f2, *_ = f2
    connection = (dist(f1[0], f2[0]), (f1[0], f2[0]))
    for p1 in f1:
        for p2 in f2:
            d = dist(p1, p2)
            if d < connection[0]:
                connection = (d, (p1, p2))
    p1, p2 = connection[1]

    fn1 = f1[:f1.index(p1)+1]
    fn2 = reversed(f2[:f2.index(p2)+1])
    fn3 = list(reversed(f2[f2.index(p2):]))
    fn4 = list(f1[f1.index(p1):])

    fn3[-1] = (fn3[-1][0], fn3[-1][1]+.001)
    fn4[0] = (fn4[0][0], fn4[0][1]+.001)

    new_figure = tuple(fn1) + tuple(fn2) + tuple(fn3) + tuple(fn4)
    return (new_figure, *tags)


def samePointsCount(raw_poly1, raw_poly2):
    '''Make equal points count for two raw_poly
    
    Simply adds missing points to a smaller one,
    return sequence of raw polygons'''
    if len(raw_poly1) != len(raw_poly2):
        n = len(raw_poly1) - len(raw_poly2)
        if n > 0:
            for i in range(n):
                raw_poly2 = *raw_poly2, raw_poly2[-1]
        if n < 0:
            for i in range(-n):
                raw_poly1 = *raw_poly1, raw_poly1[-1]
    return raw_poly1, raw_poly2


def interpolate(poly1, poly2, phase):
    '''Interpolate two polygons from 0 to 100'''
    
    phase = abs((phase % 100 - 50) * 2)
    raw_poly1, *tags = poly1
    raw_poly2, *tags = poly2
    raw_poly1, raw_poly2 = samePointsCount(raw_poly1, raw_poly2)
    new_raw_poly = [moveToPoint(raw_poly1[i], raw_poly2[i], phase)
                    for i in range(len(raw_poly1))]

    return new_raw_poly, *tags
