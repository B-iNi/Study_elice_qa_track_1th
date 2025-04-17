import string
import random

def generate_string():
  letters_set = string.ascii_letters
#['d', 'L', 'B', 'v', 'p', 'J', 'h', 'Q', 'C', 's']
  random_list = random.sample(letters_set,10) 
  return ''.join(random_list)


