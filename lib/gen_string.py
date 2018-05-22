from string import ascii_letters, digits
from random import randint, SystemRandom


def gen_string(lo, hi):
    return ''.join(SystemRandom().choice(ascii_letters + digits) for _ in range(randint(int(lo), int(hi))))
