import requests
import os

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
    
    api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {"Accept": "application/vnd.github.v3.raw"}
    
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded and saved to {save_path}")
    else:
        print(f"Error: {response.status_code}")

# Example usage:
owner = "Eletroman179"  # GitHub username
repo = "james-tool-redo"  # Repository name

# Download the "main.py" file and save it in the same directory as this script
download_github(owner, repo, "main.py", "main.py")

# If the user chooses to update/reset config.json, download it too
if input("Update/reset config.json? (yes/no)\n").strip().lower() == "yes":
    download_github(owner, repo, "config.json", "config.json")
