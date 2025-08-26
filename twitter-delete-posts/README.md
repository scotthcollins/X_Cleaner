# Twitter Delete Posts

This project is a standalone Python script that allows users to delete all their Twitter posts. It utilizes the Twitter API to authenticate the user, retrieve their tweets, and delete them as needed.

## Project Structure

```
twitter-delete-posts
├── .gitignore
├── .venv/
├── delete_tweets.py
├── requirements.txt
└── README.md
```

## Requirements

Before running the script, ensure you have the following:

- Python 3.x installed on your machine.
- A Twitter Developer account and a project set up to obtain your API keys.

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd twitter-delete-posts
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open `delete_tweets.py` and enter your Twitter API credentials.
2. Run the script:

   ```bash
   python delete_tweets.py
   ```

**Warning:** This script will permanently delete all your tweets. Use with caution!