import random

# initialize a list for the three players
player_list = ['Player 1', 'Player 2', 'Player 3']

# initialize a list for wheel with segments players can land on, in order of the wheel 
wheel = ['Lose a turn', 200, 400, 250, 150, 400, 600, 250, 350, 'Bankruptcy', 750,\
    800, 300, 200, 900, 500, 400, 300, 200, 100, 700, 200, 150, 450]

# initalize list of words 
#read in text file and choose on words with only 5 letters and more
word_list = []
f = open('words_alpha.txt')
words = f.readlines()
f.close()

for word in words:
    word = word.strip()
    if len(word) > 5:
        word_list.append(word)

# initialize dictionary for players' permanent money with player1, player2, player3 
# and 0 for the values
permanent_bank = {}
for player in player_list:
    permanent_bank.setdefault(player, 0)

# who goes next function
def who_goes_next():
    global current_player
    # if 1, set current player to 2
    if current_player == 'Player 1':
        current_player = 'Player 2'
    # if 2, set current player to 3
    elif current_player == 'Player 2':
        current_player = 'Player 3'
    # if 3, set current player to 1
    elif current_player == 'Player 3':
        current_player = 'Player 1'    
    return current_player

# to play entire round function
def play_round():
    global word, already_guessed_list, word_display
    # initialize turn money to 0
    turn_bank = 0
    #initialize list of already guessed letter 
    already_guessed_list = []
    # initialize dictionary for players' round money with player1, player2, player3 and 0 for the values
    round_bank = {}
    for player in player_list:
        round_bank.setdefault(player, 0)
    # initialize spin money to 0
    spin_amount = 0
    # randomly pick word from list of words
    word = 'random'
    # word = random.choice(word_list)
    print(display_word())


    # random pick who goes first
    current_player = random.choice(player_list)

def display_word():
    global word, already_guessed_list, word_display
    word_display = ''    
    for letter in word:
        if letter in already_guessed_list:
            word_display += letter
        else:
            word_display += '_'
    return word_display
      
play_round()