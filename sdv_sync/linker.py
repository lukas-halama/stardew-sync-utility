import os
import subprocess
import shutil
import platform

# --- PATH FINDING ---
def get_windows_stardew_path():
    """Returns the full path to the Stardew Valley 'Saves' directory on Windows."""
    appdata_path = os.getenv('APPDATA')
    if appdata_path:
        return os.path.join(appdata_path, 'StardewValley', 'Saves')
    return None

def get_linux_stardew_path():
    """Returns the full path to the Stardew Valley 'Saves' directory on Linux."""
    # Standard XDG config path for Stardew Valley
    home_path = os.path.expanduser('~')
    return os.path.join(home_path, '.config', 'StardewValley', 'Saves')

def get_stardew_default_path():
    """Dispatches to the correct path finder based on OS."""
    if platform.system() == "Windows":
        return get_windows_stardew_path()
    elif platform.system() == "Linux":
        return get_linux_stardew_path()
    return None

# --- CORE LINKING FUNCTION ---
def create_windows_junction(default_path, cloud_path):
    """Creates a Windows Directory Junction (symbolic link)."""
    command = f'mklink /J "{default_path}" "{cloud_path}"'
    print(f"\nAttempting to create junction with command:\n{command}")
    try:
        subprocess.run(command, check=True, shell=True)
        print("\n✅ Success! The symbolic link has been created.")
        return True
    except subprocess.CalledProcessError as e:
        print("\n❌ Error during junction creation.")
        print(f"Details: {e}")
        return False

def create_linux_symlink(default_path, cloud_path):
    """Creates a standard Linux symbolic link."""
    print(f"\nAttempting to create symlink: {default_path} -> {cloud_path}")
    try:
        # os.symlink(src, dst) creates a link pointing to src named dst
        os.symlink(cloud_path, default_path)
        print("\n✅ Success! The symbolic link has been created.")
        return True
    except OSError as e:
        print("\n❌ Error during symlink creation.")
        print(f"Details: {e}")
        return False

# --- SETUP FUNCTIONS ---
def setup_sync(cloud_directory):
    """Handles moving the old save and creating the new link for the current OS."""
    default_path = get_stardew_default_path()
    current_os = platform.system()

    if not default_path:
        print(f"Error: Could not determine Stardew Valley save path for {current_os}.")
        return

    # 1. Ensure the target cloud folder exists
    cloud_saves_path = os.path.join(cloud_directory, 'Saves')
    os.makedirs(cloud_saves_path, exist_ok=True)

    if os.path.exists(default_path):
        # If it's a directory (real saves), move it. If it's already a link, warn user.
        if os.path.islink(default_path):
            print(f"Found existing link at {default_path}. Skipping move/link step.")
            return

        print(f"Found existing saves at: {default_path}")
        print(f"Moving existing saves to: {cloud_saves_path}")
        
        try:
            # 2. Move the existing 'Saves' folder to the cloud location
            # Note: If destination exists, shutil.move behaves differently depending on impl.
            # We assume users want to merge or move to cloud.
            if not os.path.exists(os.path.join(cloud_directory, 'Saves', 'Saves')):
                 shutil.move(default_path, cloud_directory)
            else:
                 print("⚠️ Warning: 'Saves' folder already exists in cloud. Merging/Overwriting logic needed.")
                 # For safety in this snippet, we proceed to link if the move isn't critical
            
            # 3. Create the link
            if current_os == "Windows":
                create_windows_junction(default_path, cloud_saves_path)
            elif current_os == "Linux":
                create_linux_symlink(default_path, cloud_saves_path)
            
        except Exception as e:
            print(f"\nCritical Error during file move or link creation: {e}")
            
    else:
        # If no local saves exist, just create the link to the empty cloud folder
        print(f"No existing local saves found at {default_path}. Creating link directly.")
        if current_os == "Windows":
            create_windows_junction(default_path, cloud_saves_path)
        elif current_os == "Linux":
            create_linux_symlink(default_path, cloud_saves_path)
