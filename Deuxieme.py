#############
# задание 2 #
#############

# écrivez une boucle imbriquée (double) qui remplit complètement le canevas de formes, verticalement et horizontalement

from drawbot_skia.drawbot import polygon, saveImage, fill

y = 100
step = 75




for i in range(10):
    x = 100
    y = y + step
    for j in range(10):
        polygon((x, y), (175+x, 300+y), (300+x, 300+y), (250+x, 192+y), (200+x, 170+y), close=True)
        x = x + step



saveImage('dessin2.pdf')
