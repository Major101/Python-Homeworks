import emoji 
word = input("Input: ")
word_emojized = emoji.emojize(word, language='alias')

print(f'Output: {word_emojized}')