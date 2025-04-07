# MCP (Model Context Protocol) Integration

A Python-based implementation for interacting with GitHub's Model Context Protocol (MCP) server, providing seamless integration with GitHub's APIs and services.

## Overview

This project implements a client for GitHub's MCP server, enabling direct interaction with GitHub's APIs without requiring Docker or Go. It provides a simple command-line interface for common GitHub operations.

## Features

- Direct GitHub API integration
- Support for common GitHub operations:
  - User information retrieval
  - Repository management
  - Issue creation and management
  - Pull request creation and management
- Simple command-line interface
- Secure token-based authentication

## Prerequisites

- Python 3.8 or higher
- GitHub Personal Access Token with appropriate permissions
- Required Python packages:
  - requests
  - python-dotenv

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mcp.git
cd mcp
```

2. Install required packages:
```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project root with your GitHub token:
```
GITHUB_TOKEN=your_github_token_here
```

## Usage

1. Start the client:
```bash
python github_api_client.py
```

2. Available commands:
   - `user` - Get your GitHub account information
   - `repos [username]` - List repositories (optional username parameter)
   - `create_issue` - Create a new issue in a repository
   - `list_issues` - List issues in a repository
   - `create_pr` - Create a pull request
   - `exit` - Exit the program

## Example Usage

### Get User Information
```
Enter command: user
```

### List Repositories
```
Enter command: repos
```

### Create an Issue
```
Enter command: create_issue
Repository owner: your-username
Repository name: your-repo
Issue title: Bug Report
Issue body: Description of the issue
```

### Create a Pull Request
```
Enter command: create_pr
Repository owner: your-username
Repository name: your-repo
PR title: Feature Addition
PR body: Description of changes
Head branch: feature-branch
```

## Security

- Never commit your `.env` file or expose your GitHub token
- The token is stored securely in the `.env` file
- All API requests are made over HTTPS

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- GitHub API Documentation
- Model Context Protocol (MCP) Documentation 