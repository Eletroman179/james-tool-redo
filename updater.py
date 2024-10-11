import os 
import requests
import time
import keyboard

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


def update():
    owner = "Eletroman179"  # GitHub username
    repo = "james-tool-redo"  # Repository name

    # Download the "main.py" file and save it in the same directory as this script
    updated = download_github(owner, repo, "main.py", "main.py")
    download_github(owner, repo, "main_run.py", "main_run.py")
    

    # Ask the user to update/reset config.json
    print("\rDo you want to update/reset 'config.json' [Y/N] [3]",end="\r")

    # Start a timer for 3 seconds
    start_time = time.time()
    wait_time = 3  # Wait for 3 seconds

    while True:
        # Check for keyboard input
        print(f"\rDo you want to update/reset 'config.json' [Y/N] [{str(int(time.time() - start_time + 1))}]",end="\r")
        if keyboard.is_pressed("y"):
            download_github(owner, repo, "config.json", "config.json")
            break
        if keyboard.is_pressed("n"):
            print("Update canceled.")
            break
        # Break the loop after 3 seconds
        if time.time() - start_time > wait_time:
            print("\nTime's up! No update will be made.")
            break
    if updated:
        pyautogui.press("up")
        pyautogui.press("enter")
        return True
update()