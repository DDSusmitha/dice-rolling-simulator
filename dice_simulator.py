import random
import time

# Unicode symbols for dice faces
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

# Dictionary to track roll counts
roll_count = {i: 0 for i in range(1, 7)}

# File to save results
file_name = "dice_roll_history.txt"

def roll_dice():
    roll = random.randint(1, 6)
    roll_count[roll] += 1
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n🎲 You rolled a {roll} {dice_faces[roll]}")
    print(f"🕒 Time: {current_time}")
    
    # Save to file
    with open(file_name, "a") as f:
        f.write(f"{current_time} - Rolled: {roll} {dice_faces[roll]}\n")

while True:
    input("\nPress Enter to roll the dice... ")
    roll_dice()

    again = input("Do you want to roll again? (y/n): ").lower()
    if again != 'y':
        print("\n📊 Dice Roll Summary:")
        for face in range(1, 7):
            print(f"{face} {dice_faces[face]}: {roll_count[face]} times")
        
        print(f"\n📝 History saved to: {file_name}")
        print("👋 Thanks for playing!")
        break
