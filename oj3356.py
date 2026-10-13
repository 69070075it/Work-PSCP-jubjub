'''Bus seat'''
def main():
    '''Bus seat'''
    col_seat = int(input())
    num_row = int(input())
    ur_seat = int(input())

    for seat_off in range(col_seat, 0, -1):
        row_seat = []
        for col in range(num_row):
            seat_num = seat_off + (col * col_seat)

            if seat_num == ur_seat:
                row_seat.append('XX')
            else:
                row_seat.append(f'{seat_num:02d}')

        print(' '.join(row_seat))

        if not (seat_off - 1) % 2 and seat_off > 1:
            print()
main()
