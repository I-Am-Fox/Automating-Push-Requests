import subprocess
import os
import time


def git_operations(directory_name):
    commit_message = "Automated commit of changes"
    try:
        # Change to the specified directory
        os.chdir(directory_name)

        # Check for changes by checking the status
        status_result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if status_result.stdout.strip() == "":
            print("No changes detected. Skipping commit and push.")
            return

        # Add all changes to git
        subprocess.run(['git', 'add', '.'], check=True)

        # Commit the changes
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        # Push the changes
        subprocess.run(['git', 'push'], check=True)

        print(f"Changes pushed from {directory_name}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during git operations: {e}")


def main():
    directory_name = input("Enter the directory to monitor for changes: ").strip('"')
    wait_time = int(input("Enter how long to wait between pushes (in minutes): ")) * 60  # Convert to seconds

    try:
        while True:
            git_operations(directory_name)
            print(f"Waiting for {wait_time // 60} minutes before next operation.")
            time.sleep(wait_time)
    except KeyboardInterrupt:
        print("\nExiting the program safely.")
        # Any cleanup can be done here before exiting
        exit(0)


if __name__ == "__main__":
    main()
