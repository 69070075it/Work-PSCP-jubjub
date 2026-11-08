'''นก'''
def main():
    '''นก'''
    n = int(input())
    trees = list(map(int, input().split()))

    if n == 1:
        print(1)
        return

    count = 0
    for i in range(n):
        if not i:
            if trees[i] > trees[i + 1]:
                count += 1
        elif i == n - 1:
            if trees[i] > trees[i - 1]:
                count += 1
        else:
            if trees[i] > trees[i - 1] and trees[i] > trees[i + 1]:
                count += 1

    print(count)

main()
