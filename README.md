# X_Cleaner

A standalone Python script to delete all posts (tweets) from your X (Twitter) account.

## Features

- Deletes all tweets from your account using the Twitter API.
- Credentials can be provided via environment variables or command line arguments.
- Simple and safe: validates credentials before running.

## Setup

1. **Clone the repository**  
	```sh
	git clone https://github.com/yourusername/X_Cleaner.git
	cd X_Cleaner/twitter-delete-posts
	```

2. **Create and activate a virtual environment**  
	```sh
	python -m venv .venv
	.venv\Scripts\activate
	```

3. **Install dependencies**  
	```sh
	pip install -r requirements.txt
	```

## Usage

### Option 1: Using Environment Variables

```powershell
$env:TWITTER_API_KEY="your_api_key"
$env:TWITTER_API_SECRET_KEY="your_api_secret_key"
$env:TWITTER_ACCESS_TOKEN="your_access_token"
$env:TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
python delete_tweets.py
```

### Option 2: Using Command Line Arguments

```sh
python delete_tweets.py --api-key your_api_key --api-secret-key your_api_secret_key --access-token your_access_token --access-token-secret your_access_token_secret
```

## Warning

**This script will permanently delete all tweets from your account. Use with caution!**

## License

MIT License