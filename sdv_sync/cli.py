# sdv_sync/cli.py

import os
import platform
import sys
from .linker import setup_windows_sync  # Import the function from linker.py

def main():
    """Main function for the command-line interface."""
    
    # 1. Platform Check (Ensure it's Windows)
    if platform.system() != "Windows":
        print("This utility currently only supports Windows for PC setup.")
        print("Exiting.")
        sys.exit(1)

    # 2. Check for Administrator Privileges (Crucial for mklink)
    # This check is complex to do perfectly cross-version in Python, 
    # but a simple subprocess check works in most modern Windows environments.
    # We will rely on the user running with admin, and if not, the linker.py will fail and inform the user.
    print("--- Stardew Valley Sync Utility Setup ---")
    print("⚠️ WARNING: This tool MUST be run with Administrator privileges (Right-click -> Run as administrator).")
    print("If you proceed without admin rights, the linking step will fail.")
    print("-" * 40)
    
    # 3. Get User Input for Cloud Path
    
    # Use os.path.expanduser('~') to offer a reasonable starting path
    default_cloud_path = os.path.join(os.path.expanduser('~'), 'Google Drive') 
    
    cloud_path = input(f"Enter the ROOT path to your Cloud Sync folder (e.g., '{default_cloud_path}'):\n> ")
    cloud_path = cloud_path.strip().strip('"').strip("'")
    
    if not os.path.isdir(cloud_path):
        print(f"\n❌ Error: The path '{cloud_path}' does not appear to be a valid directory.")
        print("Please ensure the path is correct and the cloud application is running.")
        sys.exit(1)
        
    print(f"\nTarget Cloud Directory set to: {cloud_path}")
    
    # 4. Call the Core Logic
    setup_windows_sync(cloud_path)

    print("\n-----------------------------------------------------")
    print("Sync Setup Complete (PC Side).")
    print("Remember to configure the **Two-Way Sync** on your Android/Mobile device.")
    print("-----------------------------------------------------")

if __name__ == '__main__':
    main()
