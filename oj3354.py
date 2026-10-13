'''Hint'''
def check(val, op, target):
    '''check'''
    if op == '==':
        return val == target
    if op == '!=':
        return val != target
    if op == '>':
        return val > target
    if op == '>=':
        return val >= target
    if op == '<':
        return val < target
    if op == '<=':
        return val <= target
    return False

def main():
    '''Hint'''
    a1, num1 = input().split()
    a2, num2 = input().split()
    a3, num3 = input().split()

    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    for i in range(1000):
        h = i // 100
        t = (i // 10) % 10
        u = i % 10

        cku = check(u, a1, num1)
        ckt = check(t, a2, num2)
        ckh = check(h, a3, num3)

        if cku and ckt and ckh:
            print(f'{i:03d}')
main()
