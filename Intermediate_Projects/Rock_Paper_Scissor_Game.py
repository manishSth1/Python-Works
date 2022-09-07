import random

name = input("please enter your name to continue: ")

def game_statistics(total_rounds, total_draws, player_one, player_two):
    print("+-------------------------------------------------------+")
    print("|                      Game Statistics                  |")
    print("+.......................................................+")
    print("|  Total Rounds:     {}      |  Total Draws:      {}      |".format(total_rounds, total_draws))
    print("|  {}:         {}      |  {}:             {}      |".format(player_one, player_one_score, player_two, player_two_score))
    print("|                                                       |")
    if player_one_score > player_two_score:
        print("|   +-----------------------------------------------+   |")
        print("|   |                   YOU WON!                    |   |")
        print("|   +-----------------------------------------------+   |")
        print("|                                                       |")
    elif player_one_score < player_two_score:
        print("|   +-----------------------------------------------+   |")
        print("|   |                 COMPUTER WON!                 |   |")
        print("|   +-----------------------------------------------+   |")
        print("|                                                       |")
    else:
        print("|   +-----------------------------------------------+   |")
        print("|   |                   DRAW!                       |   |")
        print("|   +-----------------------------------------------+   |")
        print("|                                                       |")
    print("+-------------------------------------------------------+")

def restart_game():
    global player_one_score
    global player_two_score
    global total_rounds
    global total_draws
    player_one_score = 0
    player_two_score = 0
    total_rounds = 0
    total_draws = 0

def quit_game():
    print("Thank you for playing!")
    exit()

def compare_choices(player_one, player_two):
    global player_one_score
    global player_two_score
    global total_rounds
    global total_draws
    if player_one == player_two:
        total_draws += 1
        print("+-------------------------------------------------------+")
        print("|                      Game Statistics                  |")
        print("+.......................................................+")
        print("|  Total Rounds:     {}      |  Total Draws:      {}      |".format(total_rounds, total_draws))
        print("|  {}:         {}      |  {}:             {}      |".format(player_one, player_one_score, player_two, player_two_score))
        print("|                                                       |")
        print("|   +-----------------------------------------------+   |")
        print("|   |                   DRAW!                       |   |")
        print("|   +-----------------------------------------------+   |")
        print("|                                                       |")
        print("+-------------------------------------------------------+")
    elif player_one == "ROCK" and player_two == "SCISSOR":
        player_one_score += 1
        total_rounds += 1
        game_statistics(total_rounds, total_draws, player_one, player_two)
    elif player_one == "SCISSOR" and player_two == "ROCK":
        player_two_score += 1
        total_rounds += 1
        game_statistics(total_rounds, total_draws, player_one, player_two)
    elif player_one == "PAPER" and player_two == "SCISSOR":
        player_two_score += 1
        total_rounds += 1
        game_statistics(total_rounds, total_draws, player_one, player_two)
    elif player_one == "SCISSOR" and player_two == "PAPER":
        player_one_score += 1
        total_rounds += 1
        game_statistics(total_rounds, total_draws, player_one, player_two)
    elif player_one == "ROCK" and player_two == "PAPER":
        player_two_score += 1
        total_rounds += 1
        game_statistics(total_rounds, total_draws, player_one, player_two)
    elif player_one == "PAPER" and player_two == "ROCK":
        player_one_score += 1
        total_rounds += 1
        game_statistics(total_rounds, total_draws, player_one, player_two)

def play_game():
    options = ["ROCK", "SCISSOR", "PAPER"]
    choice = ""
    while choice != "0":
        if player_one_score == 3:
            print("+-------------------------------------------------------+")
            print("|                      Game Statistics                  |")
            print("+.......................................................+")
            print("|  Total Rounds:     {}      |  Total Draws:      {}      |".format(total_rounds, total_draws))
            print("|  {}:         {}      |  {}:             {}      |".format(player_one, player_one_score, player_two, player_two_score))
            print("|                                                       |")
            print("|   +-----------------------------------------------+   |")
            print("|   |      CONGRATULATIONS, YOU WON THE MATCH       |   |")
            print("|   +-----------------------------------------------+   |")
            print("|                                                       |")
            print("+-------------------------------------------------------+")
            restart_game()
            break
        elif player_two_score == 3:
            print("+-------------------------------------------------------+")
            print("|                      Game Statistics                  |")
            print("+.......................................................+")
            print("|  Total Rounds:     {}      |  Total Draws:      {}      |".format(total_rounds, total_draws))
            print("|  {}:         {}      |  {}:             {}      |".format(player_one, player_one_score, player_two, player_two_score))
            print("|                                                       |")
            print("|   +-----------------------------------------------+   |")
            print("|   |             COMPUTER WON THE MATCH           |   |")
            print("|   +-----------------------------------------------+   |")
            print("|                                                       |")
            print("+-------------------------------------------------------+")
            restart_game()
            break
        print("1. ROCK")
        print("2. SCISSOR")
        print("3. PAPER")
        print("0. Quit Game")
        print("9. Restart Game")
        choice = input("ROCK-PAPER-SCISSOR: ")
        if choice == "0":
            quit_game()
            break
        elif choice == "9":
            restart_game()
            break
        else:
            computer = random.choice(options)
            compare_choices(choice, computer)

player_one = name
player_two = "Computer"
player_one_score = 0
player_two_score = 0
total_rounds = 0
total_draws = 0

play_game()