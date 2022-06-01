import random

OPTIONS = ['R', 'P', 'S']
CHOICES = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}


def validate_input(user_input):
    user_input = str(user_input).upper()

    if user_input not in OPTIONS:
        print("Error: Invalid choice. Try again!!!")
        return "error"

    return user_input


def is_game_tie(choice1, choice2):
    if choice1 == 'R' and choice2 == 'S' or choice2 == 'R' and choice1 == 'S':
        print("Rock beats Scissors")
        print("Winner: Player") if choice1 == 'R' else print("Winner: CPU")
    elif choice1 == 'S' and choice2 == 'P' or choice2 == 'S' and choice1 == 'P':
        print("Scissors beats Paper")
        print("Winner: Player") if choice1 == 'S' else print("Winner: CPU")
    elif choice1 == 'P' and choice2 == 'R' or choice2 == 'P' and choice1 == 'R':
        print("Paper beats Rock")
        print("Winner: Player") if choice1 == 'P' else print("Winner: CPU")
    else:
        print("It's a tie!!!")
        print("Go Again!!!")
        return True

    return False


def main():

    tie = True
    print("***********************************************")
    print("\tA GAME OF ROCK PAPER SCISSORS")
    print("***********************************************")

    print("Player vs Computer")
    while tie:
        print("\nPlayer make your choice")
        player_choice = validate_input(input('"R", "P" or "S": '))
        if player_choice == "error":
            continue
        cpu_choice = random.choice(OPTIONS)

        print(
            f"Player ({CHOICES[player_choice]}) : CPU ({CHOICES[cpu_choice]})")

        tie = is_game_tie(player_choice, cpu_choice)


if __name__ == '__main__':
    main()
