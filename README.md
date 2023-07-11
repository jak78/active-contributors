# GitHub Active Contributors Counter

This Python script fetches data from a list of GitHub repositories and counts the number of unique contributors who submitted at least one pull request within a given date range. It also generates a text file with the URLs of the pull requests and the corresponding authors.

## Prerequisites

- Python 3.x
- `requests` library in Python
- GitHub Personal Access Token

## Installation

1. Clone this repository.
2. Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

# Usage

Before running the script, you must set the `GITHUB_TOKEN` environment variable to your 
GitHub Personal Access Token. You can generate a new token by going to 
**Settings -> Developer Settings -> Personal Access Tokens** in your GitHub account. 
Check the 'repo' scope while generating the token to grant necessary permissions.

To run the script, use the following command format:

```bash
python pr_counter.py YYYY-MM-DD YYYY-MM-DD
```

Replace `YYYY-MM-DD` with the start and end dates of the range for which you want to count contributors.

The script will print the total number of unique contributors and the name of a text file containing the URLs and authors of the pull requests.

# Example
To count the contributors from June 1, 2023, to June 28, 2023, use the following command:

```bash
python pr_counter.py 2023-06-01 2023-06-28
```

# Output

The script will print the total number of unique contributors and the name of a text file. 
This file contains the URL and author for each pull request made within the specified date range. 

Each line of the file represents one pull request and is formatted as follows:

```txt
PR URL: <url> Author: <author's GitHub username>
```

# Repositories list

To modify the list of repositories, you can simply update the `repos` variable in the script. 
This variable holds the list of repositories for which you want to count the number of unique contributors. 

# License
This project is licensed under the terms of the MIT license.

