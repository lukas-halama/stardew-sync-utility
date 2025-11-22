# 💾 Stardew Valley Cross-Platform Sync Utility

## 🌟 Overview

The **Stardew Valley Cross-Platform Sync Utility** simplifies the process of synchronizing your Stardew Valley save files between **PC (Windows)** and **Mobile (Android/iOS)** via any third-party cloud service (Google Drive, Dropbox, OneDrive).

It automates the tedious, manual steps required on the PC side by automatically creating a **Directory Junction** (Windows' version of a symbolic link). This tricks the Stardew Valley PC game into reading and writing its saves directly to your cloud folder.

This tool handles the PC side of the automation. The mobile side requires a separate third-party sync app (details provided below).

## ⚠️ Requirements & Warnings

* **Operating System:** Currently supports **Windows**.
* **Permissions:** You **MUST** run this utility with **Administrator privileges** for the linking step to succeed.
* **Existing Saves:** The tool will automatically **move** your existing local save files to the designated cloud folder, ensuring no data loss.
* **Cloud Service:** You must have a cloud service desktop application (like Google Drive for Desktop) installed and running.

## 🚀 Quick Start & Installation

### 1. Installation

Install the utility directly from PyPI (once published) using `pip`:

```bash
pip install stardew-sync-utility
