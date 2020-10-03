from random import random

l_whites = []
l_yellows = []
l_reds = []
l_blues = []
l_whites255 = []
l_yellows255 = []
l_reds255 = []
l_blues255 = []

for i in range(500):
    w = 1 - random() / 15
    l_whites.append((w,w,w))
    l_whites255.append((int(w*255),int(w*255),int(w*255)))
    
    l_reds.append((1,  random() / 4, random() / 4)) 
    l_reds255.append((255,  int(random() / 4), int(random() / 4))) 

    l_yellows.append((1, 1 - random() / 4, random() / 4)) 
    l_yellows255.append((255, int(255 - random() * 63.75), int(random() * 64))) 

    if i % 9 == 0:
        l_blues.append((0.05 - random() / 30, .04 + random() / 5, .2 + random() / 4)) 
        l_blues255.append((int(12.75 - random() * 8.5), int(10.2 + random() / 5), int(51 + random() * 63.75))) 
    else:
        l_blues.append((0.05 - random() / 30, .04 + random() / 30, .2 + random() / 5)) 
        l_blues255.append((int(12.75 - random() * 8.5), int(10.2 + random() * 8.5), int(51 + random() * 51))) 

l_whites = tuple(l_whites)
l_yellows = tuple(l_yellows)
l_reds = tuple(l_reds)
l_blues = tuple(l_blues)
l_whites255 = tuple(l_whites255)
l_yellows255 = tuple(l_yellows255)
l_reds255 = tuple(l_reds255)
l_blues255 = tuple(l_blues255)



def whites(n):
    return l_whites[n % len(l_whites)]

def whites255(n):
    return l_whites255[n % len(l_whites255)]

def reds(n):
    return l_reds[n % len(l_reds)]

def reds255(n):
    return l_reds255[n % len(l_reds255)]

def yellows(n):
    return l_yellows[n % len(l_yellows)]

def yellows255(n):
    return l_yellows255[n % len(l_yellows255)]

def blues(n):
    return l_blues[n % len(l_blues)]

def blues255(n):
    return l_blues255[n % len(l_blues255)]


l_colors = [whites, yellows, reds, blues]
l_colors255 = [whites255, yellows255, reds255, blues255]

def colors(color, n):
    return l_colors[color % len(l_colors)](n)

def colors255(color, n):
    return l_colors255[color % len(l_colors255)](n)

def pickColor(raw_color_tag, cnt, format='PIL'):
    if format == 'PIL':
        pass
    else:
        pass
