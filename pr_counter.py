import os
import requests
from datetime import datetime
import argparse

# get your token from environment variables
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise Exception("GitHub token not specified. Please set the GITHUB_TOKEN environment variable.\n" \
                    "You can generate a new token by going to Settings -> Developer Settings -> Personal Access Tokens in your GitHub account. " \
                    "Check 'repo' scope while generating the token to grant necessary permissions.")

headers = {"Authorization": "Token " + token}

# parse command line arguments for date range
parser = argparse.ArgumentParser(description="Count PR contributors for a given date range.")
parser.add_argument("date_since", help="Start date for the range in YYYY-MM-DD format.")
parser.add_argument("date_until", help="End date for the range in YYYY-MM-DD format.")
args = parser.parse_args()

# convert the dates to datetime objects
date_since = datetime.strptime(args.date_since, '%Y-%m-%d')
date_until = datetime.strptime(args.date_until, '%Y-%m-%d')

# list of repos
repos = ["apache/pulsar"]

# global set of users
users = set()

# open a file to write PR URLs and authors
filename = "pr_info.txt"
with open(filename, "w") as file:
    for repo in repos:
        # request the data
        page = 1
        while True:
            url = f"https://api.github.com/repos/{repo}/pulls?state=all&sort=created&direction=desc&per_page=100&page={page}"
            response = requests.get(url, headers=headers)

            # check the status of the request
            if response.status_code == 200:
                data = response.json()
                if not data:  # if no more data, break the loop
                    break
                for pr in data:
                    created_at = datetime.strptime(pr['created_at'], '%Y-%m-%dT%H:%M:%SZ')
                    # if the PR is older than the start date, stop fetching
                    if created_at < date_since:
                        break
                    # check if the PR is within the date range
                    if date_since <= created_at <= date_until:
                        users.add(pr['user']['login'])
                        file.write(f"PR URL: {pr['html_url']} Author: {pr['user']['login']}\n")
                else:
                    page += 1  # move to the next page
                    continue
                break
            else:
                print(f"Failed to retrieve data for repository {repo}. Status Code:", response.status_code)
                break

print(f"The total number of unique people that submitted at least one pull request to any repository: {len(users)}")
print(f"The pull request details have been written to the file: {filename}")
