'''กองชาม (จะลบ By TA)'''
def main():
    '''กองชาม (จะลบ By TA)'''
    n = int(input())
    x = [0] * 301
    for _ in range(n):
        num = int(input())
        x[num] += 1
    print(max(x))
main()
