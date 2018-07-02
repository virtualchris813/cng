from string import ascii_lowercase
import itertools
letters = ascii_lowercase
noz = letters.replace("z","")

def iter_all_strings():
  for size in itertools.count(1):
    for s in itertools.product(noz, repeat=size):
      yield "".join(s)


def getNextLetter(currentLetter):
  last_one = False
  for s in iter_all_strings():
    if last_one == False:
      if s == currentLetter:
        last_one = True
    else:
      return s
      break
