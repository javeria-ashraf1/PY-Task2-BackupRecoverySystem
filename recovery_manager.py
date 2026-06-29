import os
import shutil
import pandas as pd

from config import (
    BACKUP_FOLDER,
    SOURCE_FOLDER,
    METADATA_FILE
)

from logger import write_log


def restore_backup():

    if not os.path.exists(METADATA_FILE) or os.path.getsize(METADATA_FILE) == 0:
        print("\nNo backups available.")
        return

    data = pd.read_csv(METADATA_FILE)

    print("\n========== AVAILABLE BACKUPS ==========\n")

    for index, row in data.iterrows():

        print(f"{index + 1}. {row['Backup Name']}")

    try:

        choice = int(input("\nEnter Backup Number: "))

        if choice < 1 or choice > len(data):
            print("\nInvalid Backup Number.")
            return

        backup_name = data.iloc[choice - 1]["Backup Name"]

        backup_path = os.path.join(
            BACKUP_FOLDER,
            backup_name
        )

        if not os.path.exists(backup_path):
            print("\nBackup folder not found.")
            return

        restored_files = 0

        for file in os.listdir(backup_path):

            shutil.copy2(
                os.path.join(backup_path, file),
                os.path.join(SOURCE_FOLDER, file)
            )

            restored_files += 1

        write_log(f"Backup Restored : {backup_name}")

        print("\n=================================")
        print("Backup Restored Successfully!")
        print("=================================")
        print("Backup :", backup_name)
        print("Files Restored :", restored_files)

    except ValueError:

        print("\nPlease enter a valid number.")