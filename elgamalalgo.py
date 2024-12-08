import random
from sympy import isprime, mod_inverse

def generate_prime():
    while True:
        candidate = random.getrandbits(8)  
        if isprime(candidate):
            return candidate
 
def find_generator(p):
    for g in range(2, p):
        powers = {pow(g, x, p) for x in range(1, p)}
        if len(powers) == p - 1:
            return g
    return None

def generate_keys():
    p = generate_prime()  
    g = find_generator(p)  
    x = random.randint(2, p - 2) 
    h= pow(g, x, p) 
    return p, g, x, h

def encrypt_message(message, public_key):
    p, g, h= public_key
    ciphertext = []
    for char in message:
        m = ord(char) 
        k = random.randint(2, p - 2)
        c1 = pow(g, k, p)
        c2 = (m * pow(h, k, p)) % p
        ciphertext.append((c1, c2))
    return ciphertext

def decrypt_message(ciphertext, private_key, p):
    decrypted_message = ""
    for c1, c2 in ciphertext:
        s = pow(c1, private_key, p)
        m = (c2 * mod_inverse(s, p)) % p 
        decrypted_message += chr(m)  
    return decrypted_message

def main():
    p, g, x, h= generate_keys()
    public_key = (p, g, h)
    private_key = x

    print(f"Generated Prime: {p}")
    print(f"Generated Generator: {g}")
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    while True:
        print("1. Encrypt/Decrypt a Message")
        print("2. Exit")
        choice = input("Choose an option (1/2): ")

        if choice == "1":
            message = input("Enter the text to encrypt: ")
            encrypted_message = encrypt_message(message, public_key)
            print("Encrypted Message:", encrypted_message)

            decrypt = input("Do you want to decrypt the message? (y/n): ").strip().lower()
            if decrypt == "y":
                decrypted_message = decrypt_message(encrypted_message, private_key, p)
                print("Decrypted Message:", decrypted_message)
            elif decrypt == "n":
                break
            else:
                print("Invalid option")
        elif choice == "2":
            print("exiting the program.")
            break
        else:
            print("Invalid option")


main()
