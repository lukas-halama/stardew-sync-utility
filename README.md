# ==============================================================================
# 1. FILE: README.md (Place in the root of your repository)
# ==============================================================================

# 💾 Stardew Valley Cross-Platform Sync Utility

## 🌟 Overview

The **Stardew Valley Cross-Platform Sync Utility** is a Python CLI tool designed to automate two-way save synchronization for your Stardew Valley farm between **PC (Windows)** and **Mobile (Android)** devices using any major cloud service (Google Drive, Dropbox, OneDrive).

### How It Works:
1.  **PC Side (Automation):** This utility automatically moves your existing Stardew Valley save files to a designated folder in your cloud service and replaces the original folder with a **Directory Junction** (a type of symbolic link). The game will then read and write its saves directly to your cloud folder.
2.  **Mobile Side (Manual Setup):** You use a third-party sync application to perform a two-way synchronization between the mobile save location and the cloud folder created by this utility.

---

## ⚠️ Requirements & Critical Warnings

### Prerequisites
| Requirement | Detail |
| :--- | :--- |
| **PC OS** | Windows (7, 10, or 11) is currently supported. |
| **Python** | Python 3.6 or newer must be installed and accessible via your command line. |
| **Cloud App** | The desktop client for your chosen cloud service (Google Drive, Dropbox, etc.) must be installed and actively running. |
| **Mobile App** | A third-party mobile two-way sync app (e.g., Autosync for Google Drive or FolderSync) is required for the mobile side. |

### Critical Warnings
* **Administrator Access is MANDATORY:** The Windows command used to create the symbolic link (`mklink /J`) requires elevated permissions. **You MUST run the command prompt or PowerShell session as Administrator.**
* **Existing Saves:** The utility will automatically **move** your existing save folder (`%APPDATA%\StardewValley\Saves`) to your chosen cloud location. This action ensures no data is lost and sets up the synchronization point.

---

## 🚀 Quick Start & Installation

### 1. Installation

Install the utility globally using Python's package installer, `pip` (once published to PyPI):

```bash
pip install stardew-sync-utility
