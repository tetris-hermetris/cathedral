from cathedral.graphics.shapes import star
from cathedral.graphics.triangulation import triangulate
from cathedral.engine.render import renderPILimage, output

if __name__ == "__main__": # Code inside this statement will only run if the file is explicitly called and not just imported.
    frame = renderPILimage((star(), star(s=100)), (1000, 1000))
    output((frame,), 'output/', 'star.jpg')

