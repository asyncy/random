from lib.gen_string import gen_string
from lib.gen_integer import gen_integer


def gen_list(_type, length, max_string_length=15, lo=0, hi=100):
    if _type == 'string':
        return [gen_string(gen_integer(1, max_string_length)) for _ in range(0, int(length))]
    if _type == 'integer':
        return [gen_integer(lo, hi) for _ in range(0, int(length))]
