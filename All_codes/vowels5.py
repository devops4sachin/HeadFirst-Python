vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")

found = {}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'times.')

"""
In an attempt to remove the dictionary initialization code, we created “vowels5.py”,
which crashed with a runtime error (due to us failing to initialize the frequency counts).
"""
