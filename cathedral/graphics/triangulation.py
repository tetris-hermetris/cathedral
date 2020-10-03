from .geometry import *
from statistics import mean

def findTriangles(raw_poly, angle_of_triangulation=179):
    '''Find triangles in raw polygon'''

    points = list(raw_poly)

    angle_points = []
    triangles = []
    l = len(points)

    for i in range(l):

        p0 = raw_poly[i - 1]
        p1 = raw_poly[i]
        p2 = raw_poly[(i + 1) % l]
        
        angle_points.append((angle3(p0, p1, p2), p0, p1, p2))

    angle_points.sort()
    for a in angle_points:
        if a[0] < angle_of_triangulation:
            if a[1] in points and a[3] in points:
                inside = False
                for point in raw_poly:
                    if point not in a:
                        if isInside(a[1], a[2], a[3], point):
                            inside = True
                if not inside:
                    triangles.append((a[2], a[3], a[1]))
                    points.remove(a[2])

    return triangles, tuple(points)


def triangulate(poly, i = 9, angle_of_triangulation=179):
    '''Build triangulation for polygon,
    return them as a sequence of polygons'''
    
    raw_poly, *tags = poly
    triangles, remain_poly = findTriangles(raw_poly, angle_of_triangulation)

    while i > 0 and len(remain_poly) > 3:
        triangles_add, remain_poly = findTriangles(remain_poly, angle_of_triangulation)
        triangles += triangles_add
        i -= 1
    triangles.append(remain_poly)

    poly_sequence = ((tuple(triangle), *tags) for triangle in triangles)

    return poly_sequence


def shrink(poly, distance=4):
    '''Shrinks every point towards its angle bisection.'''

    poly, *tags = poly
    points = []
    l = len(poly)
    for i in range(l):
        p0 = poly[i - 1]
        p1 = poly[i]
        p2 = poly[(i + 1) % l]
        a = angle3(p0, p1, p2)
        if a < 180:
            points.append(moveToPoint(p1, middle(p0, p2), distance, absolute=True))
        elif a > 180:
            points.append(moveToPoint(p1, middle(p0, p2), -distance, absolute=True))
    return (tuple(points), *tags)
