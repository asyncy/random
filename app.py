import sys
from lib.gen_string import gen_string
from lib.gen_integer import gen_integer
from lib.gen_list import gen_list


if sys.argv[1] == 'string':
    try:
        print(gen_string(sys.argv[2]))
    except (IndexError, ValueError):
        print({'error': 'must provide a number for the integer length of the string to be generated'})
        exit(1)
elif sys.argv[1] == 'integer':
    try:
        print(gen_integer(sys.argv[2], sys.argv[3]))
    except ValueError:
        print({'error': 'must provide an ascending integer range'})
elif sys.argv[1] == 'list':
    if sys.argv[2] == 'string':
        try:
            print(gen_list(_type='string', length=sys.argv[3], max_string_length=sys.argv[4]))
        except IndexError:
            print({'error': 'must provide the length of the list, along with the max length of the strings to be generated'})
            exit(1)
    elif sys.argv[2] == 'integer':
        try:
            print(gen_list(_type='integer', length=sys.argv[3], lo=sys.argv[4], hi=sys.argv[5]))
        except IndexError:
            print({'error': 'must provide the length of the list, along with the low and high values of the random numbers to be generated'})
            exit(1)
    else:
        print({'error': '2nd argument for list must be one of: {string, integer}'})
        exit(1)
else:
    print({'error': '1st argument must be one of: {string, number, list}'})
    exit(1)
