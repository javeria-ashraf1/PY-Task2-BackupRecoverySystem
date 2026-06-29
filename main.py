from backup_manager import (
    create_backup,
    view_backup_history,
    generate_report,
    show_statistics
)

from recovery_manager import restore_backup


def menu():

    while True:

        print("\n" + "=" * 55)
        print("     AUTOMATED DATA BACKUP & RECOVERY SYSTEM")
        print("=" * 55)

        print("1. Create Backup")
        print("2. View Backup History")
        print("3. Restore Backup")
        print("4. Generate Report")
        print("5. Show Backup Statistics")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_backup()

        elif choice == "2":
            view_backup_history()

        elif choice == "3":
            restore_backup()

        elif choice == "4":
            generate_report()

        elif choice == "5":
            show_statistics()

        elif choice == "6":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid Choice! Please try again.")


if __name__ == "__main__":
    menu()