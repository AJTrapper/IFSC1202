class Canvas():

    def __init__(self, size, xpos, ypos, direction, pen, canvas):
        self.size = 20
        self.xpos= 0 
        self.ypos = 0
        self.direction = "U"
        self.pen = "U"
        self.canvas = [0,0]

    def printsketch(self):

CanvasList = []
CanvasRead = open("Cshape.txt")
x = CanvasRead.readline()
while x != "":
    y = x.split(",")
    canvas = Canvas()
    CanvasList.append(canvas)
    x = CanvasRead.readline()
    CanvasRead.close()
    print(xpos, ypos, direction)
    
def penup():
    content 

def pendown():
    content 

def turnleft():
    content

def turnright():
    content

def move():
    content

