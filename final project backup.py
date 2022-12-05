class Sketch():
	def __init__(self, size):
        self.size = 0
        self.xpos= 0 
        self.ypos = 0
        self.direction = "U"
        self.pen = "U"
        self.canvas = []
#		for i in range(self.size):
#			self.canvas.append([' '] * self.size)
#		return
	def printsketch(self):
		print("+" + ("-" * self.size) + "+")
		for i in range(self.size -1, -1, -1):
			print("|", sep="", end="")
			for j in range(self.size):
				print(self.canvas[i][j], sep="", end="")
			print("|")
		print("+" + ("-" * self.size) + "+")
		print("X =", self.xpos, "Y =", self.ypos, "Direction=", self.direction)
		return

	def penup(self):
    	self.pen = "U"
		return
	
	def pendown(self):
		self.pen = "D"
		return

	def turnleft(self):
		if self.direction == "U":
			self.direction = "L"
			return
		if self.direction == "L":
			self.direction = "D"
			return
		if self.direction == "D":
			self.direction = "R"
			return
		if self.direction == "R":
			self.direction = "U"
			return
		return

	def turnright(self):
		if self.direction == "U":
			self.direction = "R"
			return
		if self.direction == "R":
			self.direction = "D"
			return
		if self.direction == "D":
			self.direction = "L"
			return
		if self.direction == "L":
			self.direction = "U"
			return
		return

	def move(self, distance):
    if self.direction == "U"
	newxpos = self.xpos + distance
	if newxpos >= self.size:
		newxpos = self.size -1
	if self.pen == "D":
		for i in range(self.xpos, newxpos):
			self.canvas[i][self.ypos] = "*"
	self.xpos = newxpos

	if self.direction == "R"
	newypos = self.ypos + distance
	if newypos >= self.size:
		newypos = self.size -1
	if self.pen == "D":
		for i in range(self.ypos, newypos + 1):
			self.canvas[self.xpos][i] = "*"
	self.ypos = newypos

	if self.direction == "D"
	newxpos = self.xpos - distance
	if newxpos < 0:
		newxpos = 0
	if self.pen == "D":
		for i in range(self.xpos, newxpos -1, -1):
			self.canvas[i][self.ypos] = "*"
	self.xpos = newxpos
	
	if self.direction == "L"
	newypos = self.ypos - distance
	if newypos < 0:
		newypos = 0
	if self.pen == "D":
		for i in range(self.ypos, newypos -1, -1):
			self.canvas[self.xpos][i] = "*"
	self.ypos = newypos
	
inputfile = open("Cshape.txt")
commandtext = inputfile.readline()
mysketch = Sketch(int(commandtext))
commandtext = intputfile.readline()
while commandtext != "":
	commandtextvalues = command.split(",")
	command = commandtextvalues[0].strip()
	if command == "1":
		mysketch.penup()
	if command == "2":
		mysketch.pendown()
	if command == "3":
		mysketch.turnright()
	if command == "4":
		mysketch.turnleft()
	if command == "5":
		mysketch.move(int(commandtextvalues[1]))
	if command == "6":
		mysketch = printsketch()
	commandtext = inputfile.readline()
inputfile.close()