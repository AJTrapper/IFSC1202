print("Winners and Losers - Human is Even, Computer is Odd")
h = ("HumanScore")
hresult = 0
cresult = 0
c = ("ComputerScore")


for i in range (1,6):
    print ("Round : {}". format (i))
    x = int(input("Enter Your Guess :"))
    from random import randint
    y = randint(1,6)
    print ("Human Guess: {} - Computer Guess: {}". format (x,y))

    if (x+y)%2 == 0:
        print("Sum is Even")
        hresult = hresult + 1

    elif (x+y)%2 != 0:
        print("Sum is odd")
        cresult = cresult + 1

    else:
        print()
    print ("Human Score: {} - Computer Score: {}". format (hresult,cresult))


if hresult>cresult:
    print("Human Wins")
else :
    print("Computer Wins")