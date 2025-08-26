# X_Cleaner

![Build Status](https://github.com/scotthcollins/X_Cleaner/actions/workflows/ci.yml/badge.svg?branch=main)
![PyPI](https://img.shields.io/pypi/v/xcleaner?color=blue)

## Author
Scott H. Collins  
[LinkedIn](https://www.linkedin.com/in/scott-h-collins)

## Versioning & Release Workflow

This project uses automated version bumping in CI. To ensure versions are always correct and PyPI uploads succeed:

1. **Do not manually edit the version in `xcleaner/__init__.py` or `setup.py`.**
2. After a successful PyPI release, always create and push a new git tag matching the released version:
	```sh
	git tag vX.Y.Z
	git push --tags
	```
	Replace `X.Y.Z` with the version you just released.
3. The CI workflow and `.github/bump_version.py` script will handle version bumps for future releases.

If you need to force a new version, create and push a new tag with the next version number.

## Installation from PyPI

You can install the latest release directly from PyPI:

```sh
pip install xcleaner
```

## Usage

After installing, you can use the CLI tool:

```sh
xcleaner --api-key <your_key> --api-secret-key <your_secret> --access-token <your_token> --access-token-secret <your_token_secret>
```

Or set your credentials as environment variables and simply run:

```sh
xcleaner
```

You can also delete posts from a JSON archive:

```sh
xcleaner --json path/to/posts.json [--api-key ...]
```



**Warning:** This script will permanently delete all posts from your account. Use with caution!

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



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.