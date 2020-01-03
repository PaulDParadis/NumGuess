num_list = [8, 2, 3, 13, 21, 7]
def num_pick():
    num_guess = int(input("Pick a number, and I will tell you if it's in the list: "))
    if num_guess in num_list:
        print("Correct!")
    elif num_guess not in num_list:
        print("False!")
num_pick()
while True:
    choose_again = input("Try again? Type 'y' to continue, or 'q' to quit: ")
    if choose_again == 'y':
        num_pick()
    elif choose_again == 'q':
        print("Thanks for playing!")
        break
        
