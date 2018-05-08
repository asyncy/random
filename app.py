import sys
from lib.gen_string import gen_string
from lib.gen_integer import gen_integer
from lib.gen_list import gen_list


if len(sys.argv) < 2:
    print({'error': '1st argument must be one of: {string, number, list}'})
    exit(1)

if sys.argv[1] == 'string':
    try:
        print(gen_string(lo=sys.argv[2], hi=sys.argv[3]))
    except (IndexError, ValueError):
        print({'error': 'must provide an ascending integer interval length of the string to be generated'})
        exit(1)
elif sys.argv[1] == 'integer':
    try:
        print(gen_integer(sys.argv[2], sys.argv[3]))
    except (IndexError, ValueError):
        print({'error': 'must provide an ascending integer range for integer to be generated'})
elif sys.argv[1] == 'list':
    try:
        print(gen_list(_type=sys.argv[2], length=sys.argv[3], lo=sys.argv[4], hi=sys.argv[5]))
    except (IndexError, ValueError):
        print({'error': 'must provide the type of list one of: {integer, string}, length of list, and an ascending integer interval range'})
        exit(1)
else:
    print({'error': '1st argument must be one of: {string, number, list}'})
    exit(1)
