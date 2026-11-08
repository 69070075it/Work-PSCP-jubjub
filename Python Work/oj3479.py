'''name of card'''
def main():
    '''name of card'''
    text = input().upper()

    rank_code = text[:-1]
    suit_code = text[-1]

    ranks = {
        'A': 'Ace',
        'J': 'Jack',
        'Q': 'Queen',
        'K': 'King'
    }

    suits = {
        'D': 'Diamonds',
        'H': 'Hearts',
        'S': 'Spades',
        'C': 'Clubs'
    }

    if rank_code in ranks:
        rank_name = ranks.get(rank_code)
    else:
        rank_name = rank_code

    suit_name = suits[suit_code]

    print(f'{rank_name} of {suit_name}')
main()
