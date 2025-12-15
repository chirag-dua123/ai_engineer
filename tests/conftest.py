"""
tests/conftest.py
Ensure project root is on sys.path so tests can import the package.
"""
import sys
from pathlib import Path

# Insert project root (one level above tests/) at the front of sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
