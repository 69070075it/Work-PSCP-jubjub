'''PSCP-P02 ผลคูณเลขโดดที่ไม่เป็นศูนย์'''
def main():
    '''PSCP-P02 ผลคูณเลขโดดที่ไม่เป็นศูนย์'''
    x = input().strip()
    total = 1
    zero = False
    for i in x:
        if i != '0':
            total *= int(i)
            zero = True
    if zero:
        print(total)
    else:
        print(0)
main()
