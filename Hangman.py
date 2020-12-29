import random

# read all word from file words.txt

with open('words.txt','r') as f:
    words = f.readlines() 
words = [word[:-1] for word in words]
chances = 5
# print(words)
#Select a random word from all the words
selected_word = words[random.randint(0, len(words)-1)]
selected_word = [x for x in selected_word]
n = len(selected_word)
# print(selected_word)

print('[@] The word selected is of length {}'.format(n))
print('[@] Game Hangman start now...Start guessing')
print()
user_list = ['_' for x in range(n)]

def print_list(user_list):
    for x in user_list:
        print(x, end=" ")
    print()

while True:
    print('[@] Chance remaining - {}'.format(chances))
    # make user list and print
    print_list(user_list)
    user_char = input('[@] Guess the word: ')
    if len(user_char) != 1:
        print("1 character ka aukaat hai , kripya utne me hi rhe")
        continue
    if user_char in selected_word:
        for i in range(n):
            if selected_word[i] == user_char:
                user_list[i] = user_char
    else:
        chances -= 1

    if chances == 0:
        print('Game Over - You Lost...')
        break
    if '_' not in user_list:
        print('Game Over - You won...')
        break
    print()
