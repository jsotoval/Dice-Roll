#Dice roll
#A dice is rolled from user input, the number the dice lands is placed within a list then counted. Then the list is printed out with the number of times the dice landed on each land 1 - 6.
import random
def dice_roll():
    number_of_rolls_by_input = input("Please enter the number of rolls you would like: ")
    number_the_dice_landed = 0
    list_of_rolls = []
    while int(number_of_rolls_by_input) > 1:
        number_the_dice_landed = random.randint(1, 6)
        if(number_the_dice_landed == 1):
            list_of_rolls.append("1")
        elif(number_the_dice_landed == 2):
            list_of_rolls.append("2")
        elif(number_the_dice_landed == 3):
            list_of_rolls.append("3")
        elif(number_the_dice_landed == 4):
            list_of_rolls.append("4")
        elif(number_the_dice_landed == 5):
            list_of_rolls.append("5")
        else:
            list_of_rolls.append("6")
        number_of_rolls_by_input = int(number_of_rolls_by_input) - 1
    print("The list that dice landed on within 25 rolls are: ", list_of_rolls)
    print("The number of times the dice landed on 1 within 25 rolls was ", list_of_rolls.count("1"))
    print("The number of times the dice landed on 2 within 25 rolls was ", list_of_rolls.count("2"))
    print("The number of times the dice landed on 3 within 25 rolls was ", list_of_rolls.count("3"))
    print("The number of times the dice landed on 4 within 25 rolls was ", list_of_rolls.count("4"))
    print("The number of times the dice landed on 5 within 25 rolls was ", list_of_rolls.count("5"))
    print("The number of times the dice landed on 6 within 25 rolls was ", list_of_rolls.count("6"))
