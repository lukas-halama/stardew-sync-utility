# 💾 Stardew Valley Cross-Platform Sync Utility

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey.svg)

## 🌟 Overview & Core Value

The **Stardew Valley Cross-Platform Sync Utility** is a **Python CLI tool** designed for seamless, two-way save synchronization for your Stardew Valley farm between **PC (Windows & Linux)** and **Mobile (Android)** devices.

By leveraging **cloud services** (Google Drive, Dropbox, OneDrive) and **Symbolic Links**, this utility transforms a tedious manual transfer process into a simple, automated workflow. Play on your PC, switch to mobile, and always resume from where you left off.

---

## 🛠️ How It Works: The Synchronization Bridge

The utility creates a **symlink bridge** between the game's default save location and your cloud drive, making your save files instantly accessible and writable by both platforms.

### PC (The Automation Step)
1.  **Backup & Move:** The utility **automatically moves** your existing save folder to a designated location within your chosen cloud service folder (e.g., `~/Dropbox/StardewSync` or `C:\Users\You\Google Drive\StardewSync`).
2.  **Create Link:** The original save location is replaced with a link that points directly to the new cloud folder.
    * **Windows:** Uses a **Directory Junction**.
    * **Linux:** Uses a standard **Symbolic Link**.
3.  **Result:** When Stardew Valley saves a game, it writes directly to the cloud folder, which your cloud app then syncs.

### Mobile (The Manual Sync Step)
You use a third-party mobile sync application (e.g., FolderSync or Autosync) to create a **two-way sync job** between the mobile save location (`/storage/emulated/0/StardewValley/Saves/`) and the cloud folder created by this utility.

---

## ⚠️ Requirements & Critical Warnings

### Prerequisites

| Requirement | Detail |
| :--- | :--- |
| **PC OS** | **Windows** (7, 10, 11) or **Linux** (Most distros). |
| **Python** | **Python 3.6 or newer** must be installed and accessible via your command line (`python --version`). |
| **Cloud App** | The **desktop client** or daemon for your chosen cloud service (Google Drive, Dropbox, etc.) must be installed and actively syncing. |
| **Mobile App** | A **third-party mobile two-way sync app** (e.g., [Autosync](https://play.google.com/store/apps/details?id=com.ttxapps.drivesync) or [FolderSync Pro](https://play.google.com/store/apps/details?id=dk.tacticalsolutions.foldersync.pro)) is required for the Android side. |

### Critical Warnings
* **Administrator Access (Windows Only):** On Windows, the command used to create the link (`mklink /J`) requires elevated permissions. **You MUST run the command prompt as Administrator.**
* **Linux Permissions:** On Linux, the tool usually runs with standard user permissions, as it modifies your home directory (`~/.config/StardewValley/Saves`).
* **Existing Saves:** The utility will **move** your existing save folder to your chosen cloud location. **This action is necessary for setup.**
* **Simultaneous Play:** **Do not play the game on both devices at the same time.** Wait for the save file to completely sync to the cloud *before* opening the game on the other platform.

---

## 🚀 Quick Start & Usage

### 1. Installation

Install the utility globally using `pip`:

bash
pip install stardew-sync-utility

### 2. Run the Setup Tool

* **Windows Users:** Open Command Prompt or PowerShell as **Administrator**.
* **Linux Users:** Open your standard terminal.

Run the following command and follow the on-screen prompts:

bash
sdv-sync-tool

📱 Mobile Setup (Android)

Once the PC setup is complete, configure your Android device:

    Install App: Download a sync app like Autosync or FolderSync.

    Connect: Link it to the same cloud account used on your PC.

    Create Pair: Create a Two-Way Sync pair with the following paths:

        Cloud Folder: The Saves folder inside your cloud drive (created by this tool).

        Local Device Folder: /storage/emulated/0/StardewValley/Saves/

    Sync: Enable "Instant Sync" if available, or manually sync before/after playing.

🤝 Contributing

Pull requests are welcome! If you find a bug or want to support Mac OS, feel free to open an issue or submit a PR.
📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
