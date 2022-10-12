s =input("Enter a String :")
firstwordindex = s.find(" ")
firstword = s[:firstwordindex]
lastwordindex = s.rfind(" ") +1
lastword = s[lastwordindex:]
print(lastword,firstword)