from setuptools import setup, find_packages

setup(
    name="xcleaner",
    version="0.1.0",
    description="Delete all posts from your X (formerly Twitter) account.",
    author="Scott H. Collins",
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
    python_requires=">=3.7",
    include_package_data=True,
)