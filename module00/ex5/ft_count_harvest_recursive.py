def ft_count_harvest_recursive(days, i=1):
    if i > days:
        return
    print(f"Day {i}")
    ft_count_harvest_recursive(days, i + 1)


if __name__ == "__main__":
    days = int(input("Days until harvest: "))
    ft_count_harvest_recursive(days)
