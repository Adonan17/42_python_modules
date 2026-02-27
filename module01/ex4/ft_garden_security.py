#!/usr/bin/env python3


class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self) -> None:
        return self.__height

    def get_age(self) -> None:
        return self.__age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print()
    height = rose.get_height()
    age = rose.get_age()
    print(f"Current plant: {rose.name} ({height}cm, {age} days)")


if __name__ == "__main__":
    ft_garden_security()
