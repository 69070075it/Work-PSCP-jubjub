"""tonmai"""
import math as m
def main():
    """tonmai"""
    thick, tar = map(int, input().split())
    count = 1
    floor = 0
    multiplier = 1
    while count <= tar:
        count += multiplier
        multiplier += 1
        floor += 1
    print(m.ceil(floor / thick))

main()
