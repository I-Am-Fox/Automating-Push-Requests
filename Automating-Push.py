import subprocess
import os
import time

# Configuration
directory_name = input("Enter the directory to monitor for changes: ")
wait_time = int(input("Enter how long to wait between pushes (in minutes): ")) * 60  # Convert to seconds
commit_message = "Automated commit of changes"


# Ensure you have set up your PAT in an environment variable or SSH key for authentication
# For PAT, make sure the repository URL uses HTTPS and includes the PAT for authentication

def git_operations():
    try:
        # Change to the specified directory
        os.chdir(directory_name)

        # Check for changes (optional, could be implemented for efficiency)
        status_result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if status_result.stdout.strip() == "":
            print("No changes detected. Skipping commit and push.")
            return

        # Add all changes to git
        subprocess.check_call(['git', 'add', '.'])

        # Commit the changes
        subprocess.check_call(['git', 'commit', '-m', commit_message])

        # Push the changes
        subprocess.check_call(['git', 'push'])

        print(f"Changes pushed from {directory_name}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during git operations: {e}")


while True:
    git_operations()
    print(f"Waiting for {wait_time // 60} minutes before next operation.")
    time.sleep(wait_time)
