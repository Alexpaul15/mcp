# MCP Server Integration

This repository contains the integration between MCP Server and GitHub, allowing for automated repository management and workflow automation.

## Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/mcp.git
cd mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
   - Copy `.env.template` to `.env`
   - Add your GitHub token and MCP server configuration

## Configuration

### GitHub Token
Create a GitHub Personal Access Token with the following permissions:
- `repo` (Full control of repositories)
- `workflow` (Update GitHub Action workflows)
- `write:packages` and `delete:packages` (Package management)

### MCP Server
Configure your MCP server settings in the `.env` file:
```
MCP_SERVER_URL=http://localhost:8000
MCP_SERVER_API_KEY=your_mcp_api_key_here
```

## Usage

1. Create a new repository:
```bash
python create_repo.py
```

2. Push your code:
```bash
git add .
git commit -m "Initial commit"
git push -u origin main
```

## Features

- Automated repository creation
- GitHub API integration
- MCP server connection
- Workflow automation
- Package management

## Security

- Never commit your `.env` file
- Keep your GitHub token secure
- Use environment variables for sensitive data

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 