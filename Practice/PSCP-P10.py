'''PSCP-P10'''
# ใช้ set เพื่อ ตัดตัวซ้ำ
def main():
    '''PSCP-P10'''
    n = int(input())
    courses = set()
    for _ in range(n):
        courses.add(input())
    sort = sorted(courses)

    print(len(courses))
    for i in sort:
        print(i)
main()
