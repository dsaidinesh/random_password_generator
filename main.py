import secrets
import string

def generate_password(length=12):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each set
    password = [
        secrets.choice(uppercase_letters),
        secrets.choice(lowercase_letters),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]

    # Generate the remaining characters
    password.extend(secrets.choice(all_characters) for _ in range(length - 4))

    # Shuffle the characters to make the password more secure
    secrets.SystemRandom().shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def generate_multiple_passwords(num_passwords=5, length=12):
    return [generate_password(length) for _ in range(num_passwords)]

def main():
    print("Password Generator")

    try:
        # Get user input
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        # Generate passwords
        passwords = generate_multiple_passwords(num_passwords, length)

        # Display generated passwords
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print(f"{i}. {password}")

    except ValueError:
        print("Please enter valid numeric values for length and number of passwords.")

if __name__ == "__main__":
    main()
