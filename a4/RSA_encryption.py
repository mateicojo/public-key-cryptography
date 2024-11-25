import random
from sympy import isprime

# Define the alphabet
ALPHABET = " abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)

# Function to generate RSA keys
def generate_keys():
    # Step 1: Select two large primes
    while True:
        p = random.randint(100, 999)  # Example small primes for simplicity
        if isprime(p):
            break
    while True:
        q = random.randint(100, 999)
        if isprime(q) and q != p:
            break

    # Step 2: Compute n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Step 3: Choose public exponent e
    e = 65537  # Common choice for public exponent

    # Step 4: Compute private exponent d
    d = pow(e, -1, phi_n)

    return (e, n), (d, n)

# Write keys to files
def write_keys_to_files(public_key, private_key, public_key_file="public_key.txt", private_key_file="private_key.txt"):
    with open(public_key_file, "w") as pub_file:
        pub_file.write(f"{public_key[0]} {public_key[1]}\n")
    with open(private_key_file, "w") as priv_file:
        priv_file.write(f"{private_key[0]} {private_key[1]}\n")
    print(f"Keys written to '{public_key_file}' and '{private_key_file}'.")

# Read keys from files
def read_keys_from_files(public_key_file="public_key.txt", private_key_file="private_key.txt"):
    with open(public_key_file, "r") as pub_file:
        e, n = map(int, pub_file.read().strip().split())
    with open(private_key_file, "r") as priv_file:
        d, n = map(int, priv_file.read().strip().split())
    return (e, n), (d, n)

# Function to convert text to numeric representation
def text_to_numeric(text):
    return [ALPHABET.index(char) for char in text]

# Function to convert numeric representation back to text
def numeric_to_text(numbers):
    return ''.join(ALPHABET[num] for num in numbers)

# Encryption function
def encrypt(plaintext, public_key):
    e, n = public_key
    plaintext = plaintext.lower()

    # Validate plaintext
    for char in plaintext:
        if char not in ALPHABET:
            raise ValueError(f"Invalid character '{char}' in plaintext.")

    # Convert text to numeric representation and encrypt each number
    numeric_plaintext = text_to_numeric(plaintext)
    numeric_ciphertext = [pow(num, e, n) for num in numeric_plaintext]
    return numeric_ciphertext

# Decryption function
def decrypt(ciphertext, private_key):
    d, n = private_key
    numeric_plaintext = [pow(num, d, n) for num in ciphertext]
    return numeric_to_text(numeric_plaintext)

# Example usage
if __name__ == "__main__":
    # Step 1: Generate keys
    public_key, private_key = generate_keys()

    # Step 2: Write keys to files
    write_keys_to_files(public_key, private_key)

    # Step 3: Read the keys from files
    public_key, private_key = read_keys_from_files()

    # Input plaintext
    plaintext = "test message"
    print("\nOriginal Plaintext:", plaintext)

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, public_key)
    print("Ciphertext (numeric):", ciphertext)

    # Decrypt the ciphertext
    decrypted_plaintext = decrypt(ciphertext, private_key)
    print("Decrypted Plaintext:", decrypted_plaintext)
