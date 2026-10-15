'''resistor'''
def main():
    '''resistor'''
    color_digit = {
        'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4,
        'Green': 5, 'Blue': 6, 'Purple': 7, 'Grey': 8, 'White': 9
    }

    color_multi = {
        'Black': 1, 'Brown': 10, 'Red': 100, 'Orange': 1000, 'Yellow': 10000,
        'Green': 100000, 'Blue': 1000000, 'Purple': 10000000, 'Gold': 0.1, 'Silver': 0.01
    }

    color_tol = {
        'Brown': 1, 'Red': 2, 'Green': 0.5, 'Blue': 0.25,
        'Purple': 0.10, 'Grey': 0.05, 'Gold': 5, 'Silver': 10
    }

    c1 = input()
    c2 = input()
    c3 = input()
    c4 = input()

    if c1 in color_digit and c2 in color_digit and c3 in color_multi and c4 in color_tol:
        digit_val = color_digit[c1] * 10 + color_digit[c2]
        mult_val = color_multi[c3]
        tol_val = color_tol[c4]

        base_resistor = digit_val * mult_val
        lower_bound = base_resistor * (1 - tol_val / 100)
        upper_bound = base_resistor * (1 + tol_val / 100)

        print(f"{lower_bound:.4f}")
        print(f"{upper_bound:.4f}")
    else:
        print("Error")
main()
