'''[Recommend] 08.00 - B RNG'''
import json
def main():
    '''[Recommend] 08.00 - B RNG'''
    data = json.loads(input())
    n = int(input())
    s = int(input())
    max_sum = 0
    for i in range(256):
        path = []
        idx = i
        for _ in range(256):
            path.append(data[idx])
            idx = (idx + s) % 256
        total = sum(path) * (n // 256) + sum(path[:n % 256])
        if total > max_sum:
            max_sum = total
    print(max_sum)
main()
