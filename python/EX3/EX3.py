import math
import matplotlib.pyplot as plt
from collections import Counter


def symbols_above_percentage(file_path, percentage):
    with open(file_path, 'r') as file:
        content = file.read()

    symbol_counts = Counter(content)

    total_symbols = sum(symbol_counts.values())

    symbol_percentages = {symbol: (count / total_symbols) * 100 for symbol, count in symbol_counts.items()}

    symbols_above_perc = {symbol: freq for symbol, freq in symbol_percentages.items() if freq > percentage}

    return symbols_above_perc


def symbol_info(list_of_file_path):
    for file_path in list_of_file_path:
        if file_path.lower().endswith(('.txt', '.kt', '.htm', "java", "c")):
            with open(file_path, 'r') as file:
                content = file.read()
        else:
            with open(file_path, 'rb') as file:
                content = file.read()
        all_symbols = list(content)
        entropia = 0
        count = Counter(content)
        freq = {}
        for char, char_count in count.items():
            freq = char_count / len(all_symbols)
            infprop = math.log2(1 / freq)
            print(f"informação própria de '{char}' =", infprop)
            entropia += infprop * freq

        print("entropia=", entropia)

        plt.hist(all_symbols, 30)
        plt.title("Symbol Frequency")
        plt.xlabel("Symbol")
        plt.ylabel("Occurrences")
        plt.show()

    return 0


symbol_info(["alice29.txt"])


def most_frequent_symbols(file_path):
    symbols_freq = symbols_above_percentage(file_path, 0)
    sorted_dict = dict(sorted(symbols_freq.items(), key=lambda item: item[1], reverse=True))
    first_five_items = dict(list(sorted_dict.items())[:5])
    print("Five most frequent symbols:")
    print(first_five_items)
    return first_five_items


#most_frequent_symbols("ListaPalavrasPT.txt")
#most_frequent_symbols("ListaPalavrasEN.txt")


def most_freq_symbols(file_path):
    pairs = []
    with open(file_path, 'r') as file:
        content = file.read()
    for i in range(0, len(content), 2):
        if i + 1 < len(content):
            pairs.append((content[i], content[i + 1]))
        else:  # Handling odd number of characters
            pairs.append((content[i], None))
    pair_counts = Counter(pairs)
    most_common_pairs = pair_counts.most_common()
    first_five_items = dict(list(most_common_pairs)[:5])
    print(first_five_items)
    return


#most_freq_symbols("ListaPalavrasPT.txt")
#most_freq_symbols("ListaPalavrasEN.txt")














'''''
with open(file_path, 'r') as file:
    content = file.read()
for chars in content:
    pairs.append(chars)

symbol_counter = Counter(content)
entropia = 0
total_symbols = sum(symbol_counter.values())

all_symbols = symbols_above_percentage(file_path, 0)

for symbol, frequency in all_symbols.items():
    freq = frequency.__round__() / 100
    print(f"Símbolo: {symbol}, Frequência: {frequency:.2f}%")
    times = (total_symbols * (freq / 100)).__round__()
    print(f"Símbolo: {symbol}, times: {times}")
    infprop = math.log(1 / freq, 2)
    entropia += infprop * freq

    # pairs.append((symbol, times))
    # symbols.append(symbol)
    # symbfreq.append(freq)

print(entropia)
print(pairs)
plt.hist(pairs, 30)

plt.title = 'okeoe'
plt.ylabel = 'freq'

plt.show()
'''''
