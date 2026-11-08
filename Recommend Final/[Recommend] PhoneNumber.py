'''[Recommend] PhoneNumber'''
def main():
    '''[Recommend] PhoneNumber'''
    phone = input()
    flag = input()
    last = phone[-4:]
    mid = phone[-8:-4]
    first = phone[:-8]
    if flag == 'Domestic':
        print(f'{first} {mid} {last}')
    elif flag == 'International':
        new_p = first.replace('0', '+66', 1)
        print(f'{new_p} {mid} {last}')
main()
