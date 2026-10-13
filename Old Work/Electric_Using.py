'''Electric_Using'''
def main():
    '''Electric_Using'''
    x = int(input())
    total = 0
    if x <= 10:
        total = 5*x
    elif 11 <= x <= 50:
        total = 50 + 7*(x-10)
    elif 51 <= x <= 100:
        total = 50 + 280 + 10*(x-50)
    elif 101 <= x <= 200:
        total = 50 + 280 + 500 + 12*(x-100)
    else:
        total = 50 + 280 + 500 + 1200 + 15*(x-200)
    ft = 0.50*x
    vat = 0.07 * total
    print(f'{(total+vat+ft+0.01):.1f}')
main()
