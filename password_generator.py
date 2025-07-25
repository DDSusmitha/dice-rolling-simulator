import random
import string

def get_user_choice(prompt):
    choice = input(prompt + " (y/n): ").strip().lower()
    return choice == 'y'

def generate_password(length, use_letters, use_digits, use_symbols):
    chosen_sets = []
    password = []

    if use_letters:
        chosen_sets.append(string.ascii_letters)
        password.append(random.choice(string.ascii_letters))
    if use_digits:
        chosen_sets.append(string.digits)
        password.append(random.choice(string.digits))
    if use_symbols:
        chosen_sets.append(string.punctuation)
        password.append(random.choice(string.punctuation))

    if not chosen_sets:
        return "At least one character type must be selected!"

    all_characters = ''.join(chosen_sets)
    
    # Fill the rest of the password
    for _ in range(length - len(password)):
        password.append(random.choice(all_characters))
    
    random.shuffle(password)  # Shuffle to avoid predictable pattern
    return ''.join(password)

# ==== Main Program ====
try:
    print("🔐 Welcome to Unique Password Generator 🔐")
    length = int(input("Enter the desired password length (min 4): "))
    
    if length < 4:
        print("❌ Password length too short for strong password!")
    else:
        use_letters = get_user_choice("Include Letters (A-Z, a-z)?")
        use_digits = get_user_choice("Include Numbers (0-9)?")
        use_symbols = get_user_choice("Include Symbols (!, @, #, etc.)?")
        
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print("\n✅ Generated Secure Password:", password)
except ValueError:
    print("❌ Please enter a valid number.")
