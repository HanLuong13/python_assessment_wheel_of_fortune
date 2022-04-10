import random
from re import A

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

# to play entire round function
def play_round():
    global word, already_guessed_list, word_display, current_player, player_num_turn, \
        round_bank, player_first_turn, spin_result, continues_turn, continues_round
    word = 'car'
    #initialize list of already guessed letter 
    already_guessed_list = []
    # initialize a list for players' round money 
    round_bank = {}
    for player in player_list:
        round_bank.setdefault(player, 0)
    # initialize spin money to 0
    spin_amount = 0

    # TEST
    #initialize player_num_turn
    player_num_turn = {}
    for player in player_list:
        player_num_turn.setdefault(player, 0)

    # randomly pick word from list of words
    # word = random.choice(word_list)
    # display word
    # word_display = display_word()
    display_word()
    print('The word is:', word_display, '\n')

    # random pick who goes first
    current_player = random.choice(player_list)
    print('The first player to go is', current_player, '\n')


    player_first_turn = {'Player 1' : True, 'Player 2' : True, 'Player 3' : True}
    continues_turn = {'Player 1' : False, 'Player 2' : False, 'Player 3' : False}
    continues_turn[current_player] = True

    #round starts
    continues_round = True
    while continues_round:

        while player_first_turn[current_player]:
            print('What do you want to do?')
            print('(1) Spin wheel to guess a consenant')
            print('(2) Guess the word')

            input_valid = False
            while not input_valid:
                try:
                    player_input = int(input('Please enter 1 or 2. \n'))
                    if 1 <= player_input <= 2:
                        input_valid = True
                    else:
                        print('Please enter a valid choice.')
                except ValueError:
                    print('Please enter a valid choice.')
                
            if player_input == 1:
                # spin_result, turn = spin_wheel()
                spin_result = spin_wheel()  
                # if wheel segment is a number
                if player_first_turn[current_player]:
                    guess_consonant()
                    player_first_turn[current_player] = False
            elif player_input == 2:
                guess_word()
                player_first_turn[current_player] = False

        while continues_turn[current_player] and not player_first_turn[current_player]:
            continue_only_vowels = only_vowels()

            # print('count_consonants_left',count_consonants_left)
            # print('continue_only_vowels',continue_only_vowels)
            # print('letters_left',letters_left)     
            # print('word',word)

            #if word has more than vowels left
            if not continue_only_vowels:
                # display menu from player and prompt player to pick from 3 choices
                print('What do you want to do next?')
                print('(1) Buy a vowel')
                print('(2) Spin wheel to guess a consenant.')
                print('(3) Guess the word')
                input_valid = False
                while not input_valid:
                    try:
                        player_input = int(input('Please enter 1, 2, or 3 \n'))
                        if 1 <= player_input <= 3:
                            input_valid = True
                        else: 
                            print('Please enter a valid choice.')
                    except ValueError:
                        print('Please enter a valid choice.')

                #if 1. buy a vowel
                if player_input == 1:
                    buy_vowel()                                                               
                # if 2. spin the wheel to guess a consonant
                if player_input == 2:   
                    spin_result = spin_wheel()
                    # if they land on $, they guess a consonant 
                    if continues_turn[current_player]: 
                        guess_consonant()
                # if 3. guess the word
                if player_input == 3:
                    guess_word()
            # if only vowels are left
            elif continue_only_vowels:
                print('There\'s only vowels left. You can only choose from 2 optiosn below.')
                print('(1) Buy a vowel')
                print('(2) Guess the word')
                #validating input
                input_valid = False
                while not input_valid:
                    try:
                        player_input = int(input('Please enter 1 or 2. \n'))
                        if 1 <= player_input <= 2:
                            input_valid = True
                        else:
                            print('Please enter a valid choice.')
                    except ValueError:
                        print('Please enter a valid choice.')
                # if 1. buy a vowel
                if player_input == 1:
                    buy_vowel()
                # if 2. guess the word
                elif player_input == 2:
                    guess_word()

        # only if the round is still going
        if continues_round: 
            current_player = who_goes_next()
            continues_turn[current_player] = True


#to display word to show progress
def display_word():
    global word, already_guessed_list, word_display
    word_display = ''    
    for letter in word:
        if letter in already_guessed_list:
            word_display += letter
        else:
            word_display += '_'
    return word_display

#to spin wheel and get segment
def spin_wheel():
    global wheel, player_num_turn, player_first_turn, round_bank, continues_turn
    segment = random.choice(wheel)
    # segment = 'Bankruptcy'
    print(f'Wheel is spinning... You landed on {segment}.\n')

    if player_first_turn[current_player] and segment == 'Bankruptcy':
        player_first_turn[current_player] = False
        continues_turn[current_player] = False
    elif player_first_turn[current_player] and segment == 'Lose A Turn': 
        player_first_turn[current_player] = False
        continues_turn[current_player] = False
    elif not player_first_turn[current_player] and segment == 'Bankruptcy':
        round_bank[current_player] = 0
        continues_turn[current_player] = False
    elif not player_first_turn[current_player] and segment == 'Lose A Turn':
        continues_turn[current_player] = False
        
    return segment

#to guess a consonant
def guess_consonant():
    global already_guessed_list, word, current_player, spin_result, continues_turn, \
        word_display, continues_round
    guess = input('Please guess a consonant: ')

    # if it's the player's first time
    if player_first_turn[current_player]:
        # if consonant in already guessed
        if guess in already_guessed_list and guess in vowel_list: 
            print('Already guessed. It\'s also a vowel. You lose a turn.')
            continues_turn[current_player] = False

        # if consonant in already guessed
        elif guess in already_guessed_list: 
            print('Already guessed. You lose a turn.')
            continues_turn[current_player] = False
            
        # if guess is a consonant
        elif guess in vowel_list: 
            print('That\'s a vowel. You lose a turn.')
            continues_turn[current_player] = False       

        # if consonant is in word
        elif guess in word: 
            letter_count = 0
            for letter in word: 
                if guess == letter:
                    letter_count +=1
            guess_money = spin_result * letter_count
            already_guessed_list.append(guess) 
            display_word()
            print(f'You got it. {guess} is in the word {letter_count} times.\n')
            print(f'You get {guess_money}')
            round_bank[current_player] += guess_money
            print(round_bank)   

        # if consonant is not in word or invalid            
        elif guess.isalpha and not guess in word:
            print('Letter not in word. You lose a turn')
            continues_turn[current_player] = False
        #if guess in invalid
        else:
            print('Not a valid input. You lose a turn')
            continues_turn[current_player] = False

        #either way, first turn is done
        player_first_turn[current_player] = False

    #if not first turn
    elif not player_first_turn[current_player] and continues_turn[current_player]:
        # if consonant in already guessed
        if guess in already_guessed_list and guess in vowel_list: 
            print('Already guessed. It\'s also a vowel. You lose a turn.')
            continues_turn[current_player] = False

        # if consonant in already guessed
        if guess in already_guessed_list: 
            print('Already guessed. You lose a turn.')
            continues_turn[current_player] = False

        # if guess is a consonant
        elif guess in vowel_list: 
            print('That\'s a vowel. You lose a turn.')
            continues_turn[current_player] = False   

        # if consonant is in word
        elif guess in word: 
            letter_count = 0
            for letter in word: 
                if guess == letter:
                    letter_count +=1
            guess_money = spin_result * letter_count
            already_guessed_list.append(guess) 
            display_word()
            print(f'You got it. {guess} is in the word {letter_count} times.\n')
            print(f'You get {guess_money}')
            round_bank[current_player] += guess_money
            print(round_bank)  
            if find_unrevealed_letters():
                round_is_done()

        # if consonant is not in word or invalid            
        elif guess not in word:
            print('Letter not in word. You lose a turn')
            continues_turn[current_player] = False

        #if guess in invalid
        else:
            print('Not a valid input. You lose a turn')
            continues_turn[current_player] = False
            
    print('Current state of word is:', word_display)  



#to buy a vowel
def buy_vowel():
    global round_bank, current_player, already_guessed_list, word, vowel_list, \
        word_display, continues_round
    # check round money
    # if they don't have 250 in round money
    # back to menu    
    # current_bank = round_bank[current_player]
    if round_bank[current_player] < 250:
        print('You don\'t have enough money from this round.' +
        'Try spinning the wheel to guess a consonant or guess the word.')
    # if more than 250, prompt for guess
    elif round_bank[current_player] >= 250:
        guess = input('Enter a vowel: ')
        # if guess is not a vowel
        if not guess in vowel_list:
            print('Your guess is not a vowel. You lose 250. Your turn ends.')
            round_bank[current_player] -= 250
            continues_turn[current_player] = False
        # if their guess is already guessed
        elif guess in already_guessed_list:
            print('Already guessed. You lose 250. Your turn ends.')
            round_bank[current_player] -= 250
            continues_turn[current_player] = False   
        # if vowel is not in word                    
        elif not guess in word:
            print('Vowel not in word. You lose 250. Better luck next time!')
            round_bank[current_player] -= 250
            continues_turn[current_player] = False
        # if vowel is in word
        elif guess in word:
            # add letter to already_guessed_list
            already_guessed_list.append(guess)
            round_bank[current_player] -= 250
            # count how many times the vowel appears 
            letter_count = 0
            for letter in word: 
                if guess == letter:
                    letter_count +=1
            print(f'You got it. {guess} is in the word {letter_count} times.')
            print('250 is detracted. Your turn continues.')
            
            print(round_bank) 
            if find_unrevealed_letters():
                round_is_done()

    print('Current state of word is:', word_display)    
                
def guess_word():
    global round_bank, current_player, word, continues_round, continues_turn, player_first_turn
    player_input = input('Enter your word guess: ').lower()
    if player_input == word:
        round_is_done()
    else: 
        print('Not word. You lose your turn.')
        player_first_turn[current_player] = False
        continues_turn[current_player] = False

#find out if word is fully revealed
def find_unrevealed_letters():
    word_display = display_word()
    if '_' in word_display:
        revealed = False
    else:
        revealed = True
    return revealed

# find out if word only have vowels left unrevealed 
def only_vowels():
    global already_guessed_list, word
    letters_left = ''
    for letter in word:
        if not letter in already_guessed_list:
            letters_left += letter   
    count_consonants = 0
    for letter in letters_left:
        if letter in consonant_list:
            count_consonants += 1
    if count_consonants >= 1:
        continue_only_vowels = False
    else: 
        continue_only_vowels = True
    return continue_only_vowels

def round_is_done(): 
    global continues_round, round_bank, current_player, permanent_bank, player_first_turn,\
        continues_turn 
    permanent_bank[current_player] += round_bank[current_player]
    print('You win! Round in done. You won this round.')
    print('The round total is ', permanent_bank)

    #toggle off everything so close down round
    player_first_turn[current_player] = False
    continues_turn[current_player] = False
    continues_round = False

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
    print(f'The new player to go is {current_player}')

    return current_player



permanent_bank = {'Player 1': 100, 'Player 2': 200, 'Player 3': 0}


def play_third_round():
    global permanent_bank, already_guessed_list, word, consonant_list, vowel_list

    free_letters = 'rstlne'
    # ['r','s','t','l','n','e']

    highest_bank = max(permanent_bank.values())
    for key, value in permanent_bank.items():
        if value == highest_bank:
            final_player = key
    print(f'The player for the final and third round is {final_player}')

    word = 'car'
    #initialize list of already guessed letter 
    already_guessed_list = []

    # randomly pick word from list of words
    # word = random.choice(word_list)
    # display word
    # word_display = display_word()

    show_free_letters = ''

    #append letter in free letter to show and list of guesses
    for letter in free_letters:
        show_free_letters += letter + ' '
        already_guessed_list.append(letter)

    #display both free letters and word with those letters shown
    print('Word is shown with these letters:', show_free_letters)

    print('\nThe word is:', display_word(), '\n')

    input_invalid = True
    while input_invalid:
        print('You get 3 consonants and 1 vowel.')
        print('Enter them all at once, no spaces.')
        player_input = input('Here: ')

        consonant_count = 0
        vowel_count = 0
        repeat = 0
        for letter in player_input:
            #counting consonants and vowels and letters already given
            if letter in already_guessed_list:
                repeat += 1
            if letter in consonant_list:
                consonant_count += 1
            elif letter in vowel_list:
                vowel_count += 1
            
        if repeat >= 1 and len(player_input) < 4:
            print(f'Your guess is too short and include a free letter. Those letters are {show_free_letters}. Do it again.')
        elif repeat >= 1:
            print(f'Your guess includes a free letter. Those letters are {show_free_letters}. Do it again.')
        elif consonant_count == 3 and vowel_count == 1:
            print('Okay, let\'s see those letters in the word.')
            input_invalid = False
        else: 
            print('Did you read the instruction? Do it again.')

    #successful input, add to already guessed
    for letter in player_input:
        already_guessed_list.append(letter)
    
    print('\nThe word is now:', display_word(), '\n')
    player_guess = input('Enter your guess: ')

    if player_guess == word:
        print('Yes, you got it.')
    else: 
        print('Not the word.')



play_third_round()

# print('Welcome to Wheel of Fortune! \n')
# play_round()
# print('Alright! Second round!')
# play_round()

