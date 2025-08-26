from setuptools import setup, find_packages
import os

def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(
    name="xcleaner",
    version="0.1.1",
    description="Delete all posts from your X (formerly Twitter) account.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Scott H. Collins",
    author_email="scotthcollins@outlook.com",
    url="https://www.linkedin.com/in/scotthcollins/",
    project_urls={
        "LinkedIn": "https://www.linkedin.com/in/scotthcollins/"
    },
    packages=find_packages(),
    install_requires=[
        "tweepy",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "xcleaner=xcleaner.main:main"
        ]
    },
    python_requires=">=3.11",
    include_package_data=True,
)