import random
import time

# CONFIGURATION
# You can change these values in the config.py file
from config import MIN_NUMBER, MAX_NUMBER, NUMBERS_TO_ASK, REMOVE_ZERO

# MAIN LOGIC
def guess_number():
    # ABOUT GAME
    print("Let me guess the number you're thinking of (1 to 10)")
    print("I'll ask for 4 numbers, and then I will try")

    # LISTS
    numbers_selected = []
    final_array = []

    # ASKING FOR NUMBERS
    for i in range(NUMBERS_TO_ASK):
        number = input(f"Number {i+1}> ")
        time.sleep(1)
        if MIN_NUMBER <= int(number) <= MAX_NUMBER:
            numbers_selected.append(int(number))
        
        elif int(number) > MAX_NUMBER or int(number) < MIN_NUMBER:
            print(f"Wrong input!! you typed {number}, but it should be from {MIN_NUMBER} to {MAX_NUMBER}")
        else:
            print("Uhhh.. Are you sure about that?")

    # REMOVING NUMBERS FROM THE RANGE
    for i in range(MIN_NUMBER, MAX_NUMBER+1):
        if i not in numbers_selected:
            final_array.append(i)

    # REMOVING ZERO
    if REMOVE_ZERO and 0 in final_array:
        final_array.remove(0)

    print("Think of the next number :)")
    time.sleep(2)

    print(f"Let me guess the number you're thinking of ({MIN_NUMBER} to {MAX_NUMBER})")
    time.sleep(1)
    # PICKING RANDOM NUMBER FROM FINAL ARRAY
    picked_number = random.choice(final_array)
    print(f"I'm sure it's {picked_number}!")

# MAIN LOOP
if __name__ == "__main__":
    guess_number()
        
    

