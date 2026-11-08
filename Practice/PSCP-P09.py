'''PSCP-P09'''
def main():
    '''PSCP-P09'''
    n = int(input())
    all_num = []

    while len(all_num) < n - 1:
        line = input().split()
        for item in line:
            all_num.append(int(item))
    num = set(all_num)

    for i in range(1, n+1):
        if i not in num:
            print(i)
            break
main()
