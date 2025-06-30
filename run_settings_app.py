#!/usr/bin/env python3
"""
Simple script to run the settings configuration app
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from settings_app.app import main
    if __name__ == "__main__":
        main()
except ImportError as e:
    print(f"Error importing required modules: {e}")
    print("Please make sure you have installed the required dependencies:")
    print("pip install slint-ui screeninfo")
    sys.exit(1)
except Exception as e:
    print(f"Error running the application: {e}")
    sys.exit(1)