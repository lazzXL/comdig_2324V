import random


"""
    Simulates a binary symmetric channel by introducing errors into a binary sequence.

    Args:
        sequence (str): The input binary sequence.
        error (float): The probability of bit flip/error.

    Returns:
        str: The noisy binary sequence after introducing errors.
"""
def binary_symmetric_channel(sequence, error):
    noisy_sequence = ""
    for bit in sequence:
        if random.random() < error:
            # Flip the bit with probability 'error'
            noisy_sequence += '0' if bit == '1' else '1'
        else:
            # Keep the bit unchanged
            noisy_sequence += bit
    return noisy_sequence


"""
    Simulates transmission over a binary symmetric channel with specified length and error probability.

    Args:
        length (int): The length of the binary sequence to transmit.
        error (float): The probability of bit flip/error.

    Prints:
        Prints the length of the sequence, expected BER, and actual BER.
"""
def simulate_transmission(length, error):
    # Generate random input sequence
    input_sequence = ''.join(random.choice('01') for _ in range(length))

    # Introduce noise using binary symmetric channel
    output_sequence = binary_symmetric_channel(input_sequence, error)

    # Calculate Bit Error Rate (BER)
    num_errors = sum(bit1 != bit2 for bit1, bit2 in zip(input_sequence, output_sequence))
    ber = num_errors / length

    print(f"Sequence Length: {length} bits")
    print(f"Expected BER (p): {error}")
    print(f"Actual BER: {ber}")
    print()


"""
    Simulates transmission of a file over a binary symmetric channel with specified error probability.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to save the output file.
        error (float): The probability of bit flip/error.

    Prints:
        Prints the number of different symbols between input and output files.
"""
def simulate_file_transmission(input_file, output_file, error):
    # Read input file
    with open(input_file, 'rb') as f:
        input_data = f.read()

    # Convert input data to binary sequence
    input_sequence = ''.join(format(byte, '08b') for byte in input_data)

    # Introduce noise using binary symmetric channel
    output_sequence = binary_symmetric_channel(input_sequence, error)

    # Convert output sequence back to bytes
    output_data = bytes(int(output_sequence[i:i + 8], 2) for i in range(0, len(output_sequence), 8))

    # Write output data to file
    with open(output_file, 'wb') as f:
        f.write(output_data)

    # Calculate the number of different symbols between input and output files
    num_different_symbols = sum(
        1 for byte_input, byte_output in zip(input_data, output_data) if byte_input != byte_output)

    print(f"Number of different symbols between the files: {num_different_symbols}")


# Simulate transmission of different lengths

dimensions = [1024, 10240, 102400, 1024000, 10240000]
error_probability = 0.01

for dimension in dimensions:
    simulate_transmission(dimension, error_probability)


# Simulate transmission of files with different errors
input_file_path = "alice29.txt"
print("Error:0.1")
simulate_file_transmission(input_file_path, "output0_1_file.txt", 0.1)
print("Error:0.01")
simulate_file_transmission(input_file_path, "output0_01_file.txt", 0.01)
print("Error:0.001")
simulate_file_transmission(input_file_path, "output0_001_file.txt", 0.001)
