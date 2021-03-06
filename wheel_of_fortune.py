import random
from threading import Timer

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

#for timer
out_of_time=False

# to play entire round function
def play_round():
    global word, guessed_right_list, word_display, current_player, player_num_turn, \
        round_bank, player_first_turn, spin_result, continues_turn, continues_round, not_in_word_valid_guesses

    #initialize list of guessed right letter and the all_guesses 
    guessed_right_list = []
    not_in_word_valid_guesses = []
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

    # randomly pick word from list of words and display
    word = random.choice(word_list)
    display_word()
    print('The word is:', word_display, '\n')

    # random pick who goes first
    current_player = random.choice(player_list)
    print(f'The first player to go is {current_player}.')

    # initializing tracking for players' turns
    player_first_turn = {'Player 1' : True, 'Player 2' : True, 'Player 3' : True}
    continues_turn = {'Player 1' : False, 'Player 2' : False, 'Player 3' : False}
    continues_turn[current_player] = True

    #round starts
    continues_round = True
    while continues_round:
        # if it's their first time, they should be able spin wheel to guess consonant 
        # or guess word if others have gone before
        while player_first_turn[current_player]:
            print(f'\nWhat does {current_player} want to do?')
            print('(1) Spin wheel to guess a consonant')
            print('(2) Guess the word \n')

            #validate input, no numbers or characters in guesses
            input_valid = False
            while not input_valid:
                try:
                    player_input = int(input('Enter 1 or 2: \n'))
                    if 1 <= player_input <= 2:
                        input_valid = True
                    else:
                        print('Not a valid choice. Try again')
                except ValueError:
                    print('Not a valid choice. Try again')

            # if 1. spin wheel and guess consonant    
            if player_input == 1:
                # spin_result, turn = spin_wheel()
                spin_result = spin_wheel()  
                # if wheel segment is a number
                if player_first_turn[current_player]:
                    guess_consonant()
                    player_first_turn[current_player] = False
            # if 2. guess the word
            elif player_input == 2:
                guess_word()
                player_first_turn[current_player] = False

        # if first turn is done and second or higher turn is happening
        while continues_turn[current_player] and not player_first_turn[current_player]:
            continue_only_vowels = only_vowels()

            #if word has more than vowels left
            if not continue_only_vowels:
                # display menu from player and prompt player to pick from 3 choices
                print(f'\nWhat does {current_player} want to do next?')
                print('(1) Buy a vowel')
                print('(2) Spin wheel to guess a consonant')
                print('(3) Guess the word \n')

                #validate input
                input_valid = False
                while not input_valid:
                    try:
                        player_input = int(input('Enter 1, 2, or 3: \n'))
                        if 1 <= player_input <= 3:
                            input_valid = True
                        else: 
                            print('Not a valid choice. Try again.')
                    except ValueError:
                        print('Not a valid choice. Try again.')

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
                print(f'There\'s only vowels left. {current_player} can only choose from 2 options below.')
                print('(1) Buy a vowel')
                print('(2) Guess the word')

                #validating input
                input_valid = False
                while not input_valid:
                    try:
                        player_input = int(input('Enter 1 or 2: \n'))
                        if 1 <= player_input <= 2:
                            input_valid = True
                        else:
                            print('Not a valid choice. Try again.')
                    except ValueError:
                        print('Not a valid choice. Try again.')

                # if 1. buy a vowel
                if player_input == 1:
                    buy_vowel()
                # if 2. guess the word
                elif player_input == 2:
                    guess_word()

        # only if the round is still going and it's the next player's turn
        if continues_round: 
            current_player = who_goes_next()
            continues_turn[current_player] = True


#to display word to show progress
def display_word():
    global word, guessed_right_list, word_display
    word_display = ''    
    for letter in word:
        if letter in guessed_right_list:
            word_display += letter
        else:
            word_display += '_'
    return word_display

#to spin wheel and get segment
def spin_wheel():
    global wheel, player_num_turn, player_first_turn, round_bank, continues_turn
    segment = random.choice(wheel)
    # segment = 'Bankruptcy'
    print(f'\nWheel is spinning... {current_player} landed on {segment}.\n')

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
    global guessed_right_list, word, current_player, spin_result, continues_turn, \
        word_display, continues_round, not_in_word_valid_guesses

    input_invalid = False
    while not input_invalid:
        guess = input('Enter a consonant:\n')
        if guess.isalpha():
            guess = guess.lower()
            input_invalid = True
        else: 
            print('Not a letter. Try again.')


    # if it's the player's first time
    if player_first_turn[current_player]:

        # if guess is already guessed and not a consonant
        if guess in guessed_right_list and not guess in consonant_list: 
            print(f'\nAlready guessed and not a consonant. {current_player} loses the turn.')
            continues_turn[current_player] = False

        # if guess is already guessed
        elif guess in guessed_right_list: 
            print(f'\nAlready guessed. {current_player} loses the turn.')
            continues_turn[current_player] = False
            
        # if guess is not a consonant
        elif not guess in consonant_list: 
            print(f'\nNot a consonant. {current_player} loses the turn.')
            continues_turn[current_player] = False       

        # if consonant is in word
        elif guess in word: 
            letter_count = 0
            for letter in word: 
                if guess == letter:
                    letter_count +=1
            guess_money = spin_result * letter_count
            guessed_right_list.append(guess) 
            display_word()
            print(f'\nYes. {guess} is in the word {letter_count} times.')
            print(f'{current_player} gets {guess_money}')
            #player gets $ to their round
            round_bank[current_player] += guess_money

            #check if word is complete to see if round is done
            if find_unrevealed_letters():
                round_is_done()            

        # if consonant is not in word          
        elif not guess in word:
            print(f'\nConsonant is not in word. {current_player} loses the turn.')
            continues_turn[current_player] = False

        #either way, first turn is done
        player_first_turn[current_player] = False


    #if not first turn
    elif not player_first_turn[current_player] and continues_turn[current_player]:

        # if guess is already guessed and not a consonant
        if guess in guessed_right_list and not guess in consonant_list: 
            print(f'\nAlready guessed and not a consonant. {current_player} loses the turn.')
            continues_turn[current_player] = False

        # if guess is already guessed
        elif guess in guessed_right_list: 
            print(f'\nAlready guessed. {current_player} loses the turn.')
            continues_turn[current_player] = False

        # if guess is not a consonant
        elif not guess in consonant_list: 
            print(f'\nNot a consonant. {current_player} loses the turn.')
            continues_turn[current_player] = False   

        # if consonant is in word
        elif guess in word: 
            letter_count = 0
            for letter in word: 
                if guess == letter:
                    letter_count +=1
            guess_money = spin_result * letter_count
            guessed_right_list.append(guess) 
            display_word()
            print(f'\nYes. {guess} is in the word {letter_count} times.')
            print(f'{current_player} gets ${guess_money}.')
            #player gets $ to their round
            round_bank[current_player] += guess_money 

            #check if word is complete to see if round is done
            if find_unrevealed_letters():
                round_is_done()

        # if consonant is not in word or invalid            
        elif guess not in word:
            print(f'Consonant is not in word. {current_player} loses the turn.')
            continues_turn[current_player] = False

    # add to list of letters guessed not in word
    if guess not in guessed_right_list and guess in consonant_list:
        not_in_word_valid_guesses.append(guess)

    #keeping only unique values - next time with more time

    #displaying information for players
    print(f'\nCurrent round total is {round_bank}')
    print(f'Previous valid guesses not in word are {not_in_word_valid_guesses}')       
    print(f'Current state of word is: {word_display}')  



#to buy a vowel
def buy_vowel():
    global round_bank, current_player, guessed_right_list, word, vowel_list, \
        word_display, continues_round, not_in_word_valid_guesses
    # check round money
    # if they don't have 250 in round money = back to menu    
    if round_bank[current_player] < 250:
        print(f'\n{current_player} does not have enough money from this round. ' +
        'Try spinning the wheel to guess a consonant or guess the word.')

    # if more than 250, prompt for guess
    elif round_bank[current_player] >= 250:
        
        #validate input
        input_invalid = False
        while not input_invalid:
            guess = input('Enter a vowel:\n')
            if guess.isalpha():
                guess = guess.lower()
                input_invalid = True
            else:
                print('Not a letter. Try again.')

        # if guess is already guessed and not a vowel
        if guess in guessed_right_list and not guess in consonant_list:
            print(f'Already guessed and not a vowel. {current_player} loses 250 and turn ends.')
        
        # if guess is already guessed
        elif guess in guessed_right_list:
            print(f'Already guessed. {current_player} loses 250 and turn ends.')
            round_bank[current_player] -= 250
            continues_turn[current_player] = False 
        
        # if guess is not a vowel
        elif not guess in vowel_list:
            print(f'Not a vowel. {current_player} loses 250 and turn ends.')
            round_bank[current_player] -= 250
            continues_turn[current_player] = False

        # if vowel is not in word                    
        elif not guess in word:
            print(f'Vowel is not in word. {current_player} loses 250 and turn ends.')
            round_bank[current_player] -= 250
            continues_turn[current_player] = False

        # if vowel is in word
        elif guess in word:
            # add letter to guessed_right_list
            guessed_right_list.append(guess)
            round_bank[current_player] -= 250
            # count how many times the vowel appears 
            letter_count = 0
            for letter in word: 
                if guess == letter:
                    letter_count +=1
            print(f'Yes. {guess} is in the word {letter_count} times.')
            print(f'250 is detracted. {current_player}\'s turn continues.')
            
            #check if word is complete to see if round is done
            if find_unrevealed_letters():
                round_is_done()

        # add to list of letters guessed not in word
        if guess not in guessed_right_list and guess in vowel_list:
            not_in_word_valid_guesses.append(guess)

    #keeping only unique values - next time if more time

    #displaying information for players
    print(f'\nCurrent round total is {round_bank}')
    print(f'Previous valid guesses not in word are {not_in_word_valid_guesses}')       
    print(f'Current state of word is: {word_display}')   

# guessing the word               
def guess_word():
    global round_bank, current_player, word, continues_round, continues_turn, player_first_turn
    player_input = input('Enter word guess:\n')
    print('\n')

    # if guess is word
    if player_input == word:
        round_is_done()

    # guess is not word, player lose turn
    else: 
        print(f'Not the word. {current_player} loses the turn.')
        player_first_turn[current_player] = False
        continues_turn[current_player] = False
        print(f'\nCurrent round total is {round_bank}')
        print(f'Previous valid guesses not in word are {not_in_word_valid_guesses}')       
        print(f'Current state of word is: {word_display}')       
        

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
    global guessed_right_list, word
    letters_left = ''
    for letter in word:
        if not letter in guessed_right_list:
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

#check is round is complete 
def round_is_done(): 
    global continues_round, round_bank, current_player, permanent_bank, player_first_turn,\
        continues_turn 
    #winning/current player gets to keep $
    permanent_bank[current_player] += round_bank[current_player]
    print(f'Round is done. {current_player} won this round.')
    print(f'The game total is {permanent_bank}\n')

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
    print(f'\nThe new player to go is {current_player}.')

    return current_player

#to time the guess and input of third round
def time_ran_out():
    global out_of_time, word
    out_of_time=True
    print('5 seconds are up. Press enter to end game.')

#to play third round
def play_third_round():
    global permanent_bank, guessed_right_list, word, consonant_list, vowel_list, out_of_time

    free_letters = 'rstlne'
    # ['r','s','t','l','n','e']

    third_round_prize = 50000

    final_player = 'Player 1'

    # highest_bank = max(permanent_bank.values())
    # for key, value in permanent_bank.items():
    #     if value == highest_bank:
    #         final_player = key
    print(f'The player for the final and third round is {final_player}.')

    #initialize list of already guessed letter 
    guessed_right_list = []

    # randomly pick word from list of words
    word = random.choice(word_list)
    show_free_letters = ''

    #append letter in free letter to show and list of guesses
    for letter in free_letters:
        show_free_letters += letter + ' '
        guessed_right_list.append(letter)

    #display both free letters and word with those letters shown
    print('\nWord is shown with these given letters:', show_free_letters)

    print('\nThe word is:', display_word(), '\n')

    #validate input
    input_invalid = True
    while input_invalid:
        print('You get 3 consonants and 1 vowel.')
        print('Enter them all at once, no spaces.')
        player_input = input('Here:\n').lower()

        consonant_count = 0
        vowel_count = 0
        repeat = 0
        for letter in player_input:
            #counting consonants and vowels and letters already given
            if letter in guessed_right_list:
                repeat += 1
            if letter in consonant_list:
                consonant_count += 1
            elif letter in vowel_list:
                vowel_count += 1

        #guesses are too short and include given letters
        if repeat >= 1 and len(player_input) < 4:
            print(f'Your guess is too short and include given letters. Those letters are {show_free_letters}. Do it again.')
        #if guess includes a given letter
        elif repeat >= 1:
            print(f'Your guess includes given letter. Those letters are {show_free_letters}. Do it again.')
        #guess is valid, proceed
        elif consonant_count == 3 and vowel_count == 1:
            print('Okay, let\'s see those letters in the word.')
            input_invalid = False
        #guess include characters and whatnot
        else: 
            print('Did you read the instruction? Do it again.')

    #successful input, add to already guessed
    for letter in player_input:
        guessed_right_list.append(letter)
    
    print('\nThe word is now:', display_word(), '\n')


    # while not out_of_time:
    timer = Timer(5, time_ran_out)
    timer.start() 
    player_guess = input('You have 5 seconds. Enter your guess: \n').lower() 

    #if player enter word too late but it's right
    if player_guess == word and out_of_time:  
        print('You ran out of time, but it is the word.')
    #if guess is word and were enter in time
    elif player_guess == word and not out_of_time: 
        print(f'Yes, you got it. You won your round money of ${permanent_bank[final_player]} and $50000.')
        total_prize = permanent_bank[final_player] + third_round_prize
        print(f'Congratulations. That\'s a total of ${total_prize}.')
    #if player enter word too late but it's wrong
    elif player_guess != word and out_of_time:
        print('Better luck next time.')
    #if they guessed the wrong in time
    else:
        print('Not the word. You lost.')
    
    print(f'\nThe word is {word}.')


print('Welcome to Wheel of Fortune. \n')
play_round()
print('Alright... Second round.\n')
play_round()
play_third_round()
print('\nThanks for playing Wheel of Fortune.')

