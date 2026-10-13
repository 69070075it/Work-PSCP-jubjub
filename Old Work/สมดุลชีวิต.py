"""ชีวิตนี้เลิกโสดเมื่อไหร่"""
def main():
    """workerjerker"""
    tiarm = int(input())
    lest = [int(input()) for _ in range(tiarm)]
    less = []
    more = []
    for word in lest:
        if word <= 18:
            less.append(word)
        else:
            more.append(word)
    print(tiarm + max(0, len(more) - len(less) - 1))

main()
