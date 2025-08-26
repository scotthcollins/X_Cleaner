from setuptools import setup, find_packages
import os

def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
        return f.read()

def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'xcleaner', '__init__.py')
    with open(version_file, encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
    raise RuntimeError('Unable to find version string.')

setup(
    name="xcleaner",
    version=get_version(),
    description="Delete all posts from your X (formerly Twitter) account.",
    long_description=readme(),
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