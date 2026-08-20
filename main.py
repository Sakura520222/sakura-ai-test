#!/usr/bin/env python
"""
Sakura-AI Test Project - Main Entry Point
==========================================

This is the main entry point for the Sakura-AI test project.
It provides a simple demonstration of the Sakura-AI agent capabilities.
"""

import sys

__version__ = "0.1.0"
__author__ = "Sakura520222"

# Set UTF-8 encoding for console output (supports Windows)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


def main():
    """
    Main entry function for the Sakura-AI test application.
    """
    print("=" * 60)
    print("🌸 Sakura-AI Test Project")
    print("=" * 60)
    print()
    print("Version:", __version__)
    print("Author:", __author__)
    print()
    print("Welcome to Sakura-AI Test Project!")
    print("This project is created to test and demonstrate")
    print("the capabilities of Sakura-AI intelligent agents.")
    print()
    print("=" * 60)
    print()
    print("📋 Available Commands:")
    print("  - Run tests: pytest -v")
    print("  - Check code: ruff check .")
    print("  - Format code: ruff format .")
    print()
    print("📚 Documentation: See README.md for more information")
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
