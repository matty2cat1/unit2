#Matt Westelman
#graphics.py
#2/2/18

from ggame import *
red = Color(0xff0000, 1)
line = LineStyle(3,red)
rectangle = RectangleAsset(100,100,line,red)

Sprite(rectangle)
myApp = App()
myApp.run()
