# Define the alphabet
ALPHABET = " abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)

# # Pre-defined keys
# PUBLIC_KEY = (65537, 119159)
# PRIVATE_KEY = (65539, 119159)
#
#
# # Write keys to files
# def write_keys_to_files(public_key_file="public_key.txt", private_key_file="private_key.txt"):
#     with open(public_key_file, "w") as pub_file:
#         pub_file.write(f"{PUBLIC_KEY[0]} {PUBLIC_KEY[1]}\n")
#     with open(private_key_file, "w") as priv_file:
#         priv_file.write(f"{PRIVATE_KEY[0]} {PRIVATE_KEY[1]}\n")
#     print(f"Keys written to '{public_key_file}' and '{private_key_file}'.")


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

# Example usage
if __name__ == "__main__":
    # Write the pre-defined keys to files
    #write_keys_to_files()

    # Read the keys from files
    public_key, private_key = read_keys_from_files()

    # Input plaintext
    plaintext = "test message"
    print("\nOriginal Plaintext:", plaintext)

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, public_key)
    print("Ciphertext (numeric):", ciphertext)
