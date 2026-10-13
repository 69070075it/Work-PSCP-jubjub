"""boxes"""
def main():
    """boxers"""
    w, l, r, a = map(int, input().split())
    lest = []
    for i in range(r, a + 1):
        f = w % i
        s = l % i
        lest.append(f * s)
    print(min(lest))

main()
