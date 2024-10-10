from colorama import *
import progressbar
import keyboard
import platform
import shutil
import time as t
import json
import sys
import os

# Initialize Colorama
init(autoreset=True)

oldJt = Fore.LIGHTCYAN_EX + """
██████████████████████████████████████████████████████████████████████████████████████████
██""" + Fore.LIGHTYELLOW_EX + """                                                                                      """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """       ██  █████  ███    ███ ███████ ███████     ████████  ██████   ██████  ██        """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """       ██ ██   ██ ████  ████ ██      ██             ██    ██    ██ ██    ██ ██        """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """       ██ ███████ ██ ████ ██ █████   ███████        ██    ██    ██ ██    ██ ██        """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """  ██   ██ ██   ██ ██  ██  ██ ██           ██        ██    ██    ██ ██    ██ ██        """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """   █████  ██   ██ ██      ██ ███████ ███████        ██     ██████   ██████  ███████   """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """                                                                                      """ + Fore.LIGHTCYAN_EX + """██
██████████████████████████████████████████████████████████████████████████████████████████
"""

Jt = Fore.LIGHTCYAN_EX + """
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
██""" + Fore.LIGHTYELLOW_EX + """                                                                                                                                                         """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """                                                                                                                                                         """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """         ██████  ██████████████  ██████          ██████  ██████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████          """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """         ██████  ██████████████  ██████████████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████          """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """         ██████  ██████████████  ██████████████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████████████  ██████          """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """         ██████  ██████  ██████  ██████████████████████  ██████          ██████              ██████      ██████  ██████  ██████  ██████  ██████          """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """         ██████  ██████████████  ██████  ██████  ██████  ██████████████  ██████████████      ██████      ██████  ██████  ██████  ██████  ██████          """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """         ██████  ██████████████  ██████  ██████  ██████  ██████████████  ██████████████      ██████      ██████  ██████  ██████  ██████  ██████          """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """ ██████  ██████  ██████████████  ██████  ██████  ██████  ██████████████  ██████████████      ██████      ██████  ██████  ██████  ██████  ██████          """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """ ██████  ██████  ██████  ██████  ██████          ██████  ██████                  ██████      ██████      ██████  ██████  ██████  ██████  ██████          """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """ ██████████████  ██████  ██████  ██████          ██████  ██████████████  ██████████████      ██████      ██████████████  ██████████████  ██████████████  """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """ ██████████████  ██████  ██████  ██████          ██████  ██████████████  ██████████████      ██████      ██████████████  ██████████████  ██████████████  """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """ ██████████████  ██████  ██████  ██████          ██████  ██████████████  ██████████████      ██████      ██████████████  ██████████████  ██████████████  """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """                                                                                                                                                         """ + Fore.LIGHTCYAN_EX + """██
██""" + Fore.LIGHTYELLOW_EX + """                                                                                                                                                         """ + Fore.LIGHTCYAN_EX + """██
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""

Prompt = f"""
{platform.system()}@james-tool
↪ """

# Load configuration data
try:
    with open("config.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading configuration: {e}")
    sys.exit(1)

def load(sleep=0.03):
    left_B = Fore.LIGHTBLUE_EX + "[" + Fore.GREEN
    right_B = Fore.LIGHTBLUE_EX + "]" + Fore.GREEN
    bar = progressbar.Bar(marker='█',left=f'{left_B}{Fore.YELLOW}║',right=f'║{right_B}')
    widgets = [
        Fore.GREEN, ' ', left_B, 'Downloading', right_B, ' ', left_B, progressbar.Percentage(), Fore.GREEN, right_B,' ', Fore.YELLOW,
        bar,
        ' ', Fore.LIGHTRED_EX, '[',progressbar.AnimatedMarker(), ']', Fore.GREEN,
        ' ', left_B,'Download size: ', progressbar.DataSize(),
        right_B,'  ', left_B, progressbar.FileTransferSpeed(),
        right_B,'  ', left_B, progressbar.Timer(),
        right_B,'  ', left_B, progressbar.ETA(),right_B
    ]
    # Define the total number of steps
    total_steps = 100
    # Initialize the ProgressBar object with widgets
    progress = progressbar.ProgressBar(max_value=total_steps,widgets=widgets).start()

    # Simulate a task by updating the progress bar in a loop
    for i in range(total_steps):
        t.sleep(sleep)
        progress.update(i + 1)
        print(Fore.GREEN,end="\r")

    # Ensure the progress bar is properly finished
    progress.finish()
    print(Fore.RESET)

def clear(nom=True):
    global data
    os.system("cls" if platform.system() == "Windows" else "clear")
    if nom:
        if data["title"]["new_title"]:
            print(Jt)
        elif data["title"]["old_title"]:
            print(oldJt)


def flush_keyboard():
    print()
    prompt = ''
    inputStr = input(prompt).lower()
    print('\033[1A' + prompt + '\033[K')

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def set_background_color(hex_color):
    """Set the terminal background color using RGB values."""
    r, g, b = hex_to_rgb(hex_color)
    # ANSI escape code for RGB background
    escape_code = f"\033[48;2;{r};{g};{b}m"
    # Clear the entire screen and set background
    print(escape_code + ' ' * (shutil.get_terminal_size().columns * shutil.get_terminal_size().lines) + "\033[0m", end='')

def gradient_background(start_hex, end_hex, steps):
    """Create a gradient background from start_hex to end_hex over a specified number of steps."""
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)

    for step in range(steps + 1):
        # Interpolate between start and end colors
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * (step / steps))
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * (step / steps))
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * (step / steps))

        # Set background color
        set_background_color(f'#{r:02X}{g:02X}{b:02X}')
        t.sleep(0.1)  # Delay to see the gradient effect

def bang():
    clear()
    gradient_background('#FFFFFF', '#000000', steps=50)
    clear()

def YesNo(question="", default=1):
    print(question)
    scl = default
    scl_dis = f" {"[yes]" if scl == 1 else " yes "} {"[no]" if scl == 2 else " no "} "
    t.sleep(0.2)
    while True:
        scl_dis = f"\r {'[yes]' if scl == 1 else ' yes '} {'[no]' if scl == 2 else ' no '}"
        sys.stdout.write(scl_dis)
        sys.stdout.flush()  # Force immediate output

        if keyboard.is_pressed("left"):
            scl -= 1
            t.sleep(0.2)
        if keyboard.is_pressed("right"):
            scl += 1
            t.sleep(0.2)
        if keyboard.is_pressed("enter"):
            break

        if scl > 2:
            scl = 2
        if scl < 1:
            scl = 1
    flush_keyboard()
    return scl == 1

def JT_setup():
    title = YesNo(question="use old title?", default=2)
    if title:
        data["title"]["old_title"] = True
    else:
        data["title"]["new_title"] = True
def JT_restart():
    if YesNo(question="Are you sure?"):
        data = {
            "setup": False,
            "title": {
                "old_title": False,
                "new_title": False
            }
        }
        return data

def time():
    print(t.ctime())

commands = ["debug", "resetup", "cls or clear", "exec", "quit", "help", "time"]
bypass = False

def main():
    global data
    global bypass
    global commands
    if not data["setup"]:
        JT_setup()
        data["setup"] = True
    clear()
    while True:
        command = input(Prompt).strip().split(' ')
        if command[0] == "debug":
            bypass = True
            print("there is NO debug.")
        elif command[0] == "resetup":
            bypass = True
            data = JT_restart()
        elif command[0] == "help":
            bypass = True
            print(commands)
        elif command[0] == "cls" or command[0] == "clear":
            bypass = True
            clear()
        elif command[0] == "exec":
            bypass = True
            try:
                exec(command[1])
            except:
                pass
        elif not command[0]:
            bypass = True
            pass
        elif command[0] == "//" or command[0] == "quit" or command[0] == "exit":
            break
        if not bypass:
            if command[0] in commands:
                exec(f"{command[0]}()")
            else:
                print(f"'{command[0]}' is not recognized as an internal or external command.")
        bypass = False
if __name__ == "__main__":
    try:
        clear(nom=False)
        t.sleep(1)
        load()
        main()
        with open("config.json", "w") as file:
            json.dump(data, file, indent=4)
    except KeyboardInterrupt:
        print("\nProgram terminated.")
    