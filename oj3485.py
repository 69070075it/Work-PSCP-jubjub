'''รหัสต้องไม่ซ้ำกัน'''
def main():
    '''รหัสต้องไม่ซ้ำกัน'''
    _ = input()
    numbers = list(map(int, input().split()))

    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    unique_nums = [num for num, count in count_dict.items() if count == 1]

    unique_nums.sort()
    print(*unique_nums)

main()
