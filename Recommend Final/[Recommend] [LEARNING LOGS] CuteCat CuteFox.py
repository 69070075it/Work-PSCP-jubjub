"""CuteCat CuteFox"""
def main():
    """CuteCat CuteFox"""
    n = int(input())
    pets = {}
    for _ in range(n):
        text = input().strip("{}\n ")
        name, code = text.split(":")
        name = name.strip('" ')
        code = code.strip('" ')
        pets[name] = code
    codes = set(pets.values())
    if "Cat01" not in codes:
        pets["Garfield"] = "Cat01"
    if "Fox01" not in codes:
        pets["Fubuki"] = "Fox01"
    cats = []
    foxes = []
    for name, code in pets.items():
        if code.startswith("Cat"):
            num = int(code[3:])
            cats.append((num, name, code))
        elif code.startswith("Fox"):
            num = int(code[3:])
            foxes.append((num, name, code))
    cats.sort()
    foxes.sort()
    print(f"Cat : {len(cats)}")
    print(f"Fox : {len(foxes)}")
    for num, name, code in cats:
        print(f"{name} : {code}")
    for num, name, code in foxes:
        print(f"{name} : {code}")
main()
