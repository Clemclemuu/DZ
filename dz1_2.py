#############
# задание 2 #
#############

# écrivez une boucle imbriquée (double) qui remplit complètement le canevas de formes, verticalement et horizontalement

from drawbot_skia.drawbot import polygon, saveImage, fill

y = 0
step = 150

for i in range(6):
    x = 0
    y = y + step
    for j in range(6):
        polygon((x, y-100), (175+x, 300+y), (300+x, 300+y), (250+x, 192+y), (200+x, 170+y), close=True)
        x = x + step

saveImage('dessin2.pdf')
