from sys import argv
from lib.gen_string import gen_string
from lib.gen_integer import gen_integer
from lib.gen_list import gen_list


if len(argv) < 2:
    print({'error': '1st argument must be one of: {string, number, list}'})
    exit(1)

if argv[1] == 'string':
    try:
        print(gen_string(lo=argv[2], hi=argv[3]))
    except (IndexError, ValueError):
        print({'error': 'must provide an ascending integer interval length of the string to be generated'})
        exit(1)
elif argv[1] == 'integer':
    try:
        print(gen_integer(argv[2], argv[3]))
    except (IndexError, ValueError):
        print({'error': 'must provide an ascending integer range for integer to be generated'})
elif argv[1] == 'list':
    try:
        print(gen_list(_type=argv[2], length=argv[3], lo=argv[4], hi=argv[5]))
    except (IndexError, ValueError):
        print({'error': 'must provide the type of list one of: {integer, string}, length of list, and an ascending integer interval range'})
        exit(1)
else:
    print({'error': '1st argument must be one of: {string, number, list}'})
    exit(1)
