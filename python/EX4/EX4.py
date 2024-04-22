import random
import string

import numpy as np


def generic_symbol_source(symbols, probabilities, length):
    if len(symbols) != len(probabilities):
        raise ValueError("Number of symbols and probabilities must match.")

    entropy_val = -np.sum(probabilities * np.log2(probabilities))
    print("Entropia da fonte:", entropy_val)

    sequence = np.random.choice(symbols, size=length, p=probabilities)
    print("Sequência gerada:", sequence)

    unique, counts = np.unique(sequence, return_counts=True)
    sequence_probabilities = counts / len(sequence)
    sequence_entropy = -np.sum(sequence_probabilities * np.log2(sequence_probabilities))
    print("Entropia da sequência gerada:", sequence_entropy)

    return sequence


# symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# probabilities = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
# generic_symbol_source(symbols, probabilities, 10)


def pin_generator():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    probs = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    random_size = random.randint(4, 6)
    res = generic_symbol_source(numbers, probs, random_size)
    return res


# for i in range(10):
#    print(pin_generator())


def keys_generator():
    numbers = [str(i + 1) for i in range(50)]
    num_probs = [0.02] * 50
    key_numbers = generic_symbol_source(numbers, num_probs, 5)
    stars = [str(i + 1) for i in range(12)]
    stars_prbs = [1 / 12] * 12
    key_stars = generic_symbol_source(stars, stars_prbs, 2)
    print("numbers: {}, stars: {}".format(key_numbers, key_stars))


# for i in range(10):
#    keys_generator()


def password_generator():
    symbols = list(string.printable)[:-6]
    props = [1 / len(symbols)] * len(symbols)
    random_size = random.randint(8, 12)
    res = generic_symbol_source(symbols, props, random_size)
    return ''.join(res)


for i in range(10):
    print(password_generator())


def thousand_pass():
    with open('output_file.txt', 'w') as file:
        for i in range(1000):
            file.write(password_generator() + '\n')


#thousand_pass()
#keys_generator
#print(pin_generator())












