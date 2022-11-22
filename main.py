word_to_guess = input("Enter a word to start").lower()
word_to_guess_a = []
for letter in word_to_guess:
    word_to_guess_a.append(letter)

guess_array = []
for i in range(0, len(word_to_guess)):
     guess_array.append("*")
print(guess_array)
lives = 10
letters_guessed = 0
while lives >0:
    letter_guess = input("Enter a letter to guess")
    for i in range(0, len(word_to_guess_a)):
        if word_to_guess_a[i] == letter_guess:
            guess_array[i] = letter_guess
            letters_guessed+=1
    print(guess_array)
    lives -= 1
    if letters_guessed == len(word_to_guess_a):
        print("Well done, you guessed within your life span!")
        break
if lives <=0:
    print("The word was: " + word_to_guess)
    print("You got hanged")


