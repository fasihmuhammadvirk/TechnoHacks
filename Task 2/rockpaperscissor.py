import random

def get_user_choice():
    """
    Function to get the user's choice of rock, paper, or scissors.

    Returns:
        str: The user's choice of rock, paper, or scissors.

    Raises:
        None
    """
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    """
    Generates a random choice from a list of options and returns it.

    Returns:
        str: A randomly chosen option from the list of choices.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner based on the choices made by the user and the computer.

    Args:
        user_choice (str): The choice made by the user ("rock", "paper", or "scissors").
        computer_choice (str): The choice made by the computer ("rock", "paper", or "scissors").

    Returns:
        str: The outcome of the game ("It's a tie!", "You win!", or "Computer wins!").
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    """
    The main function that runs the Rock, Paper, Scissors game.
    
    This function prints a welcome message and then enters into a loop where the player can choose their move and play against the computer. It calls the following helper functions:
    
    - `get_user_choice()`: This function prompts the user to enter their choice of move (rock, paper, or scissors) and returns the user's choice.
    - `get_computer_choice()`: This function randomly generates the computer's choice of move (rock, paper, or scissors) and returns the computer's choice.
    - `determine_winner(user_choice, computer_choice)`: This function takes the user's choice and the computer's choice as parameters and determines the winner of the game based on the Rock, Paper, Scissors rules. It returns a string indicating the result of the game.
    
    Inside the loop, the function prints the user's choice, the computer's choice, and the result of the game. It then prompts the user to play again and breaks out of the loop if the user does not want to play again.
    
    Finally, the function prints a thank you message.
    """
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}")
        print(f"The computer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
