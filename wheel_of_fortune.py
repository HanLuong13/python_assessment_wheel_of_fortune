import random

from more_itertools import only

# initialize a list for the three players
player_list = ['Player 1', 'Player 2', 'Player 3']

# initialize a list for wheel with segments players can land on, in order of the wheel 
wheel = ['Lose A Turn', 200, 400, 250, 150, 400, 600, 250, 350, 'Bankruptcy', 750,\
    800, 300, 200, 900, 500, 400, 300, 200, 100, 700, 200, 150, 450]

#initialize list for consonants and vowels
consonant_list = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowel_list = ['a','e','i','o','u']

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

# initialize list for players' permanent money 
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
    print('Welcome to Wheel of Fortune! \n')
    global word, already_guessed_list, word_display, current_player
    # initialize turn money to 0
    turn_bank = 0
    #initialize list of already guessed letter 
    already_guessed_list = []
    # initialize a list for players' round money 
    round_bank = {}
    for player in player_list:
        round_bank.setdefault(player, 0)
    # initialize spin money to 0
    spin_amount = 0

    # randomly pick word from list of words
    word = 'ca'
    # word = random.choice(word_list)
    # display word
    # word_display = display_word()
    display_word()
    print('The word is:', word_display, '\n')

    # random pick who goes first
    current_player = random.choice(player_list)
    print('The first player to go is', current_player, '\n')
  
    # spin_result, turn = spin_wheel()
    spin_result = spin_wheel()
    print('Wheel is spinning... You landed on', spin_result, '\n')
    first_turn = True   
    while first_turn:
        # if wheel segment is bankruptcy
        if spin_result == 'Bankruptcy':
            # their turn ends & next player goes
            current_player = who_goes_next()
            first_turn = False
        # if wheel segment is lose a turn
        elif spin_result == 'Lose A Turn': 
            # their turn ends & next player goes
            current_player = who_goes_next()
            first_turn == False
        # if wheel segment is a number
        else:
            # prompt them for consonant
            # validate consonant
            consonant_input_valid = True
            while consonant_input_valid:
                consonant_input = input('Please guess a consonant: ')
                #if input is a consonant
                if consonant_input in consonant_list:
                    # if consonant is in word
                    if consonant_input in word:
                        # count how many times the consonant appears 
                        letter_count = 0
                        for letter in word: 
                            if consonant_input == letter:
                                letter_count +=1
                        guess_money = spin_result * letter_count
                        print(f'You got it. {consonant_input} is in the word {letter_count} times.\n')
                        print(f'You get {guess_money}')
                        round_bank[current_player] += guess_money
                        print(round_bank)
                        # add letter to already_guessed_list
                        already_guessed_list.append(consonant_input)
                        # display word
                        display_word()
                        print(word_display)
                        # give them money to their turn bank
                        consonant_input_valid = False
                        first_turn = False
                #if input is not a consonant, lose turn
                else:
                    print('You didn\'t guess a consonant. You lose your turn.')
                    consonant_input_valid = False
                    first_turn = False
    turn = True
    while turn:
    # find out if word only have vowels left unrevealed 
        letters_left = ''
        checking_word = word
        for letter in already_guessed_list:
            if letter in word:
                print('')





        # count_consonants = 0
        # for letter in word_display:
        #     if letter in consonant_list:
        #         count_consonants += 1
        # if count_consonants >= 1:
        #     only_vowels_left = False
        # else: 
        #     only_vowels_left = True
        # #if word has more than vowels left
        # if not only_vowels_left:
        #     print('Good to go.')
        #     break
        # elif only_vowels_left:
        #     print('Only vowels left.')
        #     break
        # else:
        #     print('Something went wrong')
        #     break






        
    # who goes next function



def display_word():
    global word, already_guessed_list, word_display
    word_display = ''    
    for letter in word:
        if letter in already_guessed_list:
            word_display += letter
        else:
            word_display += '_'
    return word_display

def spin_wheel():
    global wheel
    segment = random.choice(wheel)
    # turn = True
    # if segment == 'Bankruptcy':
    #     turn = False
    # elif segment == 'Lose A Turn': 
    #     turn = False
    return segment
    # , turn

play_round()
# who_goes_next()
# print(current_player)