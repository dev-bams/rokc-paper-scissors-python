import random


def generate_random_number():
    return random.randint(0, 2)


def generate_computer_move(random_number):
    if random_number == 0:
        return "rock"
    elif random_number == 1:
        return "paper"
    else:
        return "scissors"


def get_player_move():
    while True:
        player_move = input(
            "Enter your move (Rock(R), Paper(P), Scissors(S)): ").lower()
        if player_move in ["rock", "paper", "scissors", "r", "p", "s"]:
            if (player_move == "r"):
                player_move = "rock"
            elif (player_move == "p"):
                player_move = "paper"
            elif (player_move == "s"):
                player_move = "scissors"
            return player_move
        else:
            print("Invalid move. Please enter 'rock', 'paper', or 'scissors'.")


def compare_moves(computer_move, player_move):
    if computer_move == player_move:
        return "draw"
    elif (computer_move == "rock" and player_move == "scissors") or (computer_move == "paper" and player_move == "rock") or (computer_move == "scissors" and player_move == "paper"):
        return "lose"
    else:
        return "win"


def increase_score(result, player_score, computer_score):
    if result == "win":
        player_score += 1
    elif result == "lose":
        computer_score += 1
    return player_score, computer_score


def get_final_score(computer_score, player_score):
    if computer_score > player_score:
        return "Computer won the whole thing"
    elif player_score > computer_score:
        return "Player won the whole thing"
    else:
        return "the whole thing was a draw"


def play():
    player_score = 0
    computer_score = 0
    while True:
        random_number = generate_random_number()
        computer_move = generate_computer_move(random_number)
        player_move = get_player_move()
        result = compare_moves(computer_move, player_move)
        player_score, computer_score = increase_score(
            result, player_score, computer_score)
        print(
            f"computer played: {computer_move}. you played: {player_move}. you {result}")
        print(f"Player: {player_score} - Computer: {computer_score}")
        play_again = input("Game on? (Yes(Y), No(N)): ").lower()
        print("".center(60, "="))
        if play_again not in ["yes", "y"]:
            print(get_final_score(computer_score, player_score))
            break


play()
