import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

print(Card, Card._fields)

card_instance = Card('7', 'diamonds')

print(card_instance, card_instance.rank, card_instance.suit)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
                                
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(len(deck), deck[1], deck[-1])

# 查看最上面3张牌
print(deck[:3])

# 只看牌面是A的牌
print(deck[12::13])

print("=======================随机抽牌==============================")

from random import choice, sample
# 随机抽取一张牌
print(choice(deck))
# 随机抽取三张牌
print(sample(list(deck), 3))

print("=======================升序摆牌==============================")
# 2最小，A最大，黑桃> 红桃> 方块> 梅花
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)





