def main():

    import sys
#this is a code that will calculate the cost of a car rental for a customer based on several factors

# this is what information the user must enter

    customerName = input("please enter your first and last name ")

    ageOfCustomer = int(input("please enter your age "))

    rentalCode, budget, daily, weekly = classCodeCheck()


    numberOfDaysRented = int(input("please enter the number of days you rented the car for "))

    odometerBefore = int(input("please enter the number of km's the odometer displayed at the START\n of your rental period"))

    odometerAfter= int(input("please enter the number of km's the odometer displayed at the END of your rental\n period "))

    totalKmDriven = odometerAfter - odometerBefore

    numberOfWeeks = numOfWeeksRented(numberOfDaysRented)

    cost = totalCostOfRental(rentalCode, ageOfCustomer,budget, daily, weekly, numberOfDaysRented, totalKmDriven, numberOfWeeks)

    print ("Name ", customerName, "\nAge",  ageOfCustomer, "\nClass code ", rentalCode, "\nNumber of days car rented for ", numberOfDaysRented, "\nOdometer reading before rental period ", odometerBefore, "\nOdometer reading after rental period ", odometerAfter, "\ntotal km driven", totalKmDriven)
    print ("the total cost of your car rental was %.2f" % cost)


#this function asks a user to enter the classification code for their rental period
#it will continue to ask until a valid code has been entered

def classCodeCheck():


    budget = "B"
    weekly = "W"
    daily = "D"

    classCode = ()
    classCode = ()
    valid = False
    while not valid:
        classCode = input("please enter the classification code (i.e. B for Budget, D for Daily, or W for Weekly")
        if classCode.upper() == budget or classCode.upper() == daily or classCode.upper() == weekly:
            valid = True
        else:
            print("the class code is ", classCode.upper())

    rentalCode = classCode.upper()

    return rentalCode, budget, daily, weekly


def numOfWeeksRented(numberOfDaysRented):
    # this code figures out the total number of weeks which is need for class W rentals

    numberOfWeeks = 0

    if numberOfDaysRented % 7 > 0:
        numberOfWeeks = numberOfDaysRented//7 + 1
    else:
        numberOfWeeks = numberOfDaysRented/7


    return numberOfWeeks

def totalCostOfRental(rentalCode, ageOfCustomer,budget, daily, weekly, numberOfDaysRented, totalKmDriven, numberOfWeeks):

    #this part will calculate the cost based on the given information by the customer

    # this part of the code is simply the cost values assocaited with each code
    codeB = 20.00
    codeD = 50.00
    codeW = 200.00
    dailyKmDriven = 0.30
    cost = 0.00

    if rentalCode == budget and ageOfCustomer < 25:
        cost = (codeB * numberOfDaysRented) + (dailyKmDriven * totalKmDriven) + (numberOfDaysRented*10)

    elif rentalCode == budget and ageOfCustomer >= 25:
        cost = (codeB * numberOfDaysRented) + (dailyKmDriven * totalKmDriven)

    elif rentalCode == daily and ageOfCustomer < 25 and totalKmDriven > 100:
        cost = (codeD * numberOfDaysRented) + ((totalKmDriven - 100) *dailyKmDriven) + (numberOfDaysRented * 10)

    elif rentalCode == daily and ageOfCustomer < 25 and totalKmDriven < 100:
        cost = (codeD * numberOfDaysRented) + (numberOfDaysRented * 10)

    elif rentalCode == daily and ageOfCustomer >= 25 and totalKmDriven > 100:
        cost = (codeD * numberOfDaysRented) + (dailyKmDriven*(totalKmDriven - 100))

    elif rentalCode == daily and ageOfCustomer >= 25 and totalKmDriven <= 100:
        cost = codeD * numberOfDaysRented

    elif rentalCode  == weekly and ageOfCustomer < 25 and totalKmDriven <= 1000:
        cost = (codeW * numberOfWeeks) + (numberOfDaysRented * 10)

    elif rentalCode == weekly and ageOfCustomer < 25 and totalKmDriven <= 2000:
        cost = (codeW * numberOfWeeks) + (numberOfWeeks * 50) + (numberOfDaysRented * 10)

    elif rentalCode == weekly and ageOfCustomer < 25 and totalKmDriven > 2000:
        cost = (codeW * numberOfWeeks) + (dailyKmDriven*(totalKmDriven - 2000))+ (numberOfWeeks * 100)
        cost = cost + (numberOfDaysRented * 10)

    elif rentalCode  == weekly and ageOfCustomer >= 25 and totalKmDriven <= 1000:
        cost = (codeW * numberOfWeeks)

    elif rentalCode == weekly and ageOfCustomer >= 25 and totalKmDriven <= 2000:
        cost = (codeW * numberOfWeeks) + (numberOfWeeks * 50)

    elif rentalCode == weekly and ageOfCustomer >= 25 and totalKmDriven > 2000:
        cost = (codeW * numberOfWeeks) + (dailyKmDriven*(totalKmDriven - 2000))+ (numberOfWeeks * 100)

    else:
        print("Sorry, we were unable to calculate the cost of your rental. \n Please try again.")

    return cost

main()
