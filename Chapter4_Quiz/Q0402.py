word = input("Enter a word to check for palindrome: ")           # asking for input from the user
word = word.lower()                                              # change the letters to lowercase so that even a word contains uppercase letter, it would still check
if word == word[::-1]:                                           # reverses the letters in the word and check if they are the same
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
