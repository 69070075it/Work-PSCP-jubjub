'''PSCP-P12'''
def main():
    '''PSCP-P12'''
    x, y = map(int, input().split())
    scores = {}
    w = []

    for _ in range(x):
        st_id, score = input().split()
        scores[st_id] = score
    for _ in range(y):
        want = input()
        w.append(want)
    for i in w:
        if i in scores:
            print(scores[i])
        else:
            print('NOT FOUND')
main()
