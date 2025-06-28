def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # keep spaces and punctuation as-is
    return result


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid option. Please type 'encrypt' or 'decrypt'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    if choice == 'encrypt':
        result = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", result)


if __name__ == "__main__":
    main()



