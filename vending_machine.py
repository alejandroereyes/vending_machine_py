#Alejandro_Reyes_InClassExercise6
#Alejandro Reyes
#3/9/15
#This program will emulate a vendng machine
#It will provide the user with a menu from which to make a selection


def main():

    # Initializing variables
    selection = ""
    cost = 0.0
    payment = 0.0
    change = 0.0

    menu ()

    # User will make a selection
    userChoice = input("Enter your selection: ")
    print()

    # This will prompt the user to re enter it entry is invalid
    while not determineChoice (userChoice):
        print ("Invalid Entry, wrong code or multiple codes entered!")
        userChoice = input("Please re-enter ONE item: ")

    # Cost & user selection values will be returned from the function
    cost, selection = determineChoice(userChoice)

    # Payment from the user will be entered
    print ()
    print ("You selected ", selection, ".", sep = "")
    print ("Total due: $", format(cost, '.2f'), ".", sep = "")
    payment = float(input("Please enter payment, only $1 bills accepted :"))
    print ()

    # Will prompt user to re enter payment if input is too high or low
    while not calcChange (payment, cost):
        print ("Invalid Entry, Do Not Enter More Than $4, no less than $1!")
        payment = float(input("Please re-enter payment: "))

    # Change for the user will be returned from the function
    change = calcChange (payment, cost)

    # End message will print if payment entered is valid
    if calcChange (payment, cost):
        endmes (change, selection)

#This func will print out the menu
def menu ():
    print ("Please select the code for the item you wish. (One item only Please)\n")
    print("-----------------MENU------------------")
    print ("Snickers\tM&Ms\t\tKitKat")
    print ("$0.28\t\t$1.39\t\t$1.39")
    print ("A1\t\tA2\t\tA3")
    print ()
    print ("Lays\t\tDoritos\t\tCheetos")
    print ("$0.50\t\t$0.50\t\t$1.49")
    print ("B1\t\tB2\t\tB3")
    print ()
    print ("TicTac\t\tStarburst\tSkittles")
    print ("$1.04\t\t$0.79\t\t$2.49")
    print ("C1\t\tC2\t\tC3")
    print ()

#This will determine the user's choice and reutrn cost and item info
def determineChoice (userChoice):

    if userChoice == "A1" or userChoice == "a1":
        cost = 0.89
        item = "Snickers"
        return cost, item
    elif userChoice == "A2" or userChoice == "a2":
        cost = 1.39
        item = "M&Ms"
        return cost, item
    elif userChoice  == "A3" or userChoice == "a3":
        cost = 1.39
        item = "KitKat"
        return cost, item
    elif userChoice == "B1" or userChoice == "b1":
        cost = 0.50
        item = "Lays"
        return cost, item
    elif userChoice == "B2" or userChoice == "b2":
        cost = 0.50
        item = "Doritos"
        return cost, item
    elif userChoice == "B3" or userChoice == "b3":
        cost = 1.49
        item = "Cheetos"
        return cost, item
    elif userChoice == "C1" or userChoice == "c1":
        cost = 1.04
        item = "TicTac"
        return cost, item
    elif userChoice == "C2" or userChoice == "c2":
        cost = 0.79
        item = "Starbust"
        return cost, item
    elif userChoice == "C3" or userChoice == "c3":
        cost = 2.49
        item = "Skittles"
        return cost, item

#This will validate user input and
#calculate the amount of change and return change due to user
def calcChange (payment, cost):

    if payment >= 1 and payment <= 4:
        change = payment - cost
        return change

# End message
def endmes (change, selection):
    print ()
    print ("Thank you! Your change is $", format(change, '.2f'), sep = "")
    print ("Enjoy your", selection, "!")

main()
