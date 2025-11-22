# 💾 Stardew Valley Cross-Platform Sync Utility

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg) 
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Overview & Core Value

The **Stardew Valley Cross-Platform Sync Utility** is a **Python CLI tool** designed for seamless, two-way save synchronization for your Stardew Valley farm between **PC (Windows)** and **Mobile (Android)** devices.

By leveraging **cloud services** (Google Drive, Dropbox, OneDrive) and **Directory Junctions**, this utility transforms a tedious manual transfer process into a simple, automated workflow. Play on PC, switch to mobile, and always resume from where you left off.

---

## 🛠️ How It Works: The Synchronization Bridge

The utility creates a **symlink bridge** between the game's default save location and your cloud drive, making your save files instantly accessible and writable by both platforms.

### PC (The Automation Step)
1.  **Backup & Move:** The utility **automatically moves** your existing `StardewValley/Saves` folder to a designated location within your chosen cloud service folder (e.g., `C:\Users\YourName\Google Drive\StardewSync`).
2.  **Create Junction:** The original save location (`%APPDATA%\StardewValley\Saves`) is replaced with a **Directory Junction** (a type of symbolic link) that points directly to the new cloud folder.
3.  **Result:** When Stardew Valley saves a game, it writes directly to the cloud folder, which your cloud app then syncs. 

### Mobile (The Manual Sync Step)
You use a third-party mobile sync application (e.g., FolderSync or Autosync) to create a **two-way sync job** between the mobile save location (`/storage/emulated/0/StardewValley/Saves/`) and the cloud folder created by this utility.

---

## ⚠️ Requirements & Critical Warnings

### Prerequisites
| Requirement | Detail |
| :--- | :--- |
| **PC OS** | **Windows** (7, 10, or 11) is currently supported. |
| **Python** | **Python 3.6 or newer** must be installed and accessible via your command line (`python --version`). |
| **Cloud App** | The **desktop client** for your chosen cloud service (Google Drive, Dropbox, etc.) must be installed and actively running. |
| **Mobile App** | A **third-party mobile two-way sync app** (e.g., [Autosync for Google Drive](https://play.google.com/store/apps/details?id=com.ttxapps.drivesync) or [FolderSync Pro](https://play.google.com/store/apps/details?id=dk.tacticalsolutions.foldersync.pro)) is required for the Android side. |

### Critical Warnings
* **Administrator Access is MANDATORY:** The Windows command used to create the symbolic link (`mklink /J`) requires elevated permissions. **You MUST run the command prompt or PowerShell session as Administrator.** The utility will prompt you to do this if not already elevated.
* **Existing Saves:** The utility will automatically **move** your existing save folder (`%APPDATA%\StardewValley\Saves`) to your chosen cloud location. **This action is necessary for setup and ensures no data is lost.**
* **Simultaneous Play:** **Do not play the game on both devices at the same time.** Wait for the save file to completely sync to the cloud *before* opening the game on the other platform.

---

## 🚀 Quick Start & Usage

### 1. Installation

Install the utility globally using Python's package installer, `pip`:

```bash
pip install stardew-sync-utility
