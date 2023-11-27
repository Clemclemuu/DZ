#############
# задание 1 #
#############

# écrire une boucle qui dessine des formes verticales (carrés ou autres du lien ci-dessus)

from drawbot_skia.drawbot import polygon, saveImage, fill

y = 100

step = 75


for i in range(100):
    a = polygon((100, y), (175, 300+y), (300, 300+y), (250, 192+y), (200, 170+y), close=True)
    y += step


saveImage('dessin1.pdf')









##########################
# задание дополнительное #
# творческое, свободное  #
##########################
