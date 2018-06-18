vowels = ['a','e','i','o','u']
word = input("Provide a word to search for vowels: ")

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'times.')

"""
“vowels6.py” fixed the runtime error thanks to the use of the “setdefault”
method, which comes with every dictionary (and assigns a default value to a key if a value isn’t already set).
"""
