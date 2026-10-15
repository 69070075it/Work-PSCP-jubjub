'''Muddled Menu'''
def main():
    '''Muddled Menu'''
    menu = []

    while True:
        line = input().strip()

        if line == "DONE":
            break
        if line == "CLOSED":
            menu.clear()
            return
        if line == "SOMETHING'S WRONG":
            menu.clear()
            continue
        if line.startswith("Can't do:"):
            dish = line.split("Can't do:", 1)[1].strip()
            while dish in menu:
                menu.remove(dish)
            continue

        if "#" in line:
            dish, pos = line.rsplit("#", 1)
            dish = dish.strip()
            pos = pos.strip()

            if dish in menu:
                menu.remove(dish)

            if pos == "N":
                menu.append(dish)
            else:
                idx = int(pos) - 1
                menu.insert(idx, dish)

    print(f"Full Course: {menu} Reversed: {menu[::-1]}")

main()
