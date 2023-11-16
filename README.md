![version](https://img.shields.io/badge/version-v1.0.0-yellow.svg) ![author](https://img.shields.io/badge/author-lmcf-blue.svg)


# CHANGELOG GENERATOR
This Python script retrieves and presents Git commit information since a specified date. It analyzes a repository's commit history, identifying modified, new, and deleted files in each commit. The output includes commit details such as date, author, and a concise description commit. Developers can use this tool to track changes efficiently.

# Git Commit Analyzer: Quick Guide

The Git Commit Analyzer is a command-line tool for quickly obtaining insights into a Git repository's commit history. Follow these steps to use the tool:

## Install Dependencies:

Ensure you have Python installed on your system.
The script uses Git commands, so make sure Git is installed and accessible from the command line.

The provided Python script relies on the following standard libraries and tools, which are typically included with a standard Python installation:

- **sys**: Standard library module providing access to some variables used or maintained by the Python interpreter and functions that interact strongly with the interpreter.

- **os**: Standard library module providing a way of interacting with the operating system, including changing the current working directory.

- **datetime**: Standard library module for working with dates and times.

No external dependencies beyond these standard libraries are required for the script to function. However, it assumes that Git is installed on your system and accessible from the command line, as it leverages Git commands to gather commit information.

Ensure that Python and Git are installed on your system before using the script. If they are not installed, you can download and install them from the official websites:

Python: [Python Downloads](http://www.limni.net](https://www.python.org/downloads/)https://www.python.org/downloads/)

Git: [Git Downloads](http://www.limni.net](https://www.python.org/downloads/)https://www.python.org/downloads/](https://git-scm.com/downloads)https://git-scm.com/downloads)

## Clone or Navigate to Repository:
Clone a Git repository or navigate to an existing one using the command line.

## Usage:
- Open the command line in the repository's directory.
- Execute the script using the following command:

> python3 gitmodified.py <repository_path> <start_date>

Replace <repository_path> with the path to your Git repository and <start_date> with the desired start date in the format 'yyyy-mm-dd.'

# Review Output:

- The tool will display a summary of commits since the specified date.
- Information includes commit date, author, and a concise title.
- Modified, new, and deleted files are categorized for each commit.

# Interpret Results:

- Modified files are listed under "Modified."
- New files are listed under "New."
- Deleted files are listed under "Deleted."
- Additional commit information is displayed under "Info."

This tool streamlines the process of understanding changes in a Git repository, making it a valuable asset for developers tracking project evolution.

