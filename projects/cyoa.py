"""This program is dice guessing game. Users choose to roll either a 3 or 6-sided die.
They are rewarded 1 point for correctly guessing the outcome of a 3-sided die roll, and
2 points for correctly guessing the outcome of a 6-sided die roll. Players' points reset to
zero if they guess inforrectly. A game loop is incorporated in the main function.  The loop 
allows users to continue playing either game if they wish, or quit playing altogether.
Players are awarded a trophy if they win 3 or more points"""
from random import randint
player: str = ""
points: int 
winners_trophy: str = "\U0001F3C6"
sad_face: str = "\U0001F641"

def main() -> None:
    global points
    points = 0
    greet()
    stillPlaying: bool = True
    while stillPlaying == True:
        print(f"So, {player}. What do you want to do?")
        print("1. 3-sided die guessing game 2. 6-sided die guessing 3. Stop Playing")
        userChoice: int = int(input("Enter the number corresponding with what you want to do: "))
        if userChoice == 1:
            threeSidedDiePoints()
        if userChoice == 2:
            points += sixSidedDiePoints(points)
        if userChoice == 3:
            if points >= 3:
                print(f"Thanks for playing {player}.")
                print(f"You scored {points}!! That's amazing!")
                print(f"You earned a trophy {winners_trophy}!")
                stillPlaying = False
            if points == 0:
                print(f"Thanks for playing {player}.")
                print(f"You scored {points}.")
                print(f"Better luck next time {sad_face}")
                stillPlaying = False
            else:
                print(f"Thanks for playing {player}.")
                print(f"You scored {points}.")
                stillPlaying = False

def threeSidedDiePoints() -> None:
    """This function allows users to guess the outcome of a 3-sided die roll
    players are awarded 1 point for guessing correctly. If they guess 
    incorrectly, their points are reset to 0."""
    global points
    roll: int = randint(1, 3)
    print(f"Hi, {player}. Which number do you think the die landed on?")
    guess: int = int(input("Enter a number 1-3: "))
    if guess == roll:
        points += 1
        print("Correct!")
    else:
        print("You guessed wrong!")
        points = 0

def sixSidedDiePoints(points: int) -> int:
    """This function allows users to guess the outcome of a 6-sided die roll
    players are awarded 2 points for guessing correctly. If they guess 
    incorrectly, their points are reset to 0."""
    roll: int = randint(1, 6)
    print(f"Hi, {player}. Which number do you think the die landed on?")
    guess: int = int(input("Enter a number 1-6: "))
    if guess == roll:
        points += 2
        print("Correct!")
    else:
        print("You guessed wrong!")
        points = 0
    return points
    
    
def greet() -> None:
    """This function asks a players name, greets them, and gives the instructions for the game"""
    global player
    player = input("Enter Your Name: ")
    print(f"Welcome {player}.  The objective of this game is to guess the outcome of a three sided die roll.")
    print("You gain a point for each dice roll you guess correctly")
    print("If you're feeling lucky, you can choose to roll a six sided die instead.")
    print("Each roll you guess correctly from a six sided die awards you double the points!")
    print("If you guess incorrectly your points reset to zero")
    print("If you get 3 points or more, you win a trophy!")
    print("Lets see how many points you can get!")

if __name__ == "__main__":
    main()
