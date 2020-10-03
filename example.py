from cathedral.graphics.shapes import star
from cathedral.graphics.triangulation import triangulate
from cathedral.engine.render import renderPILimage, output

if __name__ == "__main__":
    frame = renderPILimage(triangulate(star(s=300)), (1000, 1000), q=1.5)
    output((frame,), 'output/', 'star.jpg')