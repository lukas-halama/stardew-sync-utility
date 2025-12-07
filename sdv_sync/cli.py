# sdv_sync/cli.py

import os
import platform
import sys
from .linker import setup_sync

def main():
    """Main function for the command-line interface."""
    current_os = platform.system()
    
    # 1. Platform Check
    if current_os not in ["Windows", "Linux"]:
        print(f"This utility currently implies support for Windows and Linux. Detected: {current_os}")
        sys.exit(1)

    print("--- Stardew Valley Sync Utility Setup ---")
    
    # 2. Administrator Warning (Windows Only)
    if current_os == "Windows":
        print("⚠️ WARNING: This tool MUST be run with Administrator privileges (Right-click -> Run as administrator).")
        print("If you proceed without admin rights, the linking step will fail.")
    else:
        print(f"Running on {current_os}. Ensure you have write permissions for your home directory.")
        
    print("-" * 40)
    
    # 3. Get User Input for Cloud Path
    # Default paths suggestion
    if current_os == "Windows":
        default_cloud_suggestion = os.path.join(os.path.expanduser('~'), 'Google Drive')
    else:
        # Linux users often use generic locations or mounted drives
        default_cloud_suggestion = os.path.expanduser('~/Dropbox')

    cloud_path = input(f"Enter the ROOT path to your Cloud Sync folder (e.g., '{default_cloud_suggestion}'):\n> ")
    cloud_path = cloud_path.strip().strip('"').strip("'")
    
    # Handle home directory expansion (~) if user typed it
    cloud_path = os.path.expanduser(cloud_path)
    
    if not os.path.isdir(cloud_path):
        print(f"\n❌ Error: The path '{cloud_path}' does not appear to be a valid directory.")
        sys.exit(1)
        
    print(f"\nTarget Cloud Directory set to: {cloud_path}")
    
    # 4. Call the Core Logic
    setup_sync(cloud_path)

    print("\n-----------------------------------------------------")
    print(f"Sync Setup Complete ({current_os} Side).")
    print("Remember to configure the **Two-Way Sync** on your Android/Mobile device.")
    print("-----------------------------------------------------")

if __name__ == '__main__':
    main()
