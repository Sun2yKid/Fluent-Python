import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('"The time has com," the Walrus said')

print(s)
for word in s:
    print(word)

print(s[1])
print(list(s))
print(issubclass(Sentence, abc.Iterable))

print(isinstance(s, abc.Iterable))

