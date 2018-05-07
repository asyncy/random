import random
import string


def gen_string(length):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(int(length)))
