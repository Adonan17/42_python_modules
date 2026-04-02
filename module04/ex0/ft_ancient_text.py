#!/usr/bin/env python3


def main():
    try:
        file = open("ancient_fragment.txt", "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    else:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print()
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        content = file.read()
        print(content, end="")
        print()
        file.close()
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
