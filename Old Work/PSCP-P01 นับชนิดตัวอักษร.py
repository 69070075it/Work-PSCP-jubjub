'''PSCP-P01 นับชนิดตัวอักษร'''
def main():
    '''PSCP-P01 นับชนิดตัวอักษร'''
    x = input().strip()
    low = 0
    upp = 0
    num = 0
    for i in x:
        if i.isupper():
            upp += 1
        elif i.islower():
            low += 1
        elif i.isdigit():
            num += 1
    print(f'{upp} {low} {num}')
main()
