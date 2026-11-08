'''[Recommend] Members'''
def main():
    '''[Recommend] Members'''
    a = list(input().split())
    b = list(input().split())
    set_a = set()
    set_b = set()
    for i in a:
        set_a.add(i)
    for j in b:
        set_b.add(j)
    same = set_a - set_b
    same = sorted(same)
    if not same:
        print('-')
    else:
        print(*same)
    total = len(set_a | set_b)
    print(total)
main()
