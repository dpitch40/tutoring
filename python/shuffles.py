# def shuffle(l):
#     result = list()
#     half_length = int(len(l) / 2)
#     for first, second in zip(l[:half_length], l[half_length:]):
#         result.extend([first, second])
#     return result

# l = list(range(1, 53))
# shuffled = l
# for i in range(14):
#     shuffled = shuffle(shuffled)
#     print(i + 1, shuffled == l)


import argparse

class InvalidDeckSizeException(ValueError):
    def __init__(self, n):
        super().__init__(f'Ew a deck with {n} cards. Get away!')

def shuffel(cards):
    new_cards = []
    for i in range(int(len(cards)/2)):
        new_cards.append(cards[i])
        new_cards.append(cards[i+int(len(cards)/2)])
    return new_cards

def test_shuffles(n):
    if n % 2:
        raise InvalidDeckSizeException(n)

    card_s = [i + 1 for i in range(n)]
    new_card_s = shuffel(card_s)

    num = 1
    while card_s != new_card_s:
        num += 1
        new_card_s = shuffel(new_card_s)
    return num

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int, help="The size of the deck (must be even)")
args = parser.parse_args()
try:
    print(test_shuffles(args.n))
except InvalidDeckSizeException as e:
    import traceback
    traceback.print_exc()
    # logger.error("Exception happened", exc_info=True)
