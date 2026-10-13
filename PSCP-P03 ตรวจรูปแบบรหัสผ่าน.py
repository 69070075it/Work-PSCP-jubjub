'''PSCP-P03 ตรวจรูปแบบรหัสผ่าน'''
def main():
    '''PSCP-P03 ตรวจรูปแบบรหัสผ่าน'''
    x = input().strip()
    upp = False
    num = False
    low = False
    for i in x:
        if i.isupper():
            upp = True
            continue
        if i.islower():
            low = True
            continue
        if i.isdigit():
            num = True
            continue
    if upp and num and low and len(x) >= 8:
        print("VALID")
    else:
        print('INVALID')

main()
