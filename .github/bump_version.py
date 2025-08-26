#!/usr/bin/env python3
"""
Bump the version in setup.py and xcleaner/__init__.py to the next patch version based on git tags.
"""
import re
import subprocess
from pathlib import Path

# Get latest tag (v0.1.0 if none)
def get_latest_version():
    """
    Return the latest version tag (by version order, not reachability).
    Falls back to '0.1.0' if no tags exist.
    """
    try:
        tag = subprocess.check_output(
            "git tag --list --sort=-v:refname | head -n1",
            shell=True,
            encoding='utf-8'
        ).strip()
        if tag.startswith('v'):
            tag = tag[1:]
        return tag if tag else '0.1.0'
    except subprocess.CalledProcessError:
        return '0.1.0'

def bump_patch(version):
    """
    Given a version string 'X.Y.Z', return the next patch version as a string.
    """
    major, minor, patch = map(int, version.split('.'))
    patch += 1
    return f"{major}.{minor}.{patch}"

def update_file_version(filepath, new_version):
    """
    Update the version string in the given file to new_version.
    Handles both setup.py and __init__.py version formats.
    Returns True if a version was updated, else False.
    """
    text = Path(filepath).read_text(encoding='utf-8')
    # setup.py: version="..."
    text, n = re.subn(r'version\s*=\s*[\'"]([0-9]+\.[0-9]+\.[0-9]+)[\'"]', f'version="{new_version}"', text)
    # __init__.py: __version__ = "..."
    text, m = re.subn(r'__version__\s*=\s*[\'"]([0-9]+\.[0-9]+\.[0-9]+)[\'"]', f'__version__ = "{new_version}"', text)
    Path(filepath).write_text(text, encoding='utf-8')
    return n or m

def get_code_version():
    """
    Extract and return the __version__ string from x-delete-posts/xcleaner/__init__.py.
    Returns None if not found.
    """
    init_path = Path('x-delete-posts/xcleaner/__init__.py')
    text = init_path.read_text(encoding='utf-8')
    m = re.search(r'__version__\s*=\s*[\"\']([0-9]+\.[0-9]+\.[0-9]+)[\"\']', text)
    if m:
        return m.group(1)
    return None

if __name__ == "__main__":
    latest = get_latest_version()
    code_version = get_code_version()
    if code_version is None:
        print("Could not find code version in __init__.py")
        exit(1)
    if code_version == latest:
        # Normal bump
        next_version = bump_patch(latest)
        print(f"Bumping version: {latest} -> {next_version}")
        updated = update_file_version('x-delete-posts/setup.py', next_version)
        updated_init = update_file_version('x-delete-posts/xcleaner/__init__.py', next_version)
        if not (updated or updated_init):
            print("No version string found to update.")
        else:
            print(f"Updated version to {next_version}")
    elif code_version > latest:
        print(f"Code version ({code_version}) is ahead of latest tag ({latest}). No bump needed.")
    else:
        # Code is behind, sync to tag
        print(f"Code version ({code_version}) is behind latest tag ({latest}). Syncing to tag version.")
        updated = update_file_version('x-delete-posts/setup.py', latest)
        updated_init = update_file_version('x-delete-posts/xcleaner/__init__.py', latest)
        if not (updated or updated_init):
            print("No version string found to update.")
        else:
            print(f"Updated version to {latest}")
