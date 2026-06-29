import os

# Project Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder Paths
SOURCE_FOLDER = os.path.join(BASE_DIR, "source_files")
BACKUP_FOLDER = os.path.join(BASE_DIR, "backups")
LOG_FOLDER = os.path.join(BASE_DIR, "logs")
REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

# Files
METADATA_FILE = os.path.join(BASE_DIR, "metadata.csv")
LOG_FILE = os.path.join(LOG_FOLDER, "backup.log")