from string import ascii_lowercase
import itertools
letters = ascii_lowercase
# Example of skipping z, could be modified for your specific needs.
# This makes the iterator go from a,b..x,y,aa,ab..ax,ay,ba (no z is used)
skip_letter = "z"
noz = letters.replace(skip_letter,"")

def iter_all_strings():
  for size in itertools.count(1):
    for s in itertools.product(noz, repeat=size):
      yield "".join(s)


def getNextLetter(currentLetter):
  if currentLetter == skip_letter:
    raise ValueError, 'Current Letter is the Skip Letter. Something is messed up! Exiting.'
  last_one = False
  for s in iter_all_strings():
    if last_one == False:
      if s == currentLetter:
        # If we are on the current iteration, set last_one to True
        # so we can exit after next loop iteration.
        last_one = True
    else:
      return s
      break
