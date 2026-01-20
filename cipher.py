def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    # If we are decrypting, we reverse the shift direction
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        # Check if it's an uppercase Letter
        if char.isupper():
            # Convert letter to number -> shift it -> wrap around Z to A -> back to letter
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if it's a lowercase Letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's a symbol or number, leave it alone
        else:
            result += char
    return result

def brute_force(text):
    print("\n--- HACKING IN PROGRESS ---")
    # Try every possible key from 1 to 26
    for attempt_key in range(1, 26):
        cracked_text = caesar_cipher(text, attempt_key, 'decrypt')
        print(f"Key {attempt_key}: {cracked_text}")

# Main Menu
print("--- Cyber Tool: Cipher & Breaker ---")
choice = input("Do you want to (E)ncrypt, (D)ecrypt, or (B)rute Force? ").upper()

if choice == 'B':
    message = input("Enter the secret message to hack: ")
    brute_force(message)
else:
    message = input("Enter your message: ")
    key = int(input("Enter shift key (e.g., 3): "))
    if choice == 'E':
        print(f"Result: {caesar_cipher(message, key, 'encrypt')}")
    elif choice == 'D':
        print(f"Result: {caesar_cipher(message, key, 'decrypt')}")
        