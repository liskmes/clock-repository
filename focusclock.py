import time
import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def display_current_time():
    while True:
        current_time = time.strftime("%H:%M:%S")
        clear_screen()
        print("Current Time: ", current_time)
        time.sleep(1)

if __name__ == "__main__":
    display_current_time()
