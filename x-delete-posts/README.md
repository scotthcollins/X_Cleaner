twitter-delete-posts

# X Delete Posts

This project is a standalone Python script that allows users to delete all their X (formerly Twitter) posts. It utilizes the X API to authenticate the user, retrieve their posts, and delete them as needed.

## Project Structure

```
x-delete-posts/
├── .venv/
├── authenticate_x.py
├── delete_all_x_posts.py
├── main.py
├── requirements.txt
└── README.md
```

## Requirements

Before running the script, ensure you have the following:

- Python 3.x installed on your machine.
- An X Developer account and a project set up to obtain your API keys.

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd x-delete-posts
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
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open `main.py` and enter your X API credentials, or provide them as environment variables or command line arguments.
2. Run the script:

   ```bash
   python main.py
   ```

**Warning:** This script will permanently delete all your posts. Use with caution!