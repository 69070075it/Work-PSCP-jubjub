'''บุพเพสันนิวาส'''
def main():
    '''บุพเพสันนิวาส'''
    s1 = input().strip()
    s2 = input().strip()

    len1, len2 = len(s1), len(s2)
    max_len = max(len1, len2)

    if len1 < max_len:
        i = 0
        while len(s1) < max_len:
            s1 += s1[i]
            i += 1

    if len2 < max_len:
        i = 0
        while len(s2) < max_len:
            s2 += s2[i]
            i += 1

    love_set = set('love')
    buppe_ch = []

    for c1, c2 in zip(s1, s2):
        if c1.lower() in love_set or c2.lower() in love_set:
            buppe_ch.append('w')
        else:
            buppe_ch.append('$')

    buppe = ''.join(buppe_ch)
    total_w = buppe.count('w')

    max_w_add = 0
    cur_w = 0
    for ch in buppe:
        if ch == 'w':
            cur_w += 1
            max_w_add = max(max_w_add, cur_w)
        else:
            cur_w = 0

    if total_w % 2:
        buppe += str(max_w_add)
    else:
        if max_w_add < 2:
            buppe += '#'

    print(buppe)
main()
