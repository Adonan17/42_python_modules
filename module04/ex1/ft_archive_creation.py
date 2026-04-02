#!/usr/bin/env python3


def main():
    try:
        file = open("new_discovery.txt", "w")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
        print()
        print("Initializing new storage unit: new_discovery.txt")
        print("Storage unit created successfully...")
        print()
        print("Inscribing preservation data...")
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("[ENTRY 001] New quantum algorithm discovered")
        print("[ENTRY 002] Efficiency increased by 347%")
        print("[ENTRY 003] Archived by Data Archivist trainee")
        print()
        file.close()
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
