import random

WIDTH = 40

class Game:
    def __init__(self):
        self.username = None
        self._consecutive_wins = 0
        self.last_win = None
        self._matches = 0
        self._draws = 0
        self._bot_score = 0
        self._user_score = 0
        self.user_input = None
        self.bot_input = None
 
    def __get_bot_choice(self):
        return random.choice(['Rock', 'Paper', 'Scissors'])
    
    def __display_menu(self):
        print('=' * WIDTH)
        print('Welcome to Rock Paper Scissor'.center(WIDTH))
        print('=' * WIDTH)
        print('Please enter your name: ', end = '')
        
    def start(self):
        self.__display_menu()
        self.username = input()
        print('\n')
        print(f'Hello {self.username}! Lets start the game.')
        print('-' * WIDTH)
        print('Enter "r"  for Rock')
        print('Enter "p" for Paper')
        print('Enter "s" for Scissor')
        print('Enter "t" to restart the game')
        print('Enter "q" to quit')
        
        while True:
            self.user_input = input().lower()
            
            if self.user_input == 'r':
                self.user_input = 'Rock'
            elif self.user_input == 'p':
                self.user_input = 'Paper'
            elif self.user_input == 's':
                self.user_input = 'Scissors'
            elif self.user_input == 't':
                print('=' * WIDTH)
                print('Restartting the game'.center(WIDTH))
                print('=' * WIDTH)

            elif self.user_input == 'q':
                print('=' * WIDTH)
                print('Here is the match summary'.center(WIDTH))
                print('=' * WIDTH)
                print(f'Number of matches {self.username} played: {self._matches}')
                print(f'Number of matches {self.username} won: {self._user_score}')
                print(f'Number of matches Bot won: {self._bot_score}')
                print(f'Number of draws: {self._draws}')
                print('-' * WIDTH)
                print('Thank you for playing, Goodbye!!')
                break
            else:
                print('-' * WIDTH)
                print('Invalid input! Please try again.')
                print('-' * WIDTH)
                continue
            
            self.bot_input = self.__get_bot_choice()
            print(f'Bot choice: {self.bot_input}')
            
            if self.user_input == self.bot_input:
                print('-' * WIDTH)
                print('Draw!')
                self._draws += 1
                self.last_win = None
            elif self.user_input == 'Rock' and self.bot_input == 'Paper':
                print('-' * WIDTH)
                print('You lose!')
                self._bot_score += 1
                self.last_win = False
            elif self.user_input == 'Rock' and self.bot_input == 'Scissors':
                print('-' * WIDTH)
                print('You win!')
                self._user_score += 1
                self.last_win = True
                self._consecutive_wins += 1
            elif self.user_input == 'Paper' and self.bot_input == 'Rock':
                print('-' * WIDTH)
                print('You win!')
                self._user_score += 1
                self.last_win = True
                self._consecutive_wins += 1
            elif self.user_input == 'Paper' and self.bot_input == 'Scissors':
                print('-' * WIDTH)
                print('You lose!')
                self._bot_score += 1
                self.last_win = False
            elif self.user_input == 'Scissors' and self.bot_input == 'Rock':
                print('-' * WIDTH)
                print('You lose!')
                self._bot_score += 1
                self.last_win = False
            elif self.user_input == 'Scissors' and self.bot_input == 'Paper':
                print('-' * WIDTH)
                print('You win!')
                self._user_score += 1
                self.last_win = True
                self._consecutive_wins += 1
            
            self._matches += 1
        
            if self.last_win:
                if self._consecutive_wins == 3:
                    print('-' * WIDTH)
                    print('You won 3 in a row!')
                    print('Congratulations!!!')
                    print('-') * WIDTH
                    break
                    
if __name__ == "__main__":
    game = Game()
    game.start()