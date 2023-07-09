# COP3502 Project 1 - Blackjack
# Coder: Michael Muraglia
# Date: 6/11/2023

# Imports
from p1_random import P1Random


rng = P1Random()


def print_menu():  # define user options function
    print('1. Get another card')
    print('2. Hold hand')
    print('3. Print statistics')
    print('4. Exit\n')
    return int(input('Choose an option: '))


game_continue = True  # Initializing variable for outer while loop
game_num = 1  # Initializing variable for game number
user_wins = 0  # Initializing variable for user wins
dealer_wins = 0  # Initializing variable for dealer wins
ties = 0  # Initializing variable for ties between players

while game_continue:
    print(f'START GAME #{game_num}\n')
    current_game = True  # Initializing variable for inner while loop
    player_hand = 0  # Initializing variable for player hand count
    while current_game:
        card_delt = (rng.next_int(13) + 1)  # Player Card Delt (Integer)
        if card_delt == 1:  # Name and value for face cards
            card_name = 'ACE'
        elif card_delt == 11:  # Name and value for face cards
            card_name = 'JACK'
            card_delt = 10
        elif card_delt == 12:  # Name and value for face cards
            card_name = 'QUEEN'
            card_delt = 10
        elif card_delt == 13:  # Name and value for face cards
            card_name = 'KING'
            card_delt = 10
        else:
            card_name = str(card_delt)  # string of name for card delt
        print(f'Your card is a {card_name}!')
        player_hand += card_delt  # New Player Hand value
        print(f'Your hand is: {player_hand}\n')

        if player_hand == 21:  # User blackjack
            print('BLACKJACK! You win!\n')
            user_wins += 1
            game_num += 1
            break
        if player_hand > 21:  # User over 21
            print("You exceeded 21! You lose.\n")
            dealer_wins += 1
            game_num += 1
            break

        #  Player Options
        user_choice = print_menu()
        print("")  # Formatting

        # Cycles through player options
        options = True
        while options:
            if user_choice == 1:
                break
            elif user_choice == 2:
                dealer_hand = rng.next_int(11) + 16  # Generates Dealers Hand
                if dealer_hand > 21:  # Dealer bust
                    print(f'Dealer\'s hand: {dealer_hand}')
                    print(f'Your hand is: {player_hand}')
                    print('\nYou win!\n')
                    user_wins += 1
                    game_num += 1
                    current_game = False
                    break
                elif dealer_hand == player_hand:  # Tie Game
                    print(f'Dealer\'s hand: {dealer_hand}')
                    print(f'Your hand is: {player_hand}\n')
                    print('It\'s a tie! No one wins!\n')
                    ties += 1
                    game_num += 1
                    current_game = False
                    break
                elif dealer_hand > player_hand:  # Dealer Wins
                    print(f'Dealer\'s hand: {dealer_hand}')
                    print(f'Your hand is: {player_hand}')
                    print('\nDealer wins!\n')
                    dealer_wins += 1
                    game_num += 1
                    current_game = False
                    break
                else:  # Player Wins (non-blackjack)
                    print(f'Dealer\'s hand: {dealer_hand}')
                    print(f'Your hand is: {player_hand}')
                    print('\n You Win!\n')
                    user_wins += 1
                    game_num += 1
                    current_game = False
                    break
            elif user_choice == 3:  # Prints Stats
                game_num -= 1  # does not count current game
                print(f'Number of Player wins: {user_wins}')
                print(f'Number of Dealer wins: {dealer_wins}')
                print(f'Number of tie games: {ties}')
                print(f'Total # of games played is: {game_num}')
                percentage = '{:.1%}'.format(user_wins / game_num)
                print(f'Percentage of Player wins: {percentage}\n')

                user_choice = print_menu()
                continue

            # Player Leaves Game
            elif user_choice == 4:
                current_game = False
                game_continue = False
                break

            else:  # Invalid Input by User
                print('Invalid input!')
                print('Please enter an integer value between 1 and 4.\n')
                user_choice = print_menu()
                continue
