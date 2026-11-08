'''PSCP-P07'''
def main():
    '''PSCP-P07'''
    text = input()
    result = [text[0]]
    for i in text[1:]:
        if i != result[-1]:
            result.append(i)
    print(''.join(result))
main()
