'''นักล่าอสูร'''
def main():
    '''นักล่าอสูร'''
    demons = [
        ("Spider Demon", 1),
        ("Swamp Demon", 2),
        ("Arrow Demon", 1),
        ("Hand Demon", 2),
        ("Drum Demon", 3),
        ("Mugen Train", 2),
        ("Upper Moon", 3)
    ]

    total_attacks = 0
    kills = 0

    for name, secret in demons:
        if kills == 5:
            break

        print(name)

        is_killed = False
        for _ in range(3):
            attack = int(input())
            total_attacks += 1

            if attack == secret:
                print("kill")
                kills += 1
                is_killed = True
                break

        if not is_killed:
            print("back")

    print(total_attacks)

main()
