import requests
import json
import logging
from datetime import datetime, UTC
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GitHubAPIClient:
    def __init__(self):
        """Initialize the GitHub API client"""
        self.logger = logging.getLogger(__name__)
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
            "Accept": "application/vnd.github.v3+json"
        }
        
    def get_user_info(self):
        """Get information about the authenticated user"""
        response = requests.get(f"{self.base_url}/user", headers=self.headers)
        return response.json()
        
    def list_repositories(self, username=None):
        """List repositories for a user"""
        url = f"{self.base_url}/{'users/' + username if username else 'user'}/repos"
        response = requests.get(url, headers=self.headers)
        return response.json()
        
    def create_issue(self, owner, repo, title, body, labels=None, assignees=None):
        """Create a new issue in a repository"""
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        data = {
            "title": title,
            "body": body,
            "labels": labels or [],
            "assignees": assignees or []
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()
        
    def list_issues(self, owner, repo, state="open"):
        """List issues in a repository"""
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        params = {"state": state}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
        
    def create_pull_request(self, owner, repo, title, body, head, base="main"):
        """Create a new pull request"""
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls"
        data = {
            "title": title,
            "body": body,
            "head": head,
            "base": base
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

def main():
    # Initialize logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create client
    client = GitHubAPIClient()
    
    print("\nWelcome to the GitHub API Client!")
    print("Available commands:")
    print("1. user - Get your user information")
    print("2. repos [username] - List repositories")
    print("3. create_issue - Create a new issue")
    print("4. list_issues - List issues in a repository")
    print("5. create_pr - Create a pull request")
    print("6. exit - Exit the program")
    print("-" * 50)
    
    try:
        while True:
            # Get user input
            command = input("\nEnter command: ").strip().lower()
            
            if command == "exit":
                break
            elif command == "user":
                result = client.get_user_info()
                print("\nUser Information:")
                print(json.dumps(result, indent=2))
            elif command.startswith("repos"):
                parts = command.split()
                username = parts[1] if len(parts) > 1 else None
                result = client.list_repositories(username)
                print("\nRepositories:")
                print(json.dumps(result, indent=2))
            elif command == "create_issue":
                owner = input("Repository owner: ")
                repo = input("Repository name: ")
                title = input("Issue title: ")
                body = input("Issue body: ")
                result = client.create_issue(owner, repo, title, body)
                print("\nCreated Issue:")
                print(json.dumps(result, indent=2))
            elif command == "list_issues":
                owner = input("Repository owner: ")
                repo = input("Repository name: ")
                result = client.list_issues(owner, repo)
                print("\nIssues:")
                print(json.dumps(result, indent=2))
            elif command == "create_pr":
                owner = input("Repository owner: ")
                repo = input("Repository name: ")
                title = input("PR title: ")
                body = input("PR body: ")
                head = input("Head branch: ")
                result = client.create_pull_request(owner, repo, title, body, head)
                print("\nCreated Pull Request:")
                print(json.dumps(result, indent=2))
            else:
                print("Unknown command. Type 'help' to see available commands.")
            
    except KeyboardInterrupt:
        print("\nShutting down client...")
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main() 