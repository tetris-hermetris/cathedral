from cathedral.graphics.shapes import star
from cathedral.graphics.triangulation import triangulate, shrinkSequence
from cathedral.engine.render import renderPILimage, output

if __name__ == "__main__":
    frames = [renderPILimage(shrinkSequence(triangulate(star(s=750, lenght=100 + abs(i)))), (1000, 1000), q=1.5) for i in range(-100, 100, 5)]
    output(frames, 'output/', 'star.gif')