import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_github_repo():
    """Create a new repository on GitHub"""
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN not found in .env file")
        return None
        
    print(f"Token loaded (first 10 chars): {token[:10]}...")
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    data = {
        'name': 'mcp',
        'description': 'GitHub MCP Integration',
        'private': False
    }
    
    response = requests.post(
        'https://api.github.com/user/repos',
        headers=headers,
        json=data
    )
    
    if response.status_code == 201:
        print("Repository created successfully!")
        print(f"Repository URL: {response.json()['html_url']}")
        return response.json()['clone_url']
    else:
        print(f"Error creating repository: {response.status_code}")
        print(response.json())
        return None

if __name__ == "__main__":
    repo_url = create_github_repo()
    if repo_url:
        print(f"\nYou can now push your code using:")
        print(f"git remote add origin {repo_url}")
        print("git branch -M main")
        print("git push -u origin main") 