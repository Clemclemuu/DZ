from drawbot_skia.drawbot import rect, oval, saveImage, width, height, newPage

 

a = [1, 0, 1, 0, 0, 0, 1] * 7

 

newPage(742.5, 1050)

 

x = 0

y = height()

step = width() / 6

 

for element in a:

    if element:

        rect(x, y - step, step, step)

    else:

        oval(x, y - step, step, step)

    x += step

    if x >= width():

        x = 0

        y -= step

 

saveImage("output-03.pdf")