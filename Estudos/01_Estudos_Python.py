import collections
import inspect

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# # Criando uma instância do baralho
# baralho = FrenchDeck()

# # Imprimindo as cartas do baralho
# for carta in baralho:
#     print(carta)

# Obtendo o código-fonte do namedtuple
source_code = inspect.getsource(collections.namedtuple)

# Imprimindo o código-fonte
print(source_code)
