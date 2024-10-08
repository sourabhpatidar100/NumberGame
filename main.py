

from game_utils import game, leaderboard
from enroll_user import register , search_and_update_user


def main():
    start_game_input =input("Welcome to the game! Do you wanna start the game Press Y: ")
    if start_game_input in ['Y','y']:
        print("Welcome to Number guessing Game") 
        username=input("Please Enter Username: ")

        user = register(username)
        play_input =input("Play!  Press Y: ")
        if play_input in ['Y','y']:
            while True:
                score = game(user)
                print(f"Nice! You Score {score}")
                restart_input =input("Do you wanna play Again Press Y: ")
                if restart_input in ['Y','y']:
                    continue
                else:
                    break
        
        leaderboard_input =input("Do you wanna See leaderboard Press Y: ")
        if leaderboard_input in ['Y','y']:
            leaderboard() 
        else:
            print("Thanks For Playing Good Bye!")


    else:
        print("Ab mat aana vrna guddi Lal kr dunga! ")
    


if __name__ == "__main__":
   main()