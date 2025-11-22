import os
import subprocess
import shutil

# --- PATH FINDING ---
def get_stardew_default_path():
    """Returns the full path to the Stardew Valley 'Saves' directory on Windows."""
    # This resolves to C:\Users\YourName\AppData\Roaming
    appdata_path = os.getenv('APPDATA')
    if appdata_path:
        # Appends \StardewValley\Saves to the APPDATA path
        default_path = os.path.join(appdata_path, 'StardewValley', 'Saves')
        return default_path
    return None

# --- CORE LINKING FUNCTION ---
def create_windows_junction(default_path, cloud_path):
    """
    Creates a Windows Directory Junction (symbolic link).

    Args:
        default_path (str): The location where the game expects the saves (the link location).
        cloud_path (str): The actual location of the saves (the target).
    """
    # Windows command to create a Directory Junction.
    # Requires Administrator privileges.
    command = f'mklink /J "{default_path}" "{cloud_path}"'
    
    print(f"\nAttempting to create junction with command:\n{command}")
    
    try:
        # Use shell=True for mklink, as it's a shell built-in on Windows.
        # We assume the user runs the script as Administrator.
        subprocess.run(command, check=True, shell=True)
        print("\n✅ Success! The symbolic link has been created.")
        return True
    except subprocess.CalledProcessError as e:
        print("\n❌ Error during junction creation.")
        print("This usually means the script was NOT run with Administrator privileges.")
        print(f"Details: {e}")
        return False

# --- SETUP FUNCTION (to be called from cli.py) ---
def setup_windows_sync(cloud_directory):
    """Handles moving the old save and creating the new link."""
    default_path = get_stardew_default_path()

    if not default_path:
        print("Error: Could not find Windows AppData directory.")
        return

    # 1. Ensure the target cloud folder exists
    # The actual saves will live *inside* a 'Saves' folder in the cloud path
    cloud_saves_path = os.path.join(cloud_directory, 'Saves')
    os.makedirs(cloud_saves_path, exist_ok=True)

    if os.path.exists(default_path) and os.path.isdir(default_path):
        print(f"Found existing saves at: {default_path}")
        print(f"Moving existing saves to: {cloud_saves_path}")
        
        try:
            # 2. Move the existing 'Saves' folder to the cloud location
            shutil.move(default_path, cloud_directory)
            # The result of the move is the folder at the cloud_saves_path
            
            # 3. Create the junction link where the old folder used to be
            create_windows_junction(default_path, cloud_saves_path)
            
        except Exception as e:
            print(f"\nCritical Error during file move or link creation: {e}")
            print("Please check file permissions or run as Administrator.")
            
    else:
        # If no local saves exist, just create the link to the empty cloud folder
        print(f"No existing local saves found at {default_path}. Creating link directly.")
        create_windows_junction(default_path, cloud_saves_path)
