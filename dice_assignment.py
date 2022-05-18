import datetime as datetime
import random as random


class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.num_of_rolls = 0

    def roll(self, num_of_rolls):
        roll_results = [str(random.randrange(1, self.sides + 1)) for _ in range(num_of_rolls)]
        roll_results = ", ".join(roll_results)
        return roll_results


def is_positive_int(user_input):
    while True:
        try:
            return int(user_input) >= 1
        except ValueError:
            return False


def create_file():
    file_time = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
    file_name = f"dice_rolled_on_{file_time}.txt"
    return file_name


def choose_dice():
    while True:
        dice_sides = input("Please enter a number for your dice sides or 'q' to quit: ")
        if dice_sides == 'q':
            break
        else:
            if is_positive_int(dice_sides):
                return int(dice_sides)
            else:
                print("Invalid input, please provide a valid input.")
                continue


def roll_dice(chosen_dice):
    while True:
        dice_rolls = input("Please enter the number of times you want to roll your dice or 'q' to quit: ")
        if dice_rolls == 'q':
            break
        else:
            if is_positive_int(dice_rolls):
                dice_rolls = int(dice_rolls)
                roll = chosen_dice.roll(dice_rolls)
                roll_time = datetime.datetime.now().strftime("%d/%m/%Y at %H:%M:%S")
                textfile.write(f'You rolled {dice_rolls} dice: {roll}' + " on " + roll_time + '\n')
                print(f'You rolled {dice_rolls} dice: {roll}.')
                continue
            else:
                print("Invalid input, please provide a valid input.")
                continue


def print_rolls_file(file):
    # We must return the cursor to the beginning of the file in order to be able to read its contents,
    # since the file is open during the entire time the program runs, otherwise we get empty print message.
    file.seek(0)
    results = file.readlines()
    for line in results:
        print(line)


def menu():
    global dice
    while True:
        print('Please select your choice:\n'
              'n) Choose new dice\n'
              't) Throw your dice\n'
              'p) Print your results so far\n'
              'q) Quit the program')
        user_choice = input()
        if user_choice == 'n':
            new_dice_sides = choose_dice()
            dice = Dice(new_dice_sides)
            print(f'You chose {new_dice_sides} sided dice.')
            textfile.write(f'You chose {new_dice_sides} sided dice.' + '\n')
        elif user_choice == 't':
            roll_dice(dice)
        elif user_choice == 'p':
            # We flush the data collected so far to the disk in order to be able to read it
            # from the open file and print it.
            textfile.flush()
            print_rolls_file(textfile)
        elif user_choice == 'q':
            textfile.close()
            break
        else:
            print("Invalid input, please select one from the available options.")
            continue


while True:
    dice_chosen = choose_dice()
    dice = Dice(dice_chosen)
    textfile = open(create_file(), "x+")
    textfile.write(f'You chose {dice_chosen} sided dice.' + '\n')
    roll_dice(dice)
    menu()
    break
