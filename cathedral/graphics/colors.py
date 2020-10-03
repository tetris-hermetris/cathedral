from random import random

_l_whites = []
_l_yellows = []
_l_reds = []
_l_blues = []

for i in range(500):
    w = 1 - random() / 15
    _l_whites.append((w,w,w))
    _l_reds.append((1,  random() / 4, random() / 4)) 
    _l_yellows.append((1, 1 - random() / 4, random() / 4)) 
    if i % 9 == 0:
        _l_blues.append((0.05 - random() / 30, .04 + random() / 5, .2 + random() / 4)) 
    else:
        _l_blues.append((0.05 - random() / 30, .04 + random() / 30, .2 + random() / 5)) 

colors = {'reds':    tuple(_l_whites),
          'yellows': tuple(_l_yellows),
          'reds':    tuple(_l_reds),
          'blues':   tuple(_l_blues)}

def secondItem(l):
    return l[1]

def pickColor(raw_color_tag, cnt, format=255, quantify=10):
    '''Returns final color value for given raw color tag and current counter'''
    
    qcnt = cnt % quantify
    k = quantify/sum(raw_color_tag.values())

    sorted_colores = list(raw_color_tag.items())
    sorted_colores.sort(key=secondItem)

    n = 0
    for color, amount in sorted_colores:
        if n <= qcnt <= (amount + n) * k:
            picked_color = colors[color][cnt % len(colors[color])]
            if format == 'PIL':
                return (int(value * 255) for value in picked_color)
            elif format == 'drawBot':
                return picked_color
        n += amount

    # if format == 'PIL':
    #     return raw_color_tag.items()[0][1]
    # else:
    #     pass

if __name__ == "__main__":
    print(pickColor({'reds':1, 'blues':.5}, 3))