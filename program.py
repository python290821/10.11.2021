
board = [['_','_','_'],['_','_','_'],['_','_','_']]

def get_player_choice(is_computer):
    if not is_computer:
        # loop -until square is not occupied

        # loop
        get_row = input('Please enter row: ')
        # check if valid

        # loop
        get_col = input('Please enter col: ')
        # check if valid

        # check if is free
    else:
        # loop
        # generate a random location
        # return llegal random_location
        pass


def play_game():
    game_over = false
    while not game_over:
        present_board()
        player1_choice = get_player_choice() # X
        check_if_won()
        if this_is_draw():
            break
        player2_choice = get_player_choice() # O
        check_if_won()


def main():
    play_game()

main();