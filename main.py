"""
take user input and provide nato
phonetic alphabet code for each letter
"""

import pandas

data = pandas.read_csv(
    "C:/Users/tavish/Desktop/snek/Pandas & csv/NATO-alphabet/NATO-alphabet-start/nato_phonetic_alphabet.csv"
)
# ------------------------ create dictionary ----------------------------
# using dictionary comprehension using iterrows() method

data = pandas.DataFrame(data)
phoenetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# ------------------------ create input/output ---------------------------
# using list comprehension. new item is value for corresponding letter key


def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output = [phoenetic_dict[letter] for letter in word]

    except KeyError:
        print("Only letters of the alphabet, please")
        generate_phonetic()

    else:
        print(output)


generate_phonetic()
