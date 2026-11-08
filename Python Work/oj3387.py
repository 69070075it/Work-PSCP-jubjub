'''Tuple's Sad Life'''
def main():
    '''Tuple's Sad Life'''
    data = tuple(input().split())
    target = input()

    idx = data.index(target)
    cnt = data.count(target)

    line = ' '.join([str(idx)]*cnt)
    for _ in range(cnt):
        print(line)
main()
