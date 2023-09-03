import os
import time
from resources.rename import rename_folders
from resources.DiscordTokens import token_grabber

def runner(base_folder):
    if not os.path.exists(base_folder):
        print(f"Error : '{base_folder}' does not exist")
        return
    else:
        rename_folders(os.path.join(base_folder))
        print("----Starting DIscord Token Grabber.---- ")
        time.sleep(5)
        token_grabber(base_folder ,os.path.join("data/DiscordTokens.txt"))
        print("----Starting ")
        time.sleep(5)
        


if __name__ == "__main__":
    base_folder = input("Enter base folder name ")
    runner(base_folder)
