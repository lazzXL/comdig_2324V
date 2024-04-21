import random
from PIL import Image

"""
    Generates a random ASCII character.

    Returns:
        str: A random ASCII character.
"""
def generate_random_char():
    random_ascii = random.randint(0, 127)
    return chr(random_ascii)


"""
    Creates a cypher of the specified size and writes it to a file.

    Args:
        cypher_file (str): The file to write the cypher to.
        size (int): The size of the cypher to generate.

    Returns:
        str: The generated cypher.
"""
def create_cypher(cypher_file, size):
    # Generate a random cypher of the specified size
    cypher = ''.join(generate_random_char() for _ in range(size))

    # Write the cypher to a text file
    with open(cypher_file, "w") as f:
        f.write(cypher)

    return cypher


"""
    Encrypts an image using a cypher.

    Args:
        input_file (str): The path to the input image file.
        output_file (str): The path to save the encrypted image.
        cypher_file (str): The file containing the cipher.
        left (int): The left coordinate of the region to encrypt.
        upper (int): The upper coordinate of the region to encrypt.
        right (int): The right coordinate of the region to encrypt.
        lower (int): The lower coordinate of the region to encrypt.
"""
def encrypt_image(input_file, output_file, cypher_file, left, upper, right, lower):
    # Open an image
    img = Image.open(input_file)

    if img.mode == "P":
        img = img.convert("L")

    # Crop the specified region from the image
    region = img.crop((left, upper, right, lower))

    # Get pixel data of the cropped region
    pixels = region.load()

    # Get dimensions of the cropped region
    width, height = region.size

    # Create the cypher
    cypher = create_cypher(cypher_file, width * height)

    # Iterate over each pixel and perform XOR with cypher
    cypher_index = 0
    for y in range(height):
        for x in range(width):
            # Get pixel value(s) based on image mode
            pixel = pixels[x, y]
            if img.mode == "RGB":
                r, g, b = pixel
                # Perform XOR with cypher character for each component
                r ^= (ord(cypher[cypher_index]) * 2)
                g ^= (ord(cypher[cypher_index]) * 2)
                b ^= (ord(cypher[cypher_index]) * 2)
                # Update pixel values
                pixels[x, y] = (r, g, b)
            elif img.mode == "RGBA":
                r, g, b, a = pixel
                # Perform XOR with cypher character for each component
                r ^= (ord(cypher[cypher_index]) * 2)
                g ^= (ord(cypher[cypher_index]) * 2)
                b ^= (ord(cypher[cypher_index]) * 2)
                a ^= (ord(cypher[cypher_index]) * 2)
                # Update pixel values
                pixels[x, y] = (r, g, b, a)
            elif img.mode == "L":
                l = pixel
                # Perform XOR with cypher character for the single value
                l ^= (ord(cypher[cypher_index]) * 2)
                # Update pixel value
                pixels[x, y] = l
            # Move to the next character in the cypher
            cypher_index = (cypher_index + 1)

    # Paste the modified region back into the original image
    img.paste(region, (left, upper, right, lower))

    # Save the modified image
    img.save(output_file, quality=100, keep_rgb=1)


"""
    Decrypts an image using a cypher.

    Args:
        input_file (str): The path to the input image file.
        output_file (str): The path to save the decrypted image.
        cypher_file (str): The file containing the cypher.
        left (int): The left coordinate of the region to decrypt.
        upper (int): The upper coordinate of the region to decrypt.
        right (int): The right coordinate of the region to decrypt.
        lower (int): The lower coordinate of the region to decrypt.
"""
def decrypt_image(input_file, output_file, cypher_file, left, upper, right, lower):
    # Open the encrypted image
    img = Image.open(input_file)

    if img.mode == "P":
        img = img.convert("L")

    # Crop the region to decrypt
    region = img.crop((left, upper, right, lower))

    # Get pixel data of the cropped region
    pixels = region.load()

    # Get dimensions of the cropped region
    width, height = region.size

    # Read the cypher from the cypher file
    with open(cypher_file, "r") as f:
        cypher = f.read()

    # Decrypt the region using the same algorithm as encryption
    cypher_index = 0
    for y in range(height):
        for x in range(width):
            # Get pixel value(s) based on image mode
            pixel = pixels[x, y]
            if img.mode == "RGB":
                r, g, b = pixel
                # Perform XOR with cypher character for each component
                r ^= (ord(cypher[cypher_index]) * 2)
                g ^= (ord(cypher[cypher_index]) * 2)
                b ^= (ord(cypher[cypher_index]) * 2)
                # Update pixel values
                pixels[x, y] = (r, g, b)
            elif img.mode == "RGBA":
                r, g, b, a = pixel
                # Perform XOR with cypher character for each component
                r ^= (ord(cypher[cypher_index]) * 2)
                g ^= (ord(cypher[cypher_index]) * 2)
                b ^= (ord(cypher[cypher_index]) * 2)
                a ^= (ord(cypher[cypher_index]) * 2)
                # Update pixel values
                pixels[x, y] = (r, g, b, a)
            elif img.mode == "L":
                l = pixel
                # Perform XOR with cypher character for the single value
                l ^= (ord(cypher[cypher_index]) * 2)
                # Update pixel value
                pixels[x, y] = l
            # Move to the next character in the cypher
            cypher_index = (cypher_index + 1)

    # Paste the decrypted region back into the original image
    img.paste(region, (left, upper, right, lower))

    # Save the decrypted image
    img.save(output_file, quality=100, keep_rgb=1)


# Encrypt and decrypt examples:

# square.jpg
encrypt_image("resources/square.png", "cyphered_images/cyphered_square.png", "cyphers/encryption21.txt", 150, 0, 220, 71)
decrypt_image("cyphered_images/cyphered_square.png", "decyphered_images/decyphered_square.png", "cyphers/encryption21.txt", 150, 0, 220, 71)

# goldhill.bmp
encrypt_image("resources/goldhill.bmp", "cyphered_images/cyphered_goldhill.bmp", "cyphers/encryption31.txt", 0, 0, 200, 200)
decrypt_image("cyphered_images/cyphered_goldhill.bmp", "decyphered_images/decyphered_goldhill.bmp", "cyphers/encryption31.txt", 0, 0, 200, 200)

# bird.gif
encrypt_image("resources/bird.gif", "cyphered_images/cyphered_bird.gif", "cyphers/encryption1.txt", 0, 0, 100, 100)
decrypt_image("cyphered_images/cyphered_bird.gif", "decyphered_images/decyphered_bird.gif", "cyphers/encryption1.txt", 0, 0, 100, 100)

# barries.tif
encrypt_image("resources/barries.tif", "cyphered_images/cyphered_barries.tif", "cyphers/encryption2.txt", 256, 256, 512, 512)
decrypt_image("cyphered_images/cyphered_barries.tif", "decyphered_images/decyphered_barries.tif", "cyphers/encryption2.txt", 256, 256, 512, 512)

# lena.jpg
encrypt_image("resources/lena.jpg", "cyphered_images/cyphered_lena.jpg", "cyphers/encryption123456.txt", 85, 85, 150, 150)
decrypt_image("cyphered_images/cyphered_lena.jpg", "decyphered_images/decyphered_lena.jpg", "cyphers/encryption123456.txt", 85, 85, 150, 150)
