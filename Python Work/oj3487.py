'''ติดตั้งหลอดไฟ'''
def main():
    '''ติดตั้งหลอดไฟ'''
    n = int(input())
    poles = [int(input()) for _ in range(n)]
    poles.sort()

    total_distance = 0
    prefix_sum = 0
    for pole in poles:
        prefix_sum += pole
        total_distance += prefix_sum * 2

    print(total_distance)

main()
