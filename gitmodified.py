import sys
import os
from datetime import datetime

def get_commits_since_date(repo_path, since_date):
    print("Getting information about commits since " + since_date)
    # Change to the repository directory
    os.chdir(repo_path)
    
    # Build the git log command to retrieve commits since the specified date
    cmd = f'git log --name-status --since="{since_date}"'

    try:
        # Execute the command and read the output
        result = os.popen(cmd).read()
        # Call the function to parse the commits
        parse_commits(result)
    except Exception as e:
        # Print an error message if there is an issue with executing the git log command
        print(f"Error executing git log command: {e}")

def parse_commits(log_output):
    # Initialize a list to store parsed commits
    commits = []
    # Initialize a dictionary for the current commit
    current_commit = None
    info_commits = log_output.split('\n')
    # Iterate over the lines of the git log command output
    for line in info_commits:
        # If the line starts with 'commit', start a new commit
        if line.startswith('commit'):
            if current_commit:
                # Add the previous commit to the list of commits
                commits.append(current_commit)
            # Initialize a new dictionary for the current commit
            current_commit = {'modfiles': [], 'newfiles': [], 'delfiles':[], 'titlefiles':"", 'date':'', 'author':''}
        # If the line starts with 'M + space', assume it is a modified file and add it to the list
        elif line.startswith(' '):
            current_commit['titlefiles'] = line
        elif line.startswith('M\t'):
            modified_file = line
            current_commit['modfiles'].append(modified_file)
        # If the line starts with 'A + space', assume it is a new file and add it to the list
        elif line.startswith('A\t'):
            new_file = line
            current_commit['newfiles'].append(new_file)
        # If the line starts with 'D + space', assume it is a deleted file and add it to the list
        elif line.startswith('D\t'):
            del_file = line
            current_commit['delfiles'].append(del_file)
        elif line.startswith('Author:'):
            current_commit['author'] = line
        # If the line starts with 'Date:', extract the date and add it to the current commit dictionary
        elif line.startswith('Date:'):
            current_commit['date'] = line

    # Ensure the last commit is added to the list
    if current_commit:
        commits.append(current_commit)

    # Call the function to print the parsed information
    print_commits(commits)

def print_commits(commits):
    # Initialize lists to store modified files, avoiding duplicates
    modified_files_array = []
    new_files_array = []
    del_files_array = []
    
    info = []
    current_info = None

    # Iterate over the commits
    for commit in commits:
        if current_info:
            info.append(current_info)
        
        current_info = {'titlefile':commit['titlefiles'], 'date':commit['date'], 'author':commit['author']}
        
        # Get the list of modified files, excluding the first and last row
        modified_files = commit['modfiles']
        # If there are modified files, add them to the list, avoiding duplicates
        if modified_files:
            for idx, file in enumerate(modified_files, start=1):
                modified_files_array.append(file)
                
        new_files = commit['newfiles']
        # If there are new files, add them to the list, avoiding duplicates
        if new_files:
            for idx, file in enumerate(new_files, start=1):
                new_files_array.append(file)
                
        del_files = commit['delfiles']
        # If there are deleted files, add them to the list, avoiding duplicates
        if del_files:
            for idx, file in enumerate(del_files, start=1):
                del_files_array.append(file)
                
    # Convert the lists to sets to remove duplicates
    modified_files_array = sorted(set(modified_files_array))
    new_files_array = sorted(set(new_files_array))
    del_files_array = sorted(set(del_files_array))
    
    print("-"*40)
    print("Info:\n")
    
    for i in info:
        print("\t"+ " " +i['date'].split("   ")[1] + "\t" + i['author'].split(":")[1].split()[0] +  "\t" + i['titlefile'])
        
    print("-"*40)
    print("Modified:\n")
    
    # Print each modified file
    for modfile in modified_files_array:
        print("\t"+modfile.split()[1])
    
    print("-"*40)
    print("New:\n")
    for newfile in new_files_array:
        print("\t"+newfile.split()[1])
        
    print("-"*40)
    print("Deleted:\n")
    for delfile in del_files_array:
        print("\t"+delfile.split()[1])
        
    print("-"*40)

if __name__ == "__main__":
    # Check if the necessary arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python3 gitmodified.py <repository_path> <date_in_format_yyyy-mm-dd>")
        sys.exit(1)

    # Get the repository path and date from the command line
    repo_path = sys.argv[1]
    date_str = sys.argv[2]

    try:
        # Convert the provided date string to the correct format
        since_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        # Print an error message if the date format is incorrect
        print("Incorrect date format. It should be yyyy-mm-dd.")
        sys.exit(1)

    # Check if the repository path exists
    if not os.path.exists(repo_path):
        print(f"Repository directory not found at {repo_path}")
        sys.exit(1)

    # Call the function to retrieve and parse commits since the specified date
    get_commits_since_date(repo_path, since_date)
