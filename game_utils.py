import random
from cursor_object import cursor_obj, connection_obj

def game(username, number_of_attempts=4):
    random_number = random.randint(1, 10)  # Generate a new random number for each game
    iterator = 0
    score = 100
    deduction = score / number_of_attempts
    print(f"{username} is playing!")

    while iterator < number_of_attempts:
        try:
            user_input = int(input("Guess the number (1-10): "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        if user_input < 1 or user_input > 10:
            print("Invalid input. Please enter a number between 1 and 10.")
            iterator += 1
            continue
        elif user_input == random_number:
            print("Congratulations! You've guessed the number correctly.")
            break
        elif user_input < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        iterator += 1
        score -= deduction


    cursor_obj.execute("UPDATE users SET Score = ? WHERE username = ?", (score, username))
    connection_obj.commit()
    return score


def leaderboard():
    cursor_obj.execute("SELECT username,score FROM users LIMIT 3")
    results = cursor_obj.fetchall()
    
    if results:
        for row in results:
            print(row)
    else:
        print("No users found.")
    
    connection_obj.close()
