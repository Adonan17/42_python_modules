#!/usr/bin/env python3


def secure_archive(
    filename: str,
    mode: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(filename, "r") as file:
                data = file.read()
                return (True, data)

        if mode == "write":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")

        return (False, "Invalid mode")

    except OSError as error:
        return (False, str(error))


def main():
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_fragment.txt", "write", result[1]))


if __name__ == "__main__":
    main()
