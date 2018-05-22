from lib.gen_string import gen_string
from lib.gen_integer import gen_integer


def gen_list(_type, length, lo, hi):
    if _type == 'string':
        return [gen_string(lo, hi) for _ in range(0, int(length))]
    if _type == 'integer':
        return [gen_integer(lo, hi) for _ in range(0, int(length))]
