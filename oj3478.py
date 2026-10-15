'''Easy Histogram'''
def main():
    '''Easy Histogram'''
    text = input()

    for i in range(ord('a'), ord('z') + 1):
        lower_char = chr(i)
        upper_char = chr(i).upper()

        count_lower = text.count(lower_char)
        if count_lower > 0:
            print(f"{lower_char} = {count_lower}")

        count_upper = text.count(upper_char)
        if count_upper > 0:
            print(f"{upper_char} = {count_upper}")
main()
