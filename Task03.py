import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Sorry, it's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "Fantastic, You Win!"
    else:
        return "You Lose, Better Luck Next Time!"

def reset_scores():
    return 0, 0

def play_game():
    user_score, computer_score = reset_scores()

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = get_computer_choice()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.\n")
            continue

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        result = determine_winner(user_choice, computer_choice)
        print(result + "\n")

        if "Win" in result:
            user_score += 1
        elif "Lose" in result:
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}\n")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            reset = input("Do you want to reset the scores? (y/n): ").lower()
            if reset == 'y':
                user_score, computer_score = reset_scores()
        else:
            print(f"\nFinal Scores -> You: {user_score}, Computer: {computer_score}")
            print("Thanks For Playing,\nSee You Next Time!")
            break

if __name__ == "__main__":
    play_game()
