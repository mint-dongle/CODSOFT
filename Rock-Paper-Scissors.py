import random
import os

# ANSI color codes for colourful output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_title():
    print(f"{Colors.HEADER}{Colors.BOLD}=== Rock Paper Scissors Game ==={Colors.ENDC}")

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    print(f"{Colors.OKCYAN}Choose one: {Colors.BOLD}rock{Colors.ENDC}, {Colors.BOLD}paper{Colors.ENDC}, or {Colors.BOLD}scissors{Colors.ENDC}")
    while True:
        user_input = input(f"{Colors.OKBLUE}Your choice: {Colors.ENDC}").strip().lower()
        if user_input in choices:
            return user_input
        print(f"{Colors.WARNING}Invalid choice! Please choose rock, paper, or scissors.{Colors.ENDC}")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'

def print_result(user, computer, result):
    print(f"\n{Colors.BOLD}You chose:{Colors.ENDC} {Colors.OKGREEN}{user.capitalize()}{Colors.ENDC}")
    print(f"{Colors.BOLD}Computer chose:{Colors.ENDC} {Colors.FAIL}{computer.capitalize()}{Colors.ENDC}")
    if result == 'win':
        print(f"{Colors.OKGREEN}{Colors.BOLD}You win! 🎉{Colors.ENDC}")
    elif result == 'lose':
        print(f"{Colors.FAIL}{Colors.BOLD}You lose! 😢{Colors.ENDC}")
    else:
        print(f"{Colors.WARNING}{Colors.BOLD}It's a tie! 🤝{Colors.ENDC}")

def play_again():
    answer = input(f"\n{Colors.OKCYAN}Play again? (y/n): {Colors.ENDC}").strip().lower()
    return answer == 'y'

def main():
    user_score = 0
    computer_score = 0
    round_num = 1

    clear_screen()
    print_title()
    print(f"{Colors.OKCYAN}Welcome! Let's play Rock-Paper-Scissors.{Colors.ENDC}")

    while True:
        print(f"\n{Colors.BOLD}--- Round {round_num} ---{Colors.ENDC}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = decide_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, result)

        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        print(f"\n{Colors.BOLD}Score:{Colors.ENDC} You: {Colors.OKGREEN}{user_score}{Colors.ENDC} | Computer: {Colors.FAIL}{computer_score}{Colors.ENDC}")

        if not play_again():
            print(f"\n{Colors.HEADER}{Colors.BOLD}Thanks for playing! Final Score - You: {user_score}, Computer: {computer_score}{Colors.ENDC}")
            break
        round_num += 1
        clear_screen()
        print_title()

if __name__ == "__main__":
    main()