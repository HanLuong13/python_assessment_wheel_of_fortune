import random

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
    global word, already_guessed_list, word_display, current_player, player_num_turn, \
        turn_bank, round_bank, player_first_turn, spin_result
    word = 'random'
    # initialize turn money to 0
    turn_bank = {}
    for player in player_list:
        turn_bank.setdefault(player, 0)
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


    round = True
    while round:

        while player_first_turn[current_player]:
            player_num_turn[current_player] += 1
            # spin_result, turn = spin_wheel()
            spin_result = spin_wheel()            
            # # if wheel segment is bankruptcy
            # if spin_result == 'Bankruptcy':
            #     # their turn ends & next player goes
            #     player_first_turn[current_player] = False
            # # if wheel segment is lose a turn
            # elif spin_result == 'Lose A Turn': 
            #     # their turn ends & next player goed
            #     player_first_turn[current_player] = False
            # # if wheel segment is a number
            if player_first_turn[current_player]:
                guess_consonant()
                # prompt them for consonant
                # validate consonant
                # guess = input('Please guess a consonant: ')
                # #if input is a consonant
                # if guess in consonant_list:
                #     # if consonant is in word
                #     if guess in word:
                        # count how many times the consonant appears 
                        # letter_count = 0
                        # for letter in word: 
                        #     if guess == letter:
                        #         letter_count +=1
                        # guess_money = spin_result * letter_count
                        # print(f'You got it. {guess} is in the word {letter_count} times.\n')
                        # print(f'You get {guess_money}')
                        # turn_bank[current_player] += guess_money
                        # print(turn_bank)
                        # add letter to already_guessed_list
                        # already_guessed_list.append(guess)
                        # display word
                        # print(display_word())
                        # give them money to their turn bank

                        # player_first_turn[current_player] = False
                    # if consonant is not in word
                    # their turn ends & next player goes
                    # elif not guess in word: 
                    #     print('Sorry. Consonant not in word. Next time!')
                    #     player_first_turn[current_player] = False
                #if input is not a consonant, lose turn
                # else:
                #     print('You didn\'t guess a consonant. You lose your turn.')
                #     player_first_turn[current_player] = False   

        # while round_bank[current_player] < 250:
            # player_num_turn[current_player] += 1
        #     print('What do you want to do next?')
        #     print('(1) Spin wheel to guess a consenant')
        #     print('(2) Guess the word')
        #     input_valid = False
        #     while not input_valid:
        #         try:
        #             player_input = int(input('Please enter 1, or 2 \n'))
        #             input_valid = True
        #         except ValueError:
        #             print('Please enter a valid choice.')
            


        # while continues_turn[current_player] and not player_first_turn[current_player]:
        #     player_num_turn[current_player] += 1
        #     # find out if word only have vowels left unrevealed 
        #     letters_left = ''
        #     for letter in word:
        #         if not letter in already_guessed_list:
        #             letters_left += letter

        #     count_consonants_left = 0
        #     for letter in letters_left:
        #         if letter in consonant_list:
        #             count_consonants_left += 1
        #     if count_consonants_left >= 1:
        #         continue_only_vowels = False
        #     else: 
        #         continue_only_vowels = True
        #     # print('count_consonants_left',count_consonants_left)
        #     # print('continue_only_vowels',continue_only_vowels)
        #     # print('letters_left',letters_left)     
        #     # print('word',word)

        #     #if word has more than vowels left
        #     if not continue_only_vowels:
        #         # display menu from player and prompt player to pick from 3 choices
        #         print('What do you want to do next?')
        #         print('(1) Buy a vowel')
        #         print('(2) Spin wheel to guess a consenant')
        #         print('(3) Guess the word')
        #         input_valid = False
        #         while not input_valid:
        #             try:
        #                 player_input = int(input('Please enter 1, 2, or 3 \n'))
        #                 input_valid = True
        #             except ValueError:
        #                 print('Please enter a valid choice.')

        #         #if 1. buy a vowel
        #         if player_input == 1:                                                               
        #             # check round money
        #             # if they don't have 250 in round money
        #             # back to menu
        #             current_bank = round_bank[current_player]
        #             if round_bank[current_player] <= 250:
        #                 print('You don\'t have enough money from this round.' +
        #                 'Try spinning the wheel to guess a consonant or guess the word.')
        #             # if more than 250, prompt for guess
        #             elif round_bank[current_player] > 250:
        #                 guess = input('Enter a vowel: ')
        #                 # if guess is not a vowel
        #                 if not guess in vowel_list:
        #                     print('Your guess is not a vowel. You lose 250. Your turn ends.')
        #                     round_bank[current_player] -= 250
        #                     continues_turn[current_player] = False
        #                 # if their guess is already guessed
        #                 elif guess in already_guessed_list:
        #                     print('Already guessed. You lose 250. Your turn ends.')
        #                     round_bank[current_player] -= 250
        #                     continues_turn[current_player] = False   
        #                 # if vowel is not in word                    
        #                 elif not guess in word:
        #                     print('Vowel not in word. You lose 250. Better luck next time!')
        #                     round_bank[current_player] -= 250
        #                     continues_turn[current_player] = False
        #                 # if vowel is in word
        #                 elif guess in word:
        #                     round_bank[current_player] -= 250
        #                     # count how many times the vowel appears 
        #                     letter_count = 0
        #                     for letter in word: 
        #                         if guess == letter:
        #                             letter_count +=1
        #                     guess_money = spin_result * letter_count
        #                     print(f'You got it. {guess} is in the word {letter_count} times.')
        #                     print('250 is detracted. Your turn continues!')
        #                     # add letter to already_guessed_list
        #                     already_guessed_list.append(guess)
        #         # if 2. spin the wheel to guess a consonant
        #         if player_input == 2:   
        #             spin_wheel()
        #             # if they land on $, they guess a consonant 
        #             if continues_turn[current_player]: 
        #                 print('')


        #     elif continue_only_vowels:
        #         print('Only vowels left.')
        #         break
        #     else:
        #         print('Something went wrong')
        #         break        
        

        # current_player = who_goes_next()
        # continues_turn[current_player] = True




        # count_consonants_left = 0
        # for letter in word_display:
        #     if letter in consonant_list:
        #         count_consonants_left += 1
        # if count_consonants_left >= 1:
        #     continue_only_vowels = False
        # else: 
        #     continue_only_vowels = True
        # #if word has more than vowels left
        # if not continue_only_vowels:
        #     print('Good to go.')
        #     break
        # elif continue_only_vowels:
        #     print('Only vowels left.')
        #     break
        # else:
        #     print('Something went wrong')
        #     break

def guess_consonant():
    global already_guessed_list, word, turn_bank, current_player, spin_result
    guess = input('Please guess a consonant: ')

    # if it's the player's first time
    if player_first_turn[current_player]:
        # if consonant in already guessed consonant list 
        if guess in already_guessed_list: 
            print('Already guessed. You lose a turn.')
            round_bank[current_player] += turn_bank[current_player]
            continues_turn[current_player] = False
        # if consonant is in word
        elif guess in word: 
            letter_count = 0
            for letter in word: 
                if guess == letter:
                    letter_count +=1
                    guess_money = spin_result * letter_count
                    already_guessed_list.append(guess) 
                    print(display_word())
                    print(f'You got it. {guess} is in the word {letter_count} times.\n')
                    print(f'You get {guess_money}')
                    turn_bank[current_player] += guess_money
                    print(turn_bank)   

        # if consonant is not in word or invalid            
        elif guess not in word:
            print('Letter not in word. You lose a turn')
            continues_turn[current_player] = False
        #if guess in invalid
        else:
            print('Not a valid input. You lose a turn')

    
    #if not first turn
    if not player_first_turn[current_player]:
        if guess in already_guessed_list: 
            print('Already guessed. You lose a turn.')
            round_bank[current_player] += turn_bank[current_player]
            continues_turn[current_player] = False
        # if consonant is in word
        elif guess in word: 
            letter_count = 0
            for letter in word: 
                if guess == letter:
                    letter_count +=1
                    guess_money = spin_result * letter_count
                    already_guessed_list.append(guess) 
                    print(display_word())
                    print(f'You got it. {guess} is in the word {letter_count} times.\n')
                    print(f'You get {guess_money}')
                    turn_bank[current_player] += guess_money
                    print(turn_bank)   

        # if consonant is not in word or invalid            
        elif guess not in word:
            print('Letter not in word. You lose a turn')
            round_bank[current_player] += turn_bank[current_player]
            turn_bank[current_player] = 0
            continues_turn[current_player] = False
        #if guess in invalid
        else:
            print('Not a valid input. You lose a turn')
            round_bank[current_player] += turn_bank[current_player]
            turn_bank[current_player] = 0
            continues_turn[current_player] = False    







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
    global wheel, player_num_turn, player_first_turn, round_bank, continues_turn, turn_bank
    segment = random.choice(wheel)

    print('Wheel is spinning... You landed on', segment, '\n')

    if player_first_turn[current_player] and segment == 'Bankruptcy':
        player_first_turn[current_player] = False
    elif player_first_turn[current_player] and segment == 'Lose A Turn': 
        player_first_turn[current_player] = False
    elif not player_first_turn[current_player] and segment == 'Bankruptcy':
        turn_bank[current_player] = 0
        continues_turn[current_player] = False
    elif not player_first_turn[current_player] and segment == 'Lose A Turn':
        round_bank[current_player] += turn_bank[current_player]
        turn_bank[current_player] = 0
        continues_turn[current_player] = False


    return segment
    # , turn

play_round()
# who_goes_next()
# print(current_player)