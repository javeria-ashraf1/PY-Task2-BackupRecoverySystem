import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from config import SOURCE_FOLDER, BACKUP_FOLDER, METADATA_FILE, REPORT_FOLDER
from logger import write_log


# ===========================
# CREATE BACKUP
# ===========================
def create_backup():

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_path = os.path.join(BACKUP_FOLDER, timestamp)

    os.makedirs(backup_path, exist_ok=True)

    total_files = 0

    for file in os.listdir(SOURCE_FOLDER):

        source = os.path.join(SOURCE_FOLDER, file)
        destination = os.path.join(backup_path, file)

        if os.path.isfile(source):
            shutil.copy2(source, destination)
            total_files += 1

    metadata = pd.DataFrame([{
        "Backup Name": timestamp,
        "Files": total_files,
        "Backup Time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }])

    if os.path.exists(METADATA_FILE) and os.path.getsize(METADATA_FILE) > 0:
        metadata.to_csv(METADATA_FILE, mode="a", header=False, index=False)
    else:
        metadata.to_csv(METADATA_FILE, index=False)

    write_log(f"Backup Created : {timestamp}")

    print("\n================================")
    print("Backup Created Successfully!")
    print("================================")
    print("Backup Folder :", backup_path)
    print("Files Backed Up :", total_files)


# ===========================
# VIEW HISTORY
# ===========================
def view_backup_history():

    if not os.path.exists(METADATA_FILE) or os.path.getsize(METADATA_FILE) == 0:
        print("\nNo Backup History Found.")
        return

    data = pd.read_csv(METADATA_FILE)

    print("\n==============================================")
    print("             BACKUP HISTORY")
    print("==============================================")

    print(data.to_string(index=False))

    print("==============================================")


# ===========================
# REPORT
# ===========================
def generate_report():

    if not os.path.exists(METADATA_FILE) or os.path.getsize(METADATA_FILE) == 0:
        print("\nNo Backup Data Found.")
        return

    data = pd.read_csv(METADATA_FILE)

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    report_path = os.path.join(REPORT_FOLDER, "Backup_Report.csv")

    data.to_csv(report_path, index=False)

    print("\n========== BACKUP REPORT ==========")
    print(data.to_string(index=False))

    print("\nTotal Backups :", len(data))
    print("Total Files Backed Up :", data["Files"].sum())

    print("\nReport Saved At:")
    print(report_path)


# ===========================
# GRAPH
# ===========================
def show_statistics():

    if not os.path.exists(METADATA_FILE) or os.path.getsize(METADATA_FILE) == 0:
        print("\nNo Data Available.")
        return

    data = pd.read_csv(METADATA_FILE)

    plt.figure(figsize=(8,5))

    plt.bar(
        data["Backup Name"],
        data["Files"]
    )

    plt.title("Files per Backup")
    plt.xlabel("Backup")
    plt.ylabel("Files")

    plt.xticks(rotation=30)

    graph_path = os.path.join(REPORT_FOLDER, "Backup_Statistics.png")

    plt.tight_layout()

    plt.savefig(graph_path)

    plt.show()

    print("\nGraph Saved At:")
    print(graph_path)