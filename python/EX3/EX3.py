import math
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image


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
        if file_path.lower().endswith(('.png', '.jpg', '.tif', '.gif', 'bmp')):
            return
        else:
            with open(file_path, 'r') as file:
                content = file.read()
        all_symbols = []
        for symbol in content:
            all_symbols.append(symbol)
        entropia = 0
        all_symbols_freq = symbols_above_percentage(file_path,0)
        for chars, frequency in all_symbols_freq.items():
            freq = frequency / 100
            infprop = math.log(1 / freq, 2)
            print(f"informação própria de '{chars}' =", infprop)
            entropia += infprop * freq
        print("entropia=", entropia)
        plt.hist(all_symbols, 30)
        plt.title("Symbol Frequency")
        plt.xlabel("Symbol")
        plt.ylabel("Ocurrencies")
        plt.show()

    return 0


symbol_info(["a.txt", "alice29.txt", "arrays.kt", "barries.jpg", "barries.tif", "bird.gif", "cp.htm"])

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
