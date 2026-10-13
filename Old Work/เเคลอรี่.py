'''เเคลอรี่'''
def main():
    '''เเคลอรี่'''
    total = 0
    cal_list = {
        1: 100,
        2: 120,
        3: 200,
        4: 60
    }
    while True:
        choose = int(input())
        if choose == 5:
            break
        if choose in cal_list:
            total += cal_list[choose]
    print('Bye Bye')
    print(f'Total Calories: {total}')
main()
