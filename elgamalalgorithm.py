import random

def isprime(n):
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if n <= 3: # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0: # Eliminate multiples of 2 and 3
        return False
    i = 5
    while i * i <= n: # Check divisors from 5 to sqrt(n)
        if n % i == 0 or n % (i + 2) == 0: # Check if divisible by i or i + 2
            return False
        i += 6 # Skip even numbers and multiples of 3
    return True

def mod_inverse(a, m):
    m1, x1, x2 = m, 0, 1  #Initialize m1 as the original modulus, x1 and x2 for coefficients

    while a > 1: #loop untill a becomes 1
        q = a // m # Compute the quotient of a divided by m
        m, a = a % m, m # Update m and a (similar to the Euclidean algorithm)
        x1, x2 = x2 - q * x1, x1 # Update the coefficients x1 and x2 based on the quotient
    return x2 + m1 if x2 < 0 else x2  # Ensure the modular inverse is positive



# Generate a random prime number
def generate_prime():
    while True:
        candidate = random.getrandbits(16)  # Generate a random 16-bit number
        if isprime(candidate):  # Check if the number is prime
            return candidate  # Return the prime number

# Find a generator g for the prime p
def find_generator(p):
    for g in range(2, p):  # Iterate through potential generators
        powers = {pow(g, x, p) for x in range(1, p)}  # Compute powers of g mod p
        if len(powers) == p - 1:  # Verify if g produces all unique values when raised to powers mod p

            return g  # Return the generator
    return None  # Return None if no generator is found (unlikely for a prime)

# Generate public and private keys
def generate_keys():
    p = generate_prime()  # Generate a prime number
    g = find_generator(p)  # Find a generator for the prime
    x = random.randint(2, p - 2)  # Choose a random private key x
    h = pow(g, x, p)  # Compute h = g^x mod p (part of the public key)
    return p, g, x, h  # Return the prime, generator, private key, and public key component

# Encrypt a message using the public key
def encrypt_message(message, public_key):
    p, g, h = public_key  # Extract public key components
    ciphertext = []  # Initialize the ciphertext list
    for char in message:  # Encrypt each character in the message
        m = ord(char)  # Convert the character to its ASCII value
        k = random.randint(2, p - 2)  # Choose a random value k
        c1 = pow(g, k, p)  # Compute C1 = g^k mod p
        c2 = (m * pow(h, k, p)) % p  # Compute C2 = m * h^k mod p
        ciphertext.append((c1, c2))  # Append the pair (C1, C2) to the ciphertext
    return ciphertext  # Return the encrypted message as a list of tuples

# Decrypt a message using the private key
def decrypt_message(ciphertext, private_key, p):
    decrypted_message = ""  # Initialize the decrypted message
    for c1, c2 in ciphertext:  # Decrypt each pair (C1, C2)
        K = pow(c1, private_key, p)  # Compute K = C1^x mod p
        m = (c2 * mod_inverse(K, p)) % p  # Compute m = C2 * k^-1 mod p (modular inverse of K)
        decrypted_message += chr(m)  # Convert ASCII value back to character
    return decrypted_message  # Return the decrypted plaintext message

# Main function that combines all functions 
def main():
    # Generate public and private keys
    p, g, x, h = generate_keys()  # Generate keys
    public_key = (p, g, h)  # Combine the public key components
    private_key = x  # Store the private key

    # Display the generated keys
    print(f"Generated Prime: {p}")
    print(f"Generated Generator: {g}")
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Menu user interface
    while True:
        print("1. Encrypt/Decrypt a Message")
        print("2. Exit")
        choice = input("Choose an option (1/2): ")  # User input for menu choice

        if choice == "1":  # Encryption/Decryption option
            message = input("Enter the text to encrypt: ")  # Get plaintext message
            encrypted_message = encrypt_message(message, public_key)  # Encrypt the message
            print("Encrypted Message:", encrypted_message)

            # Ask if the user wants to decrypt the message
            decrypt = input("Do you want to decrypt the message? (y/n): ").strip().lower()
            if decrypt == "y":
                decrypted_message = decrypt_message(encrypted_message, private_key, p)  # Decrypt the message
                print("Decrypted Message:", decrypted_message)
            elif decrypt == "n":
                break  # Exit the encryption loop
            else:
                print("Invalid option")  # Handle invalid input
        elif choice == "2":  # Exit option
            break  # Exit the program
        else:
            print("Invalid option")  # Handle invalid menu choice

# Execute the main program
main()
