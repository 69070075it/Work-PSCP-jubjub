'''กองชาม'''
def main():
    '''กองชาม'''
    n = int(input())
    count = {}

    for _ in range(n):
        x = int(input())

        if x in count:
            count[x] += 1
        else:
            count[x] = 1

    max_bowl = max(count.values())

    print(max_bowl)
main()
