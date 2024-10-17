from colorama import *
import progressbar
import pyautogui
import requests
import keyboard
import platform
import shutil
import random
import runpy
import time
import json
import sys
import os

# init colorama
init(autoreset=True)

# Define the required packages
required_packages = [
    'colorama',
    'progressbar2',  # Note: Change to 'progressbar2' since 'progressbar' is often not available
    'pyautogui',
    'requests',
    'keyboard',
    'platform',
    'shutil',
    'runpy',
    'json'
]

# Function to check and install required packages
def install_packages():
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            py_install(package, '')

def py_install(install, enter=''):
    try:
        os.system(f"pip install {install}{enter}")
    except OSError:
        try:
            os.system(f"pip3 install {install}{enter}")
        except OSError:
            try:
                os.system(f"python -m pip install {install}{enter}")
            except OSError:
                try:
                    os.system(f"python -m pip3 install {install}{enter}")
                except OSError:
                    print("Fix your pip installation.")

# Initialize package installations
install_packages()

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

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path=path)

# Load configuration data
try:
    with open("config.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading configuration: {e}")
    sys.exit(1)

def download_github(owner, repo, path, save_filename):
        """
        Download a file from a GitHub repository using GitHub API.

        :param owner: GitHub username or organization name
        :param repo: Repository name
        :param path: Path to the file in the repository
        :param save_filename: Name to save the file locally
        """
        # Determine the save path relative to the current script's directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(current_dir, save_filename)

        # GitHub API URL to fetch the raw file contents
        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
        headers = {"Accept": "application/vnd.github.v3.raw"}  # Raw content header

        print(f"\nChecking '{path}' in GitHub repository '{owner}/{repo}'...")

        # Make the request to GitHub API
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Check if the file already exists locally
            if os.path.exists(save_path):
                with open(save_path, 'r', encoding='utf-8') as local_file:
                    local_content = local_file.read()
                    # Compare remote content with local content
                    if response.content == local_content.encode('utf-8'):
                        print("✅ The local file is up-to-date. No download needed.")
                        return  # Exit if the file is the same
                    else:
                        print("⚠️ The local file is outdated. Downloading new version...")
            else:
                print("📁 Local file does not exist. Downloading...")

            # Save the file locally if different or not present
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"\n✅ File downloaded and saved to: {save_path}\n")
            return True
        else:
            # Error message for failed download
            print(f"❌ Error: Unable to download the file (HTTP {response.status_code}).")
            print(f"Message: {response.text}")

def get_readme(owner, repo):
    """
    Get the README file from a GitHub repository.

    :param owner: GitHub username or organization name
    :param repo: Repository name
    """
    # API URL to fetch the version
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/version"
    headers = {"Accept": "application/vnd.github.v3.raw"}  # Raw content header

    # Make the request to the GitHub API
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        # Print the content of the version
        print("version")
        print(response.text)  # The content will be in Markdown format
    else:
        print(f"Error: Unable to fetch README (HTTP {response.status_code}).")

def update():
    owner = "Eletroman179"  # GitHub username
    repo = "james-tool-redo"  # Repository name

    # Download the "main.py" file and save it in the same directory as this script
    get_readme(owner, repo)
    updated = download_github(owner, repo, "main.py", "main.py")
    download_github(owner, repo, "main_run.py", "main_run.py")
    

    # Ask the user to update/reset config.json
    print("\rDo you want to update/reset 'config.json' [Y/N] [3]",end="\r")

    # Start a timer for 3 seconds
    start_time = time.time()
    wait_time = 3  # Wait for 3 seconds
    stop = False

    while True:
        # Check for keyboard input
        print(f"\rDo you want to update/reset 'config.json' [Y/S/N] [{str(int(time.time() - start_time + 1))}]",end="\r")
        if keyboard.is_pressed("y"):
            download_github(owner, repo, "config.json", "config.json")
            break
        if keyboard.is_pressed("n"):
            print("Update canceled.")
            break
        if keyboard.is_pressed("s"):
            stop = not stop
            time.sleep(1)
        # Break the loop after 3 seconds
        if time.time() - start_time > wait_time and not stop:
            print("\nTime's up! No update will be made.")
            break
    if updated:
        pyautogui.press("up")
        pyautogui.press("enter")
        return True

def load(sleep=0.03):
    left_B = Fore.LIGHTBLUE_EX + "[" + Fore.GREEN
    right_B = Fore.LIGHTBLUE_EX + "]" + Fore.GREEN
    bar = progressbar.Bar(marker='█', left=f'{left_B}{Fore.YELLOW}║', right=f'║{right_B}')
    widgets = [
        Fore.GREEN, ' ', left_B, 'Downloading', right_B, ' ', left_B, progressbar.Percentage(), Fore.GREEN, right_B, ' ', Fore.YELLOW,
        bar,
        ' ', Fore.LIGHTRED_EX, '[', progressbar.AnimatedMarker(), ']', Fore.GREEN,
        ' ', left_B, 'Download size: ', progressbar.DataSize(),
        right_B, '  ', left_B, progressbar.FileTransferSpeed(),
        right_B, '  ', left_B, progressbar.Timer(),
        right_B, '  ', left_B, progressbar.ETA(), right_B
    ]
    # Define the total number of steps
    total_steps = 100
    # Initialize the ProgressBar object with widgets
    progress = progressbar.ProgressBar(max_value=total_steps, widgets=widgets).start()

    # Simulate a task by updating the progress bar in a loop
    for i in range(total_steps):
        time.sleep(sleep)
        progress.update(i + 1)
        print(Fore.GREEN, end="\r")

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

def find_files(directory, extension=None):
    """Find files in a given directory with an optional file extension."""
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if extension is None or file.endswith(extension):
                found_files.append(os.path.join(root, file))
    return found_files

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
        time.sleep(0.05)  # Delay to see the gradient effect

def hak():
    x = 0.03
    print(Fore.GREEN)
    try:
        while True:
            print(Fore.GREEN)
            for i in range(random.randint(20, 100)):
                print(str(random.randint(0,1)), end="")
            if keyboard.is_pressed("esc"): break
            time.sleep(x)
    except:
        pass

def bang():
    clear(nom=False)
    set_background_color('#FFFFFF')
    time.sleep(2)
    gradient_background('#FFFFFF', '#000000', steps=50)
    clear()

def YesNo(question="", default=1):
    print(question)
    scl = default
    scl_dis = f" {"[yes]" if scl == 1 else " yes "} {"[no]" if scl == 2 else " no "} "
    time.sleep(0.2)
    while True:
        scl_dis = f"\r {'[yes]' if scl == 1 else ' yes '} {'[no]' if scl == 2 else ' no '} "
        sys.stdout.write(scl_dis)
        sys.stdout.flush()  # Force immediate output

        if keyboard.is_pressed("left"):
            scl -= 1
            time.sleep(0.2)
        if keyboard.is_pressed("right"):
            scl += 1
            time.sleep(0.2)
        if keyboard.is_pressed("enter"):
            break

        if scl > 2:
            scl = 2
        if scl < 1:
            scl = 1
    flush_keyboard()
    return scl == 1

def JT_setup():
    title = YesNo(question="Use old title?", default=2)
    if title:
        data["title"]["old_title"] = True
    else:
        data["title"]["new_title"] = True

def JT_restart():
    if YesNo(question="Are you sure?"):
        return {
            "setup": False,
            "title": {
                "old_title": False,
                "new_title": False
            }
        }

def file_updated(file_path, last_modified):
    current_modified = os.path.getmtime(file_path)
    return current_modified != last_modified

def bsod():
    from ctypes import windll
    from ctypes import c_int
    from ctypes import c_uint
    from ctypes import c_ulong
    from ctypes import POINTER
    from ctypes import byref

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(c_uint(19), c_uint(1), c_uint(0), byref(c_int()))

    windll.ntdll.NtRaiseHardError(c_ulong(0xC000007B), c_ulong(0),nullptr, nullptr, c_uint(6), byref(c_uint()))

def py_install(install, emter):
    try:
        os.system(f"pip install {install} {enter}")
    except OSError:
        try:
            os.system(f"pip3 install {install} {enter}")
        except OSError:
            try:
                os.system(f"python -m pip install {install} {enter}")
            except OSError:
                try:
                    os.system(f"python -m pip3 install {install} {enter}")
                except OSError:
                    print("fix your pip")
    

def debug():
    bang()

def code():
    # Read a file with specific encoding
    with open('main.py', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
    print(f"{"=" * len(__file__)}==")
    print(f" {__file__} ")
    print(f"{"=" * len(__file__)}==")
    
def help():
    print("Available commands:")
    print("- exec")
    print("- install")
    for cmd in commands.keys():
        print(f"- {cmd}")
    # Find Python files in the mods directory
    python_files = find_files("mods\\", ".py")
    if python_files:
        print("mods command:")

    for file in python_files:
        # Remove the "mods\\" prefix from each file path for display
        print(f"- {file.replace('mods\\', '').replace('.py', '')}")

# Define the commands dictionary correctly
commands = {
    "debug": debug,
    "resetup": JT_restart,
    "help": help,
    "cls": clear,
    "clear": clear,
    "time": lambda: print(time.ctime()),
    "bang": bang,
    "hak": hak,
    "code": code,
    "update": update,
}

file_path = 'main.py'
last_modified_time = os.path.getmtime(file_path)

def main():
    global data
    global bypass
    global last_modified_time 
    
    if not data["setup"]:
        JT_setup()
        data["setup"] = True

    clear()
    
    while True:
        command = input(Prompt).strip().split(' ', 3)
        if command[0] in ["//", "quit", "exit"]:
            break

        if command[0] in commands:
            commands[command[0]]()  # Call the command function directly
        elif command[0] == "exec" and not command[1]:
            pass
        elif command[0] == "exec" and command[1]:
            try:
                exec(command[1])  # Ensure you trust the input
            except Exception as e:
                print(f"Error executing command: {e}")
        elif command[0] == "install" and command[1]:
            py_install(command[1], command[2])
        elif command[0] == '':
            pass
        else:
            try:
                runpy.run_path(f"mods\\{command[0]}.py")
            except:
                print(f"'{command[0]}' is not recognized as an internal or external command.")

        # Check if the file has been updated
        if file_updated(file_path, last_modified_time):
            print("File updated, re-running...")
            pyautogui.press("up")
            pyautogui.press("enter")
            break

if __name__ == "__main__":
    try:
        clear(nom=False)
        if not update():
            load()
            main()
            with open("config.json", "w") as file:
                json.dump(data, file, indent=4)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program terminated.{Fore.RESET}")
