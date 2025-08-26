
# X_Cleaner

Delete all posts from your X (formerly Twitter) account using a simple Python CLI.

## Features
- Delete all posts (tweets) from your X account using the X API
- Credentials via environment variables or command line arguments
- Supports deleting from JSON archive
- CLI and package usage

## Setup
1. **Clone the repository**
	```sh
	git clone https://github.com/yourusername/X_Cleaner.git
	cd X_Cleaner/x-delete-posts
	```
2. **Create and activate a virtual environment**
	```sh
	python -m venv .venv
	# On Windows:
	.venv\Scripts\activate
	# On macOS/Linux:
	source .venv/bin/activate
	```
3. **Install dependencies**
	```sh
	pip install -r requirements.txt
	```

## Usage

### Option 1: Using Environment Variables
```powershell
$env:X_API_KEY="your_api_key"
$env:X_API_SECRET_KEY="your_api_secret_key"
$env:X_ACCESS_TOKEN="your_access_token"
$env:X_ACCESS_TOKEN_SECRET="your_access_token_secret"
xcleaner
```

### Option 2: Using Command Line Arguments
```sh
xcleaner --api-key your_api_key --api-secret-key your_api_secret_key --access-token your_access_token --access-token-secret your_access_token_secret
```

### Option 3: Using JSON Archive
```sh
xcleaner --json path/to/posts.json [--api-key ...]
```

## Project Structure
```
x-delete-posts/
├── xcleaner/
│   ├── __init__.py
│   ├── authenticate_x.py
│   ├── delete_all_x_posts.py
│   └── main.py
├── tests/
│   └── test_*.py
├── requirements.txt
├── setup.py
└── README.md
```

## Author
Scott H. Collins  
[LinkedIn](https://www.linkedin.com/in/scotthcollins/)

## Warning
**This script will permanently delete all posts from your account. Use with caution!**

## License
MIT License