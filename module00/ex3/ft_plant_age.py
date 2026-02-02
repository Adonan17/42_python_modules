def ft_plant_age():
    days = input("Enter plant age in days: ")
    if int(days) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")


if __name__ == "__main__":
    ft_plant_age()
