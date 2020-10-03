from PIL import Image, ImageDraw, ImageOps
from ..graphics.colors import pickColor

def renderPILimage(poly_sequence, output_size, q=1.5, background=(0,0,0), img=None, outline=(0,0,0)):
    '''Render sequence of polygons on PIL image object.
    
    If no given PIL image object, creates a new one'''

    if img == None:
        w, h = int(output_size[0]*q), int(output_size[1]*q)
        img = Image.new('RGB', (w, h), background)
    draw = ImageDraw.Draw(img)

    for cnt, poly in enumerate(poly_sequence):
        raw_poly = poly[0]
        color = tuple(pickColor(poly[-1], cnt, format='PIL'))
        scaled_poly = ((x*q, y*q) for (x, y) in raw_poly)
        draw.polygon(tuple(scaled_poly), fill=color, outline=outline)
    img = ImageOps.flip(img)
    img = img.resize(output_size, resample=Image.BILINEAR)

    return img

def output(frames, path, name, quality=100):
    if name[-3:] == 'jpg':
        name = name[:-4]  
        for cnt, frame in enumerate(frames):
            frame.save(f'{path}{name}_{cnt:0>7}.jpg', quality=quality)
            
    if name[-3:] == 'gif':
        name = name[:-4]  
        frames[0].save(f'{path}{name}.gif', append_images=[frame for frame in frames[1:]], save_all=True, loop=0)