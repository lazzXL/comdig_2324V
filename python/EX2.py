def arithmetic(n, u, r):
    print(u)
    while n > 0:
        u += r
        print(u)
        n -= 1


arithmetic(5, 1, 2)


def factorial(n):
    result = 1
    for i in range(n):
        result = result * (i + 1)

    print(result)


factorial(5)


def mmc(a, b):
    mul = a * b
    while b != 0:
        r = a % b
        a = b
        b = r

    result = mul / a
    print(result)


mmc(4, 8)


def prime(l, r):
    left = l
    while left <= r:
        if is_prime(left): print(left, " ")
        left += 1


def is_prime(num: int) -> bool:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


prime(1, 12)

from collections import Counter


def symbols_above_percentage(file_path, percentage):

    with open(file_path, 'r') as file:
        content = file.read()

    symbol_counts = Counter(content)

    total_symbols = sum(symbol_counts.values())

    symbol_percentages = {symbol: (count / total_symbols) * 100 for symbol, count in symbol_counts.items()}

    symbols_above_percentage = {symbol: freq for symbol, freq in symbol_percentages.items() if freq > percentage}

    return symbols_above_percentage


percentage = 40
symbols_above_percentage_dict = symbols_above_percentage("input2.txt", percentage)
print("Símbolos com frequência acima de", percentage, "%:")
for symbol, frequency in symbols_above_percentage_dict.items():
    print(f"Símbolo: {symbol}, Frequência: {frequency:.2f}%")

