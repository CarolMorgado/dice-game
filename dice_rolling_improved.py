import random

total_dice_rolled = 0

while True:
    choice = input('Roll the dices? (y/n): ').lower()
    if choice == 'y':
        try:
            number_dice = int(
                input('How many dice do you want to roll? (1-10): '))
            if 1 <= number_dice <= 10:
                die = [random.randint(1, 6)
                       for x in range(number_dice)]
                total_dice_rolled += number_dice
                print(f'Dice rolls: {die}')
                print(f'Total dice rolled: {total_dice_rolled}')
            else:
                print('Please choose 1-10!')
        except ValueError:
            print('Invalid choice!')
    elif choice == 'n':
        print(f'Thank you for playing! Total dice rolled: {total_dice_rolled}')
        break
    else:
        print('Invalid choice!')
