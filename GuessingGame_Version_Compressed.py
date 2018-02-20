while True:
		computerGuessMax, userInput = int(input('Please put in a maximum value for the game! ')), int(input("Pick a number ")); computerGuessMinimum, computerGuess, numGuesses = 1, 0, 0
		while computerGuess != userInput:
			import random; computerGuess = random.randint(computerGuessMinimum, computerGuessMax - 1); print("Is this your number? {}".format(computerGuess)); numGuesses +=1
			if computerGuess > userInput: computerGuessMax = computerGuess
			else: computerGuessMinimum = computerGuess + 1
		print('I got it right! Its {}! it took me {} guesses!'.format(computerGuess, numGuesses))
		while True:
			YesNo = input('Run again? (y/N): ')
			if YesNo in ('y', 'n', ''): break
		if YesNo == 'y': continue
		break
