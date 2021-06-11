def play():

    word = input('Player1: Please enter a lowercase word: ')
    letters = ''
    count = 0


    while count < 10:
        word_length = 0
        for i in word:
            if i in letters:
                print(i)
            else:
                print("_")
                word_length += 1


        if word_length == 0:
            print('Player2 wins!')
            print(f'The word is: {word}')
            break

        guess = input("player2: Enter a letter: ")
        letters += guess

        if guess not in word:
            count += 1
            print(f'You have guessed incorrectly {count}/10 time(s)!')
        if count == 10:
            print("You could not guess correctly!")
play()
