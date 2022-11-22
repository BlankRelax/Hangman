word_to_guess = input("Enter a word to start").lower()
word_to_guess_a = []
for letter in word_to_guess:
    word_to_guess_a.append(letter)

guess_array = []
for i in range(0, len(word_to_guess)):
     guess_array.append("*")
print(guess_array)
lives = 10
while lives <11:
    letter_guess = input("Enter a letter to guess")


