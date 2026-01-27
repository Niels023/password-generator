import secrets
import string
import time
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

try:
    how_many_characters = int(input("How many characters do you want your password to have? (numbers only): "))
    how_many_passwords = int(input("How many passwords do you want? (numbers only): "))
except ValueError:
    print("Error: You must type a number.")
    exit()

saved_passwords = []

print("\n--- Generated Passwords ---")

for i in range(how_many_passwords):
    password = generate_password(how_many_characters)
    saved_passwords.append(password)
    print(f"Password: {password}")

pyperclip.copy("\n".join(saved_passwords))
print("\nAll passwords copied to clipboard!")

print("Closing in:")
for i in range(10, 0, -1):
    print(f"{i}...", end='\r')
    time.sleep(1)
