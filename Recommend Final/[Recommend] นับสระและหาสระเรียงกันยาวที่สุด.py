'''[Recommend] นับสระและหาสระเรียงกันยาวที่สุด'''
def main():
    '''[Recommend] นับสระและหาสระเรียงกันยาวที่สุด'''
    n = int(input())
    for j in range(1, n+1):
        x = input().lower()
        vowel = 0
        cur_con = 0
        max_con = 0
        for i in x:
            if i in 'aeiou':
                vowel += 1
                cur_con += 1
                max_con = max(max_con, cur_con)
            else:
                cur_con = 0
        print(f'Line {j}: vowels = {vowel}, max_consecutive = {max_con}')
main()
