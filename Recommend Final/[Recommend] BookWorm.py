'''[Recommend] BookWorm'''
def main():
    '''[Recommend] BookWorm'''
    n = int(input())
    ans = []
    for _ in range(n):
        total = 0
        count = 0
        time = float(input())
        book = int(input())
        book_time = []
        for _ in range(book):
            x = float(input())
            book_time.append(x)
        book_time.sort()
        for i in book_time:
            if total + i <= time:
                total += i
                count += 1
            else:
                break
        ans.append(count)
    for j in ans:
        print(j)
main()
